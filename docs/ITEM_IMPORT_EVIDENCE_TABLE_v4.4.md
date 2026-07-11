# v4.4 Item Import Evidence Table

> Scope: per-candidate item-level / source-level evidence for the 6 v4.3 `selected-for-build-planning` candidates. v4.4 only records URLs and identifiers — **no image is downloaded in v4.4**, and **no image file is created in v4.4**. v4.4 status values: `ready-for-asset-import` or `defer`. The status `approved` is **not used** in v4.4 or any future round.

> 收口时间：v4.4 asset import prep round 结束点。下一 round 是 **v4.4b-source-gap-fix**，不是 v4.5。

---

## Baseline

| Field | Value |
|---|---|
| Current HEAD | `166e73cff276a8111f098da7c6ff674b39ff778d` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size (baseline) | **92,976 B** (preserved) |
| Quality gate | `scripts/template_quality_gate.py` → **PASS, 37/37** |
| v4.3 selected-for-build-planning count | 6 (C-01, C-03, C-06, C-08, C-09, C-10) |
| Item-level sources checked | 2 (C-01, C-03 — both anchored on BHL item 318921) |
| Source-level sources checked | 4 (C-06, C-08, C-09, C-10 — per-item record deferred) |

---

## v4.4 status legend (only these two values appear in the table below)

| Status | Meaning |
|---|---|
| `ready-for-asset-import` | All evidence fields complete. Item URL reachable. Rights statement locatable. Image / IIIF URL locatable. Credit-line basis composable. PD-subset / double-confirmation / per-item `licence` checks passed. |
| `defer` | At least one evidence field is missing. Held back to a future round (typically v4.4b for the source-gap rows). |

The status `approved` is **not used** in v4.4 or any future round. `blocked-from-import` and `replace-with-project-generated-diagram` do not appear in this table (C-14 and the C-03 CC BY-NC-SA subset are policy-level entries — see `docs/SOURCE_AUDIT_MANIFEST_DRAFT_v4.4.md` "Policy-level entries").

---

## Item / source evidence table (6 rows)

| ID | Institution | Official item/source URL | Title | Creator / maker | Date | Identifier | Rights statement | Rights / terms URL | Image / IIIF URL known | Proposed local filename | v4.4 status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **C-01** | Biodiversity Heritage Library | https://www.biodiversitylibrary.org/item/318921 | Album of watercolors of Asian fruits and flowers | Unknown (watercolor artist) | between 1798 and 1850? | BHL item 318921 | Public domain, but must filter per-page / per-item copyright status | https://about.biodiversitylibrary.org/help/copyright-and-reuse/ | Yes — per-page image URL via BHL page-viewer (URL recorded, not downloaded) | `bhl-318921-plate.jpg` | `ready-for-asset-import` |
| **C-03** | Biodiversity Heritage Library | https://www.biodiversitylibrary.org/item/318921 | Album of watercolors of Asian fruits and flowers | Unknown (watercolor artist) | between 1798 and 1850? | BHL item 318921 | Public domain (PD subset only); CC BY-NC-SA 4.0 in-copyright subset is `blocked-from-import` at per-page / per-volume level | https://about.biodiversitylibrary.org/help/copyright-and-reuse/ | Yes — per-page image URL via BHL page-viewer (URL recorded, not downloaded) | `bhl-318921-page.jpg` | `ready-for-asset-import` (PD subset only) |
| **C-06** | Smithsonian National Museum of Natural History / NMNH Botany | https://collections.nmnh.si.edu/search/botany/ | **Collection / search-level source only; per-item record deferred.** The NMNH Botany search is the *entry URL*; a specific herbarium sheet has not been selected in v4.4. | — | — | — | Smithsonian Open Access / CC0 1.0 (to be confirmed per item) | https://www.si.edu/openaccess/faq | Per-item image URL is locatable on the per-item record (not yet selected in v4.4; v4.4 records the entry URL only) | `nmnh-<accession_number>.jpg` (accession number pending v4.4b) | `defer` |
| **C-08** | The Metropolitan Museum of Art | https://www.metmuseum.org/art/collection/search/285149 | [Botanical Specimen: Fern] | Unknown | 1860s | 285149 / 2003.562.3 | Public domain, but **double-confirmation still required** (Collection API `isPublicDomain: true` AND Open Access icon on public object page) | https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources | Yes — Met Collection API `primaryImage` field on object 285149 (URL recorded, not downloaded) | `met-285149.jpg` | `defer` (double-confirmation pending) |
| **C-09** | Rijksmuseum / Rijksprentenkabinet | https://www.rijksmuseum.nl/en/research/our-research/print-room | **Collection / search-level source only; per-item record deferred.** The Rijksprentenkabinet entry is the *collection / policy-level URL*; a specific Rijksprentenkabinet object has not been selected in v4.4. | — | — | — | Rijksmuseum two-tier policy: `CC0 1.0` (no longer in copyright) or `CC BY 4.0` (third-party grant). Per-item `licence` field to be recorded verbatim in v4.4b. | https://data.rijksmuseum.nl/policy/information-and-data-policy | Per-item Rijksstudio image URL or IIIF Image API URL (not yet selected in v4.4; v4.4 records the entry URL only) | `rijksmuseum-<object_number>.jpg` (`objectNumber` pending v4.4b) | `defer` |
| **C-10** | Rijksmuseum / Rijksprentenkabinet | https://www.rijksmuseum.nl/en/research/our-research/print-room | **Collection / search-level source only; per-item record deferred.** Same Rijksprentenkabinet entry as C-09; per-item IIIF Presentation API manifest URL pending v4.4b. | — | — | — | Rijksmuseum two-tier policy: `CC0 1.0` or `CC BY 4.0`. Per-item `license` field on the IIIF Presentation API manifest is the authoritative source. | https://data.rijksmuseum.nl/policy/information-and-data-policy | Per-item IIIF Presentation API manifest URL is on the per-item Catalogue record (not yet selected in v4.4) | (derives from C-09's per-item image) | `defer` |

