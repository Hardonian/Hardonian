import re
import unittest
from pathlib import Path


class AnalyticsJSTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analytics_path = Path(__file__).parents[1] / "assets" / "analytics.js"
        cls.content = cls.analytics_path.read_text(encoding="utf-8")

    def test_analytics_file_exists_and_non_empty(self):
        self.assertTrue(self.analytics_path.exists(), "assets/analytics.js should exist")
        self.assertGreater(len(self.content.strip()), 0, "assets/analytics.js should not be empty")

    def test_wrapped_in_script_tags_and_iife(self):
        self.assertIn("<script>", self.content)
        self.assertIn("</script>", self.content)
        self.assertIn("(function() {", self.content)
        self.assertIn("})();", self.content)

    def test_session_storage_key_and_generator(self):
        self.assertIn("sessionStorage.getItem('aas_sid')", self.content)
        self.assertIn("sessionStorage.setItem('aas_sid', sessionId)", self.content)
        self.assertIn("Math.random().toString(36)", self.content)

    def test_tracking_endpoint_url(self):
        self.assertIn("https://aiautomatedsystems.ca/api/track", self.content)

    def test_page_view_event_payload(self):
        self.assertIn("event: 'page_view'", self.content)
        self.assertIn("page: window.location.pathname", self.content)
        self.assertIn("referrer: document.referrer", self.content)
        self.assertIn("session_id: sessionId", self.content)

    def test_checkout_click_event_listener_and_selectors(self):
        self.assertIn("document.addEventListener('click'", self.content)
        self.assertIn('a[href*="buy.stripe.com"]', self.content)
        self.assertIn('a[href*="checkout"]', self.content)
        self.assertIn("event: 'checkout_click'", self.content)
        self.assertIn("product_slug: slug", self.content)
        self.assertIn("checkout_url: link.href", self.content)

    def test_error_handling_catch_swallowing(self):
        catch_count = len(re.findall(r"\.catch\(\(\)\s*=>\s*\{\}\)", self.content))
        self.assertEqual(catch_count, 2, "Both fetch calls should have .catch(() => {}) error handlers")


if __name__ == "__main__":
    unittest.main()
