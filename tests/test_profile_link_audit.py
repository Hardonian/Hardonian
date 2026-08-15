import importlib.util
import io
import socket
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import MagicMock, patch

SPEC = importlib.util.spec_from_file_location("profile_link_audit", Path(__file__).parents[1] / "scripts/profile-link-audit.py")
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class ProfileLinkAuditTests(unittest.TestCase):
    def test_extract_urls(self):
        self.assertEqual(
            audit.extract_urls("[Doc](products/a.md) ![Logo](assets/a.png) <a href=\"https://example.com\">") ,
            ["products/a.md", "assets/a.png", "https://example.com"],
        )

    def test_rejects_repository_path_traversal(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(audit.UnsafeURL):
                audit.resolve_link("products/../../etc/passwd", root)

    @patch.object(audit.socket, "getaddrinfo")
    def test_blocks_private_and_metadata_addresses(self, getaddrinfo):
        for address in ("127.0.0.1", "169.254.169.254", "10.0.0.1", "::1"):
            getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (address, 443))]
            with self.assertRaises(audit.UnsafeURL):
                audit.validate_public_http_url("https://example.test/path")

    @patch.object(audit.socket, "getaddrinfo")
    def test_allows_public_address(self, getaddrinfo):
        getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("93.184.216.34", 443))]
        audit.validate_public_http_url("https://example.com")

    def test_missing_local_link_fails_without_network(self):
        with tempfile.TemporaryDirectory() as directory:
            readme = Path(directory) / "README.md"
            readme.write_text("[Missing](products/missing.md)")
            with patch("sys.stdout", new=io.StringIO()):
                self.assertEqual(audit.audit(readme), 1)

    @patch.object(audit, "validate_public_http_url")
    @patch.object(audit.urllib.request, "build_opener")
    def test_http_warning_is_nonfatal(self, build_opener, validate):
        opener = MagicMock()
        opener.open.side_effect = urllib.error.HTTPError("https://example.com", 429, "rate limited", {}, None)
        build_opener.return_value = opener
        status, detail = audit.check_url("https://example.com", "https://example.com")
        self.assertEqual(status, "warn")
        self.assertIn("WARN 429", detail)
        validate.assert_called_once()


if __name__ == "__main__":
    unittest.main()
