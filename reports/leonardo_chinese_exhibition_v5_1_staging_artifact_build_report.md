# Leonardo Chinese Exhibition — v5.1 Second Exhibition Staging Artifact Build Report

**Round:** v5.1-staging-artifact-build
**Date:** 2026-07-11
**STATUS:** **PASS** — staging-only, not deployed

---

## Baseline

| Item | Value |
|------|-------|
| Baseline HEAD | `5218b43809fa4ab7a78545797e057d72b51e1826` |
| Origin/main | `5218b43809fa4ab7a78545797e057d72b51e1826` (matches) |
| Source tag | `v4.8-real-second-exhibition-repository-hardening` |
| Source tag object | `1c868b054424c348f273be4148a6a3f184e374ba` (annotated) |
| Source tag target | `a70c8430a8e3d01153153e54f055d9907340d6b7` |
| Existing live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Existing live byte | **92,976 B** (unchanged) |

---

## Quality gates (pre-build)

| Gate | Result |
|------|--------|
| Template quality gate | PASS 37/37 |
| Second-exhibition build gate | PASS |
| Repository QA | 161 PASS / 0 FAIL / 0 WARNINGS |
| Deployment preflight (v5.0) | PASS |
| Asset checksums | 6/6 PASS |
| JavaScript syntax (`script.js`) | PASS |
| JavaScript syntax (`browser_qa.mjs`) | PASS |

---

## Staging builder

- Script: `scripts/second_exhibition_staging_build.py`
- Run command: `python3 scripts/second_exhibition_staging_build.py --output /tmp/leonardo-pages-artifact`
- Exit code: **0 (PASS)**
- Staging output path: `/tmp/leonardo-pages-artifact`
- Staging audit path: `/tmp/leonardo-pages-artifact-audit`
- `deployment_status` field: `staging-only — not deployed`

---

## Staging gate

- Script: `scripts/second_exhibition_staging_gate.py`
- Run command: `python3 scripts/second_exhibition_staging_gate.py --artifact /tmp/leonardo-pages-artifact --audit /tmp/leonardo-pages-artifact-audit`
- Exit code: **0 (PASS)**

| Section | Subchecks | Result |
|---------|-----------|--------|
| A. Artifact location | 7 | OK |
| B. Main-site identity | 6 | OK |
| C. Second-exhibition public tree | 4 | OK |
| D. Path rewrite | 5 | OK |
| E. Asset integrity | 7 | OK |
| F. Forbidden exposure | 3 | OK |
| G. Audit separation | 8 | OK |
| H. Deployment status | 1 | OK |

---

## File accounting

| Category | Source count | Staged count | Identity |
|----------|-------------:|-------------:|----------|
| Main-site regular files | 25 | 25 | byte-identical (SHA256) |
| Main-site subdirectories | (recursive) | (recursive) | structure preserved |
| Staging top-level `index.html` bytes | 92,976 | 92,976 | identical |
| Staging top-level v2.9 marker count | 1 | 1 | identical |
| Staging top-level added dirs | 0 | 1 (`second-exhibition/`) | expected |
| Second-exhibition public files | 3 site + 6 images = 9 | 9 | allowlist only |
| Path rewrites in staged `index.html` | 0 | 6 | `../` → `./` |
| Source `index.html` SHA before build | `0e7569e...fae6` | `0e7569e...fae6` | unchanged |

---

## Staged second-exhibition files

| Public path | Bytes | SHA256 |
|-------------|------:|--------|
| `second-exhibition/index.html` | 24,380 | `3ad41fc27154d46f58ca69b2de1191a0045b92325e21863f0d4c27e74f72269d` |
| `second-exhibition/style.css`  |  8,261 | `787db9766240bdc69beff0c03f2513c2da384574bc5c7d06c888cd4bcbda4237` |
| `second-exhibition/script.js`  |  4,070 | `d0c760a5fd93d0a3c9fdb565dfc2d359b16489614ad1ef52bed28f614da87b11` |
| `second-exhibition/assets/images/bhl-318921-page-603998-c01.webp` | 306,126 | `dc4b292536761be5bdf8a459d5ef82c53c4ecf5e39252ab68d19c233293522b7` |
| `second-exhibition/assets/images/bhl-318921-page-603962-c03.webp` | 262,498 | `446d744d9b647f299532fc248e3263f14db818dff591f2c99264beb18c7d881d` |
| `second-exhibition/assets/images/smithsonian-nmnh-1529703.png`     |   3,550 | `75f523b06cc1a62713de51b1ba3a51fc4d43c4ac19268c48478d30c9e2af73a1` |
| `second-exhibition/assets/images/met-285149.jpg`                   |  95,001 | `976b1cbd365a7ddeef961e1b865ba537e5f898487b8984b49eb9cfac33dc47bf` |
| `second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg`      | 294,445 | `d3832eb3e667065892528f014affab34c2b0c2db632b8e56683826cc3c089502` |
| `second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg`      | 191,606 | `10762705aad12906d5d13d4af9afa0e40c6dcceb54708f55eefc361fe74990ba` |

All 6 staged image SHAs match `second-exhibition/assets/asset-checksums.sha256` and the
source images byte-for-byte.

---

## Allowlist / forbidden-file result

