#!/usr/bin/env python3
"""Optional Hermes Tweet / Xquik research helper for launch evidence."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

DEFAULT_BASE_URL = "https://xquik.com"


class HermesTweetError(Exception):
    """Raised when Hermes Tweet cannot complete a research request."""


def get_api_key() -> str:
    """Read a Hermes Tweet / Xquik API key from the environment."""
    return os.getenv("XQUIK_API_KEY") or os.getenv("HERMES_TWEET_API_KEY") or ""


def get_base_url() -> str:
    """Read the configured Xquik base URL."""
    return os.getenv("XQUIK_BASE_URL", DEFAULT_BASE_URL).rstrip("/")


def build_headers(api_key: str) -> dict[str, str]:
    """Build auth headers accepted by Xquik."""
    if not api_key:
        raise HermesTweetError("XQUIK_API_KEY or HERMES_TWEET_API_KEY is required.")
    headers = {"User-Agent": "viral-launch-pipeline/hermes-tweet"}
    if api_key.startswith("xq_"):
        headers["x-api-key"] = api_key
    else:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers


def build_url(path: str, params: dict[str, Any] | None = None) -> str:
    """Build a Xquik API URL."""
    query = urllib.parse.urlencode({key: value for key, value in (params or {}).items() if value not in (None, "")})
    return f"{get_base_url()}{path}" + (f"?{query}" if query else "")


def request_json(path: str, params: dict[str, Any] | None = None) -> Any:
    """Fetch JSON from Xquik."""
    request = urllib.request.Request(
        build_url(path, params),
        headers=build_headers(get_api_key()),
        method="GET",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def first_present(mapping: dict[str, Any], keys: list[str], default: Any = "") -> Any:
    """Return the first non-empty mapping value."""
    for key in keys:
        value = mapping.get(key)
        if value not in (None, ""):
            return value
    return default


def to_int(value: Any) -> int:
    """Parse numeric counters from API payloads."""
    try:
        return int(str(value or 0).replace(",", ""))
    except ValueError:
        return 0


def extract_items(payload: Any) -> list[dict[str, Any]]:
    """Extract list rows from common response envelopes."""
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if not isinstance(payload, dict):
        return []
    for key in ("tweets", "items", "results", "users"):
        value = payload.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
    data = payload.get("data")
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        nested = extract_items(data)
        return nested or [data]
    return []


def normalize_user(raw: Any) -> dict[str, Any]:
    """Normalize X user data."""
    if not isinstance(raw, dict):
        return {"username": str(raw or ""), "name": "", "followers_count": 0}
    legacy = raw.get("legacy") if isinstance(raw.get("legacy"), dict) else {}
    metrics = raw.get("public_metrics") if isinstance(raw.get("public_metrics"), dict) else {}
    return {
        "id": str(first_present(raw, ["id", "id_str", "rest_id", "user_id"], "")),
        "username": str(first_present(raw, ["username", "screen_name", "handle"], legacy.get("screen_name", ""))).lstrip("@"),
        "name": str(first_present(raw, ["name", "display_name"], legacy.get("name", ""))),
        "followers_count": to_int(first_present(raw, ["followers_count"], metrics.get("followers_count", legacy.get("followers_count", 0)))),
    }


def normalize_tweet(raw: dict[str, Any]) -> dict[str, Any]:
    """Normalize tweet data for launch evidence."""
    legacy = raw.get("legacy") if isinstance(raw.get("legacy"), dict) else {}
    metrics = raw.get("public_metrics") if isinstance(raw.get("public_metrics"), dict) else {}
    core = raw.get("core") if isinstance(raw.get("core"), dict) else {}
    user_result = core.get("user_results", {}).get("result", {}) if core else {}
    author = normalize_user(raw.get("author") or raw.get("user") or user_result or raw.get("screen_name") or "")
    tweet_id = str(first_present(raw, ["id", "id_str", "tweet_id", "rest_id"], legacy.get("id_str", "")))
    return {
        "id": tweet_id,
        "url": raw.get("url") or f"https://x.com/i/status/{tweet_id}",
        "author": author.get("username", ""),
        "text": str(first_present(raw, ["text", "full_text", "content"], legacy.get("full_text", ""))),
        "likes": to_int(first_present(raw, ["like_count", "favorite_count"], metrics.get("like_count", legacy.get("favorite_count", 0)))),
        "retweets": to_int(first_present(raw, ["retweet_count"], metrics.get("retweet_count", legacy.get("retweet_count", 0)))),
        "replies": to_int(first_present(raw, ["reply_count"], metrics.get("reply_count", legacy.get("reply_count", 0)))),
        "views": to_int(first_present(raw, ["view_count", "views"], metrics.get("view_count", legacy.get("view_count", 0)))),
    }


def search_tweets(query: str, limit: int) -> list[dict[str, Any]]:
    """Search X posts through Hermes Tweet."""
    payload = request_json("/api/v1/x/tweets/search", {"q": query, "limit": min(limit, 100)})
    return [normalize_tweet(item) for item in extract_items(payload)]


def get_user(username: str) -> dict[str, Any]:
    """Fetch a profile through Hermes Tweet."""
    payload = request_json(f"/api/v1/x/users/{urllib.parse.quote(username.lstrip('@'))}")
    items = extract_items(payload)
    source = items[0] if items else payload.get("data", payload) if isinstance(payload, dict) else {}
    return normalize_user(source)


def render_markdown(query: str, tweets: list[dict[str, Any]]) -> str:
    """Render search results as a compact evidence table."""
    rows = [
        f"### Hermes Tweet X Evidence: {query}",
        "",
        "| Post | Engagement | Launch Use |",
        "|---|---:|---|",
    ]
    for tweet in tweets:
        text = str(tweet.get("text", "")).replace("|", "\\|").replace("\n", " ")[:180]
        engagement = f"{tweet.get('likes', 0)} likes, {tweet.get('retweets', 0)} reposts, {tweet.get('replies', 0)} replies"
        rows.append(f"| [{tweet.get('author', 'unknown')}]({tweet.get('url', '')}) - {text} | {engagement} | Hook pattern, customer language, or quote-repost candidate |")
    if not tweets:
        rows.append("| No posts returned | 0 | Use another source before making a platform-specific claim |")
    return "\n".join(rows)


def main(argv: list[str]) -> int:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(description="Collect launch evidence from Hermes Tweet / Xquik.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    search = subparsers.add_parser("search", help="Search X posts.")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=5)
    search.add_argument("--format", choices=("json", "markdown"), default="markdown")

    user = subparsers.add_parser("user", help="Fetch one X profile.")
    user.add_argument("username")

    args = parser.parse_args(argv[1:])
    try:
        if args.command == "search":
            tweets = search_tweets(args.query, args.limit)
            if args.format == "json":
                print(json.dumps({"query": args.query, "tweets": tweets}, ensure_ascii=False, indent=2))
            else:
                print(render_markdown(args.query, tweets))
        elif args.command == "user":
            print(json.dumps(get_user(args.username), ensure_ascii=False, indent=2))
    except (HermesTweetError, urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": exc.__class__.__name__, "message": str(exc)}, ensure_ascii=False))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
