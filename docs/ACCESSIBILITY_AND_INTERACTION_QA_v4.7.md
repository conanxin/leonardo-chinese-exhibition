# Accessibility and Interaction QA v4.7

## Baseline

- Site: `second-exhibition/site/`
- Assets: 6 imported, not deployed
- Test command: `python3 scripts/second_exhibition_repository_qa.py`
- Local serving: `python3 -m http.server 8770 --directory second-exhibition`
- Open: `http://127.0.0.1:8770/site/`

## Heading structure

- Exactly one `h1` in `index.html`.
- `h1` text contains the exhibition title: 植物图谱与视觉分类.
- Heading levels do not jump more than one level.
- Section titles use `h2`, subsections use `h3`/`h4` as appropriate.

## Alt completeness

- All 6 artifact images have non-empty `alt` attributes.
- Decorative icons are excluded or use empty alt where appropriate.

## Button accessible names

- Every `<button>` has either visible text or an `aria-label` attribute.
- Guided-reading toggle, lightbox close, mobile menu, and section-jump buttons are labeled.

## Keyboard navigation

- Tab order follows the visual flow.
- Focus is visible on interactive elements (`:focus-visible` rule in `style.css`).
- Lightbox close button is reachable by keyboard.
- Section navigation links are reachable by keyboard.

## Focus-visible result

- `:focus-visible` styles are present in `style.css`.
- Outline offset is visible on all buttons and links.

## Guided reading toggle

- A button toggles `.guided-reading` class on the body.
- In guided mode, the visitor guide steps are highlighted sequentially.
- Toggle works with mouse and keyboard.

## Lightbox

- Five artifact cards (all except C-06) open a lightbox when their image is clicked.
- Lightbox is closed by:
  - clicking the close button,
  - clicking the overlay,
  - pressing the `Escape` key.
- Focus is trapped inside the lightbox while it is open.

## ESC close

- The `keydown` listener checks for `Escape` and calls `closeLightbox()`.

## C-06 exclusion

- C-06 has `data-lightbox-enabled="false"` and a visible low-resolution note.
- Its image does not open the lightbox.
- It is rendered at a small size (max-width: 180 px) and is never used as a hero image.

## Reduced motion

- `prefers-reduced-motion: reduce` removes the hero image fade-in and any non-essential transitions.
- All content remains readable and functional.

## No-JS fallback

- With JavaScript disabled, the page still shows:
  - the hero block and title,
  - all four sections,
  - all six artifact cards with source notes and credit lines,
  - the full glossary,
  - the visitor guide and deep-reading blocks.
- The repository-only status banner is visible without JavaScript.
- Lightbox and guided-reading toggle are unavailable without JS, which is acceptable for a no-JS baseline.

## Remaining limitations

- No skip-to-main link is currently provided; this could be added in a future hardening round.
- No automated screen-reader test was performed; only static markup and keyboard checks were executed.
- C-06 is a 90 × 90 px thumbnail; it is intentionally small and does not participate in the lightbox.

## Result

- All accessibility and interaction checks in `scripts/second_exhibition_repository_qa.py` PASS.
- See the v4.7 report for Playwright viewport results.

<!-- v4.7-partial-finding -->
## Blocking accessibility finding

- **Result:** FAIL
- Element: `#lightbox`
- Declared reference: `aria-labelledby="lightbox-title"`
- Missing target: `id="lightbox-title"`
- Effect: the lightbox dialog lacks a valid accessible name through its declared ARIA relationship.
- Automated ARIA reference audit: **9 references checked, 1 missing target**.
- The defect must be corrected in a separate `v4.7b-repository-qa-recovery` round.
- No page modification was made during v4.7 QA.
