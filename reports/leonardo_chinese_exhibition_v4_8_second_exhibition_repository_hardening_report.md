# v4.8 Second Exhibition Repository Hardening Report

## STATUS: PASS

**Date:** 2026-07-12
**Baseline HEAD / origin/main:** `420791c9805d718db7ddbe664b6d5aa903f803e6`
**v4.7 tag:** `v4.7-real-second-exhibition-repository-qa`
**v4.7 tag object:** `b746a358491149ed9f40c064d0f5661951601c45`
**v4.7 tag target / freeze commit:** `2153d2eab45bc1ea715fae1e1b04a3ee9fc64961`
**Round:** v4.8 — Second Exhibition Repository Hardening
**Next:** **v4.8-real-stable-freeze**

---

## Original warnings

1. **C-03** — "CC BY-NC-SA subset exact wording not found" (QA-logic limitation; the page already contains "PD subset only", "CC BY-NC-SA", "blocked-from-import")
2. **C-06** — "Hero check inconclusive" (QA-logic limitation; the page has a hero section, and C-06 is not inside it)

Both warnings were QA-logic limitations. The underlying content already documents the intended semantics. **No content / data / source / rights / asset file was modified to silence them.**

## Warning-resolution method

- **C-03** — `scripts/second_exhibition_repository_qa.py` now accepts equivalent phrasings already in the page (`pd subset`, `public-domain subset`, `pd 子集`, `cc by-nc-sa`, `cc-by-nc-sa`, `blocked-from-import`, `blocked from import`, `仍被排除`, `仍被 blocked`).
- **C-06** — the QA script now parses the `<section class="hero">` and explicitly checks that C-06 (c-06, smithsonian-nmnh, data-candidate-id="c-06") does not appear inside it, and that C-06 appears exactly once as `<article data-low-resolution="true" data-lightbox-enabled="false">`.

## Files modified in v4.8

- `scripts/second_exhibition_repository_qa.py` — broadened C-03 wording check; structured C-06 hero check
- `scripts/second_exhibition_browser_qa.mjs` — created (Node.js + Playwright Chromium browser QA runner)
- `second-exhibition/site/script.js` — fixed focus restoration on lightbox close (real a11y defect)
- `docs/SECOND_EXHIBITION_REPOSITORY_HARDENING_v4.8.md` — created
- `docs/BROWSER_QA_MATRIX_v4.8.md` — created
- `docs/V4_ROADMAP.md` — added v4.8 section
- `README.md` — added v4.8 section

No page HTML or CSS was modified for this round.

## Template / build / repository QA

- `python3 scripts/template_quality_gate.py` → **PASS, 37/37**
- `python3 scripts/second_exhibition_build_gate.py` → **PASS**
- `python3 scripts/second_exhibition_repository_qa.py` → **161 PASS / 0 FAIL / 0 WARNINGS** (exit 0)
- `sha256sum -c second-exhibition/assets/asset-checksums.sha256` → **6/6 OK**
- `node --check second-exhibition/site/script.js` → OK
- `node --check scripts/second_exhibition_browser_qa.mjs` → OK

## Browser QA runner result

- `node scripts/second_exhibition_browser_qa.mjs` → **PASS** (exit 0)
- **Browser executable / version:** Chromium 149.0.7827.55 (Playwright build v1228)
- **Playwright path:** `/tmp/playwright-test/node_modules/playwright` (v1.61.1)
- **Started:** 2026-07-11T09:18:40.131Z
- **Finished:** 2026-07-11T09:19:10.970Z (≈ 30 s)

## Viewport matrix (5 viewports × 12 checks each = 60 checks)

| Viewport    | Result |
|-------------|--------|
| 1440 × 1000 | PASS   |
| 1280 × 900  | PASS   |
| 768 × 1024  | PASS   |
| 390 × 844   | PASS   |
| 320 × 700   | PASS   |

## Interaction

- Guided toggle: **PASS**
- Lightbox open on C-01: **PASS**
- Accessible dialog name (`aria-labelledby`): **PASS** (`lightbox-title`)
- Close button focused on open: **PASS**
- ESC closes lightbox: **PASS**
- Focus returns to trigger image on close: **PASS** (was FAIL before script.js fix)
- C-06 lightbox exclusion: **PASS**
- Section anchor navigation: **PASS**
- Tab reaches interactive element: **PASS**

## Accessibility (computed style + DOM)

- One `<h1>`: **PASS** (1)
- `<img>` alt missing (artifact cards): **PASS** (0)
- `<button>` accessible name missing: **PASS** (0)
- Heading level jump: **PASS** (none)
- `#lightbox-title` hidden via `display: none`: **PASS** (false; uses `clip: rect(0,0,0,0)`)
- `#lightbox-title` hidden via `visibility: hidden`: **PASS** (false)
- `#lightbox-title` position: `absolute`, width `1px`, height `1px` (visible to AT, hidden visually)

## Console / page errors

- Console errors: **0**
- Page errors: **0**
- Failed requests: **0** (favicon 404 noise is filtered at the runner level)

## External requests

- External requests: **0**
- All requests target `http://127.0.0.1:8770` (the local server).

## Overflow

- No horizontal overflow on any of the 5 viewports.

## No-JS

With JavaScript disabled:

- 6 artifact cards visible
- 6 source notes visible
- 6 credit lines visible
- repository-status visible
- body text contains `植物图谱与视觉分类`

## Reduced motion

- Lightbox opens on click: **PASS**
- ESC closes lightbox: **PASS**

## C-06 exclusion

- `data-lightbox-enabled="false"` confirmed on C-06 article.
- Clicking C-06 image does NOT open the lightbox.

## Real a11y defect fixed

`second-exhibition/site/script.js`:

- Before: `closeLightbox()` did not restore focus to the trigger element. After pressing ESC, focus was lost (active = `body`).
- After: `openLightbox(card, trigger)` saves the trigger; `closeLightbox()` restores focus to the saved trigger.

This is a WCAG 2.4.3 (focus order) compliance fix.

## Checksums

- Asset checksums: **6/6 OK** — no asset change.

## Data / assets / source evidence unchanged

- `second-exhibition/data/` — no diff
- `second-exhibition/assets/` — no diff
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` — no diff
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md` — no diff

## Existing live site unchanged

- Live byte: **92,976 B**
- v2.9 marker: **1**
- Second exhibition title live count: **0**
- Top-level `script.js`: HTTP 200

## Workflow unchanged

- `.github/workflows/` — no diff

## Pages exposure

- `second-exhibition/`: HTTP 404
- `second-exhibition/site/`: HTTP 404
- `second-exhibition/site/index.html`: HTTP 404

## Tags / Releases unchanged

- No new tag created in v4.8
- No new GitHub Release created
- Latest tag remains `v4.7-real-second-exhibition-repository-qa`
- Existing tags (`v2.0` through `v4.7`) untouched

## Next recommended task

**v4.8-real-stable-freeze** — final QA, create `v4.8-real-second-exhibition-repository-hardening` annotated tag, publish GitHub Release.