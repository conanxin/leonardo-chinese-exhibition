# v4.1 Source Candidates

> Scope of this document: enumerate the candidate source institutions, collections, and asset *types* (not actual assets) for the second real exhibition, *before* any download. Companion to `docs/SECOND_EXHIBITION_SOURCE_SCOPE_v4.0.md` and `docs/SECOND_EXHIBITION_RIGHTS_RISK_REGISTER_v4.0.md`.

---

## Baseline

| Field | Value |
|---|---|
| Current HEAD | `a24379261d3bd2acb83c1e95ad89edf96bdedb4d` |
| Source release | `v3.4-real-second-exhibition-hardening` |
| Source tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| v3.4 tag object | `2d186a892af0e1ab41c1d9b8a055842e01339cb6` |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size (baseline) | 92,976 B |
| Quality gate | `scripts/template_quality_gate.py` → 37/37 PASS |
| Exhibition direction | 《植物图谱与视觉分类：从自然史图像到知识秩序》 |
| Working title | 《植物图谱与视觉分类：从自然史图像到知识秩序》 |
| Sections (from v4.0 outline) | 1. 观察 / 2. 分类 / 3. 复制 / 4. 再组织 |

---

## Research method

This round is **research only**. Specifically:

1. **Official pages first.** For each candidate institution, the rights / terms / policy page is fetched and recorded, *not* inferred from a search summary.
2. **No image download.** No image is downloaded to the repository. No image is added to `assets/`. No image is replaced on the live site.
3. **No approval.** No candidate is marked `approved`. Allowed statuses are `candidate`, `needs rights audit`, `excluded`.
4. **URLs are revisable.** Every entry in this document includes the source page URL so that v4.2 can re-derive the candidate's evidence from the same starting point.
5. **No "I remember seeing X".** Candidates are recorded only because the page was actually fetched (or, where fetch failed, because the page is at a known, named official URL and the failure is logged for v4.2 follow-up).
6. **No legal conclusions.** v4.1 does not assert that any candidate is "safe for commercial use". It only records what each institution's own page says about its open data, then defers to v4.2 audit.

---

## v4.1 non-goals

v4.1 does **not**:

- Download any image.
- Add any image file to the repository.
- Replace any image on the live site.
- Modify `site/index.html`, `site/style.css`, `site/script.js`.
- Modify `_template/site/`, `_template/data/`, `_pilots/second-exhibition-pilot/`.
- Modify `posts/`, `case-study/`, `release-assets/`.
- Modify `scripts/template_quality_gate.py`.
- Mark any candidate `approved` (this status is **not used** in v4.1).
- Create a tag, GitHub Release, or live deployment.
- Move or rewrite any pre-existing tag (`v2.0` … `v3.4`) or pre-existing GitHub Release.

---

## Institution summaries

The six institutions below are the v4.1 candidate set. Each section is **a research summary**, not an asset approval.

### Biodiversity Heritage Library

- **Candidate collection / search entry.** BHL aggregate corpus of biodiversity literature (~64M pages, 200k+ titles). Public-domain / openly-licensed natural-history books and journals, including extensive botanical illustration plates. Entry points:
  - Main portal: <https://www.biodiversitylibrary.org/>
  - Advanced search: <https://www.biodiversitylibrary.org/advsearch>
  - Flickr photostream (300,000+ illustrations, public-domain-where-applicable): <https://www.flickr.com/photos/biodivlibrary/albums>
