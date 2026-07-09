# v4.3 Asset Import Plan

> Scope: define the asset import rule, the per-candidate import plan, and the file naming convention for the future asset import round. v4.3 does not download any image. v4.3 only records the plan.
>
> 本轮不下载图片。未来如进入 asset import round，必须按本计划逐项执行。

---

## Import rule

The future asset import round (v4.4 or later) is the only round that may download a real image. The import rule is:

1. **Re-open the source URL.** The URL is the per-institution official page recorded in `docs/ITEM_EVIDENCE_DOSSIER_v4.3.md`. The import round visits the URL on the day of import; the previous visit may be days or weeks old.
2. **Re-check the rights statement.** The rights wording is captured *verbatim* from the source page on the day of import. The dossier's draft is a *plan*; the import round's capture is the *evidence*.
3. **Record the identifier.** The identifier is the per-item persistent ID (BHL `<item id>`, Wellcome canonical work ID, Smithsonian `edanmdm-...` ID, Met `objectID` / `accessionNumber`, Rijksmuseum `objectNumber` / `id.rijksmuseum.nl/...`, LoC persistent URL).
4. **Record the source URL.** The URL is the per-item page URL (not the search-entry URL).
5. **Record the image URL / IIIF URL.** The image URL is the direct image URL (or the IIIF Image API URL). The IIIF Presentation API manifest URL is recorded as a separate field.
6. **Write the credit line.** The credit line is composed from the institution's wording + the per-item rights statement. The line is recorded verbatim, not paraphrased.
7. **Write the source note.** The source note is a short paragraph that names the institution, the rights status, the holding institution (if any), and the per-item identifier. The note is in the same language as the exhibition copy.
8. **Save the local file path.** The local path is recorded in the v4.4 source audit manifest. The path follows the file naming convention below.
9. **Update the source audit manifest.** The manifest is a single table with one row per asset, ordered by section.
10. **Run the quality gate.** `scripts/template_quality_gate.py` is run after the import. The gate's image-related checks are not bypassed.
11. **Confirm no live change unless deployment round.** The import round is repository-only. The live site is updated only by a *separate* deployment round that runs the source-and-rights audit a second time on the to-be-deployed working tree.

**The import rule is hard.** Skipping any of the 11 steps means the row is not imported; the row's status is `blocked-from-build` and the section falls back to a project-generated diagram.

---

## Planned asset import table

The table below records the v4.3 plan for the 6 `selected-for-build-planning` candidates. The table is the *plan*; the future round fills in the per-item identifier / image URL / credit line / source note / local path with the per-item evidence.

The import status is one of: `not downloaded`, `wait for v4.4 asset import`, `replace with project-generated diagram`. The status `approved` is not used.

