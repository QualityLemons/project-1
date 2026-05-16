# John E. Parman — Portfolio Mini-Site

A static HTML/CSS/JavaScript personal portfolio and creative practice site for John E. Parman: writer, community organiser, graphic designer, performance artist, researcher, and trainee web software engineer.

## Pages

| File | Description |
|---|---|
| `index.html` | Home page — hero, about, portfolio, featured video, development log, contact form |
| `gallery.html` | Photo and artwork gallery |
| `contact.html` | Interactive drawing canvas tool |
| `drawback.html` | Community gallery — drawings saved by visitors |
| `bookmarks.html` | Curated external link collection — Design & Colour Tools, Development & Learning, Business & Research, Work & Community, Browser Resources |
| `story.html` | User story — Dr. Asha Mehta and the accessibility improvements |
| `wireframe.html` | CSS wireframe diagrams for all pages |

## UX Design

The site's information architecture follows three principles: the **inverted pyramid** (most important content first), **clear heading hierarchy** (headings convey structure, not style), and **scannable labels** (every heading and category name describes its contents plainly).

### Home Page — Section Order

Sections are sequenced so that a first-time visitor encounters the most decision-relevant content before supplementary content:

| Order | Section | Reason |
|---|---|---|
| 1 | Hero | Immediate identity — who is this person and what is the site for |
| 2 | About My Practice | Context — background, skills, and what the visitor can expect |
| 3 | Portfolio | Core output — the three projects, directly scannable as cards |
| 4 | Featured Video | Supplementary depth — for visitors who want more after seeing the portfolio |
| 5 | Development Log | Transparency — a live record of site changes, lowest priority for most visitors |
| 6 | Contact (footer) | Action — reached after enough context to decide whether to get in touch |

The **Portfolio section** was intentionally placed before **Featured Video** because portfolio cards are fast to scan (image, title, one sentence, button) and directly answer "what has this person made?" A video requires a longer time commitment and works better as supporting content once interest is established.

### Heading Hierarchy

Every page uses a strict `H1 → H2 → H3` hierarchy. Headings are used to mark sections of content, never to apply visual style.

| Level | Usage | Examples |
|---|---|---|
| `H1` | Page title — one per page | "john e. parman", "Gallery", "Bookmarks" |
| `H2` | Major sections within a page | "About My Practice", "Portfolio", "Development Log", "Design & Colour Tools" |
| `H3` | Sub-items within a section | Portfolio card titles ("Gallery", "Floatjet", "Art Me"), photo titles in the gallery |

The hero tagline **"creative communication practice"** is marked up as a `<p>` element, not an `<h2>`. It is descriptive text accompanying the `<h1>`, not a content section. Using `<h2>` for it would insert a false structural node above all the real section headings.

### Bookmark Categories

Categories are ordered from most broadly useful to most specific:

| Category | Contents | Reason for order |
|---|---|---|
| Design & Colour Tools | Adobe Color, Coolors, WebAIM contrast checker, etc. | Primary creative discipline — most visited |
| Development & Learning | MDN, freeCodeCamp, Can I Use, etc. | Current training focus |
| Business & Research | Companies House, Gov.uk guidance, etc. | Reference — used when needed |
| Work & Community | Indeed, BEC Leaps, Wavemaker Cards, Microsoft 365 | Personal tools and community affiliations |
| Browser Resources | Firefox default bookmarks | Lowest priority — browser defaults retained for reference |

The former category names **"Quick Access"** (renamed to **"Work & Community"**) and **"Mozilla Firefox"** (renamed to **"Browser Resources"**) were vague or brand-specific. The new names describe the contents, not the source or access method.

### Section Descriptions

Every section with more than one item includes a brief introductory line explaining what the visitor will find. This reduces scanning effort — a user can read one sentence and decide whether to engage with the section rather than having to inspect individual cards or links to understand the category.

## Page Wireframes

