import unittest
import sys
import os

# Add scripts directory to path to import profile-link-audit
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
profile_link_audit = __import__('profile-link-audit')

class TestProfileLinkAudit(unittest.TestCase):
    def setUp(self):
        self.extract_urls = profile_link_audit.extract_urls

    def test_markdown_image(self):
        text = "![alt text](https://example.com/image.jpg)"
        self.assertEqual(self.extract_urls(text), ["https://example.com/image.jpg"])

    def test_markdown_link(self):
        text = "[link text](https://example.com)"
        self.assertEqual(self.extract_urls(text), ["https://example.com"])

    def test_html_a_tag(self):
        text = '<a href="https://example.com">link</a>'
        self.assertEqual(self.extract_urls(text), ["https://example.com"])

    def test_html_img_tag(self):
        text = '<img src="https://example.com/image.jpg" />'
        self.assertEqual(self.extract_urls(text), ["https://example.com/image.jpg"])

    def test_html_single_quotes(self):
        text = "<a href='https://example.com'>link</a>"
        self.assertEqual(self.extract_urls(text), ["https://example.com"])

    def test_markdown_with_title(self):
        text = '[link text](https://example.com "title here")'
        # The script does split(' ')[0], so title shouldn't be included
        self.assertEqual(self.extract_urls(text), ["https://example.com"])

    def test_url_with_spaces_and_title(self):
        text = '[link text](https://example.com/path with spaces "title")'
        # It splits on the first space, so a url with unescaped spaces breaks
        self.assertEqual(self.extract_urls(text), ["https://example.com/path"])

    def test_multiple_on_same_line(self):
        text = "[link1](url1) and ![img2](url2) and <a href='url3'>link</a>"
        self.assertEqual(self.extract_urls(text), ["url1", "url2", "url3"])

    def test_empty_url(self):
        text = "[]()"
        # Next regex check won't match, or it will extract empty string which doesn't get appended because of `if u:`
        self.assertEqual(self.extract_urls(text), [])

    def test_malformed_tags(self):
        text = "![alt]( or [link]( or <a href= >"
        self.assertEqual(self.extract_urls(text), [])

    def test_complex_markdown(self):
        text = """
        # Header
        Here is a [link](https://github.com).
        And an image ![cat](cat.png).
        And some html <img src="dog.png" alt="dog">
        """
        self.assertEqual(self.extract_urls(text), ["https://github.com", "cat.png", "dog.png"])

if __name__ == '__main__':
    unittest.main()
