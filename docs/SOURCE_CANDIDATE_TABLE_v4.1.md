# v4.1 Source Candidate Table

> Companion to `docs/SOURCE_CANDIDATES_v4.1.md`. Each row is a **candidate**, not an approved asset. The only allowed statuses in v4.1 are: `candidate`, `needs rights audit`, `excluded`. **`approved` is not used in v4.1.** No real image file is associated with any row in this table.

---

## Candidate table

| ID | Institution | Candidate collection / item | URL | Asset type | Metadata available | Rights statement found | Initial risk | Proposed section | Status |
|---|---|---|---|---|---|---|---|---|---|
| C-01 | BHL | BHL Advanced Search (filter: subject = botany, copyright status = Public domain) | <https://www.biodiversitylibrary.org/advsearch> | Pre-1928 botanical plate | title, creator, date, holding institution, copyright status, license type, rights holder, page-level identifiers | Public domain (per BHL `<Copyright Status>` field; metadata CC0 1.0) | Low | Section 1 (观察) / Section 3 (复制) | candidate |
| C-02 | BHL | BHL Flickr photostream — botanical albums | <https://www.flickr.com/photos/biodivlibrary/albums> | High-resolution botanical illustration (Flickr-resolved) | title, item URL (back to BHL), copyright status (on the linked BHL page) | Underlying BHL item's `<Copyright Status>`; **Flickr is the third-party platform** — rights belong to the underlying work, not Flickr | Medium (platform screenshot ambiguity — see v4.0 register §3) | Section 1 (观察) / Section 3 (复制) | needs rights audit |
| C-03 | BHL | BHL Title-level record (one specific pre-1928 botanical book) | <https://www.biodiversitylibrary.org/> (search → open the title page → Show Info tab) | Digitized book page (title page + plate) | title, author, date, holding institution, copyright status, license type | Public domain (US cutoff) or CC BY-NC-SA 4.0 (in-copyright subset) — per item | Low–Medium (per item) | Section 3 (复制) | candidate |
| C-04 | Wellcome | Wellcome Works search — Engravings and Engravings (or Lithographs) | <https://wellcomecollection.org/works> | Historical botanical engraving or lithograph | title, creator, date, format, identifiers, licence field | Site-wide CC BY 4.0 ("except where otherwise noted") — per-item confirmation required | Low (with per-item CC BY 4.0 confirmation) | Section 1 (观察) | candidate |
| C-05 | Wellcome | Wellcome IIIF Image API (per-item) | <https://developers.wellcomecollection.org/api/iiif> | IIIF image of a botanical print or drawing | IIIF info.json: image metadata, format, dimensions; per-item licence via Catalogue API | Site-wide CC BY 4.0 + per-item licence field | Low–Medium (per item) | Section 4 (再组织) | needs rights audit |
| C-06 | Smithsonian Open Access (NMNH) | Smithsonian Open Access portal — filter to NMNH + CC0 | <https://www.si.edu/search/images?edan_fq[0]=media_usage%3ACC0> | Herbarium sheet photograph or specimen image | title, creator, date, accession number, CC0 icon, API + Figshare + DarwinCore | CC0 1.0 (per Smithsonian Open Access program) | Low (with CC0 icon confirmation) | Section 2 (分类) | candidate |
| C-07 | Smithsonian Open Access (general) | Smithsonian OpenAccess GitHub data dump | <https://github.com/Smithsonian/OpenAccess> | JSON / DarwinCore record pointing to a CC0 image | CC0 metadata record with title, creator, date, accession, image URL | CC0 1.0 (for the data) — image rights depend on the linked item | Low (for the metadata) / Medium (for the image) | Section 4 (再组织) | needs rights audit |
| C-08 | Met Open Access | `MetObjects.csv` (filter: Classification ~ botanical / natural-history / print) | <https://github.com/metmuseum/openaccess/blob/master/MetObjects.csv> | Object CSV row + linked CC0 image on `metmuseum.org` | CSV fields: title, artist, date, medium, classification, object URL, image URL, `Is Public Domain` flag | CC0 1.0 for the *dataset*; CC0 for the *image* only if the public object page shows the CC0 icon **and** `Is Public Domain = True` | Low (with both confirmations) / High (if only one confirms) | Section 3 (复制) | needs rights audit |
| C-09 | Rijksmuseum | Rijksstudio + Rijksmuseum data services portal (filter: classification / botanical prints and drawings) | <https://www.rijksmuseum.nl/en/rijksstudio> and <https://data.rijksmuseum.nl> | Botanical print or drawing with CC0 marking | object record: title, creator, date, materials, dimensions, identifiers, licence field, IIIF manifest URL | CC0 1.0 (when no longer in copyright) or CC BY 4.0 (third-party grant) | Low (CC0) or Low–Medium (CC BY 4.0) | Section 1 (观察) / Section 2 (分类) | candidate |
| C-10 | Rijksmuseum | Rijksmuseum IIIF Presentation API + Image API | <https://data.rijksmuseum.nl/tutorials/iiif/> | IIIF manifest of a botanical print | manifest: title, creator, date, rights (in `license` field), image service URL | Per-item (CC0 or CC BY 4.0) | Low (per item) | Section 4 (再组织) | candidate |
| C-11 | Library of Congress | LoC Prints & Photographs Online Catalog — Botanical illustrations subject heading | <https://www.loc.gov/pictures/item/tgm001244/> | 19th- or early-20th-century American botanical illustration | title, creator, date, call number, repository, rights statement, persistent item URL | "U.S. government works not subject to copyright" (17 U.S.C. § 105) or "no known copyright restrictions" — per item / per collection | Low (U.S. government work) or Medium ("no known" wording) | Section 1 (观察) / Section 2 (分类) | needs rights audit |
| C-12 | Library of Congress | LoC Digital Collections — a specific illustrated-book collection (e.g., early natural-history volume) | <https://www.loc.gov/collections/> (pick a specific collection) | Digitized book page from an early illustrated natural-history volume | per-page metadata + collection-level "Rights & Access" page | Per-collection rights wording; varies by collection | Low–Medium (per collection) | Section 3 (复制) | needs rights audit |
| C-13 | Library of Congress | LoC Prints & Photographs — a specific P&P record | <https://www.loc.gov/pictures/> (per-item record) | Prints & Photographs botanical illustration record | per-item record fields, persistent URL | Per-record rights statement | Low–Medium (per record) | Section 1 (观察) | candidate |
| C-14 | BHL | BHL Title record (in-copyright subset) | <https://about.biodiversitylibrary.org/help/copyright-and-reuse/permissions/> | In-copyright botanical volume (CC BY-NC-SA 4.0) | title, author, date, license type, rights holder | CC BY-NC-SA 4.0 (in-copyright subset) — non-commercial + share-alike | Medium–High (NC clause incompatible with openly-distributed output) | — | excluded (NC clause mismatch with openly-distributed exhibition; revisit only if distribution channel changes) |

