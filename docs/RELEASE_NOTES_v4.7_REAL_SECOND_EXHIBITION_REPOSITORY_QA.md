# v4.7 Real Second Exhibition Repository QA Release Notes

## Tag

- `v4.7-real-second-exhibition-repository-qa`

## URLs

- Live URL (existing Leonardo exhibition): https://conanxin.github.io/leonardo-chinese-exhibition/
- GitHub Release: to be inserted after Release creation

## Verified baseline

- Source tag: `v3.4-real-second-exhibition-hardening` → `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765`
- Repository build commit: `1d2da052baed13558fd978d351903d74dad52f2d`
- v4.7 PARTIAL commit: `c1157101d2b2d6581e26f46ec29adee4a10f33c6`
- v4.7b recovery commit: `ded9bd804cad40967608d590eed9227cf99c5f5e`
- Freeze commit: to be inserted after freeze commit

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

## Verification results

| Gate | Result |
|------|--------|
| Template quality gate (`scripts/template_quality_gate.py`) | **PASS, 37/37** |
| Second exhibition build gate (`scripts/second_exhibition_build_gate.py`) | **PASS** |
| Repository QA (`scripts/second_exhibition_repository_qa.py`) | **157 PASS / 0 FAIL / 2 WARNINGS** |
| Asset checksums (`sha256sum -c second-exhibition/assets/asset-checksums.sha256`) | **6/6 OK** |
| JavaScript syntax (`node --check second-exhibition/site/script.js`) | **OK** |
| Data JSON (`python3 -m json.tool`) | **all valid** |

## Remaining warnings (non-blocking)

- **C-03 CC BY-NC-SA subset exact wording not found** — informational. The page contains "CC BY-NC-SA" and "blocked" separately; the asset manifest explicitly records the blocked subset. No blocked asset was imported.
- **C-06 Hero check inconclusive** — informational. C-06 is a low-resolution 90×90 thumbnail constrained to `max-width: 180px`, so it cannot be used as a hero image. The heuristic could not positively identify a hero element, but the candidate-specific rule is satisfied.

## Browser QA evidence and limitation

- **v4.6** full Playwright desktop/mobile QA: **PASS**.
- **v4.7b** did **not** rerun the full Playwright desktop/mobile matrix because no Chromium/Playwright binary was available in the WSL execution environment.
- **v4.7b** local HTTP validation, ARIA reference audit, six-image request checks, `node --check` syntax check, and gate re-runs all passed.
- This limitation is documented and is not misrepresented as a completed browser run.

## Live site / deployment status

- Live byte size: **92,976 B** (unchanged).
- v2.9 marker live count: **1** (unchanged).
- Second exhibition title live count: **0** (unchanged).
- Top-level `script.js`: HTTP 200.
- All tested `second-exhibition/` Pages URLs return **HTTP 404**.
- Status: **repository-only-not-deployed**.

## No-touch confirmation

The following paths were not modified during v4.7b or v4.7-real-stable-freeze:

- `second-exhibition/site/script.js`
- `second-exhibition/data/` and all JSON files
- `second-exhibition/assets/` and all imported images
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
- Existing tags (`v2.0` through `v3.4`)
- Existing GitHub Releases

## What is not in this release

- The second exhibition is **not deployed** to GitHub Pages.
- No new image asset is added or replaced.
- No source / rights evidence is modified.
- No workflow change is introduced.
- No old tag or Release is moved or overwritten.

## Next

- **v4.8-second-exhibition-repository-hardening** or **v5.0-deployment-planning**.
