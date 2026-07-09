# v4.2 Source Acceptance Checks

> Scope: define, for v4.2, the **per-candidate acceptance checks** that each v4.1 shortlist row must pass before its v4.2 status can be `verified`. This is the operationalization of the v4.0 source-scope rule (§ Source acceptance rule) and the v4.0 rights-risk register (release blocker rule).
>
> v4.2 不下载图片，不导入素材，不修改 live site。`verified` 只是「可进入 v4.3 build planning 的已核验候选」，不代表已经下载、不代表已进入正式展览、不代表法律意见。

---

## Baseline

| Field | Value |
|---|---|
| Current HEAD | `8d6a13fcbe5ecd48459cdf33b5649d2a5885b013` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| v3.4 tag object | `2d186a892af0e1ab41c1d9b8a055842e01339cb6` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size (baseline) | **92,976 B** |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| v4.1 shortlist entering v4.2 | 12 rows: C-01, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, C-13 |
| Recommended direction | 《植物图谱与视觉分类：从自然史图像到知识秩序》 |
| Sections (from v4.0 outline) | 1. 观察 / 2. 分类 / 3. 复制 / 4. 再组织 |

---

## Acceptance checks

Each v4.1 shortlist row is checked against the five checks below. A row is `verified` only if **all five** checks return `yes`. The checks are written in the same order the v4.0 source-scope rule uses.

