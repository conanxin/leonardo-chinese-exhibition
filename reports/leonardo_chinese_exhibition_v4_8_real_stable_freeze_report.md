# v4.8 Real Stable Freeze Report

## STATUS: PASS

**Date:** 2026-07-12
**Baseline HEAD / origin/main (hardening commit):** `83edfa6a1e13b55c454fc9ccc28eeef5b75c0ff9`
**Hardening commit:** `83edfa6a1e13b55c454fc9ccc28eeef5b75c0ff9`
**Source release:** `v4.7-real-second-exhibition-repository-qa`
**Source tag object:** `b746a358491149ed9f40c064d0f5661951601c45`
**Source tag target / source freeze commit:** `2153d2eab45bc1ea715fae1e1b04a3ee9fc64961`
**v4.7 evidence backfill HEAD:** `420791c9805d718db7ddbe664b6d5aa903f803e6`
**Live URL:** https://conanxin.github.io/leonardo-chinese-exhibition/
**Round:** v4.8-real-stable-freeze — Second Exhibition Repository Hardening stable freeze
**Tag:** `v4.8-real-second-exhibition-repository-hardening`
**Next:** `v5.0-second-exhibition-deployment-planning`

---

## Freeze evidence three-piece

- Freeze commit: to be filled after push.
- Tag target: to be filled after tag creation.
- Verified live byte: **92,976 B**.
- Verified tag: to be filled after tag creation.
- GitHub Release: to be filled after Release creation.

---

## Verified live byte (before / after)

- Before freeze: **92,976 B**
- After freeze: **92,976 B** (unchanged — freeze adds docs/reports only)

---

## Quality gates (this freeze round, after v4.8 hardening baseline)

| Gate | Command | Result |
|------|---------|--------|
| Template quality gate | `python3 scripts/template_quality_gate.py` | **PASS, 37/37** |
| Second exhibition build gate | `python3 scripts/second_exhibition_build_gate.py` | **PASS** |
| Repository QA | `python3 scripts/second_exhibition_repository_qa.py` | **161 PASS / 0 FAIL / 0 WARNINGS** (exit 0) |
| Asset checksums | `sha256sum -c second-exhibition/assets/asset-checksums.sha256` | **6/6 OK** |
| JavaScript syntax (site) | `node --check second-exhibition/site/script.js` | **OK** |
| JavaScript syntax (browser QA) | `node --check scripts/second_exhibition_browser_qa.mjs` | **OK** |
| Data JSON | `python3 -m json.tool` | all valid |

---

## Browser QA matrix (this freeze round)

- `node scripts/second_exhibition_browser_qa.mjs` → **PASS** (exit 0)
- **Browser executable / version:** Chromium **149.0.7827.55**
- **Playwright browser build:** **1228**
- **Playwright package:** **1.61.1**
- **Server command:** `python3 -m http.server 8770 --directory second-exhibition`
- **Runner:** `node scripts/second_exhibition_browser_qa.mjs`

### Viewport matrix (5 viewports)

| Viewport    | Result |
|-------------|--------|
| 1440 × 1000 | PASS   |
| 1280 × 900  | PASS   |
| 768 × 1024  | PASS   |
| 390 × 844   | PASS   |
| 320 × 700   | PASS   |

### Interaction

| Check                                    | Result |
|------------------------------------------|--------|
| Guided toggle opens/closes               | PASS   |
| Lightbox open on C-01                    | PASS   |
| Lightbox role                            | `dialog` |
| Accessible name (`aria-labelledby`)      | `lightbox-title` |
| Close button focused on open             | PASS   |
| ESC closes lightbox                      | PASS   |
| Focus returns to trigger image on close  | PASS   |
| C-06 lightbox remains closed             | PASS   |
| Section anchor navigation                | PASS   |
| Tab focus reaches interactive element    | PASS   |

### Accessibility

| Check                                | Result |
|--------------------------------------|--------|
| Exactly one `<h1>`                   | PASS (1) |
| `<img>` alt missing (artifact cards) | PASS (0) |
| `<button>` accessible name missing   | PASS (0) |
| Heading level jump                   | PASS (none) |
| `#lightbox-title` hidden by display:none | PASS (false) |
| `#lightbox-title` hidden by visibility:hidden | PASS (false) |

### Console / page errors

- Console errors: **0**
- Page errors: **0**
- Failed requests: **0**
- External requests: **0**

### Overflow

- No horizontal overflow on any of the 5 viewports.

### No-JS

- 6 cards, 6 source notes, 6 credit lines, repository status visible, body text contains page title: **PASS**

### Reduced motion

- Lightbox opens on click + ESC closes: **PASS**

---

## Checksums

- Asset checksums: **6/6 OK** (no asset change)

## JSON validation

- `asset-import-manifest.json`, `exhibition.json`, `sections.json`, `glossary.json`, `assets.json` — all valid

---

## Deployment path HTTP results (this freeze round)

| Path                                                  | HTTP |
|-------------------------------------------------------|------|
| `https://conanxin.github.io/leonardo-chinese-exhibition/` | **200** |
| `https://conanxin.github.io/leonardo-chinese-exhibition/script.js` | **200** |
| `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` | **404** |
| `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/site/` | **404** |
| `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/site/index.html` | **404** |
| `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/assets/asset-import-manifest.json` | **404** |

- Live byte: **92,976 B**
- v2.9 marker live count: **1**
- Second exhibition title live count: **0**

Status: **repository-only-not-deployed**.

---

## Protected paths unchanged (from hardening baseline to HEAD)

The freeze commit must not modify any of the following. (Empty diff = pass.)

- `second-exhibition/site/`
- `second-exhibition/data/`
- `second-exhibition/assets/`
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md`
- `site/`
- `_template/`
- `_pilots/second-exhibition-pilot/`
- `.github/workflows/`
- `scripts/second_exhibition_repository_qa.py`
- `scripts/second_exhibition_browser_qa.mjs`

---

## Tag / Release status

- Tag created: `v4.8-real-second-exhibition-repository-hardening` (annotated)
- Tag target: to be filled after tag creation.
- GitHub Release created: to be filled after Release creation.
- Old tags (`v2.0` through `v4.7`) and Releases: untouched.

---

## Evidence backfill (optional)

After tag / Release creation, this section may be filled with:

- Tag object SHA.
- Tag target commit.
- Release URL.
- Release `createdAt`.
- GitHub Actions run ID.
- Any additional deployment-path verification.

The evidence backfill commit, if any, will be located **after** the tag target commit and will not move the tag.

---

## Notes

This freeze marks the verified state of the v4.8 Second Exhibition Repository Hardening. The second exhibition remains repository-only and is not deployed to GitHub Pages. Live publication requires a separate, future round that explicitly authorizes deployment and re-runs source/rights verification against the to-be-deployed tree.