- **Candidate asset type.** Pre-1928 botanical plates and book pages (hand-colored engravings, lithographs, watercolors) sourced from BHL-contributed volumes.
- **Rights / terms URL.** <https://about.biodiversitylibrary.org/help/copyright-and-reuse/>
- **Metadata availability.** Per-item metadata fields: `<Copyright Status>`, `<Holding Institution>`, `<License Type>`, `<Rights Holder>`, accessible from each volume's "Show Info" tab and "Title pages" panel. BHL's *metadata* (not the digitized files) is published under **CC0 1.0**.
- **Risk level.** **Low** for items whose `<Copyright Status>` is `Public domain` or `No known copyright`. **Medium** for items whose `<Copyright Status>` is `In copyright` (most are CC BY-NC-SA 4.0 — non-commercial, share-alike). **High** for items where the rights holder has not been located and `<Copyright Status>` is unstated.
- **Recommended use.** Prefer `<Copyright Status> = Public domain` items for v4.3 build. CC BY-NC-SA items are usable *only* if the exhibition's distribution channel matches the license terms (this project's rendered output is openly distributed, so CC BY-NC-SA is incompatible without scope review). Always copy the exact `<Copyright Status>` and `<License Type>` strings into the asset's metadata row at v4.2.

### Wellcome Collection

- **Candidate collection / search entry.** Catalogue "Works search" — over 1.17M works, including 25k+ Digital Images, 76k+ Pictures, 14k+ Engravings and Engravings, 12k+ Lithographs. Entry point: <https://wellcomecollection.org/works>. The image subset exposed via IIIF is at <https://developers.wellcomecollection.org/api/iiif>.
- **Candidate asset type.** Historical medical / botanical engravings, lithographs, watercolors, and digitized book pages from the Wellcome digital image subset.
- **Rights / terms URL.** Wellcome's general site notice (footer of every page): content licensed under **CC BY 4.0** "except where otherwise noted". Research access framework: <https://wellcomecollection.org/research-access-to-our-collections>.
- **Metadata availability.** IIIF Image API exposes a manifest for each open image; Catalogue API exposes title, creator, date, identifiers, and licence field. Per-item licence must be checked because "except where otherwise noted" allows individual items to be marked differently.
- **Risk level.** **Low** for items with explicit CC BY 4.0 marking. **Medium** if a specific item is *not* marked CC BY 4.0 — the fallback is unclear and v4.2 must re-confirm. The institution's overall site policy is CC BY 4.0, but **per-item verification is mandatory** in v4.2.
- **Recommended use.** Use IIIF Image API to construct the image URL without downloading the file locally. Attribution is required (CC BY 4.0). v4.2 must capture the exact licence string per asset.

### Smithsonian Open Access

- **Candidate collection / search entry.** Smithsonian Open Access portal — ~5.1M 2D and 3D items, including National Museum of Natural History (NMNH) botanical / herbarium-related holdings. Entry point: <https://www.si.edu/openaccess>. Search: <https://www.si.edu/search/images?edan_fq[0]=media_usage%3ACC0>. API: <https://edan.si.edu/openaccess/apidocs/>. GitHub data dump: <https://github.com/Smithsonian/OpenAccess>.
- **Candidate asset type.** Public-domain images of specimens, herbarium sheets, and field-book illustrations, especially from NMNH. Also: 3D models and structured metadata via DarwinCore.
- **Rights / terms URL.** <https://www.si.edu/openaccess/faq> (the official FAQ is the most complete statement). Policy: items designated CC0 may be used for any purpose, including commercial, without Smithsonian permission. Items *not* marked CC0 require a written request to <rightsmanager@si.edu>.
- **Metadata availability.** Per-item CC0 icon on the public page; per-item metadata via the public API; per-item DarwinCore records via NMNH IPT. Each item has a Smithsonian accession number and a CC0 marker.
- **Risk level.** **Low** for items marked CC0 (most are). **Medium** for items with "usage conditions apply" — requires case-by-case re-evaluation. The institutional policy is **strictly binary**: CC0 or not-CC0. There is no in-between licence family in the Smithsonian Open Access program.
- **Recommended use.** Look for items that *carry* the CC0 icon and have an associated Smithsonian accession number. The DarwinCore dump from NMNH is the most useful starting point for botanical / herbarium assets.

### The Met Open Access

