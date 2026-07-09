# v4.1 Institution Policy Notes

> Scope: record, per institution, the official rights / terms URL, the open-access / public-domain wording summary, attribution expectations, download / API notes, uncertainties, and the **v4.2 audit question** that v4.2 must answer before any row can leave `candidate` or `needs rights audit` status.
>
> **Important.** v4.1 does not make legal conclusions and does not write absolutes like "safe for commercial use". Every institution's wording is recorded *as written on the institution's own page*, with the source URL. v4.2 must re-verify per item. Where the institution's wording is non-affirmative (e.g., "no known restrictions"), the entry flags the uncertainty explicitly.

---

## Biodiversity Heritage Library

- **Official rights / terms URL.** <https://about.biodiversitylibrary.org/help/copyright-and-reuse/> (linked from the BHL footer and from every volume's "Copyright & Usage" panel).
- **Open access / public domain wording summary (as written).**
  - "Most of these works are journals published by non-profit learned societies or research institutions whose mission is involved with biodiversity."
  - Public-domain determination: "For the United States, publications are in the public domain if they were published 95 years prior to the current year: Public Domain = Current Year – 95."
  - "BHL does not claim copyright on its digitized works." If the original works are in the public domain, so too are the digital files.
  - "BHL makes its metadata available for public use under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication."
  - In-copyright subset: "Almost always a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license."
- **Attribution expectation (as written).** "Image from the Biodiversity Heritage Library. Contributed by [Holding Institution]. | www.biodiversitylibrary.org" — recommended but not strictly required for public-domain items.
- **Download / API note.** Per-volume download, per-article PDF, per-page image (JPEG2000). OAI-PMH and JSON APIs available. Download URLs are returned by the public pages; no API key is required for public-domain items.
- **Uncertainty.**
  - The US public-domain cutoff uses a 95-year moving wall — items published in the last 95 years are *not* automatically public domain; per-item `<Copyright Status>` is the only safe check.
  - BHL notes: "Works that may be in the public domain under United States law may not be in the public domain under the laws of other countries." v4.2 must keep this in mind if the exhibition's distribution extends beyond the US.
- **v4.2 audit question.** For each candidate item, confirm: (a) the `<Copyright Status>` field reads "Public domain" or "No known copyright"; (b) if "In copyright", the explicit `<License Type>` is recorded verbatim; (c) the `<Holding Institution>` and `<Rights Holder>` fields are captured for the credit line; (d) if CC BY-NC-SA 4.0, the v4.2 audit must check whether the v4.3 distribution channel is compatible with the NC + SA clauses — if not, the row is `excluded`.

---

## Wellcome Collection

- **Official rights / terms URL.** Site-wide notice in the footer of every page: <https://wellcomecollection.org/> (footer text). Research access framework: <https://wellcomecollection.org/research-access-to-our-collections>. IIIF API docs: <https://developers.wellcomecollection.org/api/iiif>.
- **Open access / public domain wording summary (as written).**
  - "Except where otherwise noted, content on this site is licensed under a Creative Commons Attribution 4.0 International Licence."
  - "We do not seek to apply fresh copyright to our digitisations of previously out-of-copyright works and encourage copyright owners also to share their content and intellectual property via Creative Commons licences."
  - "Some open material online is additionally classed as Open with Advisory — can be viewed following a click-through advisory warning."
- **Attribution expectation (as written).** CC BY 4.0 requires attribution. The site does not prescribe a single attribution string; per-item attribution is composed by the reuser.
- **Download / API note.** IIIF Image API (Image API 3.0) is publicly available for open image collections. Catalogue API exposes works, identifiers, and licence. No API key is required for the open image subset.
- **Uncertainty.**
  - "Except where otherwise noted" is *non-exhaustive*: per-item licence may differ from the site-wide CC BY 4.0 default. The audit must check the per-item page, not just the footer.
  - Wellcome's digitisation of *previously out-of-copyright* works does not assert a new copyright — this is the museum's stated policy, but it is a *position* that v4.2 should still verify by reading each item's own licence field.
- **v4.2 audit question.** For each candidate item, confirm: (a) the per-item page shows a CC BY 4.0 marker or "no known copyright restrictions"; (b) the IIIF info.json or Catalogue API record exposes the licence field; (c) the credit line is composable from Wellcome's name + the item's title + the licence string.

---

## Smithsonian Open Access

- **Official rights / terms URL.** <https://www.si.edu/openaccess/faq> (the FAQ is the most complete statement). Program landing page: <https://www.si.edu/openaccess>. Developer tools: <https://www.si.edu/openaccess/devtools>.
- **Open access / public domain wording summary (as written).**
  - "We have released these images and data into the public domain as Creative Commons Zero (CC0), meaning you can use, transform, and share our open access assets without asking permission from the Smithsonian."
  - "Open Access items carry what's called a CC0 designation."
  - "If an item is not designated as CC0, it is subject to usage conditions."
