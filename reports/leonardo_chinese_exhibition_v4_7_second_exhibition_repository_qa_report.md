# v4.7 Second Exhibition Repository QA Report

## STATUS: PARTIAL

**Date:** 2026-07-12
**Head commit before v4.7:** `1d2da052baed13558fd978d351903d74dad52f2d`
**Source tag:** `v3.4-real-second-exhibition-hardening`
**Round:** v4.7 — Second Exhibition Repository QA (QA-only round)
**Next round:** v4.7b-repository-qa-recovery

---

## QA Script

- `scripts/second_exhibition_repository_qa.py` — new, created in this round.
- Run command: `python3 scripts/second_exhibition_repository_qa.py`
- Result: **156 PASS / 1 FAIL / 2 WARNINGS**
- Exit code: **1**

## Blocker (single FAIL)

**`second-exhibition/site/index.html` uses `aria-labelledby="lightbox-title"` but the page has no element with `id="lightbox-title"`.**

This is a real accessibility / ARIA-reference defect. The independent ARIA check in the QA script found:

- 9 ARIA references (`aria-labelledby` / `aria-describedby` / `aria-controls`) in the page.
- 1 missing target: `#lightbox-title` is referenced but not present.

The lightbox dialog is otherwise reachable, has a visible close control, and responds to the `Escape` key. The missing label target is the only ARIA defect that caused the repository QA gate to fail.

## Warnings (non-blocking)

1. **C-03 wording check** — the QA script did not find the exact combined phrase "CC BY-NC-SA subset" in the page copy. The page does contain "CC BY-NC-SA" and "blocked" separately, and the rights basis in `second-exhibition/data/assets.json` explicitly records the blocked subset. No blocked asset is imported. The warning is informational.
2. **C-06 Hero check inconclusive** — C-06 has `data-low-resolution="true"` and is constrained to `max-width: 180px` in CSS, so it cannot be used as a hero image. The heuristic check could not positively identify a hero image in the page structure, so it emitted a warning rather than a pass. The candidate-specific rule for C-06 is satisfied by the HTML/CSS structure.

## Other Quality Gates

| Gate | Command | Result |
|------|---------|--------|
| Template quality gate | `python3 scripts/template_quality_gate.py` | **PASS, 37/37** |
| Second exhibition build gate | `python3 scripts/second_exhibition_build_gate.py` | **PASS** |
| Asset checksums | `sha256sum -c second-exhibition/assets/asset-checksums.sha256` | **6/6 OK** |
| JSON validity | `python3 -m json.tool` on 4 data files | **all valid** |

## Live Site / Deployment Status

- Live byte size: **92,976 B** (unchanged).
- v2.9 marker: **1** (unchanged).
- `image-placeholder-pro`: **0** (unchanged).
- v4 / second exhibition title live count: **0** (unchanged).
- `second-exhibition/` is **not deployed** by the GitHub Pages workflow. All `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/...` URLs return HTTP 404.
- Status: **repository-only-not-deployed**.

## Protected Paths

The following paths were **not modified** in v4.7:

- `second-exhibition/site/` — no diff (only inspected).
- `second-exhibition/data/` — no diff (only inspected).
- `second-exhibition/assets/` — no diff (only inspected).
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` — no diff.
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md` — no diff.
- `site/` — no diff.
- `_template/site/` — no diff.
- `_template/data/` — no diff.
- `_pilots/second-exhibition-pilot/` — no diff.
- `posts/` — no diff.
- `case-study/` — no diff.
- `release-assets/` — no diff.
- `.github/workflows/` — no diff.
- `scripts/template_quality_gate.py` — no diff.
- `scripts/second_exhibition_asset_gate.py` — no diff.
- `scripts/second_exhibition_build_gate.py` — no diff.

## Tags / Releases

- No new tag created.
- No new GitHub Release created.
- Existing tags (`v2.0` through `v3.4`) and Releases untouched.

## Created / Modified Files in v4.7

Created:

- `scripts/second_exhibition_repository_qa.py`
- `docs/SECOND_EXHIBITION_REPOSITORY_QA_v4.7.md`
- `docs/ACCESSIBILITY_AND_INTERACTION_QA_v4.7.md`
- `docs/CONTENT_ASSET_CONSISTENCY_QA_v4.7.md`
- `docs/DEPLOYMENT_SAFETY_QA_v4.7.md`
- `reports/leonardo_chinese_exhibition_v4_7_second_exhibition_repository_qa_report.md`

Modified:

- `docs/V4_ROADMAP.md`
- `README.md`

## Evidence Three-Piece (reality gate)

- Commit SHA: to be filled after push.
- Verified live byte: **92,976 B**.
- Verified tag: no new tag created in v4.7.

## Next Task

**v4.7b-repository-qa-recovery** — fix the missing `#lightbox-title` ARIA target in `second-exhibition/site/index.html` and re-run the repository QA gate to full PASS. No other changes.
