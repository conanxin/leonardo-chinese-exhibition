# v4.3 Item Evidence Dossier

> Per-item evidence plan for the 6 v4.3 `selected-for-build-planning` candidates. Each entry records the evidence that the v4.0 source-acceptance rule will require, the proposed section, the proposed use, the credit-line basis, the source-note draft, the rights-note draft, the remaining caution, and the future asset-import status. **Future asset import status: not downloaded.** This document is a plan, not a download log.

> The status `approved` is **not used**. The phrase "safe for commercial use" is **not used**. Per-item selection (e.g., a specific BHL volume, a specific NMNH accession number) is a v4.4 step. v4.3 only records the per-candidate *evidence* that v4.4 will need.

---

## C-01 — Pre-1928 BHL Public-domain botanical plate

- **Institution:** Biodiversity Heritage Library
- **Source URL:** <https://www.biodiversitylibrary.org/advsearch> (search entry → title record → volume page; the per-item selection is a v4.4 step)
- **Rights URL / statement:** <https://about.biodiversitylibrary.org/help/copyright-and-reuse/> — per the BHL `Copyright & Reuse` page, three possible `<Copyright Status>` strings: `Public domain`, `No known copyright restrictions as determined by scanning institution`, `In copyright. Digitized with the permission of the rights holder`. The C-01 selection is restricted to `Public domain`.
- **Identifier:** BHL title-level ID (e.g., `<title id>` on the title page) and per-volume `<item id>` on each volume record. The v4.4 step captures the per-item identifier verbatim.
- **Title:** TBD at v4.4 (per-item selection). The candidate type is a *pre-1928 hand-colored botanical plate* (engraving / lithograph).
- **Creator:** TBD at v4.4 (per-item).
- **Date:** Pre-1928 (US 95-year public-domain cutoff is `current year − 95`; for 2026 the cutoff is 1931, so any item published in 1931 or earlier is in the public domain for the US).
- **Collection:** BHL aggregate corpus of biodiversity literature (200k+ titles, 64M+ pages). The specific collection / holding institution is captured per-item at v4.4.
- **Proposed section:** Section 1 (观察：图像如何抓住植物特征)
- **Proposed use:** Primary real-image artifact card for Section 1; a "this is what an illustrator chose to look at" example. The plate is the canonical 观察 artifact.
- **Credit line basis:** Verbatim from the BHL per-item page: "Image from the Biodiversity Heritage Library. Contributed by [Holding Institution]. | www.biodiversitylibrary.org" (with the per-item Holding Institution name substituted). The BHL recommendation is to attribute even when not strictly required; the recommendation is followed.
- **Source note draft:** "Reproduced from a pre-1928 volume in the Biodiversity Heritage Library. Public domain. Contributed by [Holding Institution]." The source note is a short paragraph that names the institution, the rights status, and the holding institution.
- **Rights note draft:** "Public domain in the United States under the BHL 95-year cutoff. Distribution channel is openly-distributed (GitHub Pages). Non-US distribution may have different rules." This is a *project-side* note, not a legal opinion.
- **Remaining caution:**
  - The 95-year moving wall is the safe default. Items published in the last 95 years are *not* automatically public domain; the per-item `<Copyright Status>` is the only safe check.
  - BHL notes that "works that may be in the public domain under United States law may not be in the public domain under the laws of other countries." v4.4 must record this caveat in the asset's rights note.
  - The BHL recommendation for attribution is followed; the credit line is recorded verbatim.
- **Future asset import status: not downloaded.** The v4.4 asset import round will re-open the BHL title page, capture the per-item identifier, capture the `<Copyright Status>` field, and write the local file. v4.3 does not download.

---

## C-03 — BHL title-level book record (PD subset only; CC BY-NC-SA subset blocked)

