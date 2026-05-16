#!/usr/bin/env python3
"""Validate a viral launch pack markdown file for required sections and weak language."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "## Executive Summary",
    "## Assumptions and Placeholders",
    "## Research Summary",
    "## Subagent Execution",
    "## Positioning",
    "### Bold Claim",
    "## Hook Iterations",
    "## Final Launch Drafts",
    "## Weapons Check",
    "## Distribution Plan",
    "## Human Edit Notes",
]

WEAK_PHRASES = [
    "powerful platform",
    "seamless",
    "streamline workflows",
    "streamlines workflows",
    "built for modern teams",
    "all-in-one",
    "cutting-edge",
    "revolutionary",
    "game-changing",
    "unlock productivity",
    "save time with ai",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_launch_pack.py path/to/launch-pack.md", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"Missing required heading: {heading}")

    source_links = re.findall(r"https?://\S+", text)
    if "## Research Summary" in text and len(source_links) < 2:
        warnings.append("Research Summary has fewer than 2 URL citations.")

    if "## Subagent Execution" in text:
        if "Mode: spawned" not in text and "Mode: sequential-fallback" not in text:
            errors.append("Subagent Execution must declare Mode: spawned or Mode: sequential-fallback.")
        if "Spawned groups:" not in text:
            errors.append("Subagent Execution must include Spawned groups.")

    if "Mode: sequential-fallback" in text and "Reason:" not in text:
        errors.append("Subagent Execution uses sequential-fallback but has no Reason field.")

    lower = text.lower()
    for phrase in WEAK_PHRASES:
        if phrase in lower:
            warnings.append(f"Generic launch phrase found: {phrase!r}")

    final_section = text.split("## Final Launch Drafts", 1)[-1] if "## Final Launch Drafts" in text else ""
    if len(final_section.strip()) < 280:
        warnings.append("Final Launch Drafts section looks short; ensure it contains usable platform-specific launch copy.")

    if errors:
        print("INVALID")
        for error in errors:
            print(f"ERROR: {error}")
    else:
        print("VALID")

    for warning in warnings:
        print(f"WARNING: {warning}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
