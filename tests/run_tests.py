#!/usr/bin/env python3
"""
Automated audit for the John E. Parman portfolio site.
Tests: HTML structure, accessibility, internal link validity,
       Bootstrap presence, nav/footer consistency, and interactive features.
Run from the project root: python3 tests/run_tests.py
"""

import os
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HTML_FILES = [
    'index.html',
    'gallery.html',
    'contact.html',
    'drawback.html',
    'wireframe.html',
    'bookmarks.html',
    'story.html',
]

EXPECTED_NAV_LINKS = ['index.html', 'gallery.html', 'contact.html', 'drawback.html', 'bookmarks.html']
EXPECTED_FOOTER_LINKS = ['index.html', 'gallery.html', 'contact.html', 'drawback.html', 'bookmarks.html', 'story.html', 'wireframe.html']
BOOTSTRAP_CSS = 'bootstrap@5.3.3/dist/css/bootstrap.min.css'
BOOTSTRAP_JS  = 'bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js'
NAV_JS = 'assets/nav.js'

PASS = '\033[32mPASS\033[0m'
FAIL = '\033[31mFAIL\033[0m'
INFO = '\033[33mINFO\033[0m'


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = None
        self.charset = False
        self.viewport = False
        self.title = None
        self.in_title = False
        self.skip_link = False
        self.main_id = None
        self.has_footer = False
        self.has_nav = False
        self.images = []           # list of (src, alt) tuples; alt=None means missing attribute
        self.internal_links = []   # href values for <a> tags
        self.external_scripts = [] # src values for <script> tags
        self.stylesheets = []      # href values for <link rel=stylesheet>
        self.nav_hrefs = []        # links found inside <nav>
        self.footer_hrefs = []     # links found inside <footer>
        self._in_nav = False
        self._in_footer = False
        self.aria_labels = []      # aria-label values
        self.form_inputs = []      # (id, type) tuples
        self.form_labels = []      # for= values
        self.canvas_ids = []       # id attrs of <canvas> elements
        self.localStorage_use = False
        self.youtube_embed = False
        self._current_text = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)

        if tag == 'html':
            self.lang = a.get('lang')
        elif tag == 'meta':
            if a.get('charset'):
                self.charset = True
            if a.get('name') == 'viewport':
                self.viewport = True
        elif tag == 'title':
            self.in_title = True
        elif tag == 'link':
            href = a.get('href', '')
            rel = a.get('rel', '')
            if 'stylesheet' in rel or rel == 'stylesheet':
                self.stylesheets.append(href)
        elif tag == 'script':
            src = a.get('src', '')
            if src:
                self.external_scripts.append(src)
        elif tag == 'nav':
            self._in_nav = True
            self.has_nav = True
            if a.get('aria-label'):
                self.aria_labels.append(('nav', a['aria-label']))
        elif tag == 'footer':
            self._in_footer = True
            self.has_footer = True
        elif tag == 'a':
            href = a.get('href', '')
            if a.get('class') and 'skip-link' in a.get('class', ''):
                self.skip_link = True
            elif 'skip-link' in a.get('class', '') or href == '#main-content':
                self.skip_link = True
            if href and not href.startswith('http') and not href.startswith('#') and not href.startswith('mailto:'):
                self.internal_links.append(href)
            if self._in_nav and href:
                self.nav_hrefs.append(href)
            if self._in_footer and href:
                self.footer_hrefs.append(href)
        elif tag == 'img':
            src = a.get('src', '')
            alt = a.get('alt')  # None if attribute absent, '' if empty string
            self.images.append((src, alt))
        elif tag == 'main':
            self.main_id = a.get('id', '(present, no id)')
        elif tag == 'canvas':
            self.canvas_ids.append(a.get('id', '(no id)'))
        elif tag == 'input':
            if a.get('type') != 'hidden':
                self.form_inputs.append((a.get('id', ''), a.get('type', 'text')))
        elif tag == 'label':
            if a.get('for'):
                self.form_labels.append(a['for'])
        elif tag == 'iframe':
            src = a.get('src', '')
            if 'youtube.com' in src:
                self.youtube_embed = True
        if a.get('aria-label'):
            self.aria_labels.append((tag, a['aria-label']))

    def handle_endtag(self, tag):
        if tag == 'nav':
            self._in_nav = False
        elif tag == 'footer':
            self._in_footer = False
        elif tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title = (self.title or '') + data
        if 'localStorage' in data:
            self.localStorage_use = True


def parse_file(filename):
    path = os.path.join(ROOT, filename)
    with open(path, encoding='utf-8') as f:
        content = f.read()
    p = PageParser()
    p.feed(content)
    return p, content


def check(label, condition, detail=''):
    status = PASS if condition else FAIL
    line = f"  [{status}] {label}"
    if detail:
        line += f" — {detail}"
    print(line)
    return condition


