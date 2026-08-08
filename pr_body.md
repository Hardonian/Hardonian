🎯 **What:** Removed unused, duplicate, and dead code functions from `scripts/profile-link-audit.py` (including `is_local_only` and others before `def audit()`).

💡 **Why:** These functions were not being called anywhere in the script. The core logic of the script is contained entirely within the `audit()` function. Removing dead code significantly reduces complexity, removes duplication (e.g. `check_url`, `extract_urls` were defined multiple times), and improves overall maintainability of the file.

✅ **Verification:** Verified by running the existing unit tests (`test_profile_link_audit.py`) which assert that `audit()` behaves correctly for internal and external links.

✨ **Result:** The script size is reduced by 110 lines of unused functions, leaving only the required imports, `audit()`, and the execution block. All functionality is fully preserved.
