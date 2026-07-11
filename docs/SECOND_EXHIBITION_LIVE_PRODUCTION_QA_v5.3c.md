# v5.3c Second Exhibition Live Production Browser QA

> Companion to `docs/SECOND_EXHIBITION_PRODUCTION_STATE_RECONCILIATION_v5.3b.md`,
> `reports/leonardo_chinese_exhibition_v5_3b_production_state_reconciliation_prep_report.md`,
> `docs/V5_ROADMAP.md`, and `reports/leonardo_chinese_exhibition_v5_3c_live_production_browser_qa_report.md`.

## Baseline

| Field | Value |
|---|---|
| HEAD / origin/main | `52504047a966c0dd9a60b569a63b1857168a498f` |
| Public URL (root) | `https://conanxin.github.io/leonardo-chinese-exhibition/` |
| Public URL (second exhibition) | `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` |
| v5.3 deployment Actions run | `29154365778` (success, 18s) |
| v5.3b push Actions run | `29156046423` (success, in `5250404`) |
| Browser / engine | Chromium headless shell `148.0.7778.96` (Chrome for Testing) |
| QA started / finished | `2026-07-11T23:29:11.044Z` → `2026-07-11T23:30:07.186Z` |
| Network policy | Public Pages only; no third-party proxy, no extension, no local server |

## Root identity (HTTP probe)

| Probe | Result |
|---|---|
| `GET /` | HTTP 200, 92,976 bytes |
| `GET /second-exhibition/` | HTTP 200, 25,635 bytes |
| `GET /second-exhibition/style.css` | HTTP 200 |
| `GET /second-exhibition/script.js` | HTTP 200 |
| `GET /second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg` | HTTP 200 (191,606 B) |
| `GET /second-exhibition/assets/images/bhl-318921-page-603962-c03.webp` | HTTP 200 (262,498 B) |
| `GET /second-exhibition/assets/images/smithsonian-nmnh-1529703.png` | HTTP 200 (3,550 B) |
| `GET /second-exhibition/assets/images/met-285149.jpg` | HTTP 200 (95,001 B) |
| `GET /second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg` | HTTP 200 (294,445 B) |
| `GET /second-exhibition/assets/images/bhl-318921-page-603998-c01.webp` | HTTP 200 (306,126 B) |
| `sha256sum -c` of all 6 live images vs `second-exhibition/assets/asset-checksums.sha256` | **6/6 OK (byte-identical)** |

### Forbidden paths (must 404)

| Path | HTTP |
|---|---|
| `/data/` | 404 |
| `/docs/` | 404 |
| `/asset-checksums.sha256` | 404 |
| `/asset-import-manifest.json` | 404 |
| `/_template/` | 404 |
| `/_pilots/` | 404 |
| `/reports/` | 404 |
| `/scripts/` | 404 |
| `/.firecrawl/` | 404 |
| `/README.md` | 404 |
| `/V5_ROADMAP.md` | 404 |
| `/V4_ROADMAP.md` | 404 |
| `/second-exhibition/data/` | 404 |
| `/second-exhibition/docs/` | 404 |
| `/second-exhibition/assets/asset-checksums.sha256` | 404 |
| `/second-exhibition/assets/asset-import-manifest.json` | 404 |

All **16/16** forbidden public paths return HTTP 404.

## Status wording (5/5 viewports)

| Viewport | `production-deployed-v5.3` | `published-in-v5.3` | `imported-not-deployed` (historical record only) | `repository-only-not-deployed` | "未部署" stale phrase |
|---|---|---|---|---|---|
| 1440 × 1000 | ✅ visible | ✅ visible | ✅ visible (import-record annotation only) | ❌ absent | ❌ absent |
| 1280 × 900 | ✅ visible | ✅ visible | ✅ visible (import-record annotation only) | ❌ absent | ❌ absent |
| 768 × 1024 | ✅ visible | ✅ visible | ✅ visible (import-record annotation only) | ❌ absent | ❌ absent |
| 390 × 844 | ✅ visible | ✅ visible | ✅ visible (import-record annotation only) | ❌ absent | ❌ absent |
| 320 × 700 | ✅ visible | ✅ visible | ✅ visible (import-record annotation only) | ❌ absent | ❌ absent |

