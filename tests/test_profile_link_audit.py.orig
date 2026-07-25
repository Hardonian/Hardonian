import pytest
from unittest.mock import patch, MagicMock
import runpy
import urllib.error
import io
import sys
from pathlib import Path

def run_script(monkeypatch, readme_content):
    monkeypatch.setattr('pathlib.Path.read_text', lambda self: readme_content)

    # Capture stdout to verify prints and avoid cluttering test output
    captured_output = io.StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)

    try:
        runpy.run_path('scripts/profile-link-audit.py')
        exit_code = 0
    except SystemExit as e:
        exit_code = e.code

    return exit_code, captured_output.getvalue()

@patch('urllib.request.urlopen')
def test_successful_external_link(mock_urlopen, monkeypatch):
    mock_cm = MagicMock()
    mock_cm.status = 200
    mock_cm.__enter__.return_value = mock_cm
    mock_urlopen.return_value = mock_cm

    code, out = run_script(monkeypatch, "[Example](https://example.com)")

    assert code == 0
    assert "OK 200 https://example.com" in out
    assert "CHECKED 1 UNIQUE_LINKS_AND_IMAGES; FAILURES 0" in out

@patch('urllib.request.urlopen')
def test_failed_external_link(mock_urlopen, monkeypatch):
    mock_urlopen.side_effect = urllib.error.HTTPError("https://example.com", 404, "Not Found", {}, None)

    code, out = run_script(monkeypatch, "[Example](https://example.com)")

    assert code == 1
    assert "FAIL 404 https://example.com" in out
    assert "FAILURES 1" in out

@patch('pathlib.Path.exists')
def test_successful_local_link(mock_exists, monkeypatch):
    mock_exists.return_value = True

    code, out = run_script(monkeypatch, "[Example](products/test.md)")

    assert code == 0
    assert "LOCAL 200 products/test.md" in out
    assert "CHECKED 1 UNIQUE_LINKS_AND_IMAGES; FAILURES 0" in out

@patch('pathlib.Path.exists')
def test_missing_local_link(mock_exists, monkeypatch):
    mock_exists.return_value = False

    code, out = run_script(monkeypatch, "[Example](products/test.md)")

    assert code == 1
    assert "FAILURES 1" in out

def test_ignored_links(monkeypatch):
    code, out = run_script(monkeypatch, "[Example1](#anchor) [Example2](mailto:test@example.com)")

    assert code == 0
    assert "CHECKED 1 UNIQUE_LINKS_AND_IMAGES" in out

@patch('urllib.request.urlopen')
def test_http_warnings(mock_urlopen, monkeypatch):
    for status in [403, 429, 999]:
        mock_urlopen.side_effect = urllib.error.HTTPError("https://example.com", status, "Warning", {}, None)

        code, out = run_script(monkeypatch, "[Example](https://example.com)")

        assert code == 0
        assert f"WARN {status} https://example.com" in out