- **Attribution expectation (as written).** CC0 items do not require attribution; the FAQ recommends a "minimal" caption of **title, author, source, license, and source URL** for citation purposes (not for legal compliance).
- **Download / API note.** Public API at <https://edan.si.edu/openaccess/apidocs/> (API key required for some endpoints). GitHub data dump at <https://github.com/Smithsonian/OpenAccess> (no key). NMNH DarwinCore via IPT. IIIF manifests available.
- **Uncertainty.**
  - The Smithsonian's program is *binary* (CC0 or not-CC0), but the underlying work's *third-party* rights may still apply — the FAQ explicitly states: "you are responsible for obtaining any third-party permissions that may be required for your use." v4.2 cannot take the CC0 marking as a complete shield against third-party claims.
  - Not all Smithsonian units have digitised everything; missing items are not the same as restricted items. The FAQ explains the exclusion categories (under copyright, contractual restrictions, culturally sensitive, etc.).
- **v4.2 audit question.** For each candidate item, confirm: (a) the CC0 icon is visible on the item page; (b) the accession number is captured; (c) the third-party rights surface (e.g., donor restrictions, culturally sensitive content) is noted, even if the CC0 marking is present.

---

## The Met Open Access

- **Official rights / terms URL.** Dataset license: <https://github.com/metmuseum/openaccess/blob/master/LICENSE> (CC0 1.0). Dataset README: <https://github.com/metmuseum/openaccess/blob/master/README.md>. Image policy: <https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources>.
- **Open access / public domain wording summary (as written).**
  - "The Metropolitan Museum of Art provides select datasets of information on more than 470,000 artworks in its Collection for unrestricted commercial and noncommercial use. … The Metropolitan Museum of Art has waived all copyright and related or neighboring rights to this dataset using Creative Commons Zero."
  - "Images are not included and are not part of the dataset. Companion artworks listed in the dataset covered by the policy are identified in the Collection section of the Museum's website with the Creative Commons Zero (CC0) icon."
  - "At this time, the datasets are available in CSV format."
