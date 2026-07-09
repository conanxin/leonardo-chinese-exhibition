# v4.2 Verified Source Shortlist

> Purpose: list the **v4.2 verified** candidates — i.e., the candidates that may enter v4.3 build planning. This is not a list of *approved* assets. `verified` is a project-internal status from `docs/RIGHTS_AUDIT_v4.2.md` that signals a row's *mechanism* (source URL, rights statement, identifier, metadata, credit line) is in place. The list does **not** authorize any image download, asset import, or live change.

---

## Purpose

This document exists so that v4.3 build planning has a single, narrow input file: the verified candidates from v4.2. Each row here is verified at the **candidate type** level, not at a specific item. v4.3 will select one specific item per row and run the v4.0 source-acceptance rule a second time on that specific item before any download.

The v4.2 verified count is **6** (out of 12 shortlist rows; the other 6 carry `needs clarification`). The build planning rule below sets a threshold of **4 verified** as the minimum to enter v4.3 — and that threshold is met.

---

## Verified candidates

| ID | Institution | Candidate source | URL | Why it fits | Rights basis | Required credit line basis | Proposed section | Remaining caution |
|---|---|---|---|---|---|---|---|---|
| **C-01** | BHL | Pre-1928 botanical plate from a BHL Public-domain volume | <https://www.biodiversitylibrary.org/advsearch> (filter: subject = botany, copyright status = Public domain) | Fits section 1 (观察) and section 3 (复制) — observation and reproduction | `<Copyright Status> = Public domain` per the BHL `<Copyright Status>` field on the title / volume page; BHL's overall metadata under CC0 1.0 | "Image from the Biodiversity Heritage Library. Contributed by [Holding Institution]. | www.biodiversitylibrary.org" (verbatim from the BHL Copyright & Reuse page, with the per-item Holding Institution name substituted) | Section 1 (观察) / Section 3 (复制) | The US 95-year public-domain cutoff is the only safe default; non-US distribution may have different rules. v4.3 must pick a specific item and re-check `<Copyright Status>` on the volume page. |
| **C-03** | BHL | Title-level record of a pre-1928 botanical book (Public-domain subset) | <https://www.biodiversitylibrary.org/advsearch> → open title page → Show Info tab | Fits section 3 (复制) — book page as a published context | Same as C-01 (Public-domain subset of the title-level record) | Same as C-01 | Section 3 (复制) | The Public-domain subset of C-03 is verified; the CC BY-NC-SA in-copyright subset is **not** in this verified list. v4.3 must restrict to the Public-domain subset. |
| **C-06** | Smithsonian Open Access (NMNH) | NMNH herbarium sheet with CC0 marking | <https://www.si.edu/search/images?edan_fq[0]=media_usage%3ACC0> + filter to NMNH (`unit_code` = NMNH) | Fits section 2 (分类) — specimen + label as a unit of classification | CC0 1.0 (per the Smithsonian Open Access program, FAQ, and the per-item CC0 icon) | "Smithsonian National Museum of Natural History. [Object title]. [Accession number]. CC0." (composition from the EDAN record's `title` + accession number) | Section 2 (分类) | v4.3 must pick a specific NMNH specimen record and confirm the CC0 icon is present; the accession number is mandatory for the credit line. |
| **C-08** | Met Open Access | `MetObjects.csv` row pointing to a CC0 image | <https://github.com/metmuseum/openaccess/blob/master/MetObjects.csv> + Collection API `https://collectionapi.metmuseum.org/public/collection/v1/objects/{objectID}` | Fits section 3 (复制) — print / engraving as a reproducible medium | CC0 1.0 (dataset) **plus** `isPublicDomain: true` in the Collection API **plus** Open Access icon on the public object page (`https://www.metmuseum.org/art/collection/search/{objectID}`) | "The Metropolitan Museum of Art. [Title]. [Date]. [Credit line]. CC0." (the `creditLine` field is part of the API response) | Section 3 (复制) | The Met's botanical / natural-history holdings are not a primary collection strength; v4.3 must pick a specific item and the double-confirmation (API + public page) is mandatory. |
| **C-09** | Rijksmuseum | Rijksprentenkabinet botanical print with CC0 marking | <https://www.rijksmuseum.nl/en/rijksstudio> + Data Services <https://data.rijksmuseum.nl> | Fits section 1 (观察) and section 2 (分类) — Dutch Golden Age botanical illustration | CC0 1.0 (per the Rijksmuseum's two-tier policy; CC0 for objects no longer in copyright) | "Rijksmuseum. [Object title]. [Creator]. [Date]. [objectNumber]. CC0 1.0." | Section 1 (观察) / Section 2 (分类) | v4.3 must pick a specific object and confirm the `licence` field on the object record is `CC0 1.0` (or `CC BY 4.0` if the item carries the third-party grant tier). |
| **C-10** | Rijksmuseum | IIIF Presentation API manifest of a botanical print | <https://data.rijksmuseum.nl/docs/iiif/> (IIIF Image API + Presentation API + Change Discovery API) | Fits section 4 (再组织) — IIIF as a re-linking layer | Per-item (CC0 1.0 or CC BY 4.0); the IIIF manifest's `license` field is verifiable | Same as C-09 (per-item licence) | Section 4 (再组织) | The IIIF endpoint must be paired with the Catalogue-side object record (the IIIF info.json alone does not carry the rights field; the Presentation API manifest does). v4.3 picks a specific item. |