---

## Source-level vs item-level clarification

| ID | Source level in v4.4 | Notes |
|---|---|---|
| C-01 | **item-level** | BHL item 318921 is a specific, reachable item-level record. |
| C-03 | **item-level** | Same BHL item 318921, used for the Section 3 book-level image. |
| C-06 | **collection / search-level only** | The NMNH Botany search URL is a collection entry, not an item-level record. Per-item selection deferred to v4.4b. |
| C-08 | **item-level** | Met object 285149 is a specific item-level record. The defer is due to the pending double-confirmation, not the source level. |
| C-09 | **collection / policy-level only** | The Rijksprentenkabinet entry URL is a collection / policy page, not an item-level record. Per-item selection + per-item `licence` field deferred to v4.4b. |
| C-10 | **collection / policy-level only** | Same Rijksprentenkabinet entry as C-09. Per-item IIIF manifest URL + `license` field deferred to v4.4b. |

---

## Selection totals (v4.4)

| Status | Count | IDs |
|---|---|---|
| `ready-for-asset-import` | **2** | C-01, C-03 |
| `defer` | **4** | C-06, C-08, C-09, C-10 |
| `blocked-from-import` row-level | **0** | (C-14 + C-03 CC BY-NC-SA subset are policy-level entries) |
| `replace-with-project-generated-diagram` row-level | **0** | (v4.1 carry-overs are fallback-only) |
| `approved` | **0** | (not used) |
| Approved asset count | **0** | (none in v4.4) |
| Downloaded image count | **0** | (v4.4 records URLs only) |

**Threshold check.** `ready-for-asset-import` count = **2 < 4**. The next recommended task is **v4.4b-source-gap-fix** (per `docs/ASSET_IMPORT_PREP_v4.4.md` §"Selection totals (v4.4)"). v4.5 asset import is conditioned on v4.4b producing ≥ 4 `ready-for-asset-import` rows.

---

## Round boundary

v4.4 ends with:

- All 5 v4.4 prep docs committed (`ASSET_IMPORT_PREP_v4.4.md`, `ITEM_IMPORT_EVIDENCE_TABLE_v4.4.md`, `SOURCE_AUDIT_MANIFEST_DRAFT_v4.4.md`, `CREDIT_LINE_AND_SOURCE_NOTE_DRAFTS_v4.4.md`, `ASSET_FILENAME_MAP_v4.4.md`).
- `README.md` v4.4 block committed.
- `docs/V4_ROADMAP.md` v4.4 + v4.4b sections committed.
- `scripts/template_quality_gate.py` → **PASS, 37/37**.
- Live byte size still **92,976 B**, v2.9 marker still **1**, `image-placeholder-pro` still **0**.
- `find` confirms no new image files.
- `git diff` against `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`, `scripts/template_quality_gate.py` is empty.
- `ready-for-asset-import` count = 2 (recorded as < 4 → v4.4b-source-gap-fix is the next round).
- `approved` does not appear as a status value in any v4.4 doc.
- C-03's `CC BY-NC-SA subset blocked` is recorded.
- C-08's `double-confirmation required` is recorded.
- C-09 / C-10's `per-item licence field required` is recorded.
- No new tag, no new GitHub Release.

The next round is **v4.4b-source-gap-fix**.