# v4.8 Real Second Exhibition Repository Hardening

## Tag

- `v4.8-real-second-exhibition-repository-hardening`

## URLs

- Existing live URL: https://conanxin.github.io/leonardo-chinese-exhibition/
- GitHub Release: to be inserted after Release creation

## Verified baseline

- Source release: `v4.7-real-second-exhibition-repository-qa`
- Source tag object: `b746a358491149ed9f40c064d0f5661951601c45`
- Source tag target / source freeze commit: `2153d2eab45bc1ea715fae1e1b04a3ee9fc64961`
- Hardening commit: `83edfa6a1e13b55c454fc9ccc28eeef5b75c0ff9`
- v4.7 evidence backfill commit: `420791c9805d718db7ddbe664b6d5aa903f803e6`
- Freeze commit: to be inserted after push

## Verified live byte

- **92,976 B**
- v2.9 marker live count: **1**
- Second exhibition title live count: **0**
- Top-level `script.js`: HTTP 200
- Second exhibition: **repository-only-not-deployed**

## What changed in v4.8

### QA-logic hardening (no content change)

- `scripts/second_exhibition_repository_qa.py`:
  - **C-03** now accepts equivalent rights wording already present on the page (`pd subset`, `public-domain subset`, `pd 子集`, `cc by-nc-sa`, `cc-by-nc-sa`, `blocked-from-import`, `blocked from import`, `仍被排除`, `仍被 blocked`). The original QA only matched the literal string `cc by-nc-sa subset`.
  - **C-06** Hero check is now structured: the script parses the `<section class="hero">`, asserts C-06 does not appear inside it, asserts C-06 appears exactly once as `<article data-low-resolution="true" data-lightbox-enabled="false">`. Replaces the previous "inconclusive" warning.

### Browser QA runner

- New: `scripts/second_exhibition_browser_qa.mjs` (Node.js ESM, Playwright Chromium)
- Exit codes: 0 PASS, 1 QA failure, 2 browser environment not available
- Default URL: `http://127.0.0.1:8770/site/` (override with `SECOND_EXHIBITION_QA_URL`)
- Five-viewport matrix (1440 × 1000, 1280 × 900, 768 × 1024, 390 × 844, 320 × 700)
- Interaction checks (guided toggle, lightbox, accessible name, ESC close, focus restoration, C-06 exclusion, section navigation, Tab focus)
- Accessibility checks (single h1, alt text, button names, heading jumps, visually-hidden not via `display:none` / `visibility:hidden`)
- No-JS degradation check
- Reduced-motion check
- External / failed request / console-error / page-error tracking

### Real a11y defect fixed (only `script.js` change)

- `second-exhibition/site/script.js`:
  - `closeLightbox()` now restores focus to the trigger image.
  - Before: focus was lost after closing the lightbox.
  - After: focus returns to the same artifact card image that opened the lightbox.
  - `openLightbox(card, trigger)` saves the trigger element; `closeLightbox()` restores focus.

## Verified results

| Item | Result |
|------|--------|
| Template quality gate | **PASS, 37/37** |
| Second exhibition build gate | **PASS** |
| Repository QA | **161 PASS / 0 FAIL / 0 WARNINGS** |
| Browser QA | **PASS, 5/5 viewports** |
| Console errors | **0** |
| Page errors | **0** |
| Failed requests | **0** |
| External requests | **0** |
| Horizontal overflow | **0** on all 5 viewports |
| ARIA references | **9/9 valid** |
| Asset checksums | **6/6 OK** |
| Data JSON | all valid |
| No-JS | **PASS** (6 cards visible, source notes / credit lines / repo status visible) |
| Reduced motion | **PASS** (lightbox open + ESC close) |
| C-06 lightbox exclusion | **PASS** |
| Lightbox accessible name | `图片查看器` (via `aria-labelledby="lightbox-title"`) |
| Focus restoration | **PASS** (after script.js fix) |

## Browser environment

- Browser executable / version: Chromium **149.0.7827.55**
- Playwright browser build: **1228**
- Playwright package: **1.61.1**
- Server command: `python3 -m http.server 8770 --directory second-exhibition`
- Runner: `node scripts/second_exhibition_browser_qa.mjs`
- Browser cache path: `/tmp/playwright-test/node_modules/playwright-core/.local-browsers`

## Interaction results

| Check | Result |
|-------|--------|
| Guided toggle opens/closes | PASS |
| Lightbox open on C-01 | PASS |
| Lightbox role | `dialog` |
| Accessible name (`aria-labelledby`) | `lightbox-title` |
| Close button focused on open | PASS |
| ESC closes lightbox | PASS |
| Focus returns to trigger image | **PASS** (fixed in v4.8) |
| C-06 lightbox remains closed | PASS |
| Section anchor navigation | PASS |
| Tab reaches interactive element | PASS |

## Deployment

- Second exhibition remains **repository-only**.
- All `second-exhibition/` Pages URLs return HTTP 404.
- Existing Leonardo exhibition remains unchanged (92,976 B).

## No-touch confirmation

The following paths were not modified during v4.8:

- `second-exhibition/site/index.html`
- `second-exhibition/site/style.css`
- `second-exhibition/data/`
- `second-exhibition/assets/`
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md`
- `second-exhibition/docs/VISITOR_GUIDE_ZH.md`
- `second-exhibition/docs/CURATORIAL_ESSAY_ZH.md`
- `second-exhibition/docs/DEEP_RESEARCH_NOTES_ZH.md`
- `second-exhibition/docs/BUILD_ASSET_USAGE.md`
- `site/`
- `_template/`
- `_pilots/second-exhibition-pilot/`
- `posts/`
- `case-study/`
- `release-assets/` (existing files)
- `.github/workflows/`
- `scripts/template_quality_gate.py`
- `scripts/second_exhibition_asset_gate.py`
- `scripts/second_exhibition_build_gate.py`
- Existing tags (`v2.0` through `v4.7`)
- Existing GitHub Releases

## What is not in this release

- The second exhibition is **not deployed** to GitHub Pages.
- No new image asset is added or replaced.
- No source / rights evidence is modified.
- No workflow change is introduced.
- No old tag or Release is moved or overwritten.

## Next

- **v5.0-second-exhibition-deployment-planning**