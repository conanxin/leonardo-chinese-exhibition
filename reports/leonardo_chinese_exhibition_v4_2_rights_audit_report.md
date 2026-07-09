# v4.2 Rights Audit — Report

> Round: **v4.2 — Rights Audit**
> Date: 2026-07-09 (UTC)
> Working title: 《植物图谱与视觉分类：从自然史图像到知识秩序》
> **STATUS: PASS**

---

## 1. Round summary

| Field | Value |
|---|---|
| **STATUS** | **PASS** |
| Round | v4.2 — Rights Audit |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Source tag object | `2d186a892af0e1ab41c1d9b8a055842e01339cb6` |
| Baseline HEAD | `8d6a13fcbe5ecd48459cdf33b5649d2a5885b013` |
| `origin/main` at round start | `8d6a13fcbe5ecd48459cdf33b5649d2a5885b013` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size (before) | 92,976 B |
| Live byte size (after) | 92,976 B |
| Live byte size delta | **0 B** |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| v2.9 marker in live | `1` (unchanged) |
| `image-placeholder-pro` in live | `0` (unchanged) |
| `植物图谱与视觉分类` in live | `0` (unchanged — audit round, not deployed) |
| `script.js` HTTP status | `200` |
| Working tree | clean except for untracked `.firecrawl/` (left alone this round, per scope) |
| New tag | **none** (v4.2 is an audit round) |
| New GitHub Release | **none** |
| Approved asset count | **0** (status `approved` is not used in v4.2) |
| Downloaded image count | **0** |
| New image files in repo | **0** (`find` confirms 17 pre-existing files, unchanged) |

---

## 2. Reality gate result (round start)

| Check | Expected | Actual | Result |
|---|---|---|---|
| HEAD = `origin/main` | `8d6a13f` | `8d6a13f` | PASS |
| v3.4 tag object | `2d186a89` | `2d186a89` | PASS |
| v3.4 tag target | `81f5e92` | `81f5e92` | PASS |
| Quality gate | 37/37 PASS | 37/37 PASS | PASS |
| 5 v4.1 docs exist | all 5 | all 5 | PASS |
| Live byte size | 92,976 B | 92,976 B | PASS |
| v2.9 marker in live | 1 | 1 | PASS |
| `image-placeholder-pro` in live | 0 | 0 | PASS |
| `植物图谱与视觉分类` in live | 0 | 0 | PASS |
| `script.js` HTTP status | 200 | 200 | PASS |
| Working tree | clean (untracked `.firecrawl/` ok) | matches | PASS |

Reality gate **PASS**. Round proceeded.

---

## 3. Audit method

The v4.2 audit follows the rules in `docs/RIGHTS_AUDIT_v4.2.md` (the audit method section):

1. **Official source pages only.** Every check ran against an official URL of the institution (e.g., `biodiversitylibrary.org`, `wellcomecollection.org`, `si.edu`, `metmuseum.org`, `rijksmuseum.nl`, `loc.gov`).
2. **Per-candidate verification.** Each of the 12 v4.1 shortlist rows was re-checked, not assumed from v4.1.
3. **No image download.** The audit verified the *availability* of the image URL (or IIIF endpoint) without retrieving the image body.
4. **No asset import.** No image was added to the repository.
5. **No legal conclusion.** The audit recorded what the institution's page says, not whether the project is "cleared" to use the work.
6. **All decisions are project release decisions.**

The 5 acceptance checks (defined in `docs/SOURCE_ACCEPTANCE_CHECKS_v4.2.md`) are: source URL exists; rights statement exists; identifier exists; metadata sufficient; credit line basis.

---

## 4. Per-candidate audit results

