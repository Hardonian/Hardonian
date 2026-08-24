import unittest
from unittest.mock import patch, MagicMock
import urllib.error
import sys
import importlib.util
import io
from pathlib import Path

spec = importlib.util.spec_from_file_location("profile_link_audit", Path(__file__).parent / "profile-link-audit.py")
profile_link_audit = importlib.util.module_from_spec(spec)
sys.modules["profile_link_audit"] = profile_link_audit
spec.loader.exec_module(profile_link_audit)


class TestProfileLinkAudit(unittest.TestCase):

    @patch('profile_link_audit.validate_public_http_url')
    @patch('profile_link_audit.urllib.request.build_opener')
    @patch('profile_link_audit.Path.read_text')
    def test_http_error_handling(self, mock_read_text, mock_build_opener, mock_validate):
        mock_read_text.return_value = "Here is a test URL: [test](https://example.com/test)"
        opener = MagicMock()
        opener.open.side_effect = urllib.error.HTTPError(url='https://example.com/test', code=500, msg='Internal Server Error', hdrs={}, fp=None)
        mock_build_opener.return_value = opener

        with patch('sys.stdout', new=io.StringIO()):
            result = profile_link_audit.audit()

        self.assertEqual(result, 1)

    @patch('profile_link_audit.validate_public_http_url')
    @patch('profile_link_audit.urllib.request.build_opener')
    @patch('profile_link_audit.Path.read_text')
    def test_relative_path_resolution(self, mock_read_text, mock_build_opener, mock_validate):
        mock_read_text.return_value = "Here is a test URL: [test](unknown-path.md)"
        opener = MagicMock()
        mock_response = MagicMock()
        mock_response.status = 200
        opener.open.return_value.__enter__.return_value = mock_response
        mock_build_opener.return_value = opener

        with patch('sys.stdout', new=io.StringIO()):
            result = profile_link_audit.audit()

        self.assertEqual(result, 0)

    @patch('profile_link_audit.validate_public_http_url')
    @patch('profile_link_audit.urllib.request.build_opener')
    @patch('profile_link_audit.Path.read_text')
    def test_generic_exception_handling(self, mock_read_text, mock_build_opener, mock_validate):
        mock_read_text.return_value = "Here is a test URL: [test](https://example.com/test)"
        opener = MagicMock()
        opener.open.side_effect = Exception("Generic connection failure")
        mock_build_opener.return_value = opener

        with patch('sys.stdout', new=io.StringIO()):
            result = profile_link_audit.audit()

        self.assertEqual(result, 1)

    @patch('profile_link_audit.validate_public_http_url')
    @patch('profile_link_audit.urllib.request.build_opener')
    @patch('profile_link_audit.Path.read_text')
    def test_html_tags_extraction(self, mock_read_text, mock_build_opener, mock_validate):
        mock_read_text.return_value = 'Here is an HTML link: <a href="https://example.com/html-link">Link</a> and an image: <img src="https://example.com/image.png" alt="img">'
        opener = MagicMock()
        mock_response = MagicMock()
        mock_response.status = 200
        opener.open.return_value.__enter__.return_value = mock_response
        mock_build_opener.return_value = opener

        with patch('sys.stdout', new=io.StringIO()):
            result = profile_link_audit.audit()

        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
