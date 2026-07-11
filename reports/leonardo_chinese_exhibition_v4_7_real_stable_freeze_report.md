# v4.7 Real Stable Freeze Report

## STATUS: PASS

**Date:** 2026-07-12
**Baseline HEAD / origin/main:** `ded9bd804cad40967608d590eed9227cf99c5f5e`
**Recovery commit:** `ded9bd804cad40967608d590eed9227cf99c5f5e`
**Source tag:** `v3.4-real-second-exhibition-hardening` → `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765`
**Live URL:** https://conanxin.github.io/leonardo-chinese-exhibition/
**Round:** v4.7-real-stable-freeze — Second Exhibition Repository QA stable freeze
**Tag:** `v4.7-real-second-exhibition-repository-qa`
**Next:** `v4.8-second-exhibition-repository-hardening` or `v5.0-deployment-planning`

---

## Freeze evidence three-piece

- Freeze commit: 
- Tag target: 
- Verified live byte: **92,976 B**.
- Verified tag:  (object )
- GitHub Release: https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v4.7-real-second-exhibition-repository-qa (createdAt )

---

## QA history

### v4.7 original repository QA

- Result: **156 PASS / 1 FAIL / 2 WARNINGS** (exit code 1)
- **Blocker:** `second-exhibition/site/index.html` lightbox used `aria-labelledby="lightbox-title"`, but no element with `id="lightbox-title"` existed.
- Independent ARIA check: 9 references, 1 missing target (`#lightbox-title`).

### v4.7b repository QA recovery

- Fixed by adding a real heading element: `<h2 id="lightbox-title" class="visually-hidden">图片查看器</h2>` inside the lightbox `<figure>`.
- Added a standard `.visually-hidden` CSS utility in `second-exhibition/site/style.css`.
- Kept existing `aria-labelledby="lightbox-title"`; did not modify JavaScript behavior.
- ARIA references: **9/9 valid**; missing targets: **0**.
- Repository QA recovered to: **157 PASS / 0 FAIL / 2 WARNINGS** (exit code 0).

---

## Verification results

| Gate | Command | Result |
|------|---------|--------|
| Template quality gate | `python3 scripts/template_quality_gate.py` | **PASS, 37/37** |
| Second exhibition build gate | `python3 scripts/second_exhibition_build_gate.py` | **PASS** |
| Repository QA | `python3 scripts/second_exhibition_repository_qa.py` | **157 PASS / 0 FAIL / 2 WARNINGS** (exit 0) |
| Asset checksums | `sha256sum -c second-exhibition/assets/asset-checksums.sha256` | **6/6 OK** |
| JavaScript syntax | `node --check second-exhibition/site/script.js` | **OK** |
| Data JSON | `python3 -m json.tool` | all valid |

---

## ARIA recovery verification

- `#lightbox-title` count: **1**
- `#lightbox-title` text: **图片查看器**
- `aria-labelledby="lightbox-title"` present on lightbox dialog: **yes**
- ARIA references checked: **9**
- Missing targets: **0**
- `.visually-hidden` does not use `display: none`: **yes**
- `.visually-hidden` does not use `visibility: hidden`: **yes**

---

## Remaining warnings (non-blocking)

- **C-03 CC BY-NC-SA subset exact wording not found** — informational.
- **C-06 Hero check inconclusive** — informational.

---

## Browser QA evidence and limitation

- **v4.6** full Playwright desktop/mobile QA: **PASS**.
- **v4.7b** did **not** rerun the full Playwright desktop/mobile matrix because no Chromium/Playwright binary was available in the WSL execution environment.
- **v4.7b** local HTTP validation, ARIA reference audit, six-image request checks, `node --check` syntax check, and gate re-runs all passed.
- This limitation is documented and is not misrepresented as a completed browser run.

---

## Deployment safety verification

| Check | Result |
|-------|--------|
| Live byte size | **92,976 B** |
| v2.9 marker live count | **1** |
| Second exhibition title live count | **0** |
| Top-level `script.js` HTTP status | **200** |
| `second-exhibition/` Pages URL | **404** |
| `second-exhibition/site/` Pages URL | **404** |
| `second-exhibition/site/index.html` Pages URL | **404** |
| `second-exhibition/assets/asset-import-manifest.json` Pages URL | **404** |

Status: **repository-only-not-deployed**. No deployment performed.

---

## Protected paths unchanged

The following paths were not modified during v4.7-real-stable-freeze:

- `second-exhibition/site/` (freeze commit only adds docs/reports; no page changes)
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
- `release-assets/` (existing files)
- `.github/workflows/`
- `scripts/template_quality_gate.py`
- `scripts/second_exhibition_asset_gate.py`
- `scripts/second_exhibition_build_gate.py`
- `scripts/second_exhibition_repository_qa.py`

---

## Tag / Release status

- Tag created: `v4.7-real-second-exhibition-repository-qa` (annotated)
- Tag target: 
- GitHub Release created: to be filled after Release creation.
- Old tags (`v2.0` through `v3.4`) and Releases: untouched.

---

## Notes

This freeze marks the verified state of the v4.7 Second Exhibition Repository QA. The second exhibition remains repository-only and is not deployed to GitHub Pages. Live publication requires a separate, future round that explicitly authorizes deployment and re-runs source/rights verification against the to-be-deployed tree.

---

## Evidence backfill (optional)

After tag / Release creation, this section may be filled with:

- Tag object SHA.
- Tag target commit.
- Release URL: https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v4.7-real-second-exhibition-repository-qa.
- Release `createdAt`.
- GitHub Actions run ID: .
- Any additional deployment-path verification.

The evidence backfill commit, if any, will be located **after** the tag target commit and will not move the tag.