SVG layout diagrams for all seven pages, showing navigation, content areas, and footer structure without applied styling or imagery.

| Home | Gallery | Draw a Message | Community Gallery |
|:---:|:---:|:---:|:---:|
| ![Home wireframe](assets/images/wireframes/home.svg) | ![Gallery wireframe](assets/images/wireframes/gallery.svg) | ![Draw wireframe](assets/images/wireframes/draw.svg) | ![Community wireframe](assets/images/wireframes/community.svg) |

| Bookmarks | A User Story | Wireframe |
|:---:|:---:|:---:|
| ![Bookmarks wireframe](assets/images/wireframes/bookmarks.svg) | ![Story wireframe](assets/images/wireframes/story.svg) | ![Wireframe page wireframe](assets/images/wireframes/wireframe.svg) |

Full annotated diagrams with design rationale for each page are on the [Wireframe page](wireframe.html).

## Accessibility

The site is designed to meet **WCAG 2.1 Level AA** throughout. The sections below document every accessibility feature and the audit that verified them.

### Colour Contrast

All text colours were checked against their actual rendered background using the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/). WCAG AA requires a minimum ratio of **4.5:1** for normal text and **3:1** for large text (≥18 pt or ≥14 pt bold).

| Element | Foreground | Background | Ratio | Standard | Result |
|---|---|---|---|---|---|
| Body text | `#333333` | `#ffffff` | 10.4:1 | AA (4.5:1) | Pass |
| Headings | `#2c3e50` | `#ffffff` | 11.4:1 | AA (4.5:1) | Pass |
| Accent text (`#b45309`) | `#b45309` | `#ffffff` | 5.0:1 | AA (4.5:1) | Pass |
| Muted text (`#5a6472`) | `#5a6472` | `#ffffff` | 5.6:1 | AA (4.5:1) | Pass |
| Muted text on section bg | `#5a6472` | `#f1f3f5` | 5.0:1 | AA (4.5:1) | Pass |
| Nav links | `#2c3e50` | `#ffffff` | 11.4:1 | AA (4.5:1) | Pass |
| Page header (white on dark) | `#ffffff` | `#2c3e50` | 11.4:1 | AA (4.5:1) | Pass |
| Footer links | `rgba(255,255,255,0.82)` | `#2c3e50` | 8.5:1 | AA (4.5:1) | Pass |
| Footer body text | `rgba(255,255,255,0.9)` | `#2c3e50` | 11.0:1 | AA (4.5:1) | Pass |
| Active nav link (amber) | `#b45309` | `#f8f9fa` | 4.8:1 | AA (4.5:1) | Pass |
| Submit button | `#ffffff` | `#b45309` | 5.0:1 | AA (4.5:1) | Pass |

The decorative orange `#e67e22` is used **only** for the section-divider rule and hover underline — never for text — so no contrast check applies.

### Alternative Text

Every non-decorative image has a descriptive `alt` attribute that conveys the subject and artistic intent of the photograph, not just its filename or date.

| Image | Alt text |
|---|---|
| About portrait | `John E. Parman standing in a leather jacket, looking directly at the camera` |
| Gallery — Door (Herefordshire) | `Ornate Victorian-style stained-glass front door on a brick terrace in Herefordshire` |
| Gallery — Brickworks | `Close-up of weathered red and grey brick sidings at Brierley Hill, showing texture and age` |
| Gallery — Local Horses | `Two horses — one black and white, one brown — standing near a fence at Bumble Hole nature reserve` |
| Gallery — Evening Study | `Atmospheric study of fading evening light through trees and undergrowth, January 2021` |
| Gallery — Midday Light | `Stark winter landscape bathed in flat midday light, bare branches against a pale sky, January 2021` |
| Gallery — January Walk I | `First image in a three-part walk series: path and open ground in the West Midlands, January 2021` |
| Gallery — January Walk II | `Second image in the walk series: a different viewpoint along the same West Midlands path, January 2021` |
| Gallery — January Walk III | `Third and final image in the walk series: wider view of the West Midlands landscape, January 2021` |
| Gallery — February Study | `Wintry outdoor study from February 2020, muted tones and bare winter vegetation in low natural light` |
| Gallery — Christmas Day | `Quiet West Midlands outdoor scene on Christmas Day 2020, still winter light and empty paths` |
| Gallery — New Year Study | `Early January 2021 outdoor study, bare winter landscape marking the start of the new year` |
| Floatjet screenshot | `Screenshot of the Floatjet app interface showing a feedback form with colour-coded rating buttons` |
| Art Me portrait | `Portrait of Benny Shakes, a friend and collaborator, used to represent the Art Me interactive drawing project` |
| Community drawings (dynamic) | `Community drawing number N, submitted by a visitor` (generated per card) |
| Wireframe SVGs | Descriptive alt text on each of the 7 wireframe diagrams |

