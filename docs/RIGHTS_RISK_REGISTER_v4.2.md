# v4.2 Rights Risk Register

> Scope: update the v4.0 / v4.1 rights-risk register with the v4.2 audit's per-row risk levels and the open risks that v4.3 must close before any real image download or asset import. The release blocker rule is restated at the end.
>
> v4.2 does not "approve" any asset. The status `approved` is not used. The risk register tracks *risk levels* and *required actions*, not approvals.

---

## Risk summary

The v4.2 audit lands the 12 shortlist rows at the following risk levels. Rows whose status is `verified` carry a known low risk; rows whose status is `needs clarification` carry a known medium risk that v4.3 must reduce to Low or Low–Medium with a per-item check.

| Risk level | Count (v4.1 shortlist) | Notes |
|---|---|---|
| **Low** | 6 | C-01, C-03 (PD subset), C-06, C-08, C-09, C-10 — the v4.2 verified shortlist. |
| **Low–Medium** | 0 in the verified set; carried over as a *possible* downshift for C-09 / C-10 if the per-item licence is CC BY 4.0 instead of CC0. | C-09 / C-10 may downshift from Low to Low–Medium in v4.3 if a specific item carries the Rijksmuseum's CC BY 4.0 tier instead of CC0. |
| **Medium** | 6 | C-04, C-05, C-07, C-11, C-12, C-13 — the v4.2 `needs clarification` rows. |
| **High** | 0 in the 12-row shortlist. | The CC BY-NC-SA subset of C-03 is **blocked at the per-item level**, not at the row level. It is recorded as a single-row observation in `BLOCKED_OR_EXCLUDED_SOURCES_v4.2.md` (C-03 Notes column). |
| **Blocked** | 0 in the 12-row shortlist at the row level. The CC BY-NC-SA subset of C-03 is the only blocked *per-item subset*. | The C-14 row (BHL in-copyright subset) was already `excluded` in v4.1. |
| **Excluded** | 0 in the 12-row shortlist. | C-14 and C-02 (BHL Flickr) and the Section-4 screenshot row are carried over from v4.1 as `excluded` and `replace with project-generated diagram` respectively. |

The v4.2 risk distribution is therefore:

- **Verified (Low):** 6 rows.
- **Needs clarification (Medium):** 6 rows.
- **Blocked / High / Excluded at the row level:** 0 rows in the 12-row shortlist.
- **Approved:** 0 rows (status `approved` is not used in v4.2).

---

## Open risks

The following risks are *open* at the end of v4.2. Each risk has a v4.2 risk level, an evidence note, a v4.2 decision, and a required action for v4.3.