- **Institution:** Biodiversity Heritage Library
- **Source URL:** <https://www.biodiversitylibrary.org/advsearch> → open title page → Show Info tab (the per-item selection is a v4.4 step)
- **Rights URL / statement:** <https://about.biodiversitylibrary.org/help/copyright-and-reuse/>. The C-03 selection is restricted to the **Public-domain subset** only. The **CC BY-NC-SA 4.0 in-copyright subset is `blocked-from-build`** in v4.3 and is not in this dossier. Per the BHL Permissions page: "Almost always a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license" applies to in-copyright items; the NC clause is incompatible with the project's openly-distributed output.
- **Identifier:** BHL title-level ID + per-volume `<item id>`. The v4.4 step captures the per-item identifier verbatim.
- **Title:** TBD at v4.4 (per-item selection). The candidate type is a *pre-1928 title-level book record with at least one Public-domain volume*.
- **Creator:** TBD at v4.4 (per-item).
- **Date:** Pre-1928 (per the BHL 95-year cutoff).
- **Collection:** BHL aggregate corpus. The specific collection / holding institution is captured per-item at v4.4.
- **Proposed section:** Section 3 (复制：书籍、版画与数字化如何改变传播)
- **Proposed use:** Primary real-image artifact card for Section 3; a "this is what a plate looked like in its published context" example.
- **Credit line basis:** Verbatim from the BHL per-item page, same as C-01. For the Public-domain subset, the BHL-recommended attribution is "Image from the Biodiversity Heritage Library. Contributed by [Holding Institution]. | www.biodiversitylibrary.org". The CC BY-NC-SA subset is not in this dossier.
- **Source note draft:** "Reproduced from a pre-1928 volume in the Biodiversity Heritage Library. Public domain. Contributed by [Holding Institution]."
- **Rights note draft:** "Public domain in the United States under the BHL 95-year cutoff. The CC BY-NC-SA 4.0 in-copyright subset is excluded from this build (NC clause incompatible with openly-distributed output)."
- **Remaining caution:**
  - **The CC BY-NC-SA subset is `blocked-from-build` and must not be selected by v4.4.** v4.4 must filter on `<Copyright Status> = Public domain` only. If no Public-domain item is found, C-03 is replaced with the Section 3 fallback (the project-generated reproduction-chain diagram).
  - The 95-year moving wall and the non-US caveat are the same as C-01.
  - The BHL attribution is followed.
- **Future asset import status: not downloaded.** The v4.4 asset import round must filter on the Public-domain subset only.

---

## C-06 — NMNH herbarium sheet, CC0

- **Institution:** Smithsonian Open Access (National Museum of Natural History)
- **Source URL:** <https://www.si.edu/search/images?edan_fq[0]=media_usage%3ACC0> + filter to NMNH (`unit_code` = NMNH) (the per-item selection is a v4.4 step)
- **Rights URL / statement:** <https://www.si.edu/openaccess/faq> — "We have released these images and data into the public domain as Creative Commons Zero (CC0), meaning you can use, transform, and share our open access assets without asking permission from the Smithsonian." Items *not* marked CC0 are "subject to usage conditions". The C-06 selection is restricted to items with the CC0 icon.
- **Identifier:** `edanmdm-<unit>_<id>` object ID (e.g., `edanmdm-nmnhbotany_1234567`); Smithsonian accession number. The v4.4 step captures the per-item identifier verbatim.
- **Title:** TBD at v4.4 (per-item selection). The candidate type is a *herbarium sheet photograph* from NMNH.
- **Creator:** TBD at v4.4 (per-item; for an herbarium sheet, the "creator" is often the collector or the botanist who pressed / labelled the specimen).
- **Date:** TBD at v4.4 (per-item; herbarium sheets are often 19th–20th century).
- **Collection:** Smithsonian National Museum of Natural History. The specific collection / unit is captured per-item at v4.4.
- **Proposed section:** Section 2 (分类：图像如何服务命名与秩序)
- **Proposed use:** Primary real-image artifact card for Section 2; the "specimen + label" example. A herbarium sheet is *the* unit of botanical classification — name + specimen + image together.
- **Credit line basis:** Composed from the EDAN record's `title`, `unitCode`, and the accession number. Format: "Smithsonian National Museum of Natural History. [Object title]. [Accession number]. CC0." The accession number is mandatory because the Smithsonian FAQ explicitly recommends a "minimal" caption of title, author, source, license, and source URL.
- **Source note draft:** "Reproduced from the Smithsonian Open Access collection. National Museum of Natural History. CC0. Accession number [N]."
- **Rights note draft:** "CC0 1.0. Per the Smithsonian FAQ: 'CC0 only applies to copyright so you may still need someone else's permission to use a CC0-designated digital asset.' Any donor / cultural-sensitivity restrictions on the chosen item are noted at v4.4."
- **Remaining caution:**
  - The Smithsonian CC0 is rigorous but the FAQ explicitly states CC0 only covers copyright. Donor / cultural-sensitivity / trademark restrictions may still apply and are recorded at v4.4.
  - Attribution is not legally required (CC0), but the Smithsonian FAQ recommends the minimal caption. v4.4 follows the recommendation.
- **Future asset import status: not downloaded.** The v4.4 asset import round will re-open the EDAN record, capture the accession number, capture the CC0 marking, and write the local file.

---

## C-08 — Met `MetObjects.csv` row + linked CC0 image (alternate for Section 3)