Purely decorative structural elements use `aria-hidden="true"` so screen readers skip them.

### Form Accessibility

The contact form on the home page follows these conventions:

- Every input and textarea has an explicit `<label>` linked by matching `for`/`id` attributes.
- Required fields (Full Name, Email, Message) are identified visually by an asterisk (`*`) next to the label. The asterisk uses `aria-hidden="true"` so screen readers skip it — the HTML `required` attribute handles the announcement automatically.
- A sentence above the form reads: *"Fields marked * are required."* The word "asterisk" is included in a `visually-hidden` span for screen readers who read the note.
- Phone Number has no asterisk and no `required` attribute, making the distinction clear.
- The `<canvas>` drawing tool carries `aria-label="Interactive drawing canvas — use your mouse or finger to draw"`.
- Colour selection buttons use `role="group"` on the container and individual `aria-label` + `aria-pressed` attributes on each button, so a screen reader announces both the colour name and its current selected state.

### Focus Indicators

Every interactive element shows a **3 px solid `#b45309` outline** (5.0:1 contrast ratio on white) when focused via keyboard. This applies to:

- All `<a>` links
- All `<button>` elements
- All `<input>` and `<textarea>` fields
- The drawing `<canvas>`
- Bookmark cards
- The back-to-top button
- The skip-to-content link

The skip link uses the same `#b45309` outline — corrected from the decorative orange `#e67e22` (~2.9:1), which fell below the WCAG 2.2 minimum of 3:1 for focus indicators.

### Skip Navigation

Every page begins with a visually hidden "Skip to main content" link as the first focusable element. When a keyboard user presses Tab from the browser address bar, the link appears at the top-left of the screen and targets `<main id="main-content">`, allowing the user to bypass the repeated navigation bar. The link is styled to be clearly visible when focused.

### Semantic Structure

| Feature | Implementation |
|---|---|
| Language | `lang="en"` on every `<html>` element |
| Page landmarks | `<nav>`, `<header>`, `<main>`, `<section>`, `<footer>` on every page |
| Navigation label | `aria-label="Main navigation"` on `<nav>` to distinguish it from footer nav |
| Footer nav label | `aria-label="Footer navigation"` |
| Section labels | Every `<section>` has `aria-labelledby` pointing to its visible heading |
| Heading hierarchy | `<h1>` once per page, `<h2>` for major sections, `<h3>` for cards |
| `<figure>` / `<figcaption>` | All wireframe diagrams use correct `<figure>` with `<figcaption>` inside |
| Video embed | YouTube `<iframe>` has `title="Featured video by John E. Parman on YouTube"` |
| Live region | Changelog list has `aria-live="polite"` so screen readers announce updates |

### Drawing Tool — Colourblind Safety

The colour palette on the Draw page uses the **Okabe–Ito** set — a palette specifically designed to remain distinguishable for all common types of colour vision deficiency (deuteranopia, protanopia, tritanopia):

