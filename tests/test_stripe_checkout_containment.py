"""Guard checkout links that returned AccessDenied during browser verification."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "flux-inpaint-outpaint-pro.md": "flux-fill-pack",
    "architectural-interior-design.md": "arch-interior-pack",
    "game-asset-3d-generator.md": "game-3d-asset-pack",
    "voice-to-avatar-lip-sync.md": "voice-avatar-pack",
    "video-production-cinema.md": "video-cinema-pack",
    "advanced-upscale-restoration.md": "upscale-8k-pack",
}


class StripeCheckoutContainmentTest(unittest.TestCase):
    def test_each_affected_checkout_has_an_unavailable_notice_and_no_link(self):
        for page in PAGES:
            with self.subTest(page=page):
                text = (ROOT / "products" / page).read_text(encoding="utf-8")
                self.assertIn("## Checkout / Buy", text, f"Missing checkout section in {page}")
                section = text.split("## Checkout / Buy", 1)[1].split("\n---", 1)[0]
                self.assertIn("Checkout is currently unavailable", section)
                self.assertNotIn("](", section)

    def test_access_denied_urls_are_not_reintroduced_on_any_product_page(self):
        for path in (ROOT / "products").glob("*.md"):
            text = path.read_text(encoding="utf-8")
            for slug in PAGES.values():
                with self.subTest(page=path.name, slug=slug):
                    self.assertNotIn(f"https://buy.stripe.com/{slug}", text)


if __name__ == "__main__":
    unittest.main()