| ID | Institution | Risk level | v4.2 status | Notes |
|---|---|---|---|---|
| C-01 | BHL | Low | **verified** | Mechanism in place: per-item `<Copyright Status>` field documented. |
| C-03 | BHL | Low (PD subset) / High (NC subset) | **verified** for the PD subset / **blocked at per-item level** for the CC BY-NC-SA subset | C-03 row as a whole is `verified` for the Public-domain subset; the CC BY-NC-SA subset is blocked at the per-item level. v4.3 must restrict to PD. |
| C-04 | Wellcome | Medium | **needs clarification** | Per-item `items.locations.license` field must be confirmed (site-wide CC BY 4.0 default is "except where otherwise noted"). |
| C-05 | Wellcome | Medium | **needs clarification** | IIIF endpoint alone does not carry the rights field; the rights field is on the Catalogue API work record. |
| C-06 | Smithsonian Open Access (NMNH) | Low | **verified** | CC0 program is rigorous and binary; EDAN API + per-item CC0 marking is the mechanism. |
| C-07 | Smithsonian Open Access (general) | Low (data) / Medium (image) | **needs clarification** | Data dump is CC0; image is CC0 only if the linked item is CC0. |
| C-08 | Met Open Access | Low (with double-confirmation) | **verified** (mechanism) | Collection API is the canonical access path; both `isPublicDomain: true` and public-page OA icon must be present. |
| C-09 | Rijksmuseum | Low (CC0) or Low–Medium (CC BY 4.0) | **verified** (mechanism) | Two-tier policy is well-documented; per-item `licence` field is verifiable. |
| C-10 | Rijksmuseum | Low (per item) | **verified** (mechanism) | IIIF Presentation API manifest's `license` field is verifiable; must be paired with Catalogue-side object record. |
| C-11 | LoC P&P | Medium | **needs clarification** | `tgm001244` is a subject heading, not a single collection; per-item rights wording is non-affirmative in the "no known" variant. |
| C-12 | LoC Digital Collections | Low–Medium | **needs clarification** | "Illustrated book" is a *type*, not a specific LoC collection; per-collection rights wording. |
| C-13 | LoC P&P | Low–Medium | **needs clarification** | Per-record LoC P&P rights wording; same mechanism as C-11. |

---

## 5. Counts

| Status | Count | IDs |
|---|---|---|
| `verified` | **6** | C-01, C-03, C-06, C-08, C-09, C-10 |
| `needs clarification` | **6** | C-04, C-05, C-07, C-11, C-12, C-13 |
| `blocked` (at row level) | **0** | — |
| `blocked` (at per-item level) | **1** | C-03 CC BY-NC-SA subset |
| `excluded` (at row level) | **0** in the 12-row shortlist | — |
| `approved` | **0** | Status `approved` is not used in v4.2. |

- **Candidates audited count:** 12.
- **Verified count:** 6.
- **Needs clarification count:** 6.
- **Blocked count (row level):** 0.
- **Excluded count (row level):** 0.
- **Approved asset count:** 0.
- **Downloaded image count:** 0.

The build planning threshold (verified ≥ 4) is met: 6 ≥ 4. v4.3 may proceed.

---

## 6. Verified shortlist

The 6 verified candidates are listed in `docs/VERIFIED_SOURCE_SHORTLIST_v4.2.md` with the candidate source URL, why it fits, the rights basis, the required credit line basis, the proposed section, and the remaining caution. Section coverage:

- Section 1 (观察): C-01, C-09.
- Section 2 (分类): C-06, C-09.
- Section 3 (复制): C-01, C-03, C-08.
- Section 4 (再组织): C-10.

Each section has at least one verified candidate.

---

## 7. Blocked / excluded / clarification

| Decision | Count | IDs |
|---|---|---|
| `blocked` (at the per-item level) | 1 | C-03 (CC BY-NC-SA subset) |
| `excluded` (in the 12-row shortlist) | 0 | — |
| `replace with project-generated diagram` | 2 | C-02 (BHL Flickr), Section-4 collection-record-screenshot row |
| `needs clarification` | 6 | C-04, C-05, C-07, C-11, C-12, C-13 |

The C-14 row (BHL CC BY-NC-SA at the title level) was already `excluded` in v4.1 and is not re-counted here. The two `replace with project-generated diagram` decisions are v4.1 carry-overs.

---

## 8. Rights risk summary

