# v4.2 Blocked or Excluded Sources

> Purpose: record the v4.1 shortlist rows that did **not** land in v4.2 `verified`, plus the rows that were already excluded or replaced in v4.1. The purpose is to prevent accidental re-use in v4.3 and later.
>
> The Decision values in this document are limited to: `blocked`, `excluded`, `replace with project-generated diagram`, `needs clarification`. `approved` is not used.

---

## Purpose

The v4.2 audit produced **6 `verified`** rows and **6 `needs clarification`** rows in the 12-row v4.1 shortlist. The 6 `needs clarification` rows are listed here (not in the verified shortlist) so that v4.3 build planning can see them and decide whether to promote them in v4.3 by capturing the per-item evidence.

The rows already excluded or replaced in v4.1 (C-02 BHL Flickr, C-14 BHL CC BY-NC-SA, and the Section-4 collection-record-screenshot row) are also listed here as historical carry-over, with the v4.1 decision restated and the v4.2 follow-up noted.

This document does **not** authorize any image download or asset import. The `blocked`, `excluded`, and `replace with project-generated diagram` decisions are project release decisions, not legal opinions.

---

## Blocked / excluded / clarification table

| ID | Institution | Source / candidate | Decision | Reason | Future action |
|---|---|---|---|---|---|
| **C-02** | BHL | BHL Flickr photostream — botanical albums | **replace with project-generated diagram** | The Flickr URL is a *third-party platform*; the rights belong to the underlying BHL item, not Flickr. The section's argument survives a project-generated illustration-of-an-illustration diagram. (Carried over from v4.1.) | None for C-02. If a future round wants to re-include, the underlying BHL item's rights page must be captured as a new row (not as a re-promotion of C-02). |
| **C-04** | Wellcome | Wellcome Works search — Engravings / Lithographs | **needs clarification** | The site-wide CC BY 4.0 default is documented, but the audit must confirm the per-item `items.locations.license` field in the Catalogue API v2 record. The mechanism is in place; the per-item selection is deferred to v4.3. | v4.3 picks one specific Wellcome item, fetches its Catalogue API v2 record, captures `items.locations.license` verbatim, and captures the IIIF image URL. Promote to `verified` once the per-item evidence is recorded. |
| **C-05** | Wellcome | Wellcome IIIF Image API per-item | **needs clarification** | The IIIF endpoint alone does not carry the rights field; the rights field is on the Catalogue API work record, not on the IIIF endpoint. The audit confirms the *combination* (Catalogue API work + IIIF image) is the right access path. | v4.3 pairs each IIIF image with a Catalogue API work record; the rights field is captured from the Catalogue record. |
| **C-07** | Smithsonian Open Access (general) | Smithsonian OpenAccess GitHub data dump | **needs clarification** | The data dump is CC0, but the *image* is CC0 only if the linked item is CC0. The audit's mechanism (per-item check via EDAN API) is the same as C-06, so the *clarification* is structural: every C-07 row must be promoted via a per-item C-06-style check, not assumed from the dump. | v4.3 picks a specific Smithsonian record from the data dump and runs the C-06 audit (EDAN API + per-item CC0 confirmation). |
| **C-11** | LoC P&P | LoC P&P Online Catalog — Botanical illustrations subject heading | **needs clarification** | The `tgm001244` page is a subject heading (a thesaurus term), not a single collection; the audit cannot pre-clear a rights statement for an unspecified item. The general LoC pattern ("U.S. government work" or "no known copyright restrictions") is non-affirmative in the second variant. | v4.3 picks one specific P&P item, fetches its `loc.gov/pictures/item/<id>/` record, captures the rights statement verbatim, and confirms whether the wording is affirmative (U.S. government work) or non-affirmative (no known restrictions). |
| **C-12** | LoC Digital Collections | LoC Digital Collections — a specific illustrated-book collection | **needs clarification** | The "illustrated book" row in v4.1 was a *type*, not a specific collection. Each LoC Digital Collection has its own "About this Collection" → "Rights & Access" page. The audit verifies the *mechanism* is in place but the specific collection is unnamed. | v4.3 names one specific LoC Digital Collection (an illustrated-book collection), fetches its Rights & Access page, and confirms the rights wording. |
| **C-13** | LoC P&P | LoC P&P per-item record | **needs clarification** | Same as C-11. The per-record verification is the same mechanism; the per-record selection is deferred. | v4.3 picks one specific P&P record and fetches its rights statement. |
| **C-14** | BHL (in-copyright subset) | BHL in-copyright subset under CC BY-NC-SA 4.0 | **excluded** | NC clause is incompatible with this project's openly-distributed output; v4.3 cannot redistribute under NC. (Carried over from v4.1.) | None in v4.0–v4.4. May be revisited if the distribution channel changes (not in this round). |
| **C-03 (CC BY-NC-SA subset)** | BHL | BHL in-copyright subset at the title level (CC BY-NC-SA 4.0) | **blocked** at the per-item level | Same reason as C-14 (NC clause). The C-03 row as a whole is `verified` for the Public-domain subset; the in-copyright subset is blocked at the per-item level. v4.3 must restrict to the Public-domain subset. | v4.3 must restrict to the Public-domain subset. If a future round needs the in-copyright subset, it must re-evaluate the distribution channel. |
| **(Section 4 implicit row)** | (platform screenshot) | Collection record screenshot from an institution's catalog page | **replace with project-generated diagram** | Risk category 3 (platform screenshot ambiguity) per the v4.0 register; the section's argument survives a project-generated facsimile; the underlying fields are stable, the UI is not. (Carried over from v4.1.) | None for this row. If a future round wants to re-include, the platform's screenshot/reuse policy must be captured separately from the institution's content licence. |

---

## Counts

| Decision | Count | IDs |
|---|---|---|
| `blocked` (at the per-item level) | 1 | C-03 (CC BY-NC-SA subset) |
| `excluded` (in the 12-row shortlist) | 0 | — |
| `replace with project-generated diagram` | 2 | C-02 (BHL Flickr), Section-4 collection-record-screenshot row |
| `needs clarification` | 6 | C-04, C-05, C-07, C-11, C-12, C-13 |
| **`approved`** | **0** | not used |

The C-14 row was already `excluded` in v4.1 and is not re-counted here (it is outside the 12-row shortlist). The Section-4 screenshot row is also a v4.1 carry-over and is listed in the table for completeness.

---

## What this document does *not* say

- It does **not** say that any of the `needs clarification` rows are unusable. They are usable *if* v4.3 captures the per-item evidence. The clarification is a follow-up, not a closure.
- It does **not** say that the `replace with project-generated diagram` rows are rejected. They are *replaced* — the section's argument survives without the real image, and the project-generated diagram is the cleanest substitute.
- It does **not** authorize any image download, asset import, or live change. Every entry here is a project release decision, not a legal clearance.
- It does **not** say that the audit is final. v4.3 may revisit a row's decision (e.g., promote a `needs clarification` row to `verified` by capturing the per-item evidence, or re-include a `replace with project-generated diagram` row by capturing the underlying institution's terms page).