The historical `imported-not-deployed` phrase still appears in the body text, **only** inside the explicit "Import record: imported-not-deployed (v4.5)" annotation on each artifact card — it never appears as a current-status claim, matching the v5.3b status layering contract.

## Five-viewport matrix

| Viewport | Title contains 植物图谱与视觉分类 | `<section class="deep-block">` (must = 4) | `section` total (informational) | artifact cards (`[data-candidate-id]`) | glossary items (`.glossary-item`) | source notes (`.source-note`) | credit lines (`.credit-line`) | images loaded / total | horizontal overflow |
|---|---|---|---|---|---|---|---|---|---|
| 1440 × 1000 | ✅ | 4 | 13 | 6 (C-01, C-03, C-06, C-08, C-09, C-10) | 12 | 6 | 6 | 6 / 6 (+ 1 zero-src SVG icon) | no |
| 1280 × 900 | ✅ | 4 | 13 | 6 | 12 | 6 | 6 | 6 / 6 (+ 1 zero-src SVG icon) | no |
| 768 × 1024 | ✅ | 4 | 13 | 6 | 12 | 6 | 6 | 6 / 6 (+ 1 zero-src SVG icon) | no |
| 390 × 844 | ✅ | 4 | 13 | 6 | 12 | 6 | 6 | 6 / 6 (+ 1 zero-src SVG icon) | no |
| 320 × 700 | ✅ | 4 | 13 | 6 | 12 | 6 | 6 | 6 / 6 (+ 1 zero-src SVG icon) | no |

Notes:
- `section.total` (13) counts every `<section>` (hero, artifact-cards, glossary, three deep-block sections, source-rights, footer, lightbox scaffold); the brief-defined `sections = 4` requirement refers to the curated deep-block sections (`.deep-block` = 4), which is satisfied in every viewport.
- `imgLoaded` counts images with `naturalWidth > 0`. The 7th entry per viewport is the zero-src favicon SVG icon (no real image to load); every curated candidate image has `naturalWidth > 0` and `complete === true` after the long-wait + full-page-scroll settle.
- `horizontal overflow` is computed as `bodyWidth > viewportWidth || docWidth > viewportWidth`. All five viewports show zero overflow.

## Image natural sizes per viewport (sample — 1440×1000)

| Image | naturalWidth × naturalHeight | complete | alt coverage |
|---|---|---|---|
| bhl-318921-page-603998-c01.webp | 2144 × 3504 | true | ✅ |
| bhl-318921-page-603962-c03.webp | 2124 × 3514 | true | ✅ |
| smithsonian-nmnh-1529703.png | 90 × 90 | true | ✅ |
| met-285149.jpg | 449 × 624 | true | ✅ |
| rijksmuseum-rp-f-f80152.jpg | 1024 × 1293 | true | ✅ |
| rijksmuseum-rp-f-f80313.jpg | 1024 × 1291 | true | ✅ |

The other four viewports report the same six images with the same naturalWidth × naturalHeight (the SVG icon always has src="" and naturalWidth=0).

## Interaction (1440 × 1000)

| Interaction | Result |
|---|---|
| Guided toggle (`#guided-toggle`) found | ✅ |
| `aria-pressed` before click | `false` |
| `aria-pressed` after click | `true` |
| Toggle state correctly switched | ✅ |
| C-01 lightbox opens on click | ✅ (`<div id="lightbox" role="dialog" aria-modal="true" aria-labelledby="lightbox-title">`) |
| Trigger element | `<img>` with `role="button"`, `aria-label="在 lightbox 中查看 C-01"` |
| Dialog accessible name (computed via `aria-labelledby`) | **`图片查看器`** (text content of `#lightbox-title` `<h2 class="visually-hidden">图片查看器</h2>`) |
| Close button focus on open | ✅ |
| `ESC` closes lightbox | ✅ |
| Focus returns to C-01 trigger after close | ✅ |
| C-06 lightbox click is blocked | ✅ (low-resolution warning visible, no dialog opens) |
| Section navigation links (count) | 6 |
| First section nav click updates `window.location.hash` | ✅ |
| Tab-reachable primary buttons (`button` + `role="button"`, visible, non-disabled) | 6 |

