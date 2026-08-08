import unittest
from unittest.mock import patch, MagicMock
import urllib.error
import io
import sys
import importlib.util
from pathlib import Path

def run_script(readme_content):
    def mock_read_text(*args, **kwargs):
        return readme_content

    captured_output = io.StringIO()

    with patch('pathlib.Path.read_text', mock_read_text), \
         patch('sys.stdout', captured_output):

        import importlib.util
        spec = importlib.util.spec_from_file_location("profile_link_audit", "scripts/profile-link-audit.py")
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            module.audit()
            exit_code = 0
        except SystemExit as e:
            exit_code = e.code

    return exit_code, captured_output.getvalue()

class TestProfileLinkAudit(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_successful_external_link(self, mock_urlopen):
        mock_cm = MagicMock()
        mock_cm.status = 200
        mock_cm.__enter__.return_value = mock_cm
        mock_urlopen.return_value = mock_cm

        code, out = run_script("[Example](https://example.com)")

        self.assertEqual(code, 0)
        self.assertIn("OK 200 https://example.com", out)
        self.assertIn("CHECKED 1 UNIQUE_LINKS_AND_IMAGES; FAILURES 0", out)

    @patch('urllib.request.urlopen')
    def test_failed_external_link(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.HTTPError("https://example.com", 404, "Not Found", {}, None)

        code, out = run_script("[Example](https://example.com)")

        self.assertEqual(code, 1)
        self.assertIn("FAIL 404 https://example.com", out)
        self.assertIn("FAILURES 1", out)

    @patch('pathlib.Path.exists')
    def test_successful_local_link(self, mock_exists):
        mock_exists.return_value = True

        code, out = run_script("[Example](products/test.md)")

        self.assertEqual(code, 0)
        self.assertIn("LOCAL 200 products/test.md", out)
        self.assertIn("CHECKED 1 UNIQUE_LINKS_AND_IMAGES; FAILURES 0", out)

    @patch('pathlib.Path.exists')
    def test_missing_local_link(self, mock_exists):
        mock_exists.return_value = False

        code, out = run_script("[Example](products/test.md)")

        self.assertEqual(code, 1)
        self.assertIn("FAILURES 1", out)

    def test_ignored_links(self):
        code, out = run_script("[Example1](#anchor) [Example2](mailto:test@example.com)")

        self.assertEqual(code, 0)
        self.assertIn("CHECKED 1 UNIQUE_LINKS_AND_IMAGES", out)

    @patch('urllib.request.urlopen')
    def test_http_warnings(self, mock_urlopen):
        for status in [403, 429, 999]:
            mock_urlopen.side_effect = urllib.error.HTTPError("https://example.com", status, "Warning", {}, None)

            code, out = run_script("[Example](https://example.com)")

            self.assertEqual(code, 0)
            self.assertIn(f"WARN {status} https://example.com", out)

if __name__ == '__main__':
    unittest.main()

class TestGetLocalPath(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location("profile_link_audit", "scripts/profile-link-audit.py")
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)

    def test_get_local_path(self):
        root = Path('/my/root')
        test_cases = [
            ("products/test.md", "/my/root/products/test.md"),
            ("/products/test.md", "/my/root/products/test.md"),
            ("/Hardonian/project/tree/main/docs/api.md", "/my/root/docs/api.md"),
            ("/Hardonian/other-repo/blob/main/README.md", "/my/root/other-repo/blob/main/README.md"),
            ("/Hardonian/Hardonian/tree/main/architecture-playbook/index.md", "/my/root/architecture-playbook/index.md"),
            ("assets/image.png", "/my/root/assets/image.png"),
            ("/assets/image.png", "/my/root/assets/image.png"),
        ]

        for raw, expected in test_cases:
            with self.subTest(raw=raw):
                result = self.module.get_local_path(raw, root)
                self.assertEqual(result, Path(expected))