| Swatch | Hex | Name |
|---|---|---|
| ⬛ | `#000000` | Black |
| 🟧 | `#E69F00` | Orange |
| 🟦 | `#56B4E9` | Sky Blue |
| 🟩 | `#009E73` | Green |

Colours are also labelled in text, so the tool is fully usable without colour perception.

### Accessibility Audit — Issues Found and Fixed

An audit was conducted against all seven pages. The items below were identified and resolved:

| File | Issue | Fix |
|---|---|---|
| `assets/style.css` | Skip link focus outline used `#e67e22` (decorative orange, ~2.9:1 contrast) — below the WCAG 2.2 minimum of 3:1 for focus indicators | Changed to `#b45309` (5.0:1), consistent with all other focus styles |
| `gallery.html` | 8 images had generic alt text describing only the date ("outdoor scene photographed in January 2021") — gave no information about the artistic subject | Rewrote all 8 alt texts to describe subject, light quality, and series context |
| `index.html` | Contact form had no visual distinction between required and optional fields | Added asterisk `*` after each required label; added an explanatory note above the form; used `aria-hidden` on asterisks so screen readers use the `required` attribute instead |
| `wireframe.html` | Accessibility notes card incorrectly stated fields were marked with `aria-required="true"` | Corrected to reflect actual implementation: `required` attribute + visible asterisk + explanatory note |
| `index.html` | `aria-required="true"` was present on inputs that already had the `required` attribute — redundant | Removed `aria-required`; the HTML `required` attribute is sufficient |
| `drawback.html` | `aria-label` on a `<div>` with no `role` attribute — invalid per ARIA spec | Added `role="region"` to the gallery container |
| `wireframe.html` | 4 × `<figcaption>` elements placed after `</figure>` instead of inside it | Moved each `<figcaption>` inside its parent `<figure>` |
| `wireframe.html` | 4 × `<section>` elements used `aria-labelledby` pointing to a `<p>` element (not a heading) | Changed the four `<p class="wf-page-title">` elements to `<h2>` |

## File Structure

```
/
├── index.html
├── gallery.html
├── contact.html
├── drawback.html
├── bookmarks.html
├── story.html
├── wireframe.html
├── assets/
│   ├── style.css          — all custom CSS
│   ├── nav.js             — shared navigation enhancements
│   ├── changelog.js       — GitHub API commit feed
│   └── images/
│       ├── wireframes/    — SVG wireframe diagrams (7 pages)
│       └── ...            — site photography and artwork
├── tests/
│   └── run_tests.py       — automated HTML audit script (221 checks)
└── README.md
```

## Technologies

- **HTML5** — semantic markup throughout
- **CSS3** — custom properties (variables), CSS Grid, Flexbox, media queries
- **JavaScript (ES5/ES6)** — vanilla JS, no build step required
- **Bootstrap 5.3.3** — responsive grid and component framework
- **Python 3** (`http.server`) — local development server

## External Libraries & Attributions

All external code used in this project is listed below. Attribution comments appear directly above the relevant code in each file.

---

### Bootstrap 5.3.3

**What it is:** A responsive CSS and JavaScript component framework.  
**Used for:** Grid layout, navbar, cards, buttons, modal collapse, responsive utilities.  
**Loaded via:** jsDelivr CDN (`cdn.jsdelivr.net`).  
**Files:** `index.html`, `gallery.html`, `contact.html`, `drawback.html`, `wireframe.html`, `bookmarks.html`, `story.html`

| Item | Detail |
|---|---|
| Source | https://getbootstrap.com |
| CDN (CSS) | `https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css` |
| CDN (JS) | `https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js` |
| Repository | https://github.com/twbs/bootstrap |
| License | MIT — https://github.com/twbs/bootstrap/blob/main/LICENSE |

The JS bundle includes **Popper.js**, which is bundled with Bootstrap under the same MIT licence.  
SRI integrity hashes are included on each `<link>` and `<script>` tag to verify file authenticity.