| Candidate ID | Future local filename | Source URL | Image / IIIF URL known? | Rights basis | Credit line basis | Import status | Required pre-import action |
|---|---|---|---|---|---|---|---|
| **C-01** (BHL PD plate) | `bhl-<title_id>-<item_id>-plate.jpg` | <https://www.biodiversitylibrary.org/advsearch> → title record → volume page → item | not yet (per-item selection is v4.4) | `<Copyright Status> = Public domain` per the BHL `<Copyright Status>` field; BHL metadata CC0 1.0 | "Image from the Biodiversity Heritage Library. Contributed by [Holding Institution]. | www.biodiversitylibrary.org" (verbatim, per-item Holding Institution substituted) | **not downloaded** | v4.4 picks a specific Public-domain volume, opens the title page, captures the `<Copyright Status>` and `<Holding Institution>` fields, captures the per-volume `<item id>`, captures the page image URL, downloads the image, writes the local file, updates the source audit manifest. |
| **C-03** (BHL title-level book record, **PD subset only**) | `bhl-<title_id>-<page_id>-page.jpg` | <https://www.biodiversitylibrary.org/advsearch> → title record → volume page → page | not yet (per-item selection is v4.4) | `<Copyright Status> = Public domain` only — **the CC BY-NC-SA subset is `blocked-from-build` and must not be selected** | Same as C-01 | **not downloaded** | v4.4 picks a specific Public-domain volume, captures the per-page URL, downloads the page image, writes the local file, updates the source audit manifest. **The CC BY-NC-SA subset is rejected at the per-item check.** |
| **C-06** (Smithsonian NMNH CC0 herbarium sheet) | `smithsonian-nmnh-<accession_number>.jpg` | <https://www.si.edu/search/images?edan_fq[0]=media_usage%3ACC0> + filter to NMNH → item page | not yet (per-item selection is v4.4) | CC0 1.0 (per the Smithsonian Open Access program, FAQ, and the per-item CC0 icon) | "Smithsonian National Museum of Natural History. [Object title]. [Accession number]. CC0." (composition from the EDAN record's `title` + accession number) | **not downloaded** | v4.4 picks a specific NMNH specimen, confirms the CC0 icon, captures the accession number, captures the image URL, downloads the image, writes the local file, updates the source audit manifest. |
| **C-08** (Met CC0 image, Section 3 alternate) | `met-<object_id>.jpg` | <https://www.metmuseum.org/art/collection/search/<object_id>> | not yet (per-item selection is v4.4) | CC0 1.0 (image) — only if both `isPublicDomain: true` in the Collection API **and** Open Access icon on the public object page | "The Metropolitan Museum of Art. [Title]. [Date]. [Credit line]. CC0." | **not downloaded** | v4.4 picks a specific Met object, runs the double-confirmation (`isPublicDomain: true` in the API + OA icon on the public page), captures the image URL, downloads the image, writes the local file, updates the source audit manifest. **If either confirmation is missing, C-08 does not enter the build.** |
| **C-09** (Rijksmuseum CC0 botanical print) | `rijksmuseum-<object_number>.jpg` | <https://www.rijksmuseum.nl/en/rijksstudio> → <https://data.rijksmuseum.nl> → object record | not yet (per-item selection is v4.4) | CC0 1.0 (preferred) or CC BY 4.0 (third-party grant tier) — per the Rijksmuseum's two-tier policy; per-item `licence` field is captured verbatim | "Rijksmuseum. [Object title]. [Creator]. [Date]. [objectNumber]. [CC0 1.0 / CC BY 4.0]." | **not downloaded** | v4.4 picks a specific Rijksmuseum object, captures the `licence` field exactly, captures the `objectNumber` and the `id.rijksmuseum.nl/...` PID, captures the image URL (Rijksstudio image or IIIF Image API URL), downloads the image, writes the local file, updates the source audit manifest. |
| **C-10** (Rijksmuseum IIIF manifest) | `rijksmuseum-<object_number>-iiif.json` (the manifest is JSON, not an image) | <https://data.rijksmuseum.nl/docs/iiif/> → object record → IIIF manifest URL | not yet (per-item selection is v4.4) | Per-item (CC0 1.0 or CC BY 4.0); the IIIF Presentation API manifest's `license` field is the authoritative source | Same as C-09 (per-item `licence` field, recorded from the manifest's `license` field) | **not downloaded** | v4.4 fetches the IIIF Presentation API manifest (read-only), captures the `license` field, captures the IIIF image service URL, optionally downloads the image body, writes the local manifest file (and the image, if downloaded), updates the source audit manifest. The manifest is JSON; the image (if downloaded) is the standard extension. |

**Import status counts.**

- `not downloaded`: **6** (all 6 v4.3 `selected-for-build-planning` rows).
- `wait for v4.4 asset import`: **6** (same rows; "not downloaded" and "wait for v4.4" are the same in this round — v4.3 records the *plan*; v4.4 executes it).
- `replace with project-generated diagram`: **0** in the build set. The Section 1 fallback for C-01, the Section 3 fallback for C-03 / C-08, the Section 4 fallback for C-10, and the v4.1 carry-overs (C-02 BHL Flickr, Section-4 screenshot row) are all `replace with project-generated diagram` *in the build set*; they are recorded as *fallback* in `BUILD_SCOPE_v4.3.md` and are not in the import table.
- `approved`: **0** (not used).