| Check | Result |
|-------|--------|
| Allowlist extensions in second-exhibition subtree | 9/9 (`.html`, `.css`, `.js`, `.webp`, `.png`, `.jpg`) |
| `.md` files in artifact | 0 |
| `.json` files in artifact | 0 |
| `.sha256` files in artifact | 0 |
| `asset-import-manifest.json` | not present (excluded) |
| `asset-checksums.sha256` | not present (excluded) |
| `SOURCE_AUDIT_MANIFEST.md` / `RIGHTS_AND_SOURCES.md` | not present (excluded) |
| `_template/` / `_pilots/` / `reports/` / `scripts/` | not present |
| `.firecrawl/` | not present |
| Top-level `README.md` / `V4_ROADMAP.md` / `V5_ROADMAP.md` | not present |
| Hidden files / source maps / executable-bit files | none |

---

## Local HTTP QA (server: `python3 -m http.server 8771 --directory /tmp/leonardo-pages-artifact`)

| URL | Expected | Actual |
|-----|----------|--------|
| `/` | 200, 92,976 B, v2.9 marker 1 | **200, 92,976 B, v2.9 marker 1** |
| `/second-exhibition/` | 200, title present | **200, 24,380 B, title present (×2)** |
| `/second-exhibition/style.css` | 200 | **200, 8,261 B** |
| `/second-exhibition/script.js` | 200 | **200, 4,070 B** |
| `/second-exhibition/assets/images/*.webp` (×2) | 200 | **200** (306,126 B; 262,498 B) |
| `/second-exhibition/assets/images/*.png` | 200 | **200** (3,550 B) |
| `/second-exhibition/assets/images/*.jpg` (×3) | 200 | **200** (95,001 B; 294,445 B; 191,606 B) |
| `/second-exhibition/data/` | 404 | **404** |
| `/second-exhibition/docs/` | 404 | **404** |
| `/second-exhibition/assets/asset-import-manifest.json` | 404 | **404** |
| `/second-exhibition/assets/asset-checksums.sha256` | 404 | **404** |
| `/reports/` | 404 | **404** |
| `/scripts/` | 404 | **404** |
| `/_template/` | 404 | **404** |
| `/_pilots/` | 404 | **404** |

No directory listing or internal file was exposed.

---

## Staging browser QA

- Command: `SECOND_EXHIBITION_QA_URL=http://127.0.0.1:8771/second-exhibition/ node scripts/second_exhibition_browser_qa.mjs`
- Exit code: **0 (PASS)**
- Browser: Chromium 149.0.7827.55 (Playwright bundled)

| Viewport | Result |
|----------|:------:|
| 1440 × 1000 | PASS |
| 1280 × 900 | PASS |
| 768 × 1024 | PASS |
| 390 × 844 | PASS |
| 320 × 700 | PASS |

| Counter | Value |
|---------|------:|
| Console errors | **0** |
| Page errors | **0** |
| Failed requests | **0** |
| External requests | **0** |
| Horizontal overflow | **0** |
| Images loaded per viewport | 6 / 6 |

Interactions verified: guided-mode toggle, lightbox open (`role=dialog`, `aria-labelledby="lightbox-title"`), ESC close, focus return to trigger, section-nav jump, tab-focusable traversal, C-06 lightbox stays closed on initial load.

Accessibility verified: 1 `<h1>`, 0 images missing alt, 0 buttons missing accessible name, visually-hidden title correctly measured (1×1 px, `position: absolute`).

Reduced motion: lightbox opens + ESC closes correctly under `prefers-reduced-motion`.

No-JS path: 6 cards visible, 6 source notes, 6 credit lines, repository-status banner visible, body text content present.

---

## Production state after v5.1

| Check | Result |
|-------|--------|
| Workflow `.github/workflows/pages.yml` modified? | **No** — still `path: site` only |
| Production live byte | **92,976 B** (unchanged) |
| Production v2.9 marker | **1** (unchanged) |
| Production second-exhibition title live count | **0** (unchanged) |
| `/second-exhibition/` Pages URL | **404** |
| `/second-exhibition/index.html` Pages URL | **404** |
| `/second-exhibition/style.css` Pages URL | **404** |
| `/second-exhibition/script.js` Pages URL | **404** |
| `/second-exhibition/assets/images/*.webp|.png|.jpg` Pages URLs | **404** |
| Tags / Releases | **unchanged** (no new tag, no new Release) |

---

## Repository state

| Check | Result |
|-------|--------|
| Repository contains staging artifact? | **No** (artifact lives in `/tmp` only) |
| Repository contains audit files? | **No** (audit lives in `/tmp` only) |
| Working tree clean (excluding `.firecrawl/`)? | **Yes** |
| `git diff -- site/` | empty |
| `git diff -- second-exhibition/site/` | empty |
| `git diff -- second-exhibition/data/` | empty |
| `git diff -- second-exhibition/assets/` | empty |
| `git diff -- second-exhibition/docs/` | empty |
| `git diff -- _template/` | empty |
| `git diff -- _pilots/` | empty |
| `git diff -- .github/workflows/` | empty |
| `git diff -- release-assets/` | empty |

---

## Files added in v5.1

- `scripts/second_exhibition_staging_build.py`
- `scripts/second_exhibition_staging_gate.py`
- `docs/SECOND_EXHIBITION_STAGING_ARTIFACT_BUILD_v5.1.md`
- `docs/SECOND_EXHIBITION_STAGING_INVENTORY_v5.1.md`
- `docs/SECOND_EXHIBITION_STAGING_BROWSER_QA_v5.1.md`
- `docs/V5_ROADMAP.md` (updated)
- `README.md` (updated)
- `reports/leonardo_chinese_exhibition_v5_1_staging_artifact_build_report.md` (this file)

No protected path was modified. No workflow change. No tag. No Release.

---

## Next recommended task

**v5.2-deployment-dry-run** — exercise the Pages workflow change in dry-run mode,
inspect artifact contents, do not publish to production.