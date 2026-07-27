## 2024-07-24 - Accessible Badges
**Learning:** Standard static markdown badges and status shields often lack `alt` text, making them completely opaque to screen readers, creating a "black hole" of information in important areas like tech stacks or status.
**Action:** Always add descriptive `alt` attributes to `<img>` tags used for badges (e.g. `alt="Stripe Live Revenue"` or `alt="Local-First System"`) so assistive technologies can read their intended meaning.

## 2024-07-25 - Bare URLs
**Learning:** Bare URLs in Markdown files are often read character-by-character by screen readers, making them tedious and unhelpful for visually impaired users to consume.
**Action:** Always format URLs as descriptive Markdown links, or explicitly as clickable links (e.g. `[Stripe checkout](https://...)` or `<https://...>`), to provide better context and a smoother screen reader experience.

## 2026-07-23 - GitHub Aria Attribute Stripping
**Learning:** GitHub's Markdown rendering pipeline strips `aria-*` attributes (such as `aria-label`) from user-supplied HTML tags. This makes it impossible to use `aria-label` directly on `<a>` tags surrounding images in standard Markdown files on GitHub.
**Action:** For image-only links, use the `alt` text of the inner `<img>` to describe the link's destination (e.g., `alt="Visit the Python website"`) instead of just describing the image itself, ensuring the link remains accessible.

## 2024-07-25 - Contextual Links in Markdown
**Learning:** Generic template links like "Stripe checkout" or "Hardonian README" create a poor experience for screen reader users navigating via a links list, as the context is lost without surrounding text.
**Action:** Always provide descriptive context in link text, especially in template-generated content (e.g., "Purchase [Product Name] via Stripe"), to comply with WCAG SC 2.4.4. Apply the same principle to image alt texts for non-decorative images to meet SC 1.1.1.