results = {'pass': 0, 'fail': 0}

def c(label, condition, detail=''):
    ok = check(label, condition, detail)
    if ok:
        results['pass'] += 1
    else:
        results['fail'] += 1
    return ok


print("=" * 60)
print("JOHN E. PARMAN — SITE AUDIT")
print("=" * 60)


for filename in HTML_FILES:
    print(f"\n{'─' * 60}")
    print(f"FILE: {filename}")
    print('─' * 60)

    path = os.path.join(ROOT, filename)
    if not os.path.exists(path):
        print(f"  [{FAIL}] File not found — skipping")
        results['fail'] += 1
        continue

    p, content = parse_file(filename)

    # 1. HTML Structure
    print("\n  [STRUCTURE]")
    c("DOCTYPE html present",          '<!DOCTYPE html>' in content or '<!doctype html>' in content.lower())
    c("lang attribute on <html>",      p.lang == 'en',          f"found: {p.lang}")
    c("charset meta present",          p.charset)
    c("viewport meta present",         p.viewport)
    c("Non-empty <title>",             bool(p.title and p.title.strip()),  f"'{p.title}'")
    c("'Parman' in title",             'arman' in (p.title or '').lower())
    c("<nav> present",                 p.has_nav)
    c("<main> present",                p.main_id is not None,   f"id='{p.main_id}'")
    c("<footer> present",              p.has_footer)
    c("Skip-to-content link present",  p.skip_link or '#main-content' in content)

    # 2. Accessibility
    print("\n  [ACCESSIBILITY]")
    missing_alt = [(src, alt) for src, alt in p.images if alt is None]
    empty_alt   = [(src, alt) for src, alt in p.images if alt == '']
    meaningful_imgs = [(src, alt) for src, alt in p.images
                       if alt is not None and alt.strip() == '' and 'aria-hidden' not in content]
    c("All <img> have alt attribute",
      len(missing_alt) == 0,
      f"{len(missing_alt)} missing" if missing_alt else f"{len(p.images)} image(s) checked")
    unlabelled = [i for i in p.form_inputs if i[0] not in p.form_labels]
    c("All form inputs have <label>",
      len(unlabelled) == 0,
      f"{len(unlabelled)} unlabelled" if unlabelled else f"{len(p.form_inputs)} input(s) checked")
    c("Nav has aria-label",
      any(tag == 'nav' for tag, _ in p.aria_labels))

    # 3. External dependencies
    print("\n  [DEPENDENCIES]")
    c("Bootstrap CSS loaded",          any(BOOTSTRAP_CSS in s for s in p.stylesheets))
    c("Bootstrap JS loaded",           any(BOOTSTRAP_JS in s for s in p.external_scripts))
    c("nav.js loaded",                 any(NAV_JS in s for s in p.external_scripts))
    c("SRI integrity on Bootstrap CSS", 'integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"' in content)
    c("SRI integrity on Bootstrap JS",  'integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"' in content)

    # 4. Internal link validity
    print("\n  [INTERNAL LINKS]")
    broken = []
    for href in set(p.internal_links):
        # strip fragment
        base = href.split('#')[0]
        if not base:
            continue
        target = os.path.join(ROOT, base)
        if not os.path.exists(target):
            broken.append(href)
    c("All internal links resolve",
      len(broken) == 0,
      f"broken: {broken}" if broken else f"{len(set(p.internal_links))} link(s) checked")

    # 5. Nav consistency
    print("\n  [NAVIGATION]")
    nav_bases = [h.split('#')[0] for h in p.nav_hrefs if h]
    for expected in EXPECTED_NAV_LINKS:
        c(f"Nav contains link to {expected}", expected in nav_bases)

    # 6. Footer consistency
    print("\n  [FOOTER]")
    footer_bases = [h.split('#')[0] for h in p.footer_hrefs if h]
    for expected in EXPECTED_FOOTER_LINKS:
        c(f"Footer contains link to {expected}", expected in footer_bases)

    # 7. Page-specific checks
    if filename == 'index.html':
        print("\n  [HOME PAGE SPECIFIC]")
        c("YouTube iframe embedded", p.youtube_embed)

    if filename == 'contact.html':
        print("\n  [DRAWING TOOL SPECIFIC]")
        c("Canvas element present",    len(p.canvas_ids) > 0, f"ids: {p.canvas_ids}")
        c("localStorage used",         p.localStorage_use)

    if filename == 'drawback.html':
        print("\n  [COMMUNITY GALLERY SPECIFIC]")
        c("localStorage used",         p.localStorage_use)

print(f"\n{'=' * 60}")
print(f"RESULTS: {results['pass']} passed, {results['fail']} failed")
print("=" * 60)

sys.exit(0 if results['fail'] == 0 else 1)
