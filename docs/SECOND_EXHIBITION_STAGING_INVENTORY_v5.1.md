# Second Exhibition Staging Inventory — v5.1

**Round:** v5.1-staging-artifact-build
**Date:** 2026-07-11
**Baseline commit:** `5218b43809fa4ab7a78545797e057d72b51e1826`
**Source tag:** `v4.8-real-second-exhibition-repository-hardening`
**Staging artifact path:** `/tmp/leonardo-pages-artifact` (outside repository)
**Staging audit path:** `/tmp/leonardo-pages-artifact-audit` (outside repository, sibling to artifact)
**Deployment status:** `staging-only — not deployed` (builder sets `deployment_status` field in `build-summary.json` to the same literal value)
**Workflow:** `.github/workflows/pages.yml` unchanged — still `path: site` (top-level only)

---

## Artifact root (Leonardo main site)

- **Source:** `site/` (top-level)
- **Destination:** staging artifact root
- **File count:** 25 regular files (recursive)
- **Comparison method:** byte-identical copy of every file; per-file SHA256 cross-check against source
- **Identity result:** all 25 files match source SHA256
- **Top-level index byte:** `92,976` (matches production live)
- **v2.9 marker:** `1` occurrence in staged `index.html` (`v2.9-real-source-rights-audit`)

Files in staging root (sample of public-facing ones; full inventory in
`/tmp/leonardo-pages-artifact-audit/root-site-sha256.txt`):

| Public path (top-level) | Type | Bytes |
|-------------------------|------|------:|
| `index.html` | HTML | 92,976 |
| `style.css` | CSS | 42,079 |
| `script.js` | JS | 14,594 |
| `assets/og-cover.svg` | SVG | (image asset) |
| `assets/favicon.svg` | SVG | (image asset) |
| `assets/diagrams/*.svg` | SVG × 7 | (vector diagrams) |
| `assets/images/codex-atlanticus/*.jpg` | JPG × 2 | (high-resolution plates) |
| `assets/images/royal-collection/*.jpg` | JPG × 4 | (Royal Collection images) |
| `assets/images/platform/*.jpg` | JPG × 5 | (platform screenshots) |
| `assets/README.md`, `assets/images/README.md` | MD × 2 | (attribution; existing in source) |

(Total regular files in staging root: **25**; subdirectories under staging root are byte-identical copies of `site/`.)

---

## Second exhibition public subtree

- **Path:** `second-exhibition/` (inside staging artifact root)
- **Source:** `second-exhibition/site/` (HTML/CSS/JS) + `second-exhibition/assets/images/` (raster)
- **Public file count:** **9** (3 site files + 6 raster images)
- **Path rewrite:** `../assets/images/` → `./assets/images/`, applied only to the staged
  `second-exhibition/index.html`. Tracked source `second-exhibition/site/index.html` is
  byte-identical to its pre-build state.

| Public path | Source path | Type | Bytes | SHA256 | Rewrite? |
|-------------|-------------|------|------:|--------|----------|
| `second-exhibition/index.html` | `second-exhibition/site/index.html` | HTML | 24,380 | `3ad41fc27154d46f58ca69b2de1191a0045b92325e21863f0d4c27e74f72269d` | yes (6 lines) |
| `second-exhibition/style.css` | `second-exhibition/site/style.css` | CSS | 8,261 | `787db9766240bdc69beff0c03f2513c2da384574bc5c7d06c888cd4bcbda4237` | no |
| `second-exhibition/script.js` | `second-exhibition/site/script.js` | JS | 4,070 | `d0c760a5fd93d0a3c9fdb565dfc2d359b16489614ad1ef52bed28f614da87b11` | no |
| `second-exhibition/assets/images/bhl-318921-page-603998-c01.webp` | `second-exhibition/assets/images/bhl-318921-page-603998-c01.webp` | WEBP | 306,126 | `dc4b292536761be5bdf8a459d5ef82c53c4ecf5e39252ab68d19c233293522b7` | no |
| `second-exhibition/assets/images/bhl-318921-page-603962-c03.webp` | `second-exhibition/assets/images/bhl-318921-page-603962-c03.webp` | WEBP | 262,498 | `446d744d9b647f299532fc248e3263f14db818dff591f2c99264beb18c7d881d` | no |
| `second-exhibition/assets/images/smithsonian-nmnh-1529703.png` | `second-exhibition/assets/images/smithsonian-nmnh-1529703.png` | PNG | 3,550 | `75f523b06cc1a62713de51b1ba3a51fc4d43c4ac19268c48478d30c9e2af73a1` | no |
| `second-exhibition/assets/images/met-285149.jpg` | `second-exhibition/assets/images/met-285149.jpg` | JPG | 95,001 | `976b1cbd365a7ddeef961e1b865ba537e5f898487b8984b49eb9cfac33dc47bf` | no |
| `second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg` | `second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg` | JPG | 294,445 | `d3832eb3e667065892528f014affab34c2b0c2db632b8e56683826cc3c089502` | no |
| `second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg` | `second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg` | JPG | 191,606 | `10762705aad12906d5d13d4af9afa0e40c6dcceb54708f55eefc361fe74990ba` | no |