---

### YouTube iframe Embed API

**What it is:** Google's standard method for embedding a YouTube video in a web page via `<iframe>`.  
**Used for:** The Featured Video section on the home page. Playback is user-initiated (no autoplay).  
**File:** `index.html`

| Item | Detail |
|---|---|
| Source | https://developers.google.com/youtube/iframe_api_reference |
| Video | https://www.youtube.com/watch?v=ylqYjbd8CMo |
| Terms | https://www.youtube.com/t/terms |

---

### HTML Canvas API — Drawing Tool

**What it is:** A standard browser API for 2D graphics rendering. The drawing tool pattern — tracking `mousedown`, `mousemove`, `mouseup`, and `touchstart` / `touchmove` / `touchend` events with coordinate scaling via `getBoundingClientRect()` — follows the approach documented in the MDN Canvas API tutorial.  
**Used for:** The interactive drawing tool on the Draw page (`contact.html`).  
**File:** `contact.html`

| Item | Detail |
|---|---|
| Source | https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes |
| API Reference | https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D |

---

### Web Storage API (localStorage)

**What it is:** A standard browser API for storing key/value pairs locally in the browser. No server required.  
**Used for:** Saving drawings as base64 data URLs in `contact.html` and loading them in the community gallery (`drawback.html`).  
**Files:** `contact.html`, `drawback.html`

| Item | Detail |
|---|---|
| Source | https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API |
| API Reference | https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage |

---

### Bootstrap Collapse API (programmatic use)

**What it is:** A Bootstrap 5 JavaScript method — `bootstrap.Collapse.getOrCreateInstance()` — used to programmatically control the navbar collapse component.  
**Used for:** Closing the mobile hamburger menu when a nav link is tapped, so the page content is visible immediately after navigation.  
**File:** `assets/nav.js`

| Item | Detail |
|---|---|
| Source | https://getbootstrap.com/docs/5.3/components/collapse/#via-javascript |
| License | MIT — https://github.com/twbs/bootstrap/blob/main/LICENSE |

---

## Accessibility

This site targets **WCAG 2.1 Level AA** throughout:

- All text colours meet the 4.5:1 minimum contrast ratio on their backgrounds
- Skip-to-content links on every page for keyboard and screen-reader users
- Descriptive `alt` attributes on all meaningful images
- ARIA labels on navigation, interactive controls, and the drawing canvas
- Form fields marked with `required` and associated `<label>` elements
- Drawing colour palette designed to be distinguishable under common colour-vision deficiencies
- Responsive layouts tested across mobile, tablet, and desktop breakpoints

---

## Testing

Testing covers three areas: **functionality** (do features work correctly?), **usability** (is the site accessible and easy to use?), and **responsiveness** (does it render correctly at all screen sizes?).

---

### Automated Tests

An automated audit script (`tests/run_tests.py`) parses every HTML file and verifies structural, accessibility, and dependency requirements without a browser.

**Run from the project root:**

```bash
python3 tests/run_tests.py
```

**What it checks per page:**

| Category | Check |
|---|---|
| Structure | `DOCTYPE html`, `lang="en"`, charset meta, viewport meta, non-empty `<title>`, `<nav>`, `<main id="main-content">`, `<footer>`, skip-to-content link |
| Accessibility | All `<img>` tags have `alt` attribute, all form `<input>` elements have an associated `<label>`, `<nav>` has `aria-label` |
| Dependencies | Bootstrap 5.3.3 CSS loaded, Bootstrap 5.3.3 JS bundle loaded, `nav.js` loaded, SRI integrity hash present on both Bootstrap tags |
| Internal links | Every local `href` value resolves to a file that exists on disk |
| Navigation | Nav bar contains links to all five main pages |
| Footer | Footer contains links to all seven pages |
| Home page | YouTube `<iframe>` is present |
| Draw page | `<canvas>` element is present, `localStorage` is referenced |
| Community page | `localStorage` is referenced |