- **Candidate collection / search entry.** Met Open Access — ~470,000+ artworks in the dataset (CC0 CSV), with a smaller subset where *images* (not just data) are CC0 and downloadable. Entry point: <https://www.metmuseum.org/art/collection/search> and the Open Access dataset at <https://github.com/metmuseum/openaccess>. Image Resources policy: <https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources>.
- **Candidate asset type.** Botanical / natural-history artworks held by the Met (paintings, prints, drawings), if any match. Note: the Met's botanical holdings are *not* a primary collection strength — a v4.2 audit may find the corpus small for this theme. The CSV is the best starting point to confirm.
- **Rights / terms URL.** <https://github.com/metmuseum/openaccess/blob/master/LICENSE> (CC0 1.0 for the dataset). The README states: *"The Metropolitan Museum of Art provides select datasets of information on more than 470,000 artworks in its Collection for unrestricted commercial and noncommercial use. … has waived all copyright and related or neighboring rights to this dataset using Creative Commons Zero."* Note the **dataset** is CC0; the *images* on the public site are CC0 only if the object page shows the CC0 icon.
- **Metadata availability.** `MetObjects.csv` (UTF-8, large file) contains all ~470k object rows; columns include title, artist, date, medium, classification, object URL, image URL, and a `Is Public Domain` field. Per-object page on `metmuseum.org` shows the CC0 icon when applicable.
- **Risk level.** **Low** for items where the object page shows the CC0 icon and the CSV row's `Is Public Domain` field is `True`. **High** for items where the dataset is CC0 but the *image* is not — the dataset and the image have different licences, and a careless use of the CSV would conflate the two.
- **Recommended use.** Search `MetObjects.csv` for `Classification` containing botanical / natural-history / print. Cross-check each candidate's `Is Public Domain` field and the public object's CC0 icon before promoting to v4.2. The Met is a secondary source for this theme; treat it as such.

### Rijksmuseum

- **Candidate collection / search entry.** Rijksstudio + the Open Data Services portal. Botanical / natural-history prints and drawings held by the Rijksmuseum (Rijksprentenkabinet). Entry point: <https://www.rijksmuseum.nl/en/rijksstudio>. Data services portal: <https://data.rijksmuseum.nl>. IIIF tutorial: <https://data.rijksmuseum.nl/tutorials/iiif/>. Object search API via the data services portal.
- **Candidate asset type.** Botanical prints, drawings, and illustrated book pages whose copyright has expired (Rijksmuseum has, since 2011/12, made all *non-copyright* images and their associated metadata publicly available). Also: object-level IIIF manifests exposing full image + metadata.
- **Rights / terms URL.** <https://data.rijksmuseum.nl/policy/information-and-data-policy> (full English text). The policy operates with two licence families: **CC0 1.0** for objects no longer in copyright and for metadata; **CC BY 4.0** for objects where a third-party rights holder has granted the museum a written, unrestricted licence. Other in-copyright objects are *not* made available as open data.
- **Metadata availability.** Object-level API exposes title, creator, date, materials, dimensions, identifiers, and licence. IIIF Image API and IIIF Presentation API both available. IIIF Change Discovery API supports bulk discovery.
- **Risk level.** **Low** for items with explicit CC0 1.0 (most older prints and drawings). **Low–Medium** for items with explicit CC BY 4.0 (use is permitted, attribution required). The Rijksmuseum policy is well-documented; v4.2 can rely on the institution's own licence field.
- **Recommended use.** Start from the data services portal and use IIIF Image API to construct image URLs without downloading. Capture both the licence field and the IIIF manifest URL into the asset's metadata row at v4.2. Attribution required for CC BY 4.0.

### Library of Congress