Path rewrite details:
- Source `second-exhibition/site/index.html` contains 6 references to `../assets/images/`
  (one per artifact card `<img>`).
- Staged `second-exhibition/index.html` contains 0 references to `../assets/images/` and
  6 references to `./assets/images/`.
- Only 6 lines differ between source and staged index.html; all 6 are the rewritten
  `../` → `./` substitutions.
- Tracked source `second-exhibition/site/index.html` SHA256 unchanged before and after
  the build (verified in build-summary.json cross-check).

---

## Excluded repository content

The following content intentionally does **not** appear in the staging artifact:

- `second-exhibition/site/README.md` (if present) — internal note
- `second-exhibition/data/` (exhibition JSON, sections JSON)
- `second-exhibition/docs/` (`SOURCE_AUDIT_MANIFEST.md`, `RIGHTS_AND_SOURCES.md`)
- `second-exhibition/assets/asset-import-manifest.json`
- `second-exhibition/assets/asset-checksums.sha256`
- All `_template/` content
- All `_pilots/` content
- All `reports/` content
- All `scripts/` content (including the QA scripts themselves)
- All `.firecrawl/` content (not handled at all in this round)
- Top-level `README.md`, `V4_ROADMAP.md`, `V5_ROADMAP.md`
- Hidden files / repository metadata

Verification: `python3 scripts/second_exhibition_staging_gate.py` section F
(forbidden exposure) reports **OK** for all subchecks.

---

## Audit outputs

Path: `/tmp/leonardo-pages-artifact-audit/` (sibling to artifact, **not** in artifact).

| File | Purpose |
|------|---------|
| `artifact-files.txt` | Newline-delimited list of every regular file path inside the staging artifact |
| `artifact-sha256.txt` | `sha256  path` per file (all 34 staged files: 25 main-site + 9 second-exhibition) |
| `root-site-sha256.txt` | `sha256  path` for the 25 main-site files only |
| `second-exhibition-sha256.txt` | `sha256  path` for the 9 second-exhibition files |
| `build-summary.json` | Machine-readable build summary with source_commit, deployment_status, file counts, rewrite count, source/staged hashes |

These audit files are **not** part of the public artifact and are not committed to the
repository. They live only in `/tmp/leonardo-pages-artifact-audit/`.

---

## Verification commands (reproducible)

```bash
# 1. Build
rm -rf /tmp/leonardo-pages-artifact /tmp/leonardo-pages-artifact-audit
python3 scripts/second_exhibition_staging_build.py \
  --output /tmp/leonardo-pages-artifact

# 2. Gate
python3 scripts/second_exhibition_staging_gate.py \
  --artifact /tmp/leonardo-pages-artifact \
  --audit /tmp/leonardo-pages-artifact-audit

# 3. Local HTTP QA (start server in separate terminal)
python3 -m http.server 8771 --directory /tmp/leonardo-pages-artifact &
curl -L -sS http://127.0.0.1:8771/                    # expect 200, 92976 B
curl -L -sS http://127.0.0.1:8771/second-exhibition/  # expect 200, title present

# 4. Browser QA (requires playwright)
SECOND_EXHIBITION_QA_URL=http://127.0.0.1:8771/second-exhibition/ \
  node scripts/second_exhibition_browser_qa.mjs
```

All steps must exit `0`. Production Pages site is **never** touched by any of these steps.