/* nav.js — shared navigation enhancements */

(function () {
    'use strict';

    /* -------------------------------------------------------
       1. Back-to-top button
       Creates the button via JS so every page gets it from
       one file rather than duplicating HTML in six templates.
    ------------------------------------------------------- */
    var btn = document.createElement('button');
    btn.id = 'backToTop';
    btn.setAttribute('aria-label', 'Back to top');
    btn.innerHTML = '&#8679;';
    document.body.appendChild(btn);

    window.addEventListener('scroll', function () {
        btn.classList.toggle('visible', window.scrollY > 300);
    }, { passive: true });

    btn.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    /* -------------------------------------------------------
       2. Mobile hamburger: close the menu when any nav link
       is tapped. Without this, anchor links on the home page
       (About, Portfolio, Contact) leave the menu open after
       the page scrolls — confusing on phones and tablets.
    ------------------------------------------------------- */
    var navCollapse = document.getElementById('navbarMain');
    if (navCollapse) {
        document.querySelectorAll('.navbar-nav .nav-link').forEach(function (link) {
            link.addEventListener('click', function () {
                if (navCollapse.classList.contains('show')) {
                    var bsCollapse = bootstrap.Collapse.getOrCreateInstance(navCollapse);
                    bsCollapse.hide();
                }
            });
        });
    }
}());
