## 2024-07-24 - Accessible Badges
**Learning:** Standard static markdown badges and status shields often lack `alt` text, making them completely opaque to screen readers, creating a "black hole" of information in important areas like tech stacks or status.
**Action:** Always add descriptive `alt` attributes to `<img>` tags used for badges (e.g. `alt="Stripe Live Revenue"` or `alt="Local-First System"`) so assistive technologies can read their intended meaning.

## 2024-07-25 - Bare URLs
**Learning:** Bare URLs in Markdown files are often read character-by-character by screen readers, making them tedious and unhelpful for visually impaired users to consume.
**Action:** Always format URLs as descriptive Markdown links, or explicitly as clickable links (e.g. `[Stripe checkout](https://...)` or `<https://...>`), to provide better context and a smoother screen reader experience.

## 2024-07-26 - Image-Only Link Labels
**Learning:** In GitHub Flavored Markdown, wrapper `<a>` elements for image-only links have `aria-label` attributes stripped by the HTML sanitizer. Attempting to add an `aria-label` to the wrapper will not work.
**Action:** For image-only links in Markdown where `aria-label` is unsupported, modify the `alt` attribute of the `<img>` itself to describe the destination of the link (e.g. `alt="View GitHub Profile Stats"`) rather than describing the image, adhering to W3C web accessibility guidelines.
