# v4.6 — Second Exhibition Repository Build Report

Round: **v4.6-second-exhibition-repository-build**
Status: **PASS** — 6 of 6 v4.5 imported assets referenced; 4 sections, 6 artifact cards, 12 glossary items, 4 deep blocks; build gate PASS; Playwright QA PASS; live unchanged.

---

## STATUS

**PASS**

## Baseline

| Field | Value |
|---|---|
| Baseline commit (v4.4b) | `01923ea9689f509d3547c64339680e8c571952de` |
| Asset import commit (v4.5) | `2e4cef409d1fbca30b3356aa600c697f0fddc183` |
| HEAD before v4.6 commit | `2e4cef4` |
| origin/main before v4.6 commit | `2e4cef4` |
| Source tag | `v3.4-real-second-exhibition-hardening` |
| Source tag target SHA | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` (untouched) |

## Live before / after

| Metric | Before v4.6 | After v4.6 |
|---|---|---|
| Live byte size | 92,976 B | **92,976 B** (preserved) |
| v2.9-real-source-rights-audit marker | 1 | **1** (preserved) |
| `image-placeholder-pro` count | 0 | **0** (preserved) |
| v4 title (植物图谱与视觉分类) count | 0 | **0** (preserved) |
| `script.js` HEAD | HTTP/2 200 | **HTTP/2 200** (preserved) |

## Gates

| Gate | Result |
|---|---|
| `scripts/template_quality_gate.py` | **PASS, 37/37** |
| `scripts/second_exhibition_asset_gate.py` | **PASS** (exit 0) |
| `scripts/second_exhibition_build_gate.py` | **PASS** (exit 0) |
| `sha256sum -c second-exhibition/assets/asset-checksums.sha256` | **6/6 OK** |
| `node --check second-exhibition/site/script.js` | **OK** (exit 0) |
| Local Playwright QA | **PASS** |

## Data JSON validation

All 4 data JSON files valid:

| File | Valid | Notes |
|---|---|---|
| `second-exhibition/data/exhibition.json` | yes | status=`repository-only-not-deployed`, deployment_status=`repository-only-not-deployed`, section_count=4, artifact_count=6, glossary_count_target=12 |
| `second-exhibition/data/sections.json` | yes | 4 sections, each with id/kicker/title/body/takeaway/viewer_action/artifact_candidate_ids/deep_block_type |
| `second-exhibition/data/glossary.json` | yes | 12 glossary items |
| `second-exhibition/data/assets.json` | yes | 6 assets with candidate_id, filename, local_path, title, institution, identifier, section_id, alt, caption, source_note, credit_line, import_status, low_resolution, lightbox_enabled |

## Repository site files

- `second-exhibition/site/index.html` (24,313 bytes)
- `second-exhibition/site/style.css` (8,015 bytes after mobile fix)
- `second-exhibition/site/script.js` (3,808 bytes)
- `second-exhibition/site/README.md` (2,576 bytes)

## Section / artifact / glossary counts

- Sections: 4
- Artifact cards: 6 (data-candidate-id: C-01, C-03, C-06, C-08, C-09, C-10 — all unique)
- Glossary items: 12
- Deep blocks: 4 (deep-reading-block, material-evidence-block, visual-thinking-block, research-model-block)
- Source notes: 6 (one per artifact card)
- Credit lines: 6 (one per artifact card)
- Repository-status badges: 2 (header + footer)

## Imported assets referenced (count)

- Total: 6 (all 6 v4.5 imports)
- Lightbox enabled: 5 (C-01, C-03, C-08, C-09, C-10)
- Lightbox disabled: 1 (C-06, low-resolution thumbnail)
- Image naturalWidth reported by Chromium:
  - C-01: 2144 px
  - C-03: 2124 px
  - **C-06: 90 px** (matches manifest)
  - C-08: 449 px
  - C-09: 1024 px
  - C-10: 1024 px

## Local Playwright summary

`/usr/bin/python3.12 /tmp/playwright_v46_qa.py` against `http://127.0.0.1:8770/site/`:

- title contains `植物图谱与视觉分类` ✓
- `.repository-status` visible ✓
- 4 `.exhibition-section` present ✓
- 6 `.artifact-card` present ✓
- 12 `.glossary-item` present ✓
- 6 `.source-note` present ✓
- 6 `.credit-line` present ✓
- 6 `.artifact-card img` present, all `complete && naturalWidth > 0` ✓
- C-06 `naturalWidth == 90` ✓
- C-06 `data-lightbox-enabled="false"` ✓
- C-01 lightbox open via click ✓
- ESC closes lightbox ✓
- `#guided-toggle` toggle shows/hides `#guided-mode-banner` ✓
- desktop (1280×900) no horizontal overflow (body scrollWidth ≤ 1280) ✓
- mobile (390×844) no horizontal overflow (body scrollWidth ≤ 390) ✓
- console errors: **0** ✓
- failed requests: **0** ✓

## C-06 low-resolution handling

- `data-low-resolution="true"` + `data-lightbox-enabled="false"` in C-06 artifact card
- CSS: `.artifact-card[data-low-resolution="true"] img { max-width: 180px; width: auto; }`
- viewing-note explicitly says "低分辨率缩略图；不放大；不启用 lightbox"
- image-rendering uses browser default (not pixelated, not blurred)
- C-06 is **not** used as Hero or wide-screen background

## Asset integrity (no-change confirmation)

| Path | Diff after v4.6 |
|---|---|
| `second-exhibition/assets/images/*` | **empty** |
| `second-exhibition/assets/asset-import-manifest.json` | **empty** |
| `second-exhibition/assets/asset-checksums.sha256` | **empty** |
| `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` | **empty** |
| `second-exhibition/docs/RIGHTS_AND_SOURCES.md` | **empty** |

## Protected paths (no-change confirmation)

| Path | Diff after v4.6 |
|---|---|
| `site/index.html`, `site/style.css`, `site/script.js` | **empty** |
| `_template/site/` | **empty** |
| `_template/data/` | **empty** |
| `_pilots/second-exhibition-pilot/` | **empty** |
| `posts/`, `case-study/`, `release-assets/` | **empty** |
| `scripts/template_quality_gate.py` | **empty** |
| `scripts/second_exhibition_asset_gate.py` | **empty** |

## Second exhibition Pages URLs (not exposed)

All `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/...` URLs return HTTP 404 because the Pages workflow (`.github/workflows/pages.yml`) deploys only the top-level `site/` directory.

Verified URLs:

- `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` → **404**
- `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/site/` → **404**
- `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/site/index.html` → **404**
- `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/assets/images/<any>` → **404**

## Tags / Releases (no-change confirmation)

| Tag | Target SHA (untouched) |
|---|---|
| `v3.4-real-second-exhibition-hardening` | `81f5e928` |
| `v3.3-real-template-quality-gate` | `fce2efb5` |
| `v3.2-real-template-documentation` | `5a89fb20` |
| `v3.1-real-second-exhibition-pilot` | `c5e93d0f` |
| `v3.0-real-template-extraction-audit` | `dd7d589f` |
| `v2.9-real-source-rights-audit` | `a1e667e3` |
| `v2.6-content-stable` | (untouched) |
| `v2.0-public-portfolio-case` | (untouched) |

No new tag, no new GitHub Release.

## Forbidden status audit

The status words `approved`, `deployed`, `live`, `safe for commercial use`, and `cleared for all uses` are intentionally **not used** as a Status value anywhere in v4.6 artifacts. The build gate enforces this.

## Next task

**v4.7-second-exhibition-repository-qa** — separate round that does a deeper QA sweep without changing repository structure.

If v4.7 is `pass`, the next round is **v4.8-second-exhibition-deploy-decision** (a separate round that explicitly authorizes live publication and runs the full source-and-rights audit a second time on the to-be-deployed working tree).

**STATUS: PASS**