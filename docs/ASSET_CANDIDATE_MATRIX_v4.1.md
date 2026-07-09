# v4.1 Asset Candidate Matrix

> Scope: align the v4.1 candidate set with the v4.0 content outline's 4 sections. Each section lists 2–3 candidate asset *types*, with possible source institutions, source / search URLs, rights risk, why it fits the section, and whether a project-generated diagram may replace the real image if the audit fails.
>
> Important: this is a **matrix**, not an approval. No row here is `approved`. The matrix is the bridge between the institution-level research (`SOURCE_CANDIDATES_v4.1.md`) and the v4.2 per-item audit.

---

## Section 1 — 观察：图像如何抓住植物特征

**Section purpose.** A botanical illustration is a *decision* — what the illustrator chose to look at, and what they chose to leave out.

| Asset type | Possible source institutions | Source / search URL | Rights risk | Why it fits | Project-generated diagram may replace? |
|---|---|---|---|---|---|
| **Pre-1928 hand-colored botanical plate** (engraving / lithograph) | BHL, Wellcome, Rijksmuseum, LoC | BHL: <https://www.biodiversitylibrary.org/advsearch> · Wellcome: <https://wellcomecollection.org/works> · Rijksmuseum: <https://data.rijksmuseum.nl> · LoC P&P: <https://www.loc.gov/pictures/> | Low (if BHL `<Copyright Status> = Public domain`; Wellcome CC BY 4.0 per item; Rijksmuseum CC0; LoC depends on collection) | A plate is the canonical "观察" artifact — the engraver's selection of which features to depict is the section's argument. | Yes (project-generated diagram may replace *if* the audit cannot clear the real plate) — but the diagram is a *lesson*, not a substitute, and must be clearly labelled as project-generated. |
| **Field sketch or watercolor** (pre-photographic, pre-1928) | BHL, Wellcome, Smithsonian (NMNH) | BHL Flickr: <https://www.flickr.com/photos/biodivlibrary/albums> · NMNH search: <https://www.si.edu/search/images?edan_fq[0]=media_usage%3ACC0> | Medium (Flickr platform-screenshot ambiguity; NMNH CC0 if marked) | A field sketch shows the *act* of selection more visibly than a finished plate. | Yes (project-generated comparison diagram of "sketch vs. plate" can substitute if needed). |
| **High-resolution specimen illustration** (a single plant, multiple views) | BHL, Smithsonian (NMNH herbarium), Rijksmuseum | Same as above | Low–Medium (depends on item) | Multiple views on one plate = the "抓住特征" argument in visual form. | Yes (project-generated multi-view diagram may replace if needed). |

**Section 1 summary.** The natural source set is BHL + Rijksmuseum (low-risk), with Wellcome + NMNH as supplementary. Flickr-resolved BHL items carry a Medium risk that v4.2 must re-verify before the row is `verified`.

---

## Section 2 — 分类：图像如何服务命名与秩序

**Section purpose.** A botanical illustration becomes part of a taxonomic system — a binomial name, a family, an order. The image as a *node* in a naming system.

| Asset type | Possible source institutions | Source / search URL | Rights risk | Why it fits | Project-generated diagram may replace? |
|---|---|---|---|---|---|
| **Herbarium sheet photograph** (specimen + printed/handwritten label) | Smithsonian (NMNH), BHL | NMNH: <https://www.si.edu/search/images?edan_fq[0]=media_usage%3ACC0> · BHL: <https://www.biodiversitylibrary.org/advsearch> | Low (NMNH CC0 if marked; BHL Public domain if marked) | A specimen sheet is *the* unit of botanical classification — name + specimen + image together. | Partially (a project-generated comparison diagram of "label anatomy" can stand in for the sheet itself, but the section's argument is *weakened* without a real sheet). |
| **Plate annotated with binomial or taxonomic family** | BHL, Wellcome, Rijksmuseum | Same as section 1 | Low (depends on item) | The plate as it appears in a published taxonomic work — the visual unit that supports a name. | Yes (a project-generated diagram of "which features of the plate support the binomial" can substitute). |
| **Project-generated comparison diagram** (two related species, side-by-side, with the diagnostic features labelled) | Project-generated | n/a | None (the project owns it) | A clean, controlled comparison of the *visual features* that distinguish one species from a related one. **This is the most important diagram of the section.** | n/a (it *is* a project-generated diagram). |

**Section 2 summary.** The natural source set is NMNH (strong on herbarium sheets) + BHL (strong on historical taxonomic works). The project-generated comparison diagram is essential to the section's argument and does not depend on external rights.

---

## Section 3 — 复制：书籍、版画与数字化如何改变传播

**Section purpose.** The same image is multiplied — engraved, lithographed, photographed, scanned, digitized — and each medium changes what the image can do.