**6 verified candidates.** Section coverage:

- Section 1 (观察): C-01, C-09.
- Section 2 (分类): C-06, C-09.
- Section 3 (复制): C-01, C-03, C-08.
- Section 4 (再组织): C-10.

Each section has at least one verified candidate. The build planning threshold (≥ 4 verified) is met.

---

## Build planning rule

> Only verified candidates may enter v4.3 build planning. Any real image download or local asset addition must happen in a separate asset-import round after source audit evidence is recorded.

Operationally, this means:

1. v4.3 build planning reads from this shortlist. It does **not** read from the 6 `needs clarification` rows.
2. For each verified candidate, v4.3 picks **one specific item** and records the per-item evidence (source URL, rights statement, identifier, metadata, credit line) in a v4.3 entry of `docs/RIGHTS_AUDIT_v4.2.md` (or a successor document).
3. The 6 `needs clarification` rows may be promoted to `verified` in v4.3 if the per-item evidence is captured. They do not enter v4.3 build planning until then.
4. Image download and local asset addition are **separate** from v4.3 build planning. They belong to a future round that runs the v4.0 source-acceptance rule a second time on each specific item, with the per-item evidence attached.
5. Even with `verified` status, this list does **not** authorize redistribution. The credit line is mandatory; the rights statement must be reproduced verbatim where required by the licence.

The 6 `needs clarification` rows are not in this list. They are listed in `docs/BLOCKED_OR_EXCLUDED_SOURCES_v4.2.md` with their `needs clarification` decision and the follow-up action.

---

## Remaining caution (per row)

Every row above has at least one remaining caution. The cautions are not deal-breakers; they are v4.3 follow-up items.

- **C-01 / C-03 (BHL).** The US 95-year public-domain cutoff is the safe default; non-US distribution has different rules. v4.3 must restrict to Public-domain items and re-check `<Copyright Status>` on the volume page.
- **C-06 (Smithsonian NMNH).** The Smithsonian FAQ explicitly states: "CC0 only applies to copyright so you may still need someone else's permission to use a CC0-designated digital asset." v4.3 must note any donor / cultural-sensitivity restrictions on the chosen item, even with CC0.
- **C-08 (Met).** The double-confirmation (API + public page OA icon) is mandatory. The Met's botanical holdings are not a primary collection strength; v4.3 may find that the corpus is small for this theme.
- **C-09 / C-10 (Rijksmuseum).** The Rijksmuseum policy is two-tier; v4.3 must confirm the per-item `licence` field is `CC0 1.0` (or `CC BY 4.0` if the third-party grant tier applies). Attribution is mandatory for CC BY 4.0.
- **All rows.** No row in this list is "safe for commercial use" as a legal opinion. v4.3 must not represent the `verified` status as a legal clearance.