14 candidate rows. Each row has at least one URL field. Each row maps to a proposed section. Each row is in status `candidate`, `needs rights audit`, or `excluded` — never `approved`.

---

## Status legend

| Status | Meaning in v4.1 |
|---|---|
| `candidate` | Row is a plausible v4.3 input. Evidence is present in the institution's own page but v4.2 must re-verify per item. |
| `needs rights audit` | Evidence is partial or depends on a per-item check that v4.1 has not yet performed. The row enters v4.2 with the per-item check listed as a required action. |
| `excluded` | v4.1 has identified a hard reason (e.g., NC licence, platform-screenshot-only with no underlying rights, missing identifier). The row does not enter v4.2. |

The status `approved` is **not used** in v4.1. Approval is a v4.2+ concept, gated by the rights-risk register.

---

## Coverage check

| Institution | Rows in this table |
|---|---|
| BHL | C-01, C-02, C-03, C-14 |
| Wellcome | C-04, C-05 |
| Smithsonian | C-06, C-07 |
| Met | C-08 |
| Rijksmuseum | C-09, C-10 |
| Library of Congress | C-11, C-12, C-13 |

All 6 institutions are represented. BHL and LoC have multiple rows because they each have distinct access patterns (BHL: title-level + Flickr + in-copyright; LoC: P&P + illustrated books + per-record).