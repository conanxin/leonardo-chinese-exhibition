# Second Exhibition Staging Browser QA — v5.1

**Round:** v5.1-staging-artifact-build
**Date:** 2026-07-11
**Baseline commit:** `5218b43809fa4ab7a78545797e057d72b51e1826`
**Source tag:** `v4.8-real-second-exhibition-repository-hardening`
**Staging artifact:** `/tmp/leonardo-pages-artifact` (outside repository)

---

## Setup

**Artifact URL:** `http://127.0.0.1:8771/second-exhibition/`

**Server command:**
```bash
python3 -m http.server 8771 --directory /tmp/leonardo-pages-artifact
```

Server serves only the staging artifact root. No connection to production GitHub Pages.

**Browser / Playwright versions:**
- Chromium executable: `149.0.7827.55` (Playwright bundled)
- Playwright source: `/tmp/playwright-test/node_modules/playwright`

**Runner:** `scripts/second_exhibition_browser_qa.mjs` (unchanged from v4.8)
**Env override:** `SECOND_EXHIBITION_QA_URL=http://127.0.0.1:8771/second-exhibition/`

---

## Viewport matrix

| Viewport | Result | Sections | Cards | Glossary | Images | Overflow | Repo status |
|----------|:-----:|---------:|------:|---------:|-------:|:--------:|:-----------:|
| 1440×1000 | PASS | 4 | 6 | 12 | 6 / 6 loaded | none | visible |
| 1280×900  | PASS | 4 | 6 | 12 | 6 / 6 loaded | none | visible |
| 768×1024  | PASS | 4 | 6 | 12 | 6 / 6 loaded | none | visible |
| 390×844   | PASS | 4 | 6 | 12 | 6 / 6 loaded | none | visible |
| 320×700   | PASS | 4 | 6 | 12 | 6 / 6 loaded | none | visible |

All 5 viewports PASS. Identical metric counts across viewports confirm path-rewritten
artifact serves consistent content.

---

## Image requests

The 6 staged images were loaded on every viewport:

| Image | Staged bytes | HTTP served bytes | Match |
|-------|-------------:|------------------:|:-----:|
| `bhl-318921-page-603998-c01.webp` | 306,126 | 306,126 | ✓ |
| `bhl-318921-page-603962-c03.webp` | 262,498 | 262,498 | ✓ |
| `smithsonian-nmnh-1529703.png`     |   3,550 |   3,550 | ✓ |
| `met-285149.jpg`                   |  95,001 |  95,001 | ✓ |
| `rijksmuseum-rp-f-f80152.jpg`      | 294,445 | 294,445 | ✓ |
| `rijksmuseum-rp-f-f80313.jpg`      | 191,606 | 191,606 | ✓ |

All image requests resolved to the staging artifact; no 404; no extra images requested.

---

## Internal-path tests

The browser QA runner was not specifically asked to fetch internal paths (those are not
referenced by the page), but a separate `curl` matrix was run against the staging server:

| Internal path | Expected | Actual |
|---------------|----------|--------|
| `/second-exhibition/data/` | 404 | 404 |
| `/second-exhibition/docs/` | 404 | 404 |
| `/second-exhibition/assets/asset-import-manifest.json` | 404 | 404 |
| `/second-exhibition/assets/asset-checksums.sha256` | 404 | 404 |
| `/reports/` | 404 | 404 |
| `/scripts/` | 404 | 404 |
| `/_template/` | 404 | 404 |
| `/_pilots/` | 404 | 404 |

No internal directory or file was exposed by the staging server.

---

## No-JS

| Metric | Value |
|--------|------:|
| Cards visible | 6 |
| Source notes | 6 |
| Credit lines | 6 |
| Repository status visible | yes |
| Body text content | yes |

No-JS path renders correctly.

---

## Reduced motion

| Metric | Value |
|--------|------:|
| Lightbox opens | yes |
| ESC closes lightbox | yes |

Reduced motion respects the `prefers-reduced-motion` media query.

---

## External requests

| Metric | Value |
|--------|------:|
| External requests | **0** |

The page does not issue any external (non-staging-origin) requests. All CSS, JS, and
images are served from `http://127.0.0.1:8771/`. The official source-link policy is
preserved (user-click navigation only).

---

## Interaction & accessibility

| Interaction | Result |
|-------------|--------|
| Guided-mode toggle | OK |
| Lightbox opens | OK |
| Lightbox role | `dialog` |
| Lightbox accessible name | `lightbox-title` |
| Close button receives focus on open | OK |
| ESC closes lightbox | OK |
| Focus returns to trigger after close | OK |
| C-06 lightbox remains closed on initial load | OK |
| Section-nav jump | OK |
| Tab-focusable elements reachable | OK |

Accessibility snapshot:

| Check | Value |
|-------|-------|
| `h1` count | 1 |
| Images missing alt | 0 |
| Buttons missing accessible name | 0 |
| Heading jump | none |
| Visually-hidden title width | 1px |
| Visually-hidden title height | 1px |
| Visually-hidden title position | absolute |

---

## Error counters

| Counter | Value |
|---------|------:|
| Console errors | **0** |
| Page errors | **0** |
| Failed requests | **0** |
| External requests | **0** |
| Horizontal overflow | **0** |

---

## Final result

**STATUS: PASS** — 5/5 viewports PASS, all 6 images loaded, 0 errors of any kind,
all interactions and accessibility checks green, no external requests.

Browser QA was run against the staging artifact served from `/tmp/leonardo-pages-artifact`
on a local Python HTTP server. Production GitHub Pages was not contacted during this run.

The staging server was terminated after QA (`process.kill` on the background session).
Production Pages site remains at 92,976 B with v2.9 marker = 1.