| Risk ID | Candidate ID | Risk | Level | Evidence | Decision | Required action | Status |
|---|---|---|---|---|---|---|---|
| R-01 | C-01 | Per-item rights wording is on the BHL volume page, not pre-cleared by the institution-level summary | Low | BHL `<Copyright Status>` field is documented as `Public domain` / `No known copyright restrictions` / `In copyright` (verbatim from the BHL Permissions page) | Verified (mechanism) | v4.3 picks a specific volume, opens the title page, captures `<Copyright Status>` and `<Holding Institution>` verbatim | open |
| R-02 | C-03 (CC BY-NC-SA subset) | CC BY-NC-SA 4.0 carries an NC clause incompatible with this project's openly-distributed output | High | BHL Permissions page: "Almost always a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license" | Blocked at the per-item level | v4.3 restricts the C-03 row to the Public-domain subset; the CC BY-NC-SA subset is **not** in the verified list | open |
| R-03 | C-04 | Per-item `items.locations.license` field must be confirmed (site-wide CC BY 4.0 default is "except where otherwise noted") | Medium | Wellcome Catalogue API v2 docs expose the `items.locations.license` enum | needs clarification | v4.3 picks a specific Wellcome item, captures the per-item licence field verbatim | open |
| R-04 | C-05 | IIIF endpoint alone does not carry the rights field; the rights field is on the Catalogue API record | Medium | Wellcome IIIF Image API 3.0 docs do not list a rights field; Catalogue API v2 docs do | needs clarification | v4.3 pairs each IIIF image with its Catalogue API work record; the rights field is captured from the Catalogue record | open |
| R-05 | C-07 | The data dump is CC0, but the *image* is CC0 only if the linked item is CC0 | Medium | Smithsonian FAQ: "CC0 only applies to copyright so you may still need someone else's permission" | needs clarification | v4.3 promotes C-07 rows via a C-06-style per-item check (EDAN API + per-item CC0 confirmation) | open |
| R-06 | C-08 | The Met's `isPublicDomain: true` and the public object page's Open Access icon must both be present | Low (with double-confirmation) | Met Collection API docs expose `isPublicDomain`; Met Image Resources policy page says the Open Access icon marks CC0 images | Verified (mechanism) | v4.3 picks a specific Met object; the double-confirmation is mechanical | open |
| R-07 | C-09 | Per-item `licence` field on the Rijksmuseum object record is `CC0 1.0` or `CC BY 4.0` (two-tier policy) | Low (CC0) or Low–Medium (CC BY 4.0) | Rijksmuseum Information and Data Policy page; data services docs | Verified (mechanism) | v4.3 picks a specific object; the per-item licence field is recorded | open |
| R-08 | C-10 | IIIF Presentation API manifest's `license` field must be confirmed | Low (per item) | Rijksmuseum IIIF tutorial: the manifest carries the `license` field | Verified (mechanism) | v4.3 pairs each IIIF manifest with its underlying object record (same as C-09) | open |
| R-09 | C-11 | The LoC P&P `tgm001244` page is a subject heading, not a single collection; per-item rights wording is non-affirmative in the "no known" variant | Medium | LoC P&P page at `tgm001244` is a thesaurus term; the rights pattern across LoC collections is per-collection, not institution-wide | needs clarification | v4.3 picks one specific P&P item, fetches its `loc.gov/pictures/item/<id>/` record, captures the rights statement verbatim | open |
| R-10 | C-12 | "Illustrated book" is a *type*, not a specific LoC collection; per-collection rights wording | Medium | LoC Digital Collections are each their own rights page; `loc.gov/collections/` is the entry point | needs clarification | v4.3 names one specific LoC Digital Collection (illustrated-book type), fetches its Rights & Access page | open |
| R-11 | C-13 | Per-record LoC P&P rights wording; same mechanism as C-11 | Medium | Same as C-11 | needs clarification | v4.3 picks one specific P&P record and fetches its rights statement | open |
| R-12 | C-02 (BHL Flickr, v4.1 carry-over) | Flickr is a third-party platform; the rights belong to the underlying BHL item, not Flickr | Medium (platform screenshot ambiguity — risk category 3 in the v4.0 register) | v4.0 register §3; v4.1 rights-screening decision `replace with project-generated diagram` | replace with project-generated diagram | None for C-02. If a future round wants to re-include, capture the underlying BHL item's rights page as a new row. | closed at v4.1 (replaced) |
| R-13 | C-14 (BHL CC BY-NC-SA, v4.1 carry-over) | NC clause is incompatible with the project's openly-distributed output | High | BHL Permissions page; v4.1 rights-screening decision `exclude` | excluded | None in v4.0–v4.4 | closed at v4.1 (excluded) |
| R-14 | (Section 4 collection-record screenshot) | Platform screenshot ambiguity (risk category 3 in the v4.0 register) | High | v4.0 register §3; v4.1 rights-screening decision `replace with project-generated diagram` | replace with project-generated diagram | None for this row | closed at v4.1 (replaced) |

Open risks at the end of v4.2: **R-01 through R-11** (11 open risks). Closed risks (carried over from v4.1): **R-12, R-13, R-14** (3 closed).

---

## Release blocker rule

> High / Blocked risk items cannot enter a stable release unless resolved or excluded.

This rule is **hard**. It applies to:

- v4.3 build planning (no High / Blocked asset enters the working tree).
- v4.3 second exhibition build (no High / Blocked asset is downloaded or imported).
- v4.4 stable freeze (the manifest and source-audit table must show zero High / Blocked rows in the *accepted* set; High / Blocked rows may exist in the register, but only with status `blocked` or `excluded`, never `verified`).

The rule has exactly three escape paths:

1. **Resolve.** New evidence lowers the asset to Low or Low–Medium *and* the asset's metadata row carries the new evidence (rights statement copy, credit line, source note).
2. **Exclude.** The asset is moved to `audit status = excluded` with a one-line reason; it does not enter the build and does not appear in the manifest.
3. **Defer.** The asset is moved to `audit status = blocked` and tagged for a future round (v4.5 or later); it does not enter the v4.4 build.

No fourth path exists. Specifically: **a High or Blocked asset cannot be "soft-included" by being uncredited or unfootnoted**. If the audit cannot reach a clean Low or Low–Medium, the asset does not enter the release.

---

## Round-end note

At the end of v4.2:

- The v4.1 shortlist (12 rows) has been re-checked against the 5 source-acceptance checks.
- 6 rows are `verified`; 6 rows are `needs clarification`.
- 0 rows are `blocked` at the row level (1 row — C-03 — is blocked at the per-item level for its CC BY-NC-SA subset, but the row itself is `verified` for the Public-domain subset).
- 0 rows are `excluded` in the 12-row shortlist (C-14, C-02, and the Section-4 screenshot row are carry-overs from v4.1).
- 0 rows use the status `approved`.
- The release blocker rule is restated above. v4.3 build planning may read from the verified shortlist only.

The next round is **v4.3 Second Exhibition Build Planning** (only if the verified count is ≥ 4) — the verified count is 6, so v4.3 may proceed — or **v4.1b Source Candidate Research Extension** (if the verified count were < 4).