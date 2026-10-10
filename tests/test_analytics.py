import unittest
import os
import subprocess

class TestAnalyticsScript(unittest.TestCase):
    def setUp(self):
        self.analytics_path = os.path.join(os.path.dirname(__file__), "..", "assets", "analytics.js")

    def test_no_math_random_in_analytics(self):
        """Verify Math.random is not used in assets/analytics.js"""
        with open(self.analytics_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertNotIn("Math.random", content, "Math.random() should not be present in assets/analytics.js")

    def test_uses_crypto_get_random_values(self):
        """Verify crypto.getRandomValues is used in assets/analytics.js"""
        with open(self.analytics_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("crypto.getRandomValues", content, "crypto.getRandomValues should be used in assets/analytics.js")

    def test_analytics_execution_node(self):
        """Execute the analytics snippet logic via Node.js to verify valid session ID generation."""
        with open(self.analytics_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract JS code inside <script> tags
        js_code = content.split("<script>")[1].split("</script>")[0]

        # Wrap in a Node script mock environment
        node_runner = f"""
        const globalStore = {{}};
        const sessionStorage = {{
            getItem: (key) => globalStore[key] || null,
            setItem: (key, val) => {{ globalStore[key] = String(val); }}
        }};
        const window = {{ location: {{ pathname: '/test' }} }};
        const document = {{ referrer: '', addEventListener: () => {{}} }};
        const fetch = async () => ({{ catch: () => {{}} }});

        {js_code}

        console.log(sessionStorage.getItem('aas_sid'));
        """

        result = subprocess.run(
            ["node", "-e", node_runner],
            capture_output=True,
            text=True,
            check=True
        )
        session_id = result.stdout.strip()
        self.assertTrue(session_id.startswith("s"), f"Session ID should start with 's', got {session_id}")
        self.assertGreater(len(session_id), 10, f"Session ID should have adequate length, got {session_id}")

if __name__ == "__main__":
    unittest.main()
