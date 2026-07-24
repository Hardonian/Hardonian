
<!-- AI Automated Systems Analytics -->
<script>
(function() {
    const sessionId = sessionStorage.getItem('aas_sid') || ('s' + Date.now() + Math.random().toString(36).substr(2, 8));
    sessionStorage.setItem('aas_sid', sessionId);

    // Track page view
    fetch('https://aiautomatedsystems.ca/api/track', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            event: 'page_view',
            page: window.location.pathname,
            referrer: document.referrer,
            session_id: sessionId,
        })
    }).catch(() => {});

    // Track checkout clicks
    document.addEventListener('click', function(e) {
        const link = e.target.closest('a[href*="buy.stripe.com"], a[href*="checkout"]');
        if (link) {
            const slug = window.location.pathname.split('/').pop() || 'unknown';
            fetch('https://aiautomatedsystems.ca/api/track', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    event: 'checkout_click',
                    product_slug: slug,
                    checkout_url: link.href,
                    session_id: sessionId,
                })
            }).catch(() => {});
        }
    });
})();
</script>
<!-- End Analytics -->