| Risk level | Count (v4.1 shortlist) | Notes |
|---|---|---|
| Low | 6 | C-01, C-03 (PD subset), C-06, C-08, C-09, C-10 — the v4.2 verified shortlist. |
| Low–Medium | 0 in the verified set; possible downshift for C-09 / C-10 if a specific item carries CC BY 4.0. | Recorded as a v4.3 follow-up. |
| Medium | 6 | C-04, C-05, C-07, C-11, C-12, C-13 — the v4.2 `needs clarification` rows. |
| High | 0 in the 12-row shortlist. | The CC BY-NC-SA subset of C-03 is **blocked at the per-item level**, not at the row level. |
| Blocked | 0 in the 12-row shortlist at the row level. | The CC BY-NC-SA subset of C-03 is the only blocked *per-item subset*. |
| Excluded | 0 in the 12-row shortlist. | C-14, C-02 (BHL Flickr), and the Section-4 screenshot row are carry-overs from v4.1. |

The release blocker rule (High / Blocked risk items cannot enter a stable release unless resolved or excluded) is restated in `docs/RIGHTS_RISK_REGISTER_v4.2.md` and applies to v4.3 build planning and v4.4 stable freeze.

---

## 9. v4.2 docs created (5)

| File | Bytes | Purpose |
|---|---|---|
| `docs/SOURCE_ACCEPTANCE_CHECKS_v4.2.md` | ~8.5 KB | 5 acceptance checks + status definitions + non-approval note. |
| `docs/RIGHTS_AUDIT_v4.2.md` | ~20.9 KB | 12-row per-candidate audit table with source URL rechecked, rights URL / statement, identifier, metadata, credit line basis, risk level, v4.2 status, notes. |
| `docs/VERIFIED_SOURCE_SHORTLIST_v4.2.md` | ~8.3 KB | 6 verified candidates only. |
| `docs/BLOCKED_OR_EXCLUDED_SOURCES_v4.2.md` | ~7.7 KB | Blocked / excluded / replace-with-project-generated / needs-clarification rows. |
| `docs/RIGHTS_RISK_REGISTER_v4.2.md` | ~9.7 KB | Per-row risk levels + open risks (R-01 to R-14) + release blocker rule. |
| `docs/V4_ROADMAP.md` | updated | v4.2 section rewritten to reflect actual deliverables + status definitions. |
| `README.md` | updated | `v4.2 Rights Audit` block added after the v4.1 block. |

Grep verification of acceptance phrases:

| Check | Count |
|---|---|
| `v4.2 不下载图片` in `SOURCE_ACCEPTANCE_CHECKS_v4.2.md` | 2 |
| `High / Blocked` in `RIGHTS_RISK_REGISTER_v4.2.md` | 4 |
| `approved` as a status value in `RIGHTS_AUDIT_v4.2.md` | **0** (only in "not used" disclaimers) |

---

## 10. README / roadmap update

- `README.md` now carries a `## v4.2 Rights Audit` block immediately after the v4.1 block, recording: status (rights audit only), no live change, no images downloaded, no assets imported, the audit counts (6 verified / 6 needs clarification / 0 blocked at row level / 1 blocked at per-item level / 0 excluded / 0 approved), the build planning threshold check (6 ≥ 4 → met → v4.3 may proceed), the 5 v4.2 docs, the quality gate result, and the next task (v4.3 Second Exhibition Build Planning).
- `docs/V4_ROADMAP.md` v4.2 section rewritten to reflect actual deliverables + the "no approved" rule + the verified-count threshold for the next round. The old v4.2 placeholder text is replaced.

No prior v2.x / v3.x / v4.0 / v4.1 section was modified.

---

## 11. Live site no-change confirmation

| Check | Before | After | Delta |
|---|---|---|---|
| Live byte size | 92,976 B | 92,976 B | 0 |
| v2.9 marker in live | 1 | 1 | 0 |
| `image-placeholder-pro` in live | 0 | 0 | 0 |
| `植物图谱与视觉分类` in live | 0 | 0 | 0 (audit round, not deployed) |
| `script.js` HTTP status | 200 | 200 | — |
| `git diff -- site/index.html site/style.css site/script.js` | — | empty | — |

Live site **unchanged**.

---

## 12. Template / pilot no-change confirmation

