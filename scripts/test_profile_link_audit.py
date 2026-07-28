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
        # Provide some dummy markdown with a URL so the audit loops over it
        mock_read_text.return_value = "Here is a test URL: [test](https://example.com/test)"

        # Make urlopen raise an HTTPError
        mock_error = urllib.error.HTTPError(url='https://example.com/test', code=500, msg='Internal Server Error', hdrs={}, fp=None)
        mock_urlopen.side_effect = mock_error

        # Capture print statements if desired, though not strictly necessary
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            profile_link_audit.audit()

        # Verify that exit(1) was called due to the failure
        mock_exit.assert_called_once_with(1)

    @patch('profile_link_audit.urllib.request.urlopen')
    @patch('profile_link_audit.sys.exit')
    @patch('profile_link_audit.Path.read_text')
    def test_generic_exception_handling(self, mock_read_text, mock_exit, mock_urlopen):
        # Provide some dummy markdown with a URL
        mock_read_text.return_value = "Here is a test URL: [test](https://example.com/test)"

        # Make urlopen raise a generic Exception
        mock_urlopen.side_effect = Exception("Generic connection failure")

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            profile_link_audit.audit()

        # Verify that exit(1) was called due to the failure
        mock_exit.assert_called_once_with(1)


    @patch('profile_link_audit.urllib.request.urlopen')
    @patch('profile_link_audit.sys.exit')
    @patch('profile_link_audit.Path.read_text')
    def test_html_tags_extraction(self, mock_read_text, mock_exit, mock_urlopen):
        # Provide dummy markdown with HTML link and image tags
        mock_read_text.return_value = 'Here is an HTML link: <a href="https://example.com/html-link">Link</a> and an image: <img src="https://example.com/image.png" alt="img">'

        # Mock a successful response for the URLs
        mock_response = MagicMock()
        mock_response.status = 200
        mock_urlopen.return_value.__enter__.return_value = mock_response

        # Suppress standard output
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            profile_link_audit.audit()

        # Get all URLs that were requested
        requested_urls = [call.args[0].full_url for call in mock_urlopen.call_args_list]

        # Verify that both the HTML link and the image src were extracted and requested
        self.assertIn('https://example.com/html-link', requested_urls)
        self.assertIn('https://example.com/image.png', requested_urls)

        # Verify that the audit did not exit with failure
        mock_exit.assert_not_called()

if __name__ == '__main__':
    unittest.main()
