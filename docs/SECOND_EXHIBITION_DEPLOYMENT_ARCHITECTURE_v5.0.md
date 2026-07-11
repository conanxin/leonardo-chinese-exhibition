# v5.0 Second Exhibition Deployment Architecture

## Recommendation

**Option A — Existing GitHub Pages subpath**, with an **isolated staging artifact** that lives outside the repository working tree. No repository-root upload. The existing top-level site keeps its current byte-for-byte content.

## Repository source layout (unchanged in v5.0)

The repository source tree (everything that stays version-controlled) is unchanged by v5.0:

```
.
├── site/                            # existing top-level Leonardo site (currently deployed)
│   ├── index.html
│   ├── style.css
│   └── script.js
└── second-exhibition/               # repository-only second exhibition
    ├── site/
    │   ├── index.html
    │   ├── style.css
    │   └── script.js
    ├── data/                        # NOT to be published
    ├── assets/
    │   └── images/                  # 6 raster assets, the only artifact-eligible files
    └── docs/                        # NOT to be published
        ├── SOURCE_AUDIT_MANIFEST.md
        ├── RIGHTS_AND_SOURCES.md
        ├── VISITOR_GUIDE_ZH.md
        ├── CURATORIAL_ESSAY_ZH.md
        ├── DEEP_RESEARCH_NOTES_ZH.md
        └── BUILD_ASSET_USAGE.md
```

## Staging artifact layout (outside the repo)

The deployment staging directory lives outside the repository, e.g. `/tmp/leonardo-pages-artifact/`. It is **never** committed.

```
/tmp/leonardo-pages-artifact/
├── index.html                      # copy of site/index.html (byte-identical)
├── style.css                       # copy of site/style.css (byte-identical)
├── script.js                       # copy of site/script.js (byte-identical)
└── second-exhibition/
    ├── index.html                  # path-rewritten copy of second-exhibition/site/index.html
    ├── style.css                   # copy of second-exhibition/site/style.css (no rewrite needed)
    ├── script.js                   # copy of second-exhibition/site/script.js (no rewrite needed)
    └── assets/
        └── images/                 # 6 raster assets, copied from second-exhibition/assets/images/
            ├── bhl-318921-page-603998-c01.webp
            ├── bhl-318921-page-603962-c03.webp
            ├── smithsonian-nmnh-1529703.png
            ├── met-285149.jpg
            ├── rijksmuseum-rp-f-f80152.jpg
            └── rijksmuseum-rp-f-f80313.jpg
```

## What is NOT published

- Any file under `second-exhibition/data/` (machine-readable evidence stays private).
- Any file under `second-exhibition/docs/` (curatorial essay, deep research notes, source/rights audit, build asset usage, visitor guide — these are repository-only artifacts).
- `second-exhibition/assets/asset-import-manifest.json` and `second-exhibition/assets/asset-checksums.sha256` (audit metadata).
- Any `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`, `docs/`, `reports/`, `.git/`, `.firecrawl/`.
- The repository root itself.

## What IS published

- `site/index.html`, `site/style.css`, `site/script.js` (current Pages artifact, byte-identical).
- `second-exhibition/index.html`, `second-exhibition/style.css`, `second-exhibition/script.js` (the second exhibition's static files).
- 6 raster images under `second-exhibition/assets/images/`.

## Path rewriting strategy

The current source page references its images with `../assets/images/...` because the local serving contract is:

```
http://127.0.0.1:8770/site/   ← served from second-exhibition/ root
                              (so /site/index.html has ../assets/images/ → second-exhibition/assets/images/)
```

When deployed under `/second-exhibition/`, the relative reference from `/second-exhibition/index.html` should resolve to `/second-exhibition/assets/images/...`. Two strategies are possible:

### A. Artifact-only path rewrite (recommended)

- Do **not** modify the tracked `second-exhibition/site/index.html`.
- During staging assembly, perform a deterministic text-rewrite on the staging copy:
  - Replace every `src="../assets/images/` → `src="./assets/images/`
  - Replace every `href="../docs/` → blocked (do not rewrite; remove)
- Track the rewrite count and a hash inventory before / after.
- Build a regression test that the source-tree `index.html` is **unchanged** in the final commit.

### B. Repository source path refactor (rejected)

- Edit the tracked `second-exhibition/site/index.html` to use `./assets/images/`.
- This would break the existing local serving contract, change the existing QA behavior, and require re-running the full repository QA matrix. Not recommended because v4.8 is already frozen.

## Build / deploy sequence (overview)

1. **Pre-build verification:** all gates PASS, checksums OK, no High / Blocked risks open.
2. **Staging assembly:** assemble `/tmp/leonardo-pages-artifact/` from `site/` + `second-exhibition/site/` + `second-exhibition/assets/images/` with the path rewrite applied to `index.html` only.
3. **Staging QA:** serve the staging directory with `python3 -m http.server`, run the existing browser QA runner against `/second-exhibition/`, confirm 5/5 viewports and 0 external requests.
4. **Staging inventory:** record file inventory, sizes, and SHA-256 hashes. Save outside the repo.
5. **Workflow change:** introduce a small change to `.github/workflows/pages.yml` that uploads `/tmp/leonardo-pages-artifact/` instead of `site/`. The change must be one commit and one push.
6. **Live verification:** confirm `https://conanxin.github.io/leonardo-chinese-exhibition/` is still 92,976 B with the v2.9 marker present, then confirm `/second-exhibition/` is now 200.
7. **Post-deployment source/rights recheck:** re-open each source URL and confirm the per-page evidence still matches the published artifact.

## Constraints

- The staging directory is rebuilt from scratch every time. No state from previous staging runs.
- The path rewrite is deterministic and reproducible.
- No file outside the staging tree is ever published.
- The Pages workflow stays a single workflow (no second workflow).
- No CNAME, no custom domain, no DNS change.