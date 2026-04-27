# John E. Parman — Portfolio Mini-Site

A static HTML/CSS/JavaScript personal portfolio and creative practice site for John E. Parman: writer, community organiser, graphic designer, performance artist, researcher, and trainee web software engineer.

## Pages

| File | Description |
|---|---|
| `index.html` | Home page — hero, about, portfolio, featured video, contact form |
| `gallery.html` | Photo and artwork gallery |
| `contact.html` | Interactive drawing canvas tool |
| `drawback.html` | Community gallery — drawings saved by visitors |
| `bookmarks.html` | Curated external link collection in five categories |
| `story.html` | User story — Dr. Asha Mehta and the accessibility improvements |
| `wireframe.html` | CSS wireframe diagrams for all pages |

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
│   ├── style.css       — all custom CSS
│   ├── nav.js          — shared navigation enhancements
│   └── images/         — local image assets
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

## Development

No build tools, bundlers, or package managers are required. Open any HTML file in a browser, or serve the root directory:

```bash
python3 -m http.server 5000
```

Then visit `http://localhost:5000`.

## Licence

Site content and custom code © 2025 John E. Parman. All rights reserved.  
Bootstrap 5.3.3 is used under the [MIT Licence](https://github.com/twbs/bootstrap/blob/main/LICENSE).