---

## File naming convention

The convention is *suggested* and applies only to the future asset import round. v4.3 does not write any local file.

- **Lowercase.** All filenames are lowercase. Example: `bhl-title123-item456-plate.jpg`, not `BHL-Title123-Item456-Plate.JPG`.
- **Institution prefix.** The first segment is the institution's lowercase short name. Mappings:
  - BHL → `bhl-`
  - Wellcome → `wellcome-`
  - Smithsonian (NMNH or general) → `smithsonian-` (or `smithsonian-nmnh-` if NMNH-specific)
  - Met → `met-`
  - Rijksmuseum → `rijksmuseum-`
  - LoC → `loc-`
- **Short identifier.** The second segment is a short identifier that is stable across renderings. Mappings:
  - BHL: `<title_id>-<item_id>` (e.g., `title123-item456`).
  - Wellcome: `works-<id>` (e.g., `works-a222tqng`).
  - Smithsonian: `<accession_number>` (e.g., `nmnhbotany-1234567`).
  - Met: `<object_id>` (e.g., `45734`).
  - Rijksmuseum: `<object_number>` (e.g., `sk-c-5`).
  - LoC: `<id>` (e.g., `tgm001244` or a per-item ID).
- **No spaces.** Underscores or hyphens only. Hyphens are preferred for readability.
- **Extension preserved from source.** `.jpg` for JPEGs, `.tif` for TIFFs, `.json` for IIIF manifests, `.png` for PNGs. The extension matches the source's MIME type.

**Examples** (illustrative only — v4.3 does not write these files):

- `bhl-title123-item456-plate.jpg` — a BHL Public-domain plate, with title ID `title123` and item ID `item456`.
- `bhl-title789-page012-page.jpg` — a BHL Public-domain book page, with title ID `title789` and page ID `page012`.
- `smithsonian-nmnhbotany-1234567.jpg` — an NMNH herbarium sheet, accession `nmnhbotany-1234567`.
- `met-45734.jpg` — a Met object with `objectID` `45734`.
- `rijksmuseum-sk-c-5.jpg` — a Rijksmuseum object with `objectNumber` `SK-C-5`.
- `rijksmuseum-sk-c-5-iiif.json` — the IIIF Presentation API manifest for the same Rijksmuseum object.

The file names above are *illustrative*, not real. The v4.4 round will produce real filenames based on the per-item selection.

---

## Pre-import action summary

For all 6 rows, the v4.4 pre-import action is the same: **re-open the source URL, re-check the rights statement, pick a specific item that passes the 5 source-acceptance checks, capture the per-item evidence, download the image, write the local file, update the source audit manifest, run the quality gate**.

For the C-03 row, the pre-import action is the same as the others *except* the per-item check must filter on `<Copyright Status> = Public domain` only. The CC BY-NC-SA subset is rejected at the per-item check.

For the C-08 row, the pre-import action is the same as the others *except* the per-item check must run the double-confirmation (Collection API `isPublicDomain: true` + public-page OA icon). If either is missing, the row is rejected and the Section 3 alternate slot is filled by a project-generated diagram.

---

## What v4.3 does *not* do

- v4.3 does not download any image.
- v4.3 does not write any local file.
- v4.3 does not modify `site/`, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`.
- v4.3 does not modify `scripts/template_quality_gate.py`.
- v4.3 does not create a tag or GitHub Release.
- v4.3 does not move or rewrite any pre-existing tag (`v2.0` through `v3.4`) or any pre-existing GitHub Release.
- v4.3 does not process the untracked `.firecrawl/` directory.
- v4.3 does not draw any project-generated diagram. The diagrams are *planned* in `BUILD_SCOPE_v4.3.md` and `CONTENT_DRAFT_BRIEF_v4.3.md`; the actual drawing is a future round.
- v4.3 does not mark any candidate `approved` (the status `approved` is not used in v4.3 or any future round).

The asset import plan is the *plan*; the future asset import round is the *execution*.