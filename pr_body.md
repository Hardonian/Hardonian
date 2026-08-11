**💡 What:**
Updated the `alt` text of the image-only profile badges and technology stack links in the README to explicitly describe the destination of the link (e.g., "Visit the Python website") rather than just the image content ("Python").

**🎯 Why:**
For screen reader users, when an image is the sole content of a link, the `alt` text serves as the link text. Generically describing the image creates a poor user experience, especially when navigating via a links list. Providing clear, contextual link destinations complies with WCAG SC 2.4.4. Furthermore, because GitHub strips `aria-label` attributes from user-supplied HTML in Markdown, utilizing the `alt` attribute of the inner `<img>` is the standard and necessary way to make these links accessible.

**📸 Before/After:**
*(Visuals remain unchanged. Screen reader output changes from "Python" to "Visit the Python website")*

**♿ Accessibility:**
Improves screen reader navigation and context for all top-level badge links and technology stack links in the profile README, ensuring compliance with WCAG SC 2.4.4 (Link Purpose In Context).