## Accessibility

| Check | Result |
|---|---|
| Image alt coverage (5 viewports × 7 images, minus the zero-src SVG icon) | 30/35 with non-empty alt (86%); 5 misses are decorative `<img>` placeholders inside lightbox scaffold with `alt=""` by design |
| Close button receives focus on lightbox open | ✅ |
| Focus returns to C-01 trigger after ESC close | ✅ |
| Dialog accessible name resolves to `图片查看器` via `aria-labelledby="lightbox-title"` | ✅ |
| Tab reaches primary buttons | ✅ (6 visible, non-disabled) |
| Section navigation uses real `<a href="#…">` links | ✅ |

## no-JS render (JavaScript disabled, 1440 × 1000)

| Probe | Result |
|---|---|
| `<title>` | `植物图谱与视觉分类 · 第二展览 v0.1` |
| `production-deployed-v5.3` in body text | ✅ |
| `published-in-v5.3` in body text | ✅ |
| `imported-not-deployed` in body text | ✅ (preserved historical record) |
| artifact card count (`[data-candidate-id]`) | 6 |
| source notes / credit lines visible | 12 / 6 (`.source-note` = 12 incl. prose + cards; `.credit-line` = 6) |
| `.repository-status` element visible | ✅ |

The page is fully readable with JavaScript disabled: status wording, candidate cards, source notes, credit lines, and historical import record all survive.

## reduced-motion (1440 × 1000, `reducedMotion: "reduce"`)

| Check | Result |
|---|---|
| `matchMedia('(prefers-reduced-motion: reduce)').matches` | true |
| Lightbox opens under reduced motion | ✅ |
| ESC closes lightbox under reduced motion | ✅ |

## Requests / errors / external

| Metric | 1440×1000 | 1280×900 | 768×1024 | 390×844 | 320×700 | Total |
|---|---|---|---|---|---|---|
| External (non-`conanxin.github.io`) requests | 0 | 0 | 0 | 0 | 0 | **0** |
| Failed requests | 0 | 0 | 0 | 0 | 0 | **0** |
| Console errors | 0 | 0 | 0 | 0 | 0 | **0** |
| Page errors | 0 | 0 | 0 | 0 | 0 | **0** |
| Horizontal overflow | no | no | no | no | no | **0** |

`externalHosts` set across all five viewports is **empty**: every loaded resource (HTML / CSS / JS / 6 images) is fetched from `conanxin.github.io`.

## Source / rights evidence unchanged

No tracked file under the following paths was modified this round (`git status -sb`):

- `second-exhibition/site/`
- `second-exhibition/data/`
- `second-exhibition/assets/`
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md`
- `site/`
- `_template/`
- `_pilots/`
- `release-assets/`
- `reports/` (existing files)
- `.github/workflows/pages.yml`
- `scripts/` (no changes; the QA runner was placed under `/tmp/qa/`, not the repo)

## Working tree state (this round)

| Field | Value |
|---|---|
| `git status -sb` | 0 modified, 3 untracked (`.firecrawl/`, 2 v5.3b prep files) |
| `git reflog` | unchanged at `5250404` (no new commits this round) |
| `git diff --check` | clean |
| No `git add` performed in this round | confirmed |
| No `git commit` performed in this round | confirmed |
| No `git push` performed in this round | confirmed |
| No GitHub Actions triggered | confirmed |
| No real Pages deploy | confirmed |
| No tag / Release created | confirmed |
| Production state | unchanged from `5250404` |

## Rollback method

If a follow-up round finds a regression traced to v5.3b's status wording, rollback is a single `git revert <v5.3c-commit-sha>` followed by `git push origin main`. The v5.3c commit modifies only `docs/V5_ROADMAP.md`, `README.md`, `docs/SECOND_EXHIBITION_LIVE_PRODUCTION_QA_v5.3c.md`, and `reports/leonardo_chinese_exhibition_v5_3c_live_production_browser_qa_report.md`; no live page / data / asset / workflow file is touched, so the revert restores HEAD `5250404`'s live state bit-for-bit.

## Required authorization

```
DEPLOY v5.3c
```

Only after receiving this exact string will commit + push of the two new docs and the README/ROADMAP update be executed.