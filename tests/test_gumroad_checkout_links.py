"""Guard against restoring Gumroad product URLs confirmed to return 404.

Replacement links require separate verification of seller, product, and delivery.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BROKEN_SLUGS = (
    "upscale-8k", "arch-interior", "ictrbg", "cauzzx", "cqfiev",
    "bsjqfm", "flux-fill", "game-3d-asset", "video-cinema", "voice-avatar",
)


class GumroadCheckoutLinksTest(unittest.TestCase):
    def test_verified_404_urls_are_not_linked_from_product_pages(self):
        for path in (ROOT / "products").glob("*.md"):
            text = path.read_text(encoding="utf-8")
            for slug in BROKEN_SLUGS:
                with self.subTest(page=path.name, slug=slug):
                    self.assertNotIn(f"https://scottrmhardie.gumroad.com/l/{slug})", text)


if __name__ == "__main__":
    unittest.main()
