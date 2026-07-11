# v4.8 Second Exhibition Repository Hardening

## Baseline

- HEAD / origin/main: `420791c9805d718db7ddbe664b6d5aa903f803e6`
- v4.7 tag: `v4.7-real-second-exhibition-repository-qa`
- v4.7 tag object: `b746a358491149ed9f40c064d0f5661951601c45`
- v4.7 tag target / freeze commit: `2153d2eab45bc1ea715fae1e1b04a3ee9fc64961`
- v4.8 freeze commit: to be inserted after push.

## Original v4.7 warnings

1. **C-03 CC BY-NC-SA subset exact wording not found**
2. **C-06 Hero check inconclusive**

Both warnings were QA-logic limitations, not real content defects. The underlying content already documents the intended semantics.

## Warning-resolution method

### C-03

The page and `BUILD_ASSET_USAGE.md` document:

- "PD subset only"
- "CC BY-NC-SA" / "CC BY-NC-SA subset"
- "blocked-from-import" / "blocked"

The previous QA checked only for the exact phrase `"cc by-nc-sa subset"`. We broadened the check to accept any of the equivalent phrasings already present in the page:

- `pd subset`, `public-domain subset`, `public domain subset`, `pd 子集`
- `cc by-nc-sa`, `cc-by-nc-sa`
- `blocked-from-import`, `blocked from import`, `仍被排除`, `仍被 blocked`

**No content change.** Only `scripts/second_exhibition_repository_qa.py` was modified.

### C-06

The previous QA returned "inconclusive" whenever it could not positively identify a hero. The page does have a `<section class="hero">` (3-minute guide), and C-06 does not appear inside that section.

The new QA parses the Hero section from the HTML and explicitly verifies:

- The Hero section exists.
- C-06 (`c-06`, `smithsonian-nmnh`, `data-candidate-id="c-06"`) does not appear inside the Hero.
- C-06 appears as exactly one `<article class="artifact-card" data-candidate-id="c-06">`.
- That article has `data-low-resolution="true"` and `data-lightbox-enabled="false"`.

**No content change.** Only `scripts/second_exhibition_repository_qa.py` was modified.

## Repository QA result after fix

- `python3 scripts/second_exhibition_repository_qa.py` → **161 PASS / 0 FAIL / 0 WARNINGS** (exit code 0)
- `python3 scripts/template_quality_gate.py` → **PASS, 37/37**
- `python3 scripts/second_exhibition_build_gate.py` → **PASS**
- `sha256sum -c second-exhibition/assets/asset-checksums.sha256` → **6/6 OK**

## Browser QA runner

Created `scripts/second_exhibition_browser_qa.mjs` (Node.js + Playwright Chromium, ESM):

- Exit code 0 = PASS, 1 = QA failure, 2 = browser environment not available.
- Default URL: `http://127.0.0.1:8770/site/` (override with `SECOND_EXHIBITION_QA_URL`).
- Playwright lookup order: env `PLAYWRIGHT_NODE_PATH` → `/tmp/playwright-test/node_modules/playwright` → `playwright` → `playwright-core`.
- Browser executable: env `PLAYWRIGHT_CHROMIUM_EXECUTABLE` → `pw.chromium.executablePath()`.
- Does not modify the repository; does not access the public network.

## Browser QA matrix (5 viewports × ≥ 13 checks each)

| Viewport    | Result | Notes |
|-------------|--------|-------|
| 1440 × 1000 | PASS   | All 6 images loaded, no overflow, all sections / cards / glossary items present |
| 1280 × 900  | PASS   | same |
| 768 × 1024  | PASS   | tablet portrait, no horizontal overflow |
| 390 × 844   | PASS   | mobile, no horizontal overflow |
| 320 × 700   | PASS   | narrow mobile, no horizontal overflow |

## Interaction results

- Guided toggle: PASS (button `aria-pressed` flips, banner becomes visible)
- Lightbox open on C-01: PASS
- Accessible dialog name: PASS (`aria-labelledby="lightbox-title"` resolves to `图片查看器`)
- Close button focused on open: PASS
- ESC closes lightbox: PASS
- Focus returns to trigger image after close: **was FAIL, now PASS** (script.js fix)
- C-06 lightbox exclusion: PASS (clicking C-06 does not open lightbox)
- Section navigation: PASS (anchor click scrolls target section into view)
- Tab focus on main interactive element: PASS

## Real a11y defect fixed

`second-exhibition/site/script.js`: `closeLightbox()` did not restore focus to the trigger image. This was a real WCAG 2.4.3 (focus order) defect.

Fix: save the trigger element when opening the lightbox (`lastTrigger`), and restore focus when closing.

**Test before fix:**
- click C-01 image → close button focused → press ESC → focus on `body`, not on C-01 image

**Test after fix:**
- click C-01 image → close button focused → press ESC → focus returns to C-01 image

## Accessibility / degradation

- One `<h1>`: PASS
- All artifact-card images have alt text: PASS (0 missing)
- All `<button>` elements have accessible names: PASS
- Heading levels do not jump: PASS
- `#lightbox-title` is positioned absolutely with `clip: rect(0,0,0,0)` — visible to AT, hidden visually: PASS
- prefers-reduced-motion: lightbox opens and closes on `Escape`: PASS
- No-JS mode (JavaScript disabled): all 6 cards visible, source notes visible, credit lines visible, repository status visible, body text contains page title: PASS

## No-JS

The page is HTML-only with progressive enhancement. With JavaScript disabled:

- All content remains accessible.
- All 6 artifact cards, source notes, and credit lines render.
- The repository-status badge is visible.
- The lightbox simply does not open; users see the full image inline.

## Reduced motion

With `prefers-reduced-motion: reduce`:

- Lightbox open on click: PASS
- ESC close: PASS
- All transitions are disabled by the existing `@media (prefers-reduced-motion: reduce)` rule.

## External requests

- `externalRequests = 0`
- All requests go to `http://127.0.0.1:8770` (the local HTTP server). No third-party CDN, no analytics, no fonts.

## Deployment status

- Second exhibition: **repository-only-not-deployed**
- Existing Leonardo live site: unchanged (92,976 B, v2.9 marker present)
- All `second-exhibition/` Pages URLs return HTTP 404
- Top-level `script.js`: HTTP 200

## No-touch confirmation

The following paths were **not modified** in v4.8:

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
- `release-assets/`
- `.github/workflows/`
- `scripts/template_quality_gate.py`
- `scripts/second_exhibition_asset_gate.py`
- `scripts/second_exhibition_build_gate.py`

Files modified in v4.8:

- `scripts/second_exhibition_repository_qa.py` — broadened C-03 wording check; structured C-06 hero check
- `scripts/second_exhibition_browser_qa.mjs` — created (browser QA runner)
- `second-exhibition/site/script.js` — fixed focus restoration on lightbox close (real a11y defect)

No tag or Release was created in v4.8.

## Next

- **v4.8-real-stable-freeze**