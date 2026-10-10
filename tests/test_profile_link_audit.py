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

    def test_resolves_generic_relative_file_and_ignores_fragment(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "CONTRIBUTING.md"
            document.write_text("# Contributing")
            target, local = audit.resolve_link("CONTRIBUTING.md#workflow", root)
            self.assertIsNone(target)
            self.assertEqual(local, document.resolve())

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

    @patch.object(audit.time, "sleep")
    @patch.object(audit, "validate_public_http_url")
    @patch.object(audit.urllib.request, "build_opener")
    def test_transient_timeout_is_retried(self, build_opener, validate, sleep):
        opener = MagicMock()
        response = MagicMock()
        response.status = 200
        response_context = MagicMock()
        response_context.__enter__.return_value = response
        opener.open.side_effect = [TimeoutError("The read operation timed out"), response_context]
        build_opener.return_value = opener

        status, detail = audit.check_url("https://img.shields.io/test.svg", "https://img.shields.io/test.svg")

        self.assertEqual(status, "ok")
        self.assertIn("OK 200", detail)
        self.assertEqual(opener.open.call_count, 2)
        sleep.assert_called_once()

    @patch.object(audit.time, "sleep")
    @patch.object(audit, "validate_public_http_url")
    @patch.object(audit.urllib.request, "build_opener")
    def test_repeated_transient_timeout_is_warning(self, build_opener, validate, sleep):
        opener = MagicMock()
        opener.open.side_effect = TimeoutError("The read operation timed out")
        build_opener.return_value = opener

        status, detail = audit.check_url("https://img.shields.io/test.svg", "https://img.shields.io/test.svg")

        self.assertEqual(status, "warn")
        self.assertIn("WARN TRANSIENT", detail)
        self.assertEqual(opener.open.call_count, 2)

    @patch.object(audit, "validate_public_http_url")
    @patch.object(audit.urllib.request, "build_opener")
    def test_hard_http_failure_still_fails(self, build_opener, validate):
        opener = MagicMock()
        opener.open.side_effect = urllib.error.HTTPError(
            "https://example.com/missing", 404, "not found", {}, None
        )
        build_opener.return_value = opener

        status, detail = audit.check_url("https://example.com/missing", "https://example.com/missing")

        self.assertEqual(status, "fail")
        self.assertEqual(detail[1], 404)



    @patch.object(audit, "check_url")
    def test_audit_success(self, mock_check_url):
        mock_check_url.return_value = ("ok", "OK 200 https://example.com")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            doc = root / "doc.md"
            doc.write_text("# Test")
            readme = root / "README.md"
            readme.write_text("[Doc](doc.md) [Anchor](#section) [Mail](mailto:test@example.com) [Ext](https://example.com)")
            with patch("sys.stdout", new=io.StringIO()):
                result = audit.audit(readme)
            self.assertEqual(result, 0)
            mock_check_url.assert_called_once_with("https://example.com", "https://example.com")

    @patch.object(audit, "check_url")
    def test_audit_external_warning_returns_zero(self, mock_check_url):
        mock_check_url.return_value = ("warn", "WARN 429 https://example.com")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = root / "README.md"
            readme.write_text("[Ext](https://example.com)")
            with patch("sys.stdout", new=io.StringIO()):
                result = audit.audit(readme)
            self.assertEqual(result, 0)

    @patch.object(audit, "check_url")
    def test_audit_external_failure_returns_one(self, mock_check_url):
        mock_check_url.return_value = ("fail", ("https://example.com", 404, "Not Found"))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = root / "README.md"
            readme.write_text("[Ext](https://example.com)")
            with patch("sys.stdout", new=io.StringIO()):
                result = audit.audit(readme)
            self.assertEqual(result, 1)

    @patch.object(audit, "resolve_link")
    def test_audit_unsafe_url_returns_one(self, mock_resolve_link):
        mock_resolve_link.side_effect = audit.UnsafeURL("Unsafe link")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = root / "README.md"
            readme.write_text("[Unsafe](http://unsafe.com)")
            with patch("sys.stdout", new=io.StringIO()):
                result = audit.audit(readme)
            self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
