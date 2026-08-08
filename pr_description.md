💡 **What:** Refactored sequential network requests into concurrent requests using ThreadPoolExecutor.
🎯 **Why:** The sequential loop made the script network-bound, taking upwards of 23 seconds.
📊 **Measured Improvement:** Baseline performance was ~23s. After using concurrent fetches with a max worker pool of 10, the time drops to ~2.7s.
