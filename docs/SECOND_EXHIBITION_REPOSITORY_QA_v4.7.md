# v4.7 Second Exhibition Repository QA

## Baseline

- HEAD: `1d2da052baed13558fd978d351903d74dad52f2d`
- Source tag: `v3.4-real-second-exhibition-hardening`
- Live byte size: 92,976 B
- Build status: `repository-only-not-deployed`
- Site path: `second-exhibition/site/`
- Assets: 6

## QA scope

- structure
- JSON consistency
- asset integrity
- semantic HTML
- local links
- accessibility
- interaction
- responsive layouts
- deployment safety
- stage-gate applicability

## Gate applicability

- `scripts/second_exhibition_asset_gate.py` belongs to the **v4.5 asset-import stage**. It checks that six assets were imported, that their checksums match, that paths are confined to `second-exhibition/assets/images/`, and that `second-exhibition/site/` does not yet exist. That last invariant is **stage-specific**: after `v4.6` legitimately created the repository-only site, the gate's "site must not exist" check is superseded.
- `scripts/second_exhibition_build_gate.py` belongs to the **v4.6 repository-build stage**. It validates that the site, data, docs, and assets form a consistent repository-only structure and that no live deployment path exists.
- `scripts/second_exhibition_repository_qa.py` belongs to the **v4.7 repository QA stage**. It re-validates the v4.5 asset records and the v4.6 build, adds semantic/accessibility/interaction checks, and confirms that the top-level live exhibition remains untouched.
- Asset integrity remains required and is directly rechecked by both the build gate and the QA gate.

## PASS criteria

- repository QA script PASS
- build gate PASS
- checksums 6/6
- local Playwright PASS
- no console errors
- no failed requests
- no horizontal overflow
- no external image requests
- no live deployment exposure

## Result

See `reports/leonardo_chinese_exhibition_v4_7_second_exhibition_repository_qa_report.md` for the current run.

<!-- v4.7-partial-finding -->
## QA outcome

- **STATUS:** PARTIAL
- Repository QA script: **156 PASS / 1 FAIL / 2 WARNINGS**
- Exit code: **1**
- Blocking defect: the lightbox dialog declares `aria-labelledby="lightbox-title"`, but no element with `id="lightbox-title"` exists.
- Impact: the dialog does not receive a valid accessible name from its declared ARIA reference.
- Content, data, assets, checksums, deployment safety, and existing live site remain unchanged.
- This QA round does not modify `second-exhibition/site/`.
- Required recovery round: `v4.7b-repository-qa-recovery`.
