import os
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

import hermes_tweet_research as research


class HermesTweetResearchTests(unittest.TestCase):
    def test_build_headers_supports_x_api_key(self):
        self.assertEqual(research.build_headers("xq_test")["x-api-key"], "xq_test")

    def test_build_headers_supports_bearer_token(self):
        self.assertEqual(research.build_headers("token")["Authorization"], "Bearer token")

    def test_build_url_encodes_query(self):
        with mock.patch.dict(os.environ, {"XQUIK_BASE_URL": "https://xquik.test"}):
            url = research.build_url("/api/v1/x/tweets/search", {"q": "launch AI agent", "limit": 2})
        self.assertEqual(url, "https://xquik.test/api/v1/x/tweets/search?q=launch+AI+agent&limit=2")

    def test_extract_items_reads_nested_payload(self):
        payload = {"data": {"tweets": [{"id": "1"}, {"id": "2"}]}}
        self.assertEqual(research.extract_items(payload), [{"id": "1"}, {"id": "2"}])

    def test_normalize_tweet_keeps_launch_evidence_fields(self):
        tweet = research.normalize_tweet(
            {
                "id": "42",
                "text": "Launch hook with proof.",
                "author": {"username": "alice", "followers_count": "1,200"},
                "public_metrics": {"like_count": 9, "retweet_count": 2, "reply_count": 1, "view_count": "300"},
            }
        )
        self.assertEqual(tweet["id"], "42")
        self.assertEqual(tweet["author"], "alice")
        self.assertEqual(tweet["likes"], 9)
        self.assertEqual(tweet["views"], 300)

    def test_render_markdown_includes_evidence_table(self):
        output = research.render_markdown(
            "AI launch",
            [{"author": "alice", "url": "https://x.com/i/status/42", "text": "Launch proof", "likes": 9, "retweets": 2, "replies": 1}],
        )
        self.assertIn("| Post | Engagement | Launch Use |", output)
        self.assertIn("alice", output)


if __name__ == "__main__":
    unittest.main()
