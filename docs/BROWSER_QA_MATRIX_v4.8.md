# v4.8 Browser QA Matrix

**Round:** v4.8-second-exhibition-repository-hardening
**Date:** 2026-07-12
**Started:** 2026-07-11T09:18:40.131Z
**Finished:** 2026-07-11T09:19:10.970Z (≈ 30 s)
**URL:** `http://127.0.0.1:8770/site/`
**Server:** `python3 -m http.server 8770 --directory second-exhibition`
**Browser executable / version:** Chromium **149.0.7827.55** (Playwright build v1228)
**Playwright path:** `/tmp/playwright-test/node_modules/playwright` (v1.61.1)
**Browser binaries path:** `/tmp/playwright-test/node_modules/playwright-core/.local-browsers`
**Runner:** `node scripts/second_exhibition_browser_qa.mjs`

## Viewport matrix

| Viewport    | Page 200 | Images loaded | Console errors | Failed requests | External requests | Overflow | Result |
|-------------|----------|---------------|----------------|-----------------|-------------------|----------|--------|
| 1440 × 1000 | ✓        | 6 / 6         | 0              | 0               | 0                 | none     | PASS   |
| 1280 × 900  | ✓        | 6 / 6         | 0              | 0               | 0                 | none     | PASS   |
| 768 × 1024  | ✓        | 6 / 6         | 0              | 0               | 0                 | none     | PASS   |
| 390 × 844   | ✓        | 6 / 6         | 0              | 0               | 0                 | none     | PASS   |
| 320 × 700   | ✓        | 6 / 6         | 0              | 0               | 0                 | none     | PASS   |

For each viewport, the runner also asserts:

- title contains `植物图谱与视觉分类`
- h1 contains `植物图谱与视觉分类`
- exactly 4 sections
- exactly 6 artifact cards
- ≥ 10 glossary items
- ≥ 6 source notes
- ≥ 6 credit lines
- 6 images, 6 loaded (`naturalWidth > 0`)
- repository-status visible
- no body / document horizontal overflow

## Interaction

| Check                                    | Before v4.8 | After v4.8 |
|------------------------------------------|-------------|------------|
| Guided toggle opens/closes               | PASS        | PASS       |
| C-01 lightbox opens                      | PASS        | PASS       |
| Lightbox role                            | `dialog`    | `dialog`   |
| Accessible name (`aria-labelledby`)      | `lightbox-title` | `lightbox-title` |
| Close button focused on open             | PASS        | PASS       |
| ESC closes lightbox                      | PASS        | PASS       |
| Focus returns to trigger image on close  | **FAIL**    | **PASS**   |
| C-06 lightbox remains closed             | PASS        | PASS       |
| Section anchor navigation works          | PASS        | PASS       |
| Tab reaches interactive element          | PASS        | PASS       |

## Accessibility

| Check                                | Result |
|--------------------------------------|--------|
| Exactly one `<h1>`                   | PASS (1) |
| `<img>` alt missing (artifact cards) | PASS (0) |
| `<button>` accessible name missing   | PASS (0) |
| Heading level jump                   | PASS (none) |
| `#lightbox-title` hidden by display:none | PASS (false) |
| `#lightbox-title` hidden by visibility:hidden | PASS (false) |
| `#lightbox-title` computed position  | `absolute` |
| `#lightbox-title` computed width     | `1px` |
| `#lightbox-title` computed height    | `1px` |

## No-JS

With JavaScript disabled (init script override):

| Check                              | Result |
|------------------------------------|--------|
| 6 artifact cards                   | PASS   |
| 6 source notes                     | PASS   |
| 6 credit lines                     | PASS   |
| Repository-status visible           | PASS   |
| Body text contains `植物图谱与视觉分类` | PASS   |

## Reduced motion

`emulateMedia({ reducedMotion: "reduce" })`:

| Check                | Result |
|----------------------|--------|
| C-01 lightbox opens  | PASS   |
| ESC closes lightbox  | PASS   |

## External requests

- Count: **0**
- All requests go to `http://127.0.0.1:8770`.

## Result summary

- **STATUS:** PASS
- Exit code: **0**
- Viewports: **5 / 5 PASS**
- Interaction: **all checks PASS** (focus-return was a real defect; fixed in v4.8)
- Accessibility: **all checks PASS**
- No-JS: **all checks PASS**
- Reduced-motion: **all checks PASS**
- External requests: **0**
- Failed requests: **0**
- Console errors: **0**
- Page errors: **0**

## Notes on environment

- The Chromium browser binary was installed via `cd /tmp/playwright-test && npx playwright install chromium`. The binary lives in the user-level Playwright cache, not in the repository.
- No `package.json` / `package-lock.json` was modified.
- No `sudo` was used; no system-level packages were installed.
- The runner is invoked with `PLAYWRIGHT_BROWSERS_PATH` and `PLAYWRIGHT_NODE_PATH` pointing at the user-level Playwright install.