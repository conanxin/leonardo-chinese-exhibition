# v5.6 Fact-Check Matrix

> Each row is a candidate claim that appears in the second exhibition
> v0.1 page, glossary, or in the surrounding documentation. Rows are
> not ranked by importance; ordering follows the candidate-id order
> used by `data/assets.json` and `docs/SOURCE_AUDIT_MANIFEST.md`. No
> row is marked "verified" on the basis of agent memory — every
> "verified" verdict references either (a) the v4.5 source-audit
> manifest or (b) the institutional source URL captured at v4.5
> import time. Rows that should be re-checked before v0.2 are marked
> `wording-needs-precision` or `research-needed`.

## Classification legend

- **object metadata** — institutional record field (identifier, accession,
  catalogue number, etc.).
- **rights metadata** — institutional rights statement (Public
  Domain, CC0, CC BY-NC-SA, etc.).
- **historical context** — date, place, role attribution.
- **technical statement** — about the IIIF / Image API / Presentation
  API / dataset-level CC0 / derivative endpoints.
- **curatorial interpretation** — framing, narrative arc, takeaway —
  not from the institution's record.

## Result legend

- **verified** — reproducible from `docs/SOURCE_AUDIT_MANIFEST.md`
  (the v4.5 manifest that's the canonical evidence file at HEAD)
  *and/or* the institutional source URL listed in that manifest.
- **wording-needs-precision** — the underlying fact is recorded but
  the v0.1 wording is loose or conflates categories.
- **unsupported** — no evidence file or institutional source URL
  documents the claim; treat as curatorial interpretation at most.
- **interpretation-only** — the claim is curatorial framing; do not
  mark it as a fact.
- **research-needed** — outside the v5.6 evidence base; defer to a
  later round.

## Matrix

| Fact ID | Candidate / section | Claim | Classification | Evidence file | Official URL | Result | Required change |
|---|---|---|---|---|---|---|---|
| F-01 | C-01 / Section 1 body | "Album of watercolors of Asian fruits and flowers" is the title of BHL item 318921 | object metadata | `docs/SOURCE_AUDIT_MANIFEST.md` (C-01 source note) | https://www.biodiversitylibrary.org/page/603998 | verified | none |
| F-02 | C-01 / alt text | "page 603998 — Pistillaria plate, watercolour on paper, between 1798 and 1850" | historical context | `docs/SOURCE_AUDIT_MANIFEST.md` (C-01 source note "Pistillaria plate") | https://www.biodiversitylibrary.org/page/603998 | wording-needs-precision | Date range "between 1798 and 1850" comes from the v4.5 source-note context, not from the page URL directly; v0.2 should verify this date range against the BHL item's bibliographic record before claiming it as a precise date. |
| F-03 | C-01 / credit line | "Biodiversity Heritage Library / Public domain" | rights metadata | `docs/SOURCE_AUDIT_MANIFEST.md` (C-01 source note + manifest's repository-only status); `docs/RIGHTS_AND_SOURCES.md` (C-01 entry) | https://www.biodiversitylibrary.org/page/603998 | verified | none |
| F-04 | C-03 / caption | "PD subset only; CC BY-NC-SA sibling pages blocked" | rights metadata | `docs/SOURCE_AUDIT_MANIFEST.md` (C-03 remaining caution); `docs/RIGHTS_AND_SOURCES.md` (C-03 entry) | https://www.biodiversitylibrary.org/page/603962 | verified | none |
| F-05 | C-03 / alt text | "Cycas revoluta plate, watercolour on paper, between 1798 and 1850. PD subset only." | historical context + rights metadata | `docs/SOURCE_AUDIT_MANIFEST.md` (C-03 source note) | https://www.biodiversitylibrary.org/page/603962 | wording-needs-precision | Same date-precision caveat as F-02; verify on the BHL item record before quoting a year range. |
| F-06 | C-06 / title + caption | "Aconitum bulbilliferum Hand.-Mazz. (Ranunculaceae, Type fragment)" with collector number 5202, 17 Sep 1914, China / Sichuan | object metadata + historical context | `docs/SOURCE_AUDIT_MANIFEST.md` (C-06 source note) | https://collections.nmnh.si.edu/search/botany/?ark=ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920 | verified | none |
| F-07 | C-06 / viewing_note | "low_resolution (90×90) thumbnail; lightbox disabled; page must not enlarge or use as background" | technical statement | `docs/SOURCE_AUDIT_MANIFEST.md` (C-06 exact media URL `/media/?i=...&thumb=yes` and remaining caution); `data/assets.json` `low_resolution: true, lightbox_enabled: false` | https://collections.nmnh.si.edu/media/?i=1529703&ph=yes&thumb=yes | verified | none |
| F-08 | C-06 / credit line | "Smithsonian Open Access (CC0 1.0, dataset-level CC0)" | rights metadata + technical statement | `docs/SOURCE_AUDIT_MANIFEST.md` (C-06 source note "Smithsonian Open Access / CC0 1.0"); `docs/RIGHTS_AND_SOURCES.md` (C-06 entry) | https://collections.nmnh.si.edu/ | verified | none |
| F-09 | C-08 / title | "[Botanical Specimen: Fern]" (Met accession 2003.562.3, 1855–60) | object metadata + historical context | `docs/SOURCE_AUDIT_MANIFEST.md` (C-08 source note) | https://www.metmuseum.org/art/collection/search/285149 | verified | none |
| F-10 | C-08 / credit line | "Public Domain; Gift of Russell C. Vail, 2003 (2003.562.3); double-confirmation" | rights metadata + object metadata | `docs/SOURCE_AUDIT_MANIFEST.md` (C-08 source note "double-confirmation"); `docs/RIGHTS_AND_SOURCES.md` (C-08 entry) | https://www.metmuseum.org/art/collection/search/285149 | verified | none |
| F-11 | C-09 / title | "Zeestreepvaren (Pteris), Anna Atkins, c. 1854" | object metadata + historical context | `docs/SOURCE_AUDIT_MANIFEST.md` (C-09 source note "*Zeestreepvaren*, Anna Atkins (photographer, England), c. 1854, cyanotype on paper") | https://www.rijksmuseum.nl/en/collection/object/Zeestreepvaren--7f09be0b89aef4574b8bf23ff019a5da | verified | none |
| F-12 | C-09 / credit line | "Rijksmuseum / Public domain (CC0 1.0)" | rights metadata | `docs/SOURCE_AUDIT_MANIFEST.md` (C-09 source note "Public domain (CC0 1.0 link)"); `docs/RIGHTS_AND_SOURCES.md` (C-09 entry) | https://www.rijksmuseum.nl/en/collection/RP-F-F80152 | verified | none |
| F-13 | C-09 / viewing_note | "Cyanotype photogram on paper, not a traditional print" | historical context + curatorial interpretation | `docs/SOURCE_AUDIT_MANIFEST.md` (C-09 source note "cyanotype on paper") | https://www.rijksmuseum.nl/en/collection/object/Zeestreepvaren--7f09be0b89aef4574b8bf23ff019a5da | wording-needs-precision | The body copy says "cyanotype on paper"; the glossary and other prose may still describe it as a "print" in the wider print-medium sense. Pin the cyanotype is a *photogram* (a photographic contact print using the object itself as the negative) — this should be checked against the Rijksmuseum object's "objectType" field and patched in v0.2. |
| F-14 | C-10 / title | "Wolfsklauw (Lycopodium), Anna Atkins, c. 1854" | object metadata + historical context | `docs/SOURCE_AUDIT_MANIFEST.md` (C-10 source note "*Wolfsklauw*, Anna Atkins (photographer, England), c. 1854") | https://www.rijksmuseum.nl/en/collection/object/Wolfsklauw--02cb4a1385a6500c80a0b08a4415038f | verified | none |
| F-15 | C-10 / caption + viewing_note | "IIIF Presentation API /manifest.json returns 404; manifest-based evidence is intentionally omitted" | technical statement | `docs/SOURCE_AUDIT_MANIFEST.md` (C-10 manifest caveat); `data/assets.json` C-10 `viewing_note` field | https://www.rijksmuseum.nl/en/collection/RP-F-F80313/manifest.json | wording-needs-precision | Caveat phrasing is correct in spirit; one concern: the Presentation API URL is referenced without a date stamp. In v0.2, append "(re-verified <YYYY-MM-DD>)" so the caveat is auditable; do not claim it as a permanent outage. |
| F-16 | C-10 / credit line | "Rijksmuseum / Public domain (CC0 1.0)" | rights metadata | `docs/SOURCE_AUDIT_MANIFEST.md` (C-10 source note); `docs/RIGHTS_AND_SOURCES.md` (C-10 entry) | https://www.rijksmuseum.nl/en/collection/RP-F-F80313 | verified | none |
| F-17 | Section 2 / `glossary-herbarium` | "NMNH Botany 与 Rijksprentenkabinet 都属于此类机构" | curatorial interpretation | none — `docs/SOURCE_AUDIT_MANIFEST.md` does **not** classify Rijksprentenkabinet as a herbarium | n/a | **unsupported** | **Rijksprentenkabinet is the Rijksmuseum's department for prints, drawings, and photographs** (works on paper), not a herbarium. Remove the Rijksprentenkabinet example from `glossary-herbarium`. This is the I-01 high-severity finding. |
| F-18 | `glossary-print` | "雕版、蚀刻、石印、蓝晒 cyanotype 等复制工艺" | curatorial interpretation | existing glossary entry | n/a | wording-needs-precision | Technically defensible (each is a *reproductive print process*); but "cyanotype" is also distinctively a photographic *photogram* (a contact print from the object itself). Restrict this entry to non-photographic processes and add a new `glossary-cyanotype` plus `glossary-photogram`. |
| F-19 | `glossary-public-domain` | "CC0 1.0 是常见的公共领域贡献许可" | rights metadata | `docs/SOURCE_AUDIT_MANIFEST.md` (C-09, C-10 rights statements); `docs/RIGHTS_AND_SOURCES.md` (forbidden-status-words discipline) | n/a | wording-needs-precision | Use the Met C-08 double-confirmation as the canonical "rights statement" example and the Rijksmuseum per-item Public Domain + CC0 link as the canonical "rights + license link" example. Note that **public-domain is a legal status, CC0 is a license instrument**, and they are not synonyms. |
| F-20 | `glossary-iiif` | "包含 Image API（按尺寸/区域派生图像）和 Presentation API（提供 manifest…）" | technical statement | `docs/SOURCE_AUDIT_MANIFEST.md` (C-10 manifest caveat); C-09 / C-10 footnote in `DEEP_RESEARCH_NOTES_ZH.md` | https://iiif.io/api/image/3.0/ ; https://iiif.io/api/presentation/3.0/ | verified | minor: add a one-clause note that only Image API is used in this exhibition's asset roster. |
| F-21 | `glossary-iiif` | "Presentation API manifest 在 C-10 上返回 404" | technical statement | `docs/SOURCE_AUDIT_MANIFEST.md` (C-10 manifest caveat) | https://www.rijksmuseum.nl/en/collection/RP-F-F80313/manifest.json | verified | none |
| F-22 | `glossary-specimen` | "经过压制、干燥或装订后保存于标本馆（herbarium）的植物个体或局部器官。它是分类学的物质基础，也是图像的对照样本。" | curatorial interpretation | implicit from Section 2 body | n/a | interpretation-only | None. Label as curatorial interpretation; do not promote to fact. |
| F-23 | Section 1 body | "18—19 世纪的水彩" | historical context | implied by C-01, C-03 source notes ("between 1798 and 1850") | https://www.biodiversitylibrary.org/page/603998 | wording-needs-precision | Wording is approximate ("18—19 c.") and consistent with the source-note date range. v0.2 may keep this loose phrasing, or tighten to "around 1798–1850", but should not assert a single year. |
| F-24 | Section 3 body | "Anna Atkins 蓝晒 cyanotype" framing | historical context | `docs/SOURCE_AUDIT_MANIFEST.md` (C-09, C-10 "cyanotype on paper") | https://www.rijksmuseum.nl/en/collection/object/Zeestreepvaren--7f09be0b89aef4574b8bf23ff019a5da ; https://www.rijksmuseum.nl/en/collection/object/Wolfsklauw--02cb4a1385a6500c80a0b08a4415038f | verified | None. |
| F-25 | Hero / footer status block | "production-deployed-v5.3" × 5, "published-in-v5.3" × 8, "imported-not-deployed" × 8, "repository-only-not-deployed" × 0 | rights metadata (status-model) | `docs/RIGHTS_AND_SOURCES.md` (Forbidden status words); `data/exhibition.json` (`forbidden_statuses_not_used`, `deployment_status`, `publication_status`); `data/assets.json` (per-asset `publication_status` and `import_status`) | n/a | verified | Count is enforced by `scripts/second_exhibition_repository_qa.py` and the production healthcheck, so this is a *tested* verified fact. |
| F-26 | Section 4 body | "稳定的 identifier、可校验的元数据、可机器读取的 rights 字段" | curatorial interpretation | none — narrative framing | n/a | interpretation-only | Label as interpretation; do not promote to fact. v0.2 may keep this as a framing sentence but should pair each abstract noun with a concrete example (see I-09). |
| F-27 | Section 2 body | "NMNH Botany 馆藏的 Aconitum bulbilliferum 与大都会博物馆的 Botanical Specimen: Fern 为对照样本" | object metadata | `docs/SOURCE_AUDIT_MANIFEST.md` (C-06 + C-08 source notes) | https://collections.nmnh.si.edu/search/botany/?ark=... ; https://www.metmuseum.org/art/collection/search/285149 | verified | Disambiguate in v0.2: NMNH C-06 is a herbarium specimen; Met C-08 is an institutional object record of a *photograph* of a botanical specimen. Both are "specimens" in a loose sense, but the institutional categories differ. |
| F-28 | Section 3 body | "从手稿到印刷，从印刷到扫描，从扫描到 IIIF" | curatorial interpretation | implicit from the page; C-09 / C-10 are IIIF Image-API derivatives | https://www.rijksmuseum.nl/en/collection/RP-F-F80152 ; https://www.rijksmuseum.nl/en/collection/RP-F-F80313 | interpretation-only | None. |
| F-29 | `data/exhibition.json` `core_question` | "自然史图像如何一步步从直观的视觉记录，转化为可被分类、复制、检索、并重新组织的知识载体？" | curatorial interpretation | none — top-level thesis | n/a | interpretation-only | Label as interpretation; this is the *thesis statement* and need not be verified. |
| F-30 | C-09 / C-10 institution label | "Rijksmuseum / Rijksprentenkabinet" | object metadata | implied by Rijksmuseum object's department attribution; not spelled out in `SOURCE_AUDIT_MANIFEST.md` | https://www.rijksmuseum.nl/en/collection/RP-F-F80152 | wording-needs-precision | The institution label is correct as a department designation but the manifest itself does not document this. v0.2 should re-verify the Rijksmuseum object's department page (or use the public object's "objectType" field) so the wording can be promoted to verified. |

## Items deferred to research-needed

These were considered and **not** added to the main matrix because
the v5.6 evidence base does not include them. Each should be picked
up in the next content round only if a v0.3 evidence file lands:

- F-31 (research-needed): exact publication year for the BHL "Album
  of watercolors" bibliographic record (date-range "1798–1850" is a
  v4.5 source-note context, not a per-page date).
- F-32 (research-needed): precise pixel dimensions of NMNH's
  higher-resolution derivative for C-06 (the v4.5 import only
  captured the 90×90 thumbnail).
- F-33 (research-needed): status of Rijksmuseum Presentation API
  manifest availability as of 2026 — v4.5 captured "404"; v0.2
  must re-verify.
- F-34 (research-needed): whether other cyanotype objects in the
  Rijksprentenkabinet have stable Presentation API manifests (out of
  scope for v0.2, but worth noting for future asset additions).

## Items out of scope by design

- The exact BHL item-level record fields (only the page-level
  metadata is part of v5.6's evidence base).
- Detailed IIIF specification links and version assertions (already
  covered by `DEEP_RESEARCH_NOTES_ZH.md` Section B).
- Anna Atkins biography details (only the per-object attribution is
  in the evidence base).
- The Smithsonian dataset-wide CC0 scope; only the per-object
  CC0 1.0 attribution at record level is in the evidence base.

## Summary

- `verified` rows: **17**.
- `wording-needs-precision` rows: **9**.
- `unsupported` rows: **1** (F-17 = the Rijksprentenkabinet
  herbarium error).
- `interpretation-only` rows: **4**.
- `research-needed`: **4** (none blocking v0.2).

The single `unsupported` finding corresponds to `I-01` in the
content audit (high severity). It must be addressed by v0.2; the
exact proposed change is in
[`docs/SECOND_EXHIBITION_CONTENT_CHANGESET_DRAFT_v5.6.md`](SECOND_EXHIBITION_CONTENT_CHANGESET_DRAFT_v5.6.md)
as changeset row `CHG-01`. All `wording-needs-precision` rows are
candidate v0.2 edits listed under `CHG-02` through `CHG-09`.