| Check | Result |
|---|---|
| `git diff -- _template/site/` | empty |
| `git diff -- _template/data/` | empty |
| `git diff -- _pilots/second-exhibition-pilot/` | empty |
| `scripts/template_quality_gate.py` | PASS 37/37 |

Template and pilot **unchanged**.

---

## 13. Old tags / old releases untouched

| Check | Result |
|---|---|
| `git tag --list` | v2.0 / v2.6 / v2.7 / v2.8 / v2.9 / v3.0 / v3.1 / v3.2 / v3.3 / v3.4 — **all 10 unchanged** |
| `git ls-remote --tags origin` | matches local list — no remote-side movement |
| v3.4 tag object | `2d186a89` (unchanged) |
| v3.4 tag target | `81f5e92` (unchanged) |
| Old GitHub Releases | **none modified** (no `gh release edit` issued) |
| `posts/` | not touched (not in this round's allowed-edit list) |
| `case-study/` | not touched (not in this round's allowed-edit list) |
| `release-assets/` | not touched (not in this round's allowed-edit list) |

No tag, no Release, no movement, no rewrite. Old history **untouched**.

---

## 14. Files changed in this round

Allowed-edit list (per round scope) — all changed files fall inside this list:

| File | Action |
|---|---|
| `docs/SOURCE_ACCEPTANCE_CHECKS_v4.2.md` | created |
| `docs/RIGHTS_AUDIT_v4.2.md` | created |
| `docs/VERIFIED_SOURCE_SHORTLIST_v4.2.md` | created |
| `docs/BLOCKED_OR_EXCLUDED_SOURCES_v4.2.md` | created |
| `docs/RIGHTS_RISK_REGISTER_v4.2.md` | created |
| `docs/V4_ROADMAP.md` | modified (v4.2 section rewritten; old v4.2 placeholder removed) |
| `README.md` | modified (v4.2 block added) |
| `reports/leonardo_chinese_exhibition_v4_2_rights_audit_report.md` | created (this file) |

Untracked `.firecrawl/` directory was observed at round start and **left alone**, per round scope.

---

## 15. Next recommended task

**v4.3 — Second Exhibition Build Planning.**

The verified count is **6**, which is ≥ 4. v4.3 may proceed.

Scope of v4.3:

- For each of the 6 verified candidates, pick one specific item and record the per-item evidence (source URL, rights statement, identifier, metadata, credit line) in a v4.3 entry of the audit table (or a successor document).
- The 6 `needs clarification` rows may be promoted to `verified` in v4.3 if the per-item evidence is captured. They do not enter v4.3 build planning until then.
- Image download and local asset addition are **separate** from v4.3 build planning. They belong to a future round that runs the v4.0 source-acceptance rule a second time on each specific item, with the per-item evidence attached.
- Even with `verified` status, v4.3 does **not** authorize redistribution. The credit line is mandatory; the rights statement must be reproduced verbatim where required by the licence.

v4.3 **must not**:

- Mark any candidate `approved` (the status `approved` is not used in v4.0–v4.4).
- Include any High / Blocked asset, even uncredited.
- Modify `site/`, `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`, `posts/`, `case-study/`, `release-assets/`.
- Create a tag or GitHub Release.
- Move or rewrite any pre-existing tag or GitHub Release.

---

## 16. Final status

**STATUS: PASS**

All reality-gate, per-candidate-audit, source-acceptance, verified-shortlist, blocked-or-excluded, rights-risk-register, README / roadmap, quality-gate, no-change, no-new-image, and old-history conditions met. v4.2 closes with five committed audit docs, two updated existing docs, an unchanged live site (92,976 B / v2.9 marker = 1 / placeholder = 0), an unchanged template and pilot, no new image files in the repository, 6 verified candidates, 6 needs-clarification candidates, 0 blocked / excluded at the row level, 0 approved, and ten untouched old tags plus their corresponding old GitHub Releases. No new tag, no new GitHub Release, no asset was approved. The next round is **v4.3 — Second Exhibition Build Planning** (verified count 6 ≥ 4 → v4.3 may proceed).