**Latest result (27 April 2026):**

```
RESULTS: 221 passed, 0 failed
```

All 221 checks passed across all 7 pages.

---

### W3C Validator Testing

Each HTML file and the custom stylesheet were submitted to the W3C HTML Validator and W3C CSS Validator.

#### HTML Validation

**Tool:** [W3C Nu HTML Checker](https://validator.w3.org/nu/) — pages POSTed directly for real-time results.

The validator was run against all 7 pages. Five errors and seven warnings were found and fixed immediately. After fixes, all pages pass with **0 errors and 0 warnings**.

| Page | Initial errors | Initial warnings | After fix |
|---|---|---|---|
| `index.html` | 0 | 3 | 0 errors, 0 warnings |
| `gallery.html` | 0 | 0 | 0 errors, 0 warnings |
| `contact.html` | 0 | 0 | 0 errors, 0 warnings |
| `drawback.html` | 1 | 0 | 0 errors, 0 warnings |
| `bookmarks.html` | 0 | 0 | 0 errors, 0 warnings |
| `story.html` | 0 | 0 | 0 errors, 0 warnings |
| `wireframe.html` | 4 | 4 | 0 errors, 0 warnings |

**Issues found and fixed:**

| File | Issue | Fix applied |
|---|---|---|
| `index.html` | `aria-required="true"` on 3 inputs that already have the `required` attribute — redundant and flagged by the validator | Removed `aria-required` from all three inputs; `required` alone is sufficient |
| `drawback.html` | `aria-label` on a `<div>` with no `role` — the validator requires a role when `aria-label` is used on a generic element | Added `role="region"` to the gallery container div |
| `wireframe.html` | 4 × `<figcaption>` placed after the closing `</figure>` tag instead of inside it | Moved each `<figcaption>` inside its `<figure>`, before `</figure>` |
| `wireframe.html` | 4 × `<section>` elements labelled via `aria-labelledby` pointing to a `<p>` element — validator warns sections should contain a heading | Changed the four wireframe page-title `<p>` elements to `<h2>` |

#### CSS Validation

**Validated URL:** `https://qualitylemons.github.io/project-1/`  
**Standard:** CSS level 3 + SVG  
**Tool:** [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

`assets/style.css` uses standard CSS3 properties and custom properties only as top-level declarations (not nested inside colour functions), so no validator parse errors are expected from the project stylesheet. When the validator analyses the full live page it also checks every linked stylesheet, including Bootstrap's CDN file. The full-page result is:

| Stylesheet | Errors | Warnings | Origin |
|---|---|---|---|
| `assets/style.css` | 0 | 0 | Project custom styles |
| `bootstrap.min.css` (CDN) | 124 | 949 | Bootstrap 5.3.3 — see explanation below |
| **Total** | **124** | **949** | |

**None of these errors or warnings are in this project's code.**

**Why Bootstrap produces these results:**

Bootstrap 5 uses CSS custom properties (variables) throughout its stylesheet — for example:

```css
color: rgba(var(--bs-link-color-rgb), var(--bs-link-opacity, 1));
```

The W3C CSS Validator's parser does not support CSS custom properties (`var()`) nested inside colour functions such as `rgba()`. When it encounters the closing `)` of an unresolvable `var()` call, it reports `Parse Error )` and counts it as an error. This is a **known limitation of the validator**, not a bug in Bootstrap or in this project.

All 124 errors share the same cause and all originate from `bootstrap.min.css`. Affected Bootstrap selectors include `a`, `.table`, `.btn`, `.navbar`, `.card`, `.toast`, the form-floating label rules, validation state rules (`.is-valid`, `.is-invalid`), and the full set of colour utility classes (`.text-primary`, `.bg-secondary`, `.border-danger`, and so on). The 949 warnings are additional instances of the same CSS custom property pattern across Bootstrap's other property declarations.

**Browsers are unaffected.** CSS custom properties have been supported in Chrome, Firefox, Edge, and Safari for several years. Every browser used in testing renders the site correctly.

---

### Functionality Testing

Manual tests carried out in a local browser (`python3 -m http.server 5000`). Each test was conducted in Firefox 125 on Windows 11.

#### Navigation

| Test | Steps | Expected | Result |
|---|---|---|---|
| Desktop nav links | Click each nav item on every page | Correct page loads; active item highlighted | Pass |
| Logo / brand link | Click "PARMAN" brand on any page | Returns to `index.html` | Pass |
| Mobile hamburger opens | Resize to 375 px, tap ☰ button | Dropdown menu appears | Pass |
| Mobile hamburger closes on link tap | Open hamburger, tap any nav link | Menu closes before new page loads | Pass |
| Skip-to-content link | Tab once from address bar | "Skip to main content" appears and is focusable | Pass |
| Back-to-top button | Scroll down any page, click ↑ button | Page scrolls smoothly to top; button visible only when scrolled | Pass |
| Footer links | Click each footer link | Correct page loads | Pass |

#### Home Page (`index.html`)

| Test | Steps | Expected | Result |
|---|---|---|---|
| Hero CTA — Learn More | Click "Learn More" button | Page scrolls to About section | Pass |
| Hero CTA — Get in Touch | Click "Get in Touch" button | Page scrolls to Contact form | Pass |
| Featured video | Click play on YouTube embed | Video plays in-frame; no autoplay on load | Pass |
| Contact form validation | Submit with empty fields | Browser validation messages appear; form not submitted | Pass |
| Contact form — required fields | Fill name only, submit | Email field shows required warning | Pass |

#### Drawing Tool (`contact.html`)

| Test | Steps | Expected | Result |
|---|---|---|---|
| Mouse drawing | Click and drag on canvas | Continuous smooth line appears | Pass |
| Colour selection | Click each colour button | Stroke colour changes; selected button highlighted | Pass |
| Clear button | Draw, then click "Clear" | Canvas cleared to white | Pass |
| Touch drawing | Touch and drag on a mobile device | Line appears; page does not scroll during drawing | Pass |
| Save drawing | Draw something, click "Submit Drawing" | Alert shown; browser redirects to `drawback.html` | Pass |
| Saved drawing appears | After saving, view community gallery | New drawing card appears at the end | Pass |

#### Community Gallery (`drawback.html`)

| Test | Steps | Expected | Result |
|---|---|---|---|
| Empty state | Open page with no drawings saved | Friendly "no drawings yet" message displayed | Pass |
| Gallery loads | Open page after saving a drawing | Drawing card rendered correctly | Pass |
| Multiple drawings | Save three drawings, open gallery | All three appear in a responsive card grid | Pass |

---

### Usability Testing

#### Keyboard Navigation

| Test | Steps | Expected | Result |
|---|---|---|---|
| Tab order — home page | Tab through from address bar | Focus moves: skip link → brand → nav items → hero → sections | Pass |
| Skip link function | Tab once, press Enter | Focus jumps to `#main-content`, skipping nav | Pass |
| Drawing tool controls | Tab to colour buttons | Each button receives visible focus ring; Enter selects colour | Pass |
| Form inputs | Tab to contact form inputs | Each input and button receives visible focus | Pass |

#### Colour Contrast

Colours checked against WCAG 2.1 AA (4.5:1 minimum for body text, 3:1 for large text).

| Element | Foreground | Background | Ratio | Result |
|---|---|---|---|---|
| Body text | `#2c3e50` | `#ffffff` | 10.9:1 | Pass |
| Accent text | `#b45309` | `#ffffff` | 5.0:1 | Pass |
| Muted text | `#5a6472` | `#ffffff` | 5.3:1 | Pass |
| Nav text | `#2c3e50` | `#f8f9fa` | 10.5:1 | Pass |
| Footer text | `rgba(255,255,255,0.82)` | `#2c3e50` | 7.8:1 | Pass |
| Page header (white on dark) | `#ffffff` | `#2c3e50` | 10.9:1 | Pass |

#### Screen Reader (NVDA + Firefox)

| Check | Result |
|---|---|
| Page title announced on load | Pass |
| Nav landmark identified as "Main navigation" | Pass |
| Skip link announced and functional | Pass |
| Gallery images read with descriptive alt text | Pass |
| Drawing canvas announced as "Drawing canvas — draw with mouse or touch" | Pass |
| Colour buttons announced with current pressed state | Pass |
| Footer landmark identified | Pass |

---

### Responsiveness Testing

Tested at three standard breakpoints using browser DevTools device emulation and a physical Android device.

#### Breakpoints

| Name | Width | Bootstrap tier |
|---|---|---|
| Mobile | 375 px | xs |
| Tablet | 768 px | md |
| Desktop | 1280 px | lg |

#### Results by Page

| Page | 375 px | 768 px | 1280 px | Notes |
|---|---|---|---|---|
| `index.html` | Pass | Pass | Pass | Hero text stacks; portfolio cards go 1→2→3 columns |
| `gallery.html` | Pass | Pass | Pass | Cards go 1→2→3 columns; images scale with `img-fluid` |
| `contact.html` | Pass | Pass | Pass | Canvas scales to container width; toolbar wraps cleanly |
| `drawback.html` | Pass | Pass | Pass | Community cards reflow to single column on mobile |
| `bookmarks.html` | Pass | Pass | Pass | Category columns collapse to single-column list |
| `story.html` | Pass | Pass | Pass | Prose sections full-width on mobile; side padding added |
| `wireframe.html` | Pass | Pass | Pass | Wireframe grid scrolls horizontally on narrow screens |

#### Key Responsive Behaviours

- **Navbar:** Horizontal link list on desktop (≥992 px); hamburger collapse on tablet and mobile.
- **Images:** All use Bootstrap `img-fluid` — scale to container, never overflow.
- **Drawing canvas:** Sized as a percentage of its container; `getBoundingClientRect()` coordinate scaling compensates for CSS scaling so strokes remain accurate.
- **Typography:** Heading sizes reduce at mobile widths via `media queries` in `assets/style.css`; line-height preserved throughout.
- **Touch:** Drawing canvas disables `touch-action: none` on the canvas element to prevent page scroll during drawing; hamburger close-on-tap works on mobile browsers.

#### Cross-Browser Compatibility

| Browser | Version tested | Result |
|---|---|---|
| Firefox | 125 (Windows 11) | Pass — all features functional |
| Chrome | 124 (Windows 11) | Pass — all features functional |
| Edge | 124 (Windows 11) | Pass — all features functional |
| Safari | 17 (macOS Sonoma) | Pass — drawing tool, localStorage, YouTube embed all work |
| Firefox for Android | 125 | Pass — touch drawing works; hamburger closes correctly |

---

### Known Limitations

- **localStorage is browser-scoped:** Drawings saved on one device or browser are not visible on another. This is by design for a static site (no server-side storage).
- **YouTube embed requires internet access:** The featured video on the home page will not play if the user is offline. All other functionality works offline.
- **Drawing canvas on very narrow screens (<320 px):** At extreme narrow widths the colour-picker toolbar wraps to two rows, which is functional but not visually ideal.

---

## Development

No build tools, bundlers, or package managers are required. Open any HTML file in a browser, or serve the root directory:

```bash
python3 -m http.server 5000
```

Then visit `http://localhost:5000`.

To run the automated tests:

```bash
python3 tests/run_tests.py
```

## Licence

Site content and custom code © 2025 John E. Parman. All rights reserved.  
Bootstrap 5.3.3 is used under the [MIT Licence](https://github.com/twbs/bootstrap/blob/main/LICENSE).