| Asset type | Possible source institutions | Source / search URL | Rights risk | Why it fits | Project-generated diagram may replace? |
|---|---|---|---|---|---|
| **Digitized book page** (a plate in its published context) | BHL, Wellcome, LoC (specific illustrated-book collections) | BHL: <https://www.biodiversitylibrary.org/advsearch> · Wellcome: <https://wellcomecollection.org/works> · LoC: <https://www.loc.gov/collections/> | Low (BHL Public domain; Wellcome per-item CC BY 4.0; LoC per-collection) | A book page shows the plate as it was *meant* to be read — with surrounding text, scale, and binding context. | Partially (a project-generated diagram of "page anatomy" can substitute, but loses the citation chain). |
| **Two editions of the same plate** (e.g., a 1750 engraving and a 1900 photographic reproduction) | BHL, Wellcome, Rijksmuseum, LoC | Same as section 1 | Medium (depends on whether the 1900 reproduction is in copyright — often yes, especially if the photographer is identifiable) | Two editions make the "复制" argument visible — what changes when a plate is re-produced. | Partially (a project-generated comparison of the two editions can substitute, with clear labelling). |
| **Project-generated "reproduction chain" diagram** (engraving → lithograph → photograph → scan → digital) | Project-generated | n/a | None (the project owns it) | The section's argument is *about* the chain — a diagram is the natural form. | n/a (it *is* a project-generated diagram). |

**Section 3 summary.** The "two editions" row is the most rights-sensitive — a 1900 photographic reproduction may carry a photographer's copyright that does not exist on the 1750 engraving. v4.2 must check the *reproduction's* rights separately from the *original's* rights. The reproduction-chain diagram is essential and project-owned.

---

## Section 4 — 再组织：数字馆藏如何让图像重新连接

**Section purpose.** A digital collection re-links images that the printed book separated. The same image gains new neighbours when the catalog gains new fields.

| Asset type | Possible source institutions | Source / search URL | Rights risk | Why it fits | Project-generated diagram may replace? |
|---|---|---|---|---|---|
| **IIIF manifest of a botanical print** (Wellcome / Rijksmuseum) | Wellcome, Rijksmuseum | Wellcome IIIF: <https://developers.wellcomecollection.org/api/iiif> · Rijksmuseum IIIF: <https://data.rijksmuseum.nl/tutorials/iiif/> | Low (per item; IIIF info.json exposes the licence) | A IIIF manifest is the canonical "再组织" artifact — the same image is addressable by multiple URLs (image API, presentation API, change discovery API) and can be re-linked. | No (the section's argument *is* the IIIF manifest — a diagram cannot stand in for it). |
| **Collection record from a structured-data dump** (Smithsonian OpenAccess, Met `MetObjects.csv`) | Smithsonian, Met | Smithsonian GitHub: <https://github.com/Smithsonian/OpenAccess> · Met CSV: <https://github.com/metmuseum/openaccess/blob/master/MetObjects.csv> | Low (Smithsonian CC0; Met CC0 with image-icon confirmation) | A structured-data row is a re-linking node — title, creator, date, accession, image URL, all fielded. | No (the section's argument *is* the structured record). |
| **Project-generated network diagram** (one botanical species connected across two herbaria, two editions, two records) | Project-generated | n/a | None (the project owns it) | The section's *visualization* of "再组织" is the network diagram. | n/a (it *is* a project-generated diagram). |
| **Collection record screenshot from an institution's catalog page** | Wellcome, Rijksmuseum, Met, Smithsonian, LoC | Same as above | High (risk category 3 in the v4.0 register — *platform screenshot ambiguity*) | A screenshot of a catalog page is the most *immediately readable* form of a record, but its rights surface is layered (the page's own design + the underlying record + the linked image). | Yes (a project-generated facsimile of the record's fields can substitute; the section's argument survives without the screenshot). |

**Section 4 summary.** The "collection record screenshot" row is the **highest-risk** row in the entire matrix. v4.2 should treat it as a `needs rights audit` item and may end up `excluded`; the project-generated network diagram and the structured-data row already carry the section's argument without the screenshot.

---

## Cross-section observations

1. **BHL and Rijksmuseum dominate the low-risk surface.** For pre-1928 botanical plates, the natural starting set is BHL (US public-domain cutoff + metadata CC0) and Rijksmuseum (CC0 + well-documented policy). NMNH (Smithsonian) is the strongest single source for *herbarium sheets specifically* because NMNH's holdings are extensive and the CC0 program is rigorous.

2. **Project-generated diagrams carry the argument in three of the four sections.** Section 2 needs the comparison diagram; Section 3 needs the reproduction-chain diagram; Section 4 needs the network diagram. None of these depend on external rights. The real images (when available) *enrich* the argument; they are not strictly required.

3. **The Met is a secondary source for this theme.** The Met's botanical / natural-history holdings are not a primary collection strength. v4.2's Met search is worthwhile but should not be over-invested in.

4. **Wellcome's "except where otherwise noted" is the v4.2 audit's most important single check.** The site-wide CC BY 4.0 default is good, but every per-item check is mandatory.

5. **LoC's per-collection rights surface is the most error-prone of the six.** A v4.2 candidate that "looks LoC, looks public-domain" may still need a per-collection rights page visit. The default is *not* to assume.

6. **The collection-record screenshot (Section 4) is the only row where project-generated substitution is both *possible* and *preferred*.** Real institutional UI is a moving target; the underlying fields are stable.