import unittest
from unittest.mock import patch, MagicMock
import urllib.error
import sys
import importlib.util
import io

# Dynamically import the module since it has hyphens in the filename
spec = importlib.util.spec_from_file_location("profile_link_audit", "scripts/profile-link-audit.py")
profile_link_audit = importlib.util.module_from_spec(spec)
sys.modules["profile_link_audit"] = profile_link_audit
spec.loader.exec_module(profile_link_audit)

class TestProfileLinkAudit(unittest.TestCase):

    @patch('profile_link_audit.urllib.request.urlopen')
    @patch('profile_link_audit.sys.exit')
    @patch('profile_link_audit.Path.read_text')
    def test_http_error_handling(self, mock_read_text, mock_exit, mock_urlopen):
        mock_read_text.return_value = "Here is a test URL: [test](https://example.com/test)"
        mock_error = urllib.error.HTTPError(url='https://example.com/test', code=500, msg='Internal Server Error', hdrs={}, fp=None)
        mock_urlopen.side_effect = mock_error

        with patch('sys.stdout', new=io.StringIO()):
            profile_link_audit.audit()

        mock_exit.assert_called_once_with(1)

    @patch('profile_link_audit.urllib.request.urlopen')
    @patch('profile_link_audit.sys.exit')
    @patch('profile_link_audit.Path.read_text')
    def test_generic_exception_handling(self, mock_read_text, mock_exit, mock_urlopen):
        mock_read_text.return_value = "Here is a test URL: [test](https://example.com/test)"
        mock_urlopen.side_effect = Exception("Generic connection failure")

        with patch('sys.stdout', new=io.StringIO()):
            profile_link_audit.audit()

        mock_exit.assert_called_once_with(1)

    @patch('profile_link_audit.urllib.request.urlopen')
    @patch('profile_link_audit.sys.exit')
    @patch('profile_link_audit.Path.read_text')
    def test_successful_external_link(self, mock_read_text, mock_exit, mock_urlopen):
        mock_read_text.return_value = "[Example](https://example.com)"
        mock_cm = MagicMock()
        mock_cm.status = 200
        mock_cm.__enter__.return_value = mock_cm
        mock_urlopen.return_value = mock_cm

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            profile_link_audit.audit()
            out = fake_out.getvalue()

        mock_exit.assert_not_called()
        self.assertIn("OK 200 https://example.com", out)
        self.assertIn("CHECKED 1 UNIQUE_LINKS_AND_IMAGES; FAILURES 0", out)

    @patch('profile_link_audit.urllib.request.urlopen')
    @patch('profile_link_audit.sys.exit')
    @patch('profile_link_audit.Path.read_text')
    def test_failed_external_link(self, mock_read_text, mock_exit, mock_urlopen):
        mock_read_text.return_value = "[Example](https://example.com)"
        mock_urlopen.side_effect = urllib.error.HTTPError("https://example.com", 404, "Not Found", {}, None)

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            profile_link_audit.audit()
            out = fake_out.getvalue()

        mock_exit.assert_called_once_with(1)
        self.assertIn("FAIL 404 https://example.com", out)
        self.assertIn("FAILURES 1", out)

    @patch('profile_link_audit.Path.exists')
    @patch('profile_link_audit.sys.exit')
    @patch('profile_link_audit.Path.read_text')
    def test_successful_local_link(self, mock_read_text, mock_exit, mock_exists):
        mock_read_text.return_value = "[Example](products/test.md)"
        mock_exists.return_value = True

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            profile_link_audit.audit()
            out = fake_out.getvalue()

        mock_exit.assert_not_called()
        self.assertIn("LOCAL 200 products/test.md", out)
        self.assertIn("CHECKED 1 UNIQUE_LINKS_AND_IMAGES; FAILURES 0", out)

    @patch('profile_link_audit.Path.exists')
    @patch('profile_link_audit.sys.exit')
    @patch('profile_link_audit.Path.read_text')
    def test_missing_local_link(self, mock_read_text, mock_exit, mock_exists):
        mock_read_text.return_value = "[Example](products/test.md)"
        mock_exists.return_value = False

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            profile_link_audit.audit()
            out = fake_out.getvalue()

        mock_exit.assert_called_once_with(1)
        self.assertIn("FAILURES 1", out)

    @patch('profile_link_audit.sys.exit')
    @patch('profile_link_audit.Path.read_text')
    def test_ignored_links(self, mock_read_text, mock_exit):
        mock_read_text.return_value = "[Example1](#anchor) [Example2](mailto:test@example.com)"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            profile_link_audit.audit()
            out = fake_out.getvalue()

        mock_exit.assert_not_called()
        self.assertIn("CHECKED 1 UNIQUE_LINKS_AND_IMAGES", out)

    @patch('profile_link_audit.urllib.request.urlopen')
    @patch('profile_link_audit.sys.exit')
    @patch('profile_link_audit.Path.read_text')
    def test_http_warnings(self, mock_read_text, mock_exit, mock_urlopen):
        for status in [403, 429, 999]:
            with self.subTest(status=status):
                mock_read_text.return_value = "[Example](https://example.com)"
                mock_urlopen.side_effect = urllib.error.HTTPError("https://example.com", status, "Warning", {}, None)
                mock_exit.reset_mock()

                with patch('sys.stdout', new=io.StringIO()) as fake_out:
                    profile_link_audit.audit()
                    out = fake_out.getvalue()

                mock_exit.assert_not_called()
                self.assertIn(f"WARN {status} https://example.com", out)

if __name__ == '__main__':
    unittest.main()
