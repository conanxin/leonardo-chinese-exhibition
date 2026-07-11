# Second Exhibition Base-Path QA — v5.2

**Round:** v5.2-deployment-dry-run
**Date:** 2026-07-11
**STATUS:** **PASS** — 14/14 allowlist + 16/16 forbidden probes + 5/5 viewports

---

## Project-site base path model

GitHub Pages serves a user/org site at the apex (`https://<owner>.github.io/`) or a
project site under `/<repo>/`. This repository (`conanxin/leonardo-chinese-exhibition`)
is a **project site**, so the public base path is:

```
/leonardo-chinese-exhibition/
```

Every public URL is prefixed with this base path:

| Public URL | Path under base |
|------------|-----------------|
| `https://conanxin.github.io/leonardo-chinese-exhibition/` | `/leonardo-chinese-exhibition/` |
| `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` | `/leonardo-chinese-exhibition/second-exhibition/` |
| `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/assets/images/bhl-...webp` | `/leonardo-chinese-exhibition/second-exhibition/assets/images/bhl-...webp` |

The dry-run simulates this by running a local `BasePathHTTPRequestHandler` that
translates `/<repo>/<rest>` → `<artifact>/<rest>`.

---

## Allowlist probes (14/14 PASS)

Probe server URL pattern: `http://127.0.0.1:<port>/leonardo-chinese-exhibition/<rest>`.

| Probe name | URL | HTTP | Bytes |
|------------|-----|-----:|------:|
| root_index | `/leonardo-chinese-exhibition/` | 200 | 92,976 |
| root_index_html | `/leonardo-chinese-exhibition/index.html` | 200 | 92,976 |
| root_style_css | `/leonardo-chinese-exhibition/style.css` | 200 | 42,079 |
| root_script_js | `/leonardo-chinese-exhibition/script.js` | 200 | 14,594 |
| se_index | `/leonardo-chinese-exhibition/second-exhibition/` | 200 | 24,380 |
| se_index_html | `/leonardo-chinese-exhibition/second-exhibition/index.html` | 200 | 24,380 |
| se_style_css | `/leonardo-chinese-exhibition/second-exhibition/style.css` | 200 | 8,261 |
| se_script_js | `/leonardo-chinese-exhibition/second-exhibition/script.js` | 200 | 4,070 |
| se_img_1 (bhl-...c01.webp) | `/leonardo-chinese-exhibition/second-exhibition/assets/images/bhl-318921-page-603998-c01.webp` | 200 | 306,126 |
| se_img_2 (bhl-...c03.webp) | `/leonardo-chinese-exhibition/second-exhibition/assets/images/bhl-318921-page-603962-c03.webp` | 200 | 262,498 |
| se_img_3 (smithsonian-nmnh-1529703.png) | `/leonardo-chinese-exhibition/second-exhibition/assets/images/smithsonian-nmnh-1529703.png` | 200 | 3,550 |
| se_img_4 (met-285149.jpg) | `/leonardo-chinese-exhibition/second-exhibition/assets/images/met-285149.jpg` | 200 | 95,001 |
| se_img_5 (rijksmuseum-rp-f-f80152.jpg) | `/leonardo-chinese-exhibition/second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg` | 200 | 294,445 |
| se_img_6 (rijksmuseum-rp-f-f80313.jpg) | `/leonardo-chinese-exhibition/second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg` | 200 | 191,606 |

All byte counts match the staging artifact file sizes recorded by the v5.1 builder.

---

## Forbidden probes (16/16 PASS — all 404)

| Path | Expected | Actual |
|------|---------:|-------:|
| `/leonardo-chinese-exhibition/second-exhibition/data/` | 404 | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/docs/` | 404 | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/data/exhibition.json` | 404 | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/data/sections.json` | 404 | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` | 404 | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/docs/RIGHTS_AND_SOURCES.md` | 404 | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/asset-import-manifest.json` | 404 | 404 |
| `/leonardo-chinese-exhibition/second-exhibition/assets/asset-checksums.sha256` | 404 | 404 |
| `/leonardo-chinese-exhibition/_template/` | 404 | 404 |
| `/leonardo-chinese-exhibition/_pilots/` | 404 | 404 |
| `/leonardo-chinese-exhibition/reports/` | 404 | 404 |
| `/leonardo-chinese-exhibition/scripts/` | 404 | 404 |
| `/leonardo-chinese-exhibition/.firecrawl/` | 404 | 404 |
| `/leonardo-chinese-exhibition/README.md` | 404 | 404 |
| `/leonardo-chinese-exhibition/V4_ROADMAP.md` | 404 | 404 |
| `/leonardo-chinese-exhibition/V5_ROADMAP.md` | 404 | 404 |

Out-of-base sanity: `/some-other-base/second-exhibition/` → 404.

---

## Base-path assertions on `/second-exhibition/index.html`

| Assertion | Expected | Actual |
|-----------|---------:|-------:|
| Byte count | 24,380 | **24,380** |
| Title contains `植物图谱与视觉分类` | yes | **yes (count = 2)** |
| `../assets/images/` references | 0 | **0** |
| `./assets/images/` references | 6 | **6** |
| Image links resolve under base path | 6/6 | **6/6** |

The staged `index.html` uses `./assets/images/...` (artifact-only rewrite applied in
v5.1). The page sends 6 image requests, all resolved locally against the base path.

---

## Browser QA under base path

Setup:

- Local base-path server: `python3 /tmp/v52-basepath-helper.py 8773 /tmp/leonardo-pages-artifact`
- Target URL: `http://127.0.0.1:8773/leonardo-chinese-exhibition/second-exhibition/`
- Wrapper: `scripts/second_exhibition_deployment_dry_run_browser.mjs`
- Browser: Chromium 149.0.7827.55 (Playwright bundled, installed under
  `/tmp/playwright-test/node_modules/playwright` for this round)

**Result: PASS, 5/5 viewports.**

| Counter | Value |
|---------|------:|
| Console errors | 0 |
| Page errors | 0 |
| Failed requests | 0 |
| External requests | 0 |
| Horizontal overflow | 0 |
| Images loaded per viewport | 6 / 6 |

Interactions: guided-toggle, lightbox (role=dialog, aria-labelledby=lightbox-title),
ESC close, focus return to trigger, section-nav jump, tab-focusable traversal, C-06
lightbox stays closed on initial load.

Accessibility: 1 `<h1>`, 0 images missing alt, 0 buttons missing accessible name,
visually-hidden title correctly measured.

Reduced motion: lightbox opens + ESC closes correctly under `prefers-reduced-motion`.

No-JS: 6 cards / 6 source notes / 6 credit lines / repo-status banner visible / body
text content present.

---

## Conclusion

Under the project-site base path `/leonardo-chinese-exhibition/`:

- The staging artifact mounts cleanly and serves the same byte count as production.
- All 14 public URLs return 200 with the exact byte sizes recorded in v5.1.
- All 16 forbidden URLs return 404 — no internal content leaks under the base path.
- Browser QA passes against the project-site URL with zero errors.
- Pack → tar.gz → unpack preserves per-file SHA256 identity.
- Rollback rehearsal documents a 1-line revert that restores `path: site`.

The artifact is ready for v5.3 controlled deployment (one-line workflow change).