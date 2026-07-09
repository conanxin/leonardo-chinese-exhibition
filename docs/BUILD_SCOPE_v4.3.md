# v4.3 Build Scope

> Scope: define the second exhibition's section scope, page structure, and the writing tasks that a future round will execute. v4.3 does not write to `site/`. v4.3 does not produce a deployed exhibition. v4.3 produces the *plan* for the future build.
>
> The status `approved` is **not used**. The phrase "safe for commercial use" is **not used**. No real image is downloaded in v4.3.

---

## Exhibition working title

《植物图谱与视觉分类：从自然史图像到知识秩序》

(English working title, for reference only: *Botanical Plates and Visual Taxonomy: From Natural-History Images to the Order of Knowledge*.)

---

## Section scope

4 sections, each with a *purpose*, a *planned candidate item* (the v4.3 `selected-for-build-planning` row), a *fallback project-generated diagram* (the substitution when the real image is unavailable), a *source evidence status* (the v4.2 verified / needs clarification status of the planned candidate), a *rights caution* (the per-section rights note), and *writing tasks* (the future-round work).

### Section 1 — 观察：图像如何抓住植物特征

- **Purpose.** A botanical illustration is a *decision* — what the illustrator chose to look at, and what they chose to leave out. The image as a *decision*, not a copy.
- **Planned candidate item.** **C-01** (BHL pre-1928 Public-domain botanical plate), with **C-09** (Rijksmuseum botanical print, CC0) as the cross-section alternate.
- **Fallback project-generated diagram.** A side-by-side comparison of two editions of the same plate (engraving vs. lithograph) — the section's argument about selection becomes visible. Drawn by the project; the diagram is *not* a substitute for a real image, it is a teaching aid.
- **Source evidence status.** C-01 v4.2 = `verified`; C-09 v4.2 = `verified (mechanism)`. Both pass the 5 source-acceptance checks.
- **Rights caution.** The C-01 selection must restrict to the BHL Public-domain subset. The C-09 selection must record the per-item `licence` field exactly. Non-US distribution may have different rules.
- **Writing tasks.** Section body (~200–350 Chinese characters); 1–2 artifact card captions; source notes; credit line per item. *Not produced in v4.3; the writing brief is in `CONTENT_DRAFT_BRIEF_v4.3.md`.*

### Section 2 — 分类：图像如何服务命名与秩序

- **Purpose.** A botanical illustration becomes part of a taxonomic system — a binomial name, a family, an order. The image as a *node* in a naming system.
- **Planned candidate item.** **C-06** (Smithsonian NMNH herbarium sheet, CC0), with **C-09** (Rijksmuseum) as the cross-section alternate.
- **Fallback project-generated diagram.** A side-by-side comparison of two related species, with the diagnostic features labelled. The section's argument is *visual*: classification is a visual operation. The diagram is a clean, controlled comparison of the features that distinguish one species from a related one.
- **Source evidence status.** C-06 v4.2 = `verified`; C-09 v4.2 = `verified (mechanism)`. Both pass the 5 source-acceptance checks.
- **Rights caution.** C-06 must record the accession number (mandatory for the credit line). The Smithsonian CC0 only covers copyright; donor / cultural-sensitivity / trademark restrictions are recorded at v4.4.
- **Writing tasks.** Section body; 1–2 artifact card captions; source notes; credit line per item; the *why it fits* paragraph that connects the herbarium sheet to the "name + specimen + image" argument.

### Section 3 — 复制：书籍、版画与数字化如何改变传播

- **Purpose.** The same image is multiplied — engraved, lithographed, photographed, scanned, digitized — and each medium changes what the image can do.
- **Planned candidate item.** **C-03** (BHL title-level book record, **PD subset only**; CC BY-NC-SA subset blocked), with **C-08** (Met `MetObjects.csv` row + linked CC0 image) as the alternate.
- **Fallback project-generated diagram.** A "reproduction chain" diagram showing engraving → lithograph → photograph → scan → digital. The diagram is the section's argument in visual form: each medium adds or removes something.
- **Source evidence status.** C-03 v4.2 = `verified (PD subset only)`; C-08 v4.2 = `verified (mechanism)`. The C-03 CC BY-NC-SA subset is `blocked-from-build` in v4.3 and is not in the build.
- **Rights caution.** **C-03 selection must filter on `<Copyright Status> = Public domain` only.** The CC BY-NC-SA subset is incompatible with the project's openly-distributed output. C-08 requires double-confirmation (`isPublicDomain: true` in the Collection API **and** Open Access icon on the public object page).
- **Writing tasks.** Section body; 1–2 artifact card captions; source notes; credit line per item; a short paragraph that explains the "reproduction chain" diagram and how each medium changes what the image can do.

### Section 4 — 再组织：数字馆藏如何让图像重新连接

