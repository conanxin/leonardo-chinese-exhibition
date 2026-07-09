# v4.1 Rights Screening Decisions

> Scope: a *preliminary* set of decisions on the v4.1 candidate set, before v4.2 audit. The decisions here are *research-time triage*, not approvals. The only allowed Decision values in v4.1 are: `keep for v4.2 audit`, `exclude`, `replace with project-generated diagram`. **`approved` is not used in v4.1.** v4.2 re-makes every decision on the basis of the per-item evidence it collects.

---

## Decision rules

The following rules govern every decision in this document. They are written *before* the table so that the table is mechanical to read.

**v4.1 不批准任何资产进入正式展览。** / *v4.1 does not approve any asset for entry into the formal exhibition.*

The rules below operationalize that policy.

1. **v4.1 does not approve any asset.** No row's Decision is `approved`. The only v4.1 Decisions are `keep for v4.2 audit`, `exclude`, `replace with project-generated diagram`.
2. **Low risk is still only a candidate.** Even a row that v4.1 has labeled "Low" in the source candidate table is *not* approved by that label. v4.2 must re-verify per item.
3. **Medium and High risk rows must enter v4.2 rights audit.** A Medium or High row is not excluded by its label; it is *queued* for v4.2. v4.2 may downgrade (to Low) or upgrade (to Blocked) on the basis of per-item evidence.
4. **Blocked is excluded at v4.1.** A row whose v4.1 evidence already shows a Blocked-equivalent reason (e.g., CC BY-NC-SA with a non-commercial clause that the v4.3 distribution channel cannot accept) is excluded at v4.1, not queued for v4.2. v4.2 may *re-include* a row if new evidence emerges.
5. **No source URL, no rights statement, no identifier → excluded.** If a candidate has no traceable source page, no rights statement, or no persistent identifier, it is *excluded* — not "kept for v4.2". The reason: v4.2 has nothing to audit.
6. **High-risk platform screenshots do not enter the v4.2 asset shortlist** unless they have explicit reuse guidance from the platform. A screenshot of an institution's catalog page is a *platform screenshot*; the institution's reuse guidance is a separate question from the institution's content licence. v4.2 may *keep* such a row if the platform's reuse guidance is clear (e.g., a documented screenshot policy), but the default is `replace with project-generated diagram`.
7. **Project-generated substitution is the safe default when a real image's rights are unclear.** Where the section's argument survives a project-generated diagram (see `ASSET_CANDIDATE_MATRIX_v4.1.md` § Cross-section observations), v4.1 prefers to mark the row `replace with project-generated diagram`. This is not a downgrade of the candidate — it is a defensive default that protects the exhibition's release.

---

## Preliminary decisions

| Candidate ID | Decision | Reason | Required v4.2 action |
|---|---|---|---|
| **C-01** (BHL, Public-domain botanical plate) | keep for v4.2 audit | Low initial risk; per-item `<Copyright Status>` check is the gate | Locate one specific title; capture `<Copyright Status>` / `<Holding Institution>` / `<License Type>`; confirm US public-domain cutoff. |
| **C-02** (BHL, Flickr photostream) | replace with project-generated diagram | The Flickr URL is a *third-party platform*; the rights belong to the underlying BHL item, but the section's argument survives a project-generated illustration-of-an-illustration diagram. | None for C-02 itself. If v4.2 wants to re-include, it must capture the linked BHL item's rights page (i.e., promote C-02 to a separate row). |
| **C-03** (BHL, title-level book) | keep for v4.2 audit | Low–Medium; per-item licence is the gate | Locate one specific title; capture title-page metadata; confirm `<Copyright Status>` field. |
| **C-04** (Wellcome, Works search — Engravings / Lithographs) | keep for v4.2 audit | Low (per-item CC BY 4.0) | Locate one specific item; confirm CC BY 4.0 on the item page; capture IIIF info.json or Catalogue API record. |
| **C-05** (Wellcome, IIIF Image API) | keep for v4.2 audit | Low–Medium (per item) | Capture the IIIF manifest URL; confirm the `license` field; capture the credit-line composition. |
| **C-06** (Smithsonian NMNH, herbarium sheet) | keep for v4.2 audit | Low (CC0 icon required) | Locate one specific NMNH specimen; confirm CC0 icon; capture accession number and any third-party-restriction notes. |
| **C-07** (Smithsonian OpenAccess data dump) | keep for v4.2 audit | Low (metadata) / Medium (image) | Locate one specific record; confirm the linked item's CC0 status on its public page. |
| **C-08** (Met OpenAccess `MetObjects.csv`) | keep for v4.2 audit | Low (if both `Is Public Domain = True` AND public object page CC0 icon) / High (otherwise) | Locate one specific CSV row; cross-check the public object page; confirm both fields. |
| **C-09** (Rijksmuseum, Rijksstudio + data services) | keep for v4.2 audit | Low (CC0) or Low–Medium (CC BY 4.0) | Locate one specific object; capture the licence field and the IIIF manifest URL. |
| **C-10** (Rijksmuseum, IIIF Presentation API) | keep for v4.2 audit | Low (per item) | Use the IIIF APIs to confirm the licence and the image service URL; do not download. |
| **C-11** (LoC P&P, Botanical illustrations subject heading) | keep for v4.2 audit | Low (U.S. government work) or Medium ("no known restrictions") | Pick one specific P&P item; visit its persistent URL; capture the exact rights wording; visit the *collection's* "Rights & Access" page. |
| **C-12** (LoC Digital Collections, illustrated-book collection) | keep for v4.2 audit | Low–Medium (per collection) | Pick one specific collection; fetch its "Rights & Access" page; confirm the rights wording. |
| **C-13** (LoC P&P, per-item record) | keep for v4.2 audit | Low–Medium (per record) | Pick one specific record; capture the per-record rights statement verbatim. |
| **C-14** (BHL in-copyright subset, CC BY-NC-SA 4.0) | **exclude** | NC clause is incompatible with this project's openly-distributed output; v4.3 cannot redistribute under NC. The SA clause is also problematic. | None — excluded at v4.1. May be revisited if the distribution channel changes (not in v4.0–v4.4). |
| **(Section 4 implicit row)** Collection record screenshot from an institution's catalog page | **replace with project-generated diagram** | Risk category 3 (platform screenshot ambiguity) per the v4.0 register; the section's argument survives a project-generated facsimile; the underlying fields are stable, the UI is not. | If v4.2 wants to re-include, it must capture the platform's screenshot/reuse policy separately from the institution's content licence. Not a v4.1 priority. |

---

## v4.1 decision totals

- `keep for v4.2 audit`: **12** (C-01, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, C-13).
- `replace with project-generated diagram`: **2** (C-02 BHL Flickr, plus the Section-4 screenshot row).
- `exclude`: **1** (C-14 CC BY-NC-SA 4.0 in-copyright subset).
- `approved`: **0** (not used in v4.1).

Total rows in the v4.1 source candidate table: **14**.
Rows entering v4.2 audit: **12**.
Rows excluded at v4.1: **1** (NC clause mismatch).
Rows replaced with project-generated diagram at v4.1: **2**.

---

## What v4.1 explicitly does *not* do

- It does **not** assert that any Low-risk row is "safe to use". v4.2 re-verifies.
- It does **not** allow a `Medium` row to skip v4.2. Every Medium row enters v4.2 with the per-item check listed as the required action.
- It does **not** decide which candidate becomes the v4.3 build's first asset. That is a v4.2 / v4.3 decision.
- It does **not** create any image file. No download, no asset, no screenshot.
- It does **not** modify any live site, template, pilot, or quality-gate file.