import sys
import importlib.util
from pathlib import Path

# Load the script dynamically because it has hyphens in the filename
script_path = Path(__file__).parent.parent / "scripts" / "profile-link-audit.py"
spec = importlib.util.spec_from_file_location("profile_link_audit", script_path)
profile_link_audit = importlib.util.module_from_spec(spec)
sys.modules["profile_link_audit"] = profile_link_audit
spec.loader.exec_module(profile_link_audit)

extract_urls = profile_link_audit.extract_urls

def test_markdown_link():
    assert extract_urls("[link text](https://example.com)") == ["https://example.com"]

def test_markdown_image():
    assert extract_urls("![alt text](https://example.com/image.png)") == ["https://example.com/image.png"]

def test_html_link():
    assert extract_urls("<a href=\"https://example.com\">link text</a>") == ["https://example.com"]

def test_html_image():
    assert extract_urls("<img src=\"https://example.com/image.png\" alt=\"alt text\" />") == ["https://example.com/image.png"]

def test_html_link_single_quotes():
    assert extract_urls("<a href='https://example.com'>link text</a>") == ["https://example.com"]

def test_markdown_link_with_title():
    assert extract_urls("[link text](https://example.com \"Title\")") == ["https://example.com"]

def test_markdown_image_with_title():
    assert extract_urls("![alt text](https://example.com/image.png \"Title\")") == ["https://example.com/image.png"]

def test_multiple_urls():
    text = "[link1](https://example1.com) and ![img](https://example2.com/img.png) and <a href='https://example3.com'>link3</a>"
    assert extract_urls(text) == ["https://example1.com", "https://example2.com/img.png", "https://example3.com"]

def test_malformed_link():
    # Should not match
    assert extract_urls("[link](https://example.com") == []
    assert extract_urls("link](https://example.com)") == []
    assert extract_urls("<a href=https://example.com>link</a>") == []

def test_url_with_spaces_in_title():
    assert extract_urls("[link text](https://example.com/path  \"Title\")") == ["https://example.com/path"]

def test_url_with_query_params():
    assert extract_urls("[link text](https://example.com/path?key=value&other=1)") == ["https://example.com/path?key=value&other=1"]

def test_url_with_fragment():
    assert extract_urls("[link text](https://example.com/path#fragment)") == ["https://example.com/path#fragment"]