- **Purpose.** A digital collection re-links images that the printed book separated. The same image gains new neighbours when the catalog gains new fields.
- **Planned candidate item.** **C-10** (Rijksmuseum IIIF Presentation API manifest).
- **Fallback project-generated diagram.** A network diagram showing one botanical species connected across two herbaria, two editions, two records. The diagram is the section's argument in visual form: the digital collection is a re-linking engine.
- **Source evidence status.** C-10 v4.2 = `verified (mechanism)`. The IIIF Presentation API manifest's `license` field is the authoritative source.
- **Rights caution.** The IIIF info.json alone does not carry the rights field; the Presentation API manifest does. v4.4 must pair the IIIF manifest with the Catalogue-side object record.
- **Writing tasks.** Section body; 1–2 artifact card captions; source notes; credit line per item; a short paragraph that explains the IIIF re-linking layer and the "facsimile" fallback (project-generated record facsimile, since the v4.1 Section-4 screenshot row is `replace with project-generated diagram`).

---

## Minimum page structure

The future build (a future round, not v4.3) will instantiate the template into a new exhibition working directory and write the content. The page structure follows the v4.0 content outline and the MVE.

| Slot | Count | Content source |
|---|---|---|
| **Hero** | 1 (~80–120 Chinese characters) | `docs/CONTENT_DRAFT_BRIEF_v4.3.md` § Hero draft. The text in the brief is a *draft*, not a final page element. |
| **3-minute guide** | 1 (~600–900 Chinese characters) | `docs/CONTENT_DRAFT_BRIEF_v4.3.md` § 3-minute guide draft. The text in the brief is a *draft*. |
| **Exhibition map** | 1 | A short index of the 4 sections + the 3-minute guide + the curatorial essay. |
| **Sections** | 4 (观察 / 分类 / 复制 / 再组织) | Section bodies; see `CONTENT_DRAFT_BRIEF_v4.3.md` § Section draft briefs. |
| **Artifact cards** | 4–6 (one per section minimum) | Cards keyed to the v4.3 `selected-for-build-planning` candidates (C-01 / C-06 / C-03 / C-10 + C-09 / C-08 alternates). The build set is **6** real-image artifact cards (4 primary + 2 alternates); v4.4 may pick 4–6 for the final render. |
| **Glossary** | 6–10 terms | The 10 candidates from `docs/SECOND_EXHIBITION_CONTENT_OUTLINE_v4.0.md` (botanical illustration / taxonomy / herbarium / specimen / plate / engraving / digitization / metadata / collection record / public domain). |
| **Source and rights notes** | 1 page each | Aggregated from the v4.3 item evidence dossier. |
| **Curatorial essay** | 1 (~1,500–2,500 Chinese characters) | A single reflective essay on the exhibition's argument; written in a future round. |
| **Footer marker** | 1 | The v4.3 marker (planned, not yet installed in `site/`). The marker text is fixed in the future build round, not in v4.3. |

The build does **not** modify `site/`. The future build instantiates a *new* exhibition working directory (e.g., `_exhibitions/second-botanical-taxonomy/`); the exact path is decided in the future build round, not in v4.3.

---

## Cross-section observations

1. **No real image is in the build set yet.** v4.3 selects the *candidates*, not the specific items. Per-item selection is a v4.4 step.
2. **C-09 is the cross-section alternate.** C-09 is a Section 1 primary and a Section 2 alternate. The build set allows one candidate to appear in two sections if the rights + credit-line basis support it; the final render picks one section per artifact.
3. **C-08 is a Section 3 alternate.** C-08 is a strong Section 3 candidate only if the Met holds a botanical print with `isPublicDomain: true` *and* the public-page OA icon. v4.4 must run the double-confirmation.
4. **The Section 4 screenshot row is `replace-with-project-generated-diagram`**, carried over from v4.1. The Section 4 primary is C-10 (Rijksmuseum IIIF). The project-generated network diagram is the Section 4 fallback.
5. **The 4 project-generated diagrams** (one per section) are *planned* in v4.3; they are not drawn. Drawing is a future round.
6. **Glossary terms are inherited from v4.0.** No new glossary terms are added in v4.3; the 10 candidates from the v4.0 outline are sufficient for the build.

---

## Round-end note

v4.3 records the build scope. The future build round will:

1. Pick one specific item per `selected-for-build-planning` row (6 rows → 6 specific items).
2. Re-check the per-item evidence against the v4.0 source-acceptance rule (the v4.3 dossier is the *plan*; the future round captures the *evidence*).
3. Write the page elements (hero, 3-minute guide, exhibition map, 4 section bodies, 4–6 artifact cards, glossary, source notes, rights notes, curatorial essay, footer marker).
4. Draw the 4 project-generated diagrams.
5. Run `template_quality_gate.py` against the new structure.
6. **Not** deploy. v4.3 / v4.4 is repository-only; live publication is a separate, future round that runs the source-and-rights audit a second time on the *to-be-deployed* working tree.

The build scope here is the *plan*. The future build is the *execution*.