- **Candidate collection / search entry.** Library of Congress Digital Collections (<https://www.loc.gov/collections/>) and the Prints & Photographs Online Catalog (<https://www.loc.gov/pictures/>). Botanical illustration is a subject heading in the P&P Thesaurus For Graphic Materials (<https://www.loc.gov/pictures/item/tgm001244/>). Specific relevant collections include historic illustrated books and the "Cabinet of American Illustration".
- **Candidate asset type.** 19th- and early-20th-century botanical illustrations, lithographs, and book pages, especially those produced as U.S. government works (which are public domain under 17 U.S.C. § 105) or those whose copyright has expired.
- **Rights / terms URL.** Per-collection "Rights & Access" page, e.g. <https://www.loc.gov/collections/single-sheet-maps-title-collection/about-this-collection/rights-and-access>. The general pattern is: "U.S. government works not subject to copyright in the United States and have no known copyright restrictions" (Geography & Map Division) or "no known copyright or other restrictions" (Motion Picture / other divisions). No single global LoC rights URL — **each collection has its own page**.
- **Metadata availability.** Per-item record exposes title, creator, date, call number, repository, and rights statement. Persistent URLs of the form `https://www.loc.gov/item/<id>/` for item pages and `https://www.loc.gov/pictures/item/<id>/` for P&P items.
- **Risk level.** **Low** for items explicitly marked as U.S. government works (federal employee, official duties) or in the public domain. **Medium** for items from donations where the rights statement is "no known copyright restrictions" — the language is *non-affirmative* and v4.2 should record the exact wording. **High** for items that have not yet had their rights page consulted.
- **Recommended use.** Treat each candidate as needing a **per-collection** rights confirmation, not a per-institution one. Always visit the collection's "About this Collection" → "Rights & Access" page first, then the item page. Use the LoC's persistent URLs as identifiers.

---

## Shortlist

The following 10 candidate directions are **candidates, not approved assets**. They are organized as: institution → candidate collection / item → asset type → why relevant → risk level → next step. At least one row per institution; the BHL and Smithsonian NMNH rows are repeated in multiple shapes because botanical / herbarium assets are the most natural fit for this theme.

| # | Institution | Collection / search URL | Candidate asset type | Why relevant | Risk level | Next step |
|---|---|---|---|---|---|---|
| 1 | **BHL** | <https://www.biodiversitylibrary.org/advsearch> (filter to Public domain + botanical subject) | Pre-1928 hand-colored botanical plate from a BHL-contributed volume | Fits section 1 (观察) and section 3 (复制) — observation and reproduction | Low (Public domain subset) | v4.2 — locate one specific item, record `<Copyright Status>` / `<Holding Institution>` / `<License Type>` |
| 2 | **BHL** | <https://www.flickr.com/photos/biodivlibrary/albums> | High-resolution botanical illustration (Flickr photostream subset) | Fits section 1 (观察) and section 3 (复制) — but Flickr is a third-party platform — add a `platform screenshot` caveat | Medium (platform screenshot ambiguity, even when underlying image is PD) | v4.2 — locate one specific item, prefer the BHL item page over the Flickr image URL |
| 3 | **Wellcome** | <https://wellcomecollection.org/works> (filter to Engravings and Engravings / Lithographs) | Historical botanical engraving from Wellcome's digitised image subset | Fits section 1 (观察) — engraving as a deliberate selection of features | Low (with per-item CC BY 4.0 confirmation) | v4.2 — locate one specific item, confirm CC BY 4.0 marking on the item page, capture IIIF image URL |
| 4 | **Wellcome** | <https://developers.wellcomecollection.org/api/iiif> (IIIF Image API) | IIIF manifest of a botanical print or drawing | Fits section 4 (再组织) — IIIF as a re-linking layer | Low–Medium (depends on item-level licence) | v4.2 — use API to verify the manifest's rights field; do not download |
| 5 | **Smithsonian Open Access (NMNH)** | <https://www.si.edu/search/images?edan_fq[0]=media_usage%3ACC0> + filter to NMNH | Herbarium sheet photograph (NMNH specimen) | Fits section 2 (分类) — specimen + label as a unit of classification | Low (CC0 marking required) | v4.2 — locate one specific NMNH specimen record, confirm CC0 icon and accession number |
| 6 | **Smithsonian Open Access (general)** | <https://github.com/Smithsonian/OpenAccess> (data dump) | Structured metadata row pointing to a CC0 botanical illustration | Fits section 4 (再组织) — structured data as a re-linking layer | Low (for the metadata), Medium (for the image — depends on the underlying item) | v4.2 — locate one specific item via the data dump, follow the link to confirm CC0 |
| 7 | **The Met Open Access** | <https://github.com/metmuseum/openaccess> (`MetObjects.csv`, filter Classification ~ botanical / natural-history / print) | Met object CSV row pointing to a CC0 botanical print / drawing / painting | Fits section 3 (复制) — print / engraving as a reproducible medium | Low (if `Is Public Domain = True` AND the public object page shows CC0 icon) | v4.2 — search the CSV, cross-check `Is Public Domain` field and the public object page |
| 8 | **Rijksmuseum** | <https://data.rijksmuseum.nl> (Rijksstudio + IIIF APIs) | Rijksprentenkabinet botanical print or drawing with CC0 marking | Fits section 1 (观察) and section 2 (分类) — Dutch Golden Age botanical illustration is a strong source family | Low (CC0) or Low–Medium (CC BY 4.0) | v4.2 — locate one specific object via the data services portal, capture licence field and IIIF manifest URL |
| 9 | **Rijksmuseum** | <https://data.rijksmuseum.nl/tutorials/iiif/> (IIIF Image API + Presentation API) | IIIF manifest of a botanical print | Fits section 4 (再组织) — IIIF as a re-linking layer | Low (depends on item) | v4.2 — use the IIIF APIs to confirm the licence and the image service URL; do not download |
| 10 | **Library of Congress** | <https://www.loc.gov/pictures/item/tgm001244/> (Botanical illustrations subject heading) | 19th-century American botanical illustration (e.g., from the Cabinet of American Illustration) | Fits section 1 (观察) and section 3 (复制) — American 19th-century botanical print tradition | Low (if U.S. government work) or Medium ("no known copyright restrictions") | v4.2 — locate one specific item, follow the collection's "Rights & Access" page, capture the exact rights statement |
| 11 | **Library of Congress** | <https://www.loc.gov/collections/> (specific illustrated-book collection) | Digitized book page from an early illustrated natural-history volume | Fits section 3 (复制) — book page as a published context | Low–Medium (depends on collection) | v4.2 — pick one specific collection, fetch its "Rights & Access" page, confirm the rights wording |
| 12 | **Library of Congress** | <https://www.loc.gov/pictures/> (Prints & Photographs Online Catalog) | Prints & Photographs botanical illustration record | Fits section 1 (观察) and section 2 (分类) — single-image record as a unit of classification | Low–Medium (per-record verification) | v4.2 — pick one specific P&P item, confirm the per-record rights statement |

10–12 candidate directions, ≥ 1 row per institution, all in status **candidate** (no approval). Section axes match the v4.0 outline (`观察` / `分类` / `复制` / `再组织`).

---

## Round-1 risk distribution (initial)

- **Low** risk candidates (4): #1 BHL Public-domain, #5 Smithsonian NMNH CC0, #7 Met CC0 (if both fields confirm), #8 Rijksmuseum CC0.
- **Low–Medium** risk candidates (4): #4 Wellcome IIIF, #6 Smithsonian data dump, #9 Rijksmuseum IIIF, #10 LoC P&P botanical illustrations.
- **Medium** risk candidates (3): #2 BHL Flickr, #3 Wellcome (per-item), #11 LoC illustrated book (depends on collection).
- **Medium / per-collection** risk candidates (1): #12 LoC Prints & Photographs (per-record).

Every row above enters v4.2 with status `candidate`. No row in this round is promoted to `approved`. No row is `excluded` either — exclusion requires a specific reason in v4.2 (e.g., a rights statement that is impossible to verify, or a platform-screenshot-only entry with no underlying image rights).