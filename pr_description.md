🎯 **What:** Removed unused/dead functions (`check_url`, `extract_urls`, `resolve_local_or_target`, etc.) from `scripts/profile-link-audit.py` that were duplicated or never called.
💡 **Why:** These functions were defined but never used, as the `audit()` function handles all logic inline. Removing them improves maintainability, reduces file size, and avoids confusion.
✅ **Verification:** Ran `python -m unittest discover -s tests` and `python scripts/profile-link-audit.py` to verify functionality is preserved.
✨ **Result:** A cleaner, smaller, more maintainable script without dead code.
