## 2024-07-24 - Accessible Badges
**Learning:** Standard static markdown badges and status shields often lack `alt` text, making them completely opaque to screen readers, creating a "black hole" of information in important areas like tech stacks or status.
**Action:** Always add descriptive `alt` attributes to `<img>` tags used for badges (e.g. `alt="Stripe Live Revenue"` or `alt="Local-First System"`) so assistive technologies can read their intended meaning.

## 2024-07-25 - Bare URLs
**Learning:** Bare URLs in Markdown files are often read character-by-character by screen readers, making them tedious and unhelpful for visually impaired users to consume.
**Action:** Always format URLs as descriptive Markdown links, or explicitly as clickable links (e.g. `[Stripe checkout](https://...)` or `<https://...>`), to provide better context and a smoother screen reader experience.

## 2026-07-22 - GitHub Markdown ARIA Stripping
**Learning:** GitHub's Markdown rendering pipeline strips `aria-*` attributes (such as `aria-label`) from user-supplied HTML tags. This means standard accessibility techniques for image-only links won't work in README files.
**Action:** For image-only links in GitHub Markdown files, always use the `alt` text of the inner `<img>` tag to describe the link's destination instead of just describing the image itself.