- **Institution:** The Metropolitan Museum of Art
- **Source URL:** <https://github.com/metmuseum/openaccess/blob/master/MetObjects.csv> + Collection API `https://collectionapi.metmuseum.org/public/collection/v1/objects/{objectID}` + public object page `https://www.metmuseum.org/art/collection/search/{objectID}` (the per-item selection is a v4.4 step)
- **Rights URL / statement:** Dataset: CC0 1.0. Image: CC0 only if (a) `isPublicDomain: true` in the API record **and** (b) the public object page shows the Open Access icon. Image Resources policy page: <https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources>. The C-08 selection is restricted to items where both confirmations are present.
- **Identifier:** `objectID` (unique) and `accessionNumber` (often unique). The v4.4 step captures both verbatim.
- **Title:** TBD at v4.4 (per-item selection). The candidate type is a *botanical / natural-history print or drawing held by the Met*.
- **Creator:** TBD at v4.4 (per-item).
- **Date:** TBD at v4.4 (per-item).
- **Collection:** The Met (collection: Drawings and Prints, or similar). The specific department is captured per-item at v4.4.
- **Proposed section:** Section 3 (复制) — **alternate**. The Section 3 primary is C-03 (PD subset).
- **Proposed use:** Alternate real-image artifact card for Section 3; a print / engraving from the Met. C-08 is an *alternate*, not the primary, because the Met's botanical / natural-history holdings are not a primary collection strength.
- **Credit line basis:** "The Metropolitan Museum of Art. [Title]. [Date]. [Credit line]. CC0." The Met's `creditLine` field is part of the Collection API response and is captured verbatim. The dataset is CC0 1.0; the *image* is CC0 only if both `isPublicDomain: true` and the public-page OA icon are present.
- **Source note draft:** "Reproduced from The Metropolitan Museum of Art's Open Access dataset. [Title]. [Date]. [Credit line]. CC0. Double-confirmed: `isPublicDomain: true` in the Collection API; Open Access icon on the public object page."
- **Rights note draft:** "CC0 1.0 for both the dataset and the image. The Met is a secondary source for this exhibition's botanical theme; C-08 is an alternate, not a primary."
- **Remaining caution:**
  - **Double-confirmation mandatory at v4.4.** Both `isPublicDomain: true` in the Collection API and the Open Access icon on the public object page must be present. If only one is present, C-08 does not enter the build and the Section 3 alternate slot is filled by a project-generated diagram.
  - The Met's `creditLine` field is captured verbatim (not paraphrased).
- **Future asset import status: not downloaded.** The v4.4 asset import round will run the double-confirmation and write the local file.

---

## C-09 — Rijksmuseum botanical print, CC0