- **Attribution expectation (as written).** The dataset README: "Please consider attributing or citing The Metropolitan Museum of Art's CC0 select datasets, especially with respect to research or publication." (Consideration, not legal requirement, because the dataset is CC0.)
- **Download / API note.** `MetObjects.csv` is a large UTF-8 file (stored via Git LFS). The CSV is the canonical dataset; the *image* lives on the public site (or, for higher resolution, on Wikimedia Commons via the Met's donation program). Collection search at <https://www.metmuseum.org/art/collection/search>.
- **Uncertainty.**
  - The **dataset** and the **image** are licensed differently. The dataset is CC0 for *all* ~470,000 objects; the image is CC0 only for objects where the public page shows the CC0 icon. A row's `Is Public Domain` flag is the *dataset's* flag, not necessarily the *image's* status. v4.2 must cross-check.
  - "The Met" is also used as a search-result collision with MET Group (an energy company) and with other "Met" institutions. URLs must be the `metmuseum.org` / `github.com/metmuseum` canonical forms.
- **v4.2 audit question.** For each candidate row, confirm: (a) `Is Public Public Domain` is `True` in the CSV; (b) the public object page shows the CC0 icon; (c) the object URL captured from the CSV resolves to the same object page; (d) the Met's recommended attribution is recorded even though CC0 does not require it.

---

## Rijksmuseum

- **Official rights / terms URL.** Information and Data Policy (English, full): <https://data.rijksmuseum.nl/policy/information-and-data-policy>. Policy summary: <https://data.rijksmuseum.nl/policy>. IIIF tutorial: <https://data.rijksmuseum.nl/tutorials/iiif/>.
- **Open access / public domain wording summary (as written).**
  - "The Rijksmuseum has made all photos (in all variants, from high resolution to thumbnail) available of collection objects that are no longer subject to copyright as public property."
  - "The museum also does not claim copyright on associated metadata to these collection objects."
  - "If the Information and Data are protected by copyright and this copyright belongs to a third party who has stated in writing to the Rijksmuseum that the Rijksmuseum may publish and reproduce the Information and Data without restrictions and attribution and may sublicense this right, the Rijksmuseum will provide this Information and Data with a Creative Commons Zero 1.0 (CC0 1.0) licence."
  - "If the Information and Data are protected by copyright and this copyright belongs to a third party without that party having stated that it does not wish to exercise this right, the Rijksmuseum will not make this Information and Data available as open data."
- **Attribution expectation (as written).** "We kindly ask that when using our information and data, you credit the Rijksmuseum (and, where possible, our staff) as the original creator, even if this is not required." (Request, not legal requirement, for CC0 items.) For CC BY 4.0 items, attribution is a legal requirement.
- **Download / API note.** IIIF Image API 3.0, IIIF Presentation API 3.0, IIIF Change Discovery API 1.0 — all three are publicly documented and usable. The legacy Rijksstudio API requires an API key (different from the IIIF endpoints). The full IIIF tutorial walks through the object-record → VisualItem → DigitalObject chain to obtain the IIIF image identifier.
- **Uncertainty.**
  - The policy is two-tier (CC0 or CC BY 4.0), but a third tier — in-copyright with no third-party grant — is *not* released. v4.2 should not encounter this third tier in the data services portal; if it does, the row is `excluded`.
  - Rijksmuseum's policy is published under CC BY 4.0 itself; the policy document's licence is *not* the same as the licence of the data the museum publishes. v4.2 should not conflate the two.
- **v4.2 audit question.** For each candidate item, confirm: (a) the licence field on the object record is `CC0 1.0` or `CC BY 4.0` (no other values are in the data services portal); (b) the IIIF manifest URL resolves and contains the same licence; (c) the credit line includes "Rijksmuseum" and, if the licence is CC BY 4.0, an explicit attribution string.

---

## Library of Congress

- **Official rights / terms URL.** **Per collection**, not per institution. Example: <https://www.loc.gov/collections/single-sheet-maps-title-collection/about-this-collection/rights-and-access>. General entry point: <https://www.loc.gov/collections/> and <https://www.loc.gov/pictures/>.
- **Open access / public domain wording summary (as written, per-collection examples).**
  - Geography & Map Division: "The folder exteriors depicted in this collection were created by the Geography and Map Division, Library of Congress. They are U.S. government works not subject to copyright in the United States and have no known copyright restrictions."
  - National Screening Room: "The Library of Congress is not aware of any U.S. copyright or other restrictions in the vast majority of motion pictures in these collections. Absent any such restrictions, these materials are free to use and reuse."
  - Web Archives: "The Library of Congress is making its Web Archives Collection available for educational and research purposes. The Library has obtained permission for the use of many materials in the Collection, and presents additional materials for educational and research purposes in accordance with fair use."
- **Attribution expectation (as written).** Per-collection: "Credit Line: Library of Congress, [Division Name]." Citation format per Citing Primary Sources: <https://www.loc.gov/teachers/usingprimarysources/citing.html>.
- **Download / API note.** Per-item record pages expose thumbnails, medium-resolution images, and (for some collections) high-resolution TIFFs. JSON-LD per-item records available via the persistent URL with `.json` suffix (e.g., <https://www.loc.gov/item/<id>/.json>).
- **Uncertainty.**
  - The LoC's rights wording is **collection-specific**. There is no single "Library of Congress open access" license equivalent to the Met's CC0 or the Smithsonian's CC0. v4.2 *must* check the collection's "Rights & Access" page, not assume.
  - "U.S. government works not subject to copyright" applies to works prepared by LoC staff in their official duties; many LoC holdings are *not* U.S. government works and have separate rights status.
  - "No known copyright restrictions" is *non-affirmative*: it states that the LoC is unaware of restrictions, not that no restrictions exist. v4.2 must record the exact wording.
- **v4.2 audit question.** For each candidate item, confirm: (a) the **collection's** "Rights & Access" page was consulted; (b) the **item's** persistent URL was visited; (c) the exact rights wording was copied verbatim into the asset's metadata row; (d) if the rights wording is "U.S. government work", the credit line is "Library of Congress, [Division]"; (e) if the wording is "no known restrictions", the credit line includes that phrase and the credit string is composed carefully (because the non-affirmative wording does not constitute a clearance).

---

## Round-level uncertainty (applies to all institutions)

1. **Licence changes.** Institution policies may change between v4.1 and v4.4. v4.2 must re-fetch each cited URL on the day of audit, not rely on a copy-paste from this document.
2. **Per-item over institution-level.** A row's risk may be lower or higher than the institution-level default. v4.2 must check the per-item page, not the institution's landing page.
3. **Distribution channel.** This project distributes the rendered output openly on GitHub Pages. Any candidate whose licence restricts commercial use, derivative use, or share-alike is *not automatically* excluded, but v4.2 must record the licence terms and check compatibility with the distribution channel.
4. **Reuse guidance, not legal advice.** v4.1 records what each institution says; v4.2 captures what each item carries. Neither is a legal conclusion. Any final clearance before deployment is a separate step (not in v4.0–v4.4).