# v5.3c Live Production Browser QA Report

## STATUS

**PASS** — public second exhibition verified end-to-end across 5 viewports + 4 environment variants (default, interaction, no-JS, reduced-motion) on `2026-07-11T23:29:11.044Z → 2026-07-11T23:30:07.186Z` using Chromium headless shell `148.0.7778.96` (Chrome for Testing).

## HEAD / origin

| Field | Value |
|---|---|
| HEAD | `52504047a966c0dd9a60b569a63b1857168a498f` |
| `origin/main` | `52504047a966c0dd9a60b569a63b1857168a498f` |
| HEAD subject | `Reconcile second-exhibition production state (v5.3b)` |
| v5.3b push Actions run | `29156046423` (success) |
| v5.3 first deploy Actions run | `29154365778` (success, 18s, all 9 steps green) |
| Recent source-freeze tag | `v4.8-real-second-exhibition-repository-hardening` |

## Live root byte / hash

| Field | Value |
|---|---|
| `GET /` HTTP | 200 |
| `GET /` byte count | **92,976** (uncompressed HTML body) |
| `GET /` SHA-256 | `5a5fd33b96a1be76f6090e1b9b5fce8e14240d7c4dd2d08203ba6da7a3a5bc39` |
| v2.9 marker occurrences in body | 4 |
| Root identity preserved from v5.3 | ✅ |

## Second exhibition status

| Field | Value |
|---|---|
| `GET /second-exhibition/` HTTP | 200 |
| `GET /second-exhibition/` byte count | 25,635 |
| `GET /second-exhibition/style.css` HTTP | 200 |
| `GET /second-exhibition/script.js` HTTP | 200 |
| Top-level `exhibition.json` status (live) | `production-deployed-v5.3` |
| Top-level `assets.json` status (live) | `production-deployed-v5.3` |
| Per-asset `publication_status` (live, 6/6) | `published-in-v5.3` |
| Per-asset `import_status` (preserved, 6/6) | `imported-not-deployed` (v4.5 historical) |
| `deployment_url` in `exhibition.json` | `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` |
| `deployment_round` | `v5.3-controlled-deployment` |

## Five-viewport matrix

| Viewport | Status text trio ✅ | Deep-block sections | Artifact cards | Glossary items | Source notes | Credit lines | Images (loaded/total) | Overflow | Ext / Fail / Console / Page errors |
|---|---|---|---|---|---|---|---|---|---|
| 1440 × 1000 | ✅✅✅ | 4 | 6 | 12 | 6 | 6 | 6 / 6 (+ 1 zero-src SVG icon) | none | 0 / 0 / 0 / 0 |
| 1280 × 900 | ✅✅✅ | 4 | 6 | 12 | 6 | 6 | 6 / 6 (+ 1 zero-src SVG icon) | none | 0 / 0 / 0 / 0 |
| 768 × 1024 | ✅✅✅ | 4 | 6 | 12 | 6 | 6 | 6 / 6 (+ 1 zero-src SVG icon) | none | 0 / 0 / 0 / 0 |
| 390 × 844 | ✅✅✅ | 4 | 6 | 12 | 6 | 6 | 6 / 6 (+ 1 zero-src SVG icon) | none | 0 / 0 / 0 / 0 |
| 320 × 700 | ✅✅✅ | 4 | 6 | 12 | 6 | 6 | 6 / 6 (+ 1 zero-src SVG icon) | none | 0 / 0 / 0 / 0 |

Status text trio = `production-deployed-v5.3` ✅, `published-in-v5.3` ✅, `imported-not-deployed` ✅ (only inside `Import record: imported-not-deployed (v4.5)` annotations).

## Console / page / request errors

| Metric | Total |
|---|---|
| Console errors across all 5 viewports + 4 environment variants | **0** |
| Page errors (uncaught exceptions) | **0** |
| Failed requests | **0** |
| External (non-`conanxin.github.io`) requests | **0** |

## External requests

**Zero.** Every loaded resource — HTML, CSS, JS, 6 images, favicon SVG — is fetched from `conanxin.github.io`. `externalHosts` set is empty.

## Overflow

**Zero** horizontal overflow in any of the 5 viewports. `body.scrollWidth === viewportWidth` and `document.scrollWidth === viewportWidth` for every viewport (1440 / 1280 / 768 / 390 / 320).

## Interactions (1440 × 1000)

| Interaction | Result |
|---|---|
| Guided toggle (`#guided-toggle`) `aria-pressed` change | `false` → `true` ✅ |
| C-01 trigger element | `<img role="button" aria-label="在 lightbox 中查看 C-01">` |
| Lightbox dialog opens | ✅ |
| Dialog `role` | `dialog` |
| Dialog `aria-modal` | `true` |
| Dialog accessible name (computed from `#lightbox-title`) | **`图片查看器`** |
| Close button receives focus on open | ✅ |
| `ESC` keypress closes the lightbox | ✅ |
| Focus returns to C-01 trigger after close | ✅ |
| C-06 (low-resolution) click blocked | ✅ |
| Section navigation links | 6 links, first click updates `window.location.hash` ✅ |
| Tab-reachable primary buttons | 6 visible / non-disabled |

## no-JS render (JavaScript disabled, 1440 × 1000)