| # | Check | What "yes" requires | What "no" means |
|---|---|---|---|
| 1 | **Official source URL exists** | The source URL is an official page of the institution (e.g., `biodiversitylibrary.org`, `wellcomecollection.org`, `si.edu`, `metmuseum.org`, `rijksmuseum.nl`, `loc.gov`), reached with HTTP 200 on the day of audit, and is a *page-level* URL (not a search engine result). | The source URL is third-party (e.g., a blog, a search snippet), 4xx / 5xx, or only exists in the institution's search-page listing without a per-item page. |
| 2 | **Rights statement exists, page-specific or institution-specific** | The source URL exposes a *named* rights statement (e.g., "Public domain", "CC0 1.0", "CC BY 4.0", "U.S. government work", "no known copyright restrictions") that is either (a) the institution's documented policy *as written on the institution's own page* or (b) page-specific (e.g., the rights field on a Smithsonian EDAN record, or a LoC collection's "Rights & Access" page). | No rights statement is locatable, or the only available wording is a third-party summary. |
| 3 | **Object / item / collection identifier exists** | The page exposes a persistent identifier (BHL title ID / page URL, Wellcome canonical work ID, Smithsonian accession / `edanmdm-…` ID, Met `objectID` / `accessionNumber`, Rijksmuseum `objectNumber` / `id.rijksmuseum.nl/{id}`, LoC `loc.gov/item/<id>/` or call number). | No persistent identifier is on the page; only a transient URL. |
| 4 | **Metadata sufficient for title / creator / date / institution / identifier** | The page or its API record exposes at least the five fields above, even if some are derived (e.g., date as a year span). | One or more of the five fields is missing or labelled "unknown" without a per-item check that would close the gap. |
| 5 | **Credit line basis** | A credit line can be composed *from the institution's own rights statement + the item's metadata* without guessing. The credit line is recorded in the audit row. | The credit line can only be written by guess, by inference from a similar item, or by a third-party summary. |

**Optional checks (recorded when present, not required for `verified`).**

| # | Check | What it adds |
|---|---|---|
| 6 | Image URL / IIIF / download endpoint exists | A per-item image URL is locatable (without download). For IIIF, an `info.json` is locatable. |
| 7 | Institution terms URL exists | The institution's own terms / policy page is documented in `docs/INSTITUTION_POLICY_NOTES_v4.1.md` and was re-checked in v4.2. |
| 8 | API documentation exists | An API doc page is documented (BHL OAI-PMH, Wellcome Catalogue API v2, Smithsonian EDAN Open Access API, Met Collection API, Rijksmuseum Data Services docs, LoC JSON API). |

---

## Status definitions

Each row in `docs/RIGHTS_AUDIT_v4.2.md` is assigned exactly one of the following v4.2 statuses. The status `approved` is **not used** in v4.2.

| Status | Definition | Enter v4.3 build planning? |
|---|---|---|
| `verified` | All 5 acceptance checks returned `yes` and the risk level is `Low` or `Low–Medium`. The credit line is recorded verbatim. | **Yes**, as a v4.3 input. |
| `needs clarification` | At least one acceptance check returned `partial` (e.g., rights wording is on the institution page but is *non-affirmative* and the per-item wording has not yet been captured). A specific follow-up action is recorded. | No, until the clarification is captured in a subsequent round. |
| `blocked` | A `High` or `Blocked` risk is identified in v4.2 (e.g., rights wording is incompatible with the distribution channel, or the identifier is not locatable, or the rights statement is on a third-party page only). | **No.** High / Blocked cannot enter a stable release unless resolved or excluded. |
| `excluded` | The row is removed from scope for a structural reason (e.g., the candidate type is incompatible with the section's argument, or the institution's API is unavailable, or a prior-round exclusion holds). | No. |

`approved` is intentionally absent. v4.2 does not "approve" anything. v4.3 build planning reads from the v4.2 verified shortlist; any real image download or local asset addition must happen in a separate asset-import round after v4.2 evidence is recorded.

---

## Non-approval note

> v4.2 不下载图片，不导入素材，不修改 live site；`verified` 只是进入 v4.3 build planning 的候选状态。

`verified` is a project-internal status, not a legal opinion. It signals that:

1. A source URL is reachable on the day of audit and is official.
2. A rights statement is locatable on the institution's own page.
3. An identifier is on the page or in its API record.
4. The metadata is sufficient for the 5 required fields.
5. A credit line can be written *without guessing*.

It does **not** signal that the project is cleared to download, redistribute, or display the image. v4.3 is a build *planning* round. Actual image download and local asset addition must happen in a separate round that records per-asset evidence, runs the v4.0 source-acceptance rule again, and produces a final `freeze report` (per the v3.4 freeze discipline).

---

## Round-1 risk distribution expectation

Based on the v4.1 institution summaries, the v4.2 audit is expected to land roughly in the following distribution (subject to per-item evidence):

- **Verified (Low or Low–Medium).** C-01, C-03 (BHL Public-domain), C-04 (Wellcome per-item CC BY 4.0), C-06 (Smithsonian NMNH CC0), C-08 (Met with double-confirmation), C-09 (Rijksmuseum CC0), C-10 (Rijksmuseum IIIF per item), C-12 (LoC collection with rights page consulted).
- **Needs clarification.** C-05 (Wellcome IIIF per item), C-07 (Smithsonian data dump — image rights depend on linked item), C-11 (LoC P&P — non-affirmative "no known" wording), C-13 (LoC P&P per record).
- **Blocked / Excluded.** None in the v4.1 shortlist. The C-14 NC clause row was already `excluded` in v4.1 and does not re-enter v4.2.
- **Replaced with project-generated diagram (carried over from v4.1).** C-02 (BHL Flickr) and the Section-4 collection-record-screenshot row.

The actual v4.2 table may differ from the expectation; the table in `RIGHTS_AUDIT_v4.2.md` is the single source of truth.

---

## Round boundary

v4.2 ends with:

- All 12 v4.1 shortlist rows assigned exactly one v4.2 status.
- 0 rows with `approved` status.
- 0 images downloaded.
- 0 image files added to the repository.
- 0 changes to `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`.
- 0 changes to `scripts/template_quality_gate.py`.
- No new tag, no new GitHub Release.
- Live byte size still **92,976 B**.

The next round is **v4.3 Second Exhibition Build Planning** (only if the verified count is ≥ 4), or **v4.1b Source Candidate Research Extension** (if the verified count is < 4 and more sources need to be added to the shortlist).