- **Institution:** Rijksmuseum
- **Source URL:** <https://www.rijksmuseum.nl/en/rijksstudio> + Data Services <https://data.rijksmuseum.nl> + Persistent Identifier Resolver `id.rijksmuseum.nl/{identifier}` (the per-item selection is a v4.4 step)
- **Rights URL / statement:** <https://data.rijksmuseum.nl/policy/information-and-data-policy> — two-tier: **CC0 1.0** (objects no longer in copyright + associated metadata) or **CC BY 4.0** (objects where a third-party rights holder has granted the museum a written, unrestricted licence). The C-09 selection prefers CC0 1.0; CC BY 4.0 is allowed only if the credit-line basis preserves the per-item licence string.
- **Identifier:** `objectNumber` (e.g., `SK-C-5`); persistent ID `id.rijksmuseum.nl/{identifier}`. The June 2026 Rijksmuseum data-services update makes `id.rijksmuseum.nl/...` the canonical PID. The v4.4 step captures the per-item identifier verbatim.
- **Title:** TBD at v4.4 (per-item selection). The candidate type is a *Rijksprentenkabinet botanical print or drawing*.
- **Creator:** TBD at v4.4 (per-item).
- **Date:** TBD at v4.4 (per-item).
- **Collection:** Rijksprentenkabinet (Rijksmuseum's print room). The specific collection is captured per-item at v4.4.
- **Proposed section:** Section 1 (观察) — **primary**; Section 2 (分类) — **alternate**.
- **Proposed use:** Primary real-image artifact card for Section 1; alternate for Section 2. A Dutch Golden Age botanical print is a strong source family for the observation theme.
- **Credit line basis:** Composed from the Rijksmuseum object record. Format: "Rijksmuseum. [Object title]. [Creator]. [Date]. [objectNumber]. [CC0 1.0 / CC BY 4.0]." Attribution is mandatory for CC BY 4.0; for CC0, the Rijksmuseum policy requests (but does not legally require) attribution. v4.4 follows the request.
- **Source note draft:** "Reproduced from the Rijksmuseum collection. [Object title]. [Creator]. [Date]. [objectNumber]. [CC0 1.0 / CC BY 4.0]."
- **Rights note draft:** "Rijksmuseum two-tier policy: CC0 1.0 (no longer in copyright) or CC BY 4.0 (third-party written grant). The per-item `licence` field is recorded verbatim. Attribution is requested for CC0 and required for CC BY 4.0."
- **Remaining caution:**
  - The Rijksmuseum policy is two-tier; v4.4 must record the per-item `licence` field exactly.
  - The Rijksmuseum itself publishes its policy document under CC BY 4.0; the policy document's licence is *not* the same as the licence of the data the museum publishes. v4.4 must not conflate the two.
  - The June 2026 Rijksmuseum data-services update changed the redirect behaviour of the Linked Data Resolver; the canonical PID is now `id.rijksmuseum.nl/...`. v4.4 uses the canonical PID.
- **Future asset import status: not downloaded.** The v4.4 asset import round will re-open the Rijksmuseum object record, capture the `licence` field, capture the `objectNumber` and PID, and write the local file.

---

## C-10 — Rijksmuseum IIIF Presentation API manifest

- **Institution:** Rijksmuseum
- **Source URL:** <https://data.rijksmuseum.nl/docs/iiif/> (IIIF Image API + Presentation API + Change Discovery API) + Persistent Identifier Resolver `id.rijksmuseum.nl/{identifier}` (the per-item selection is a v4.4 step)
- **Rights URL / statement:** Same as C-09 (CC0 1.0 or CC BY 4.0); the IIIF Presentation API manifest exposes a `license` field. v4.4 records the manifest's `license` field verbatim.
- **Identifier:** Same as C-09 (`objectNumber` + `id.rijksmuseum.nl/...` PID). The IIIF manifest URL contains the persistent ID.
- **Title:** TBD at v4.4 (per-item selection). The candidate type is a *Rijksprentenkabinet botanical print exposed as an IIIF Presentation API manifest*.
- **Creator:** TBD at v4.4 (per-item).
- **Date:** TBD at v4.4 (per-item).
- **Collection:** Rijksprentenkabinet. The specific collection is captured per-item at v4.4.
- **Proposed section:** Section 4 (再组织：数字馆藏如何让图像重新连接)
- **Proposed use:** Primary real-image artifact card for Section 4; the "IIIF as a re-linking layer" example. The section's argument is *about* the IIIF manifest, not just about a plate.
- **Credit line basis:** Same as C-09 (per-item `licence` field). The IIIF manifest's `license` field is recorded verbatim.
- **Source note draft:** "Reproduced from the Rijksmuseum's IIIF Presentation API. [Object title]. [Creator]. [Date]. [objectNumber]. [CC0 1.0 / CC BY 4.0]. Manifest URL: [IIIF manifest URL]."
- **Rights note draft:** "Rijksmuseum two-tier policy applies. The IIIF manifest's `license` field is the authoritative source. The IIIF info.json alone does not carry the rights field; the Presentation API manifest does."
- **Remaining caution:**
  - The IIIF endpoint must be paired with the Catalogue-side object record. The IIIF info.json does not carry the rights field; the Presentation API manifest does.
  - The Rijksmuseum IIIF tutorials walk through the object-record → VisualItem → DigitalObject chain; v4.4 must follow the canonical chain.
  - The IIIF manifest URL is recorded as part of the asset's metadata.
- **Future asset import status: not downloaded.** The v4.4 asset import round will fetch the IIIF Presentation API manifest (read-only), capture the `license` field, capture the IIIF image service URL, and write the local file.

---

## Round-end note

All 6 selected-for-build-planning rows have a complete evidence dossier:

- **Source URL.** Official, reachable, page-level URL.
- **Rights URL / statement.** Verbatim from the institution's own page.
- **Identifier.** Per-item ID type identified; the specific ID is captured at v4.4.
- **Title / creator / date.** Captured per-item at v4.4.
- **Proposed section.** Recorded.
- **Proposed use.** Recorded.
- **Credit line basis.** Composed from the institution's wording + the per-item rights statement.
- **Source note draft.** Recorded.
- **Rights note draft.** Recorded.
- **Remaining caution.** Recorded per-row.
- **Future asset import status: not downloaded.** All 6 rows.

The status `approved` is **not used** in this document. The phrase "safe for commercial use" is **not used** in this document. Per-item selection is a v4.4 step.