| Probe | Result |
|---|---|
| `<title>` | `植物图谱与视觉分类 · 第二展览 v0.1` |
| Body text contains `production-deployed-v5.3` | ✅ |
| Body text contains `published-in-v5.3` | ✅ |
| Body text contains `imported-not-deployed` (historical) | ✅ |
| `[data-candidate-id]` card count | 6 |
| `.source-note` count | 12 (incl. prose) / 6 (in artifact-meta only) |
| `.credit-line` count | 6 |
| `.repository-status` element present | ✅ |

## reduced-motion (1440 × 1000, `reducedMotion: "reduce"`)

| Probe | Result |
|---|---|
| `matchMedia('(prefers-reduced-motion: reduce)').matches` | true |
| Lightbox opens under reduced motion | ✅ |
| `ESC` closes lightbox under reduced motion | ✅ |

## Image SHA comparison (live vs local)

| Image | Live byte count | Live SHA-256 (first 16) | Local SHA-256 (first 16) | Identical? |
|---|---|---|---|---|
| rijksmuseum-rp-f-f80313.jpg | 191,606 | `10762705aad12906` | `10762705aad12906` | ✅ |
| bhl-318921-page-603962-c03.webp | 262,498 | `446d744d9b647f29` | `446d744d9b647f29` | ✅ |
| smithsonian-nmnh-1529703.png | 3,550 | `75f523b06cc1a627` | `75f523b06cc1a627` | ✅ |
| met-285149.jpg | 95,001 | `976b1cbd365a7dde` | `976b1cbd365a7dde` | ✅ |
| rijksmuseum-rp-f-f80152.jpg | 294,445 | `d3832eb3e6670658` | `d3832eb3e6670658` | ✅ |
| bhl-318921-page-603998-c01.webp | 306,126 | `dc4b292536761be5` | `dc4b292536761be5` | ✅ |

`sha256sum -c second-exhibition/assets/asset-checksums.sha256` = **6/6 OK**.

## Forbidden paths

| Path | HTTP |
|---|---|
| `/data/`, `/docs/`, `/_template/`, `/_pilots/`, `/reports/`, `/scripts/`, `/.firecrawl/`, `/README.md`, `/V4_ROADMAP.md`, `/V5_ROADMAP.md`, `/asset-checksums.sha256`, `/asset-import-manifest.json`, `/second-exhibition/data/`, `/second-exhibition/docs/`, `/second-exhibition/assets/asset-checksums.sha256`, `/second-exhibition/assets/asset-import-manifest.json` | **16/16 → 404** |

## Protected paths unchanged

| Path | This round |
|---|---|
| `site/` | ✅ no changes (`git diff` clean) |
| `second-exhibition/site/` | ✅ no changes |
| `second-exhibition/data/` | ✅ no changes |
| `second-exhibition/assets/` (incl. image bytes) | ✅ no changes (`sha256sum -c` 6/6 OK) |
| `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` | ✅ no changes |
| `second-exhibition/docs/RIGHTS_AND_SOURCES.md` | ✅ no changes |
| `_template/` | ✅ no changes |
| `_pilots/` | ✅ no changes |
| `release-assets/` | ✅ no changes |
| `reports/` (existing files) | ✅ no changes |
| `.github/workflows/pages.yml` | ✅ no changes |
| `scripts/` | ✅ no changes (QA runner placed in `/tmp/qa/`) |

## Tags / Releases unchanged

| Tag | Status |
|---|---|
| `v2.0-public-portfolio-case` | unchanged |
| `v2.6-content-stable` | unchanged |
| `v2.7-zh-exhibition-polish` | unchanged |
| `v2.8-real-deep-content` | unchanged |
| `v2.9-real-source-rights-audit` | unchanged |
| `v3.0-real-template-extraction-audit` | unchanged |
| `v3.1-real-second-exhibition-pilot` | unchanged |
| `v3.2-real-template-documentation` | unchanged |
| `v3.3-real-template-quality-gate` | unchanged |
| `v3.4-real-second-exhibition-hardening` | unchanged |
| `v4.7-real-second-exhibition-repository-qa` | unchanged |
| `v4.8-real-second-exhibition-repository-hardening` | unchanged (most recent source-freeze anchor) |
| `v5.0-real-second-exhibition-deployment` | **not created** (deferred to v5.4) |

No GitHub Releases created or modified in this round.

## Next

```
v5.4-real-stable-freeze
```

The next round moves from "live production browser QA" to "public stable freeze":

- Draft `docs/RELEASE_NOTES_v5_0_REAL_SECOND_EXHIBITION_DEPLOYMENT.md`.
- Draft `release-assets/v5.0-real-second-exhibition-deployment-manifest.md`.
- Draft `reports/leonardo_chinese_exhibition_v5_4_public_stable_freeze_report.md`.
- Run all gates one final time.
- Create annotated tag `v5.0-real-second-exhibition-deployment`.
- Push the tag to origin.
- Create the GitHub Release.
- Backfill the freeze report with tag object SHA, tag target SHA, Release URL, `createdAt`, and the v5.3c Actions run ID.

`v5.4` must not move any existing tag or overwrite any existing Release.

## Required authorization

```
DEPLOY v5.3c
```

Only after receiving this exact string will the commit + push + Pages re-deploy (which will re-emit the same 92,976-byte root and the same live second-exhibition page) be executed.