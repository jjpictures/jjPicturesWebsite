document.addEventListener("DOMContentLoaded", function() {
    var links = document.querySelectorAll('a');
    links.forEach(function(link) {
        link.addEventListener('click', function(event) {
            var href = link.getAttribute('href');
            if (href.startsWith('#')) {  // Only handle internal anchor links
                event.preventDefault();
                smoothScroll(href);
            }
        });
    });

    function smoothScroll(target) {
        var targetElement = document.querySelector(target);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop,
                behavior: 'smooth'
            });
        }
    }
});
