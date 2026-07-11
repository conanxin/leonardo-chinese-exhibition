# Second Exhibition — Rights and Sources Summary

Round: **v4.5-asset-import**
Deployment status: **repository-only-not-deployed**

> This document is **not** a legal opinion. It records per-asset rights basis as observed during v4.5. The current round is repository-only and does not deploy, does not link into the live site, and does not create a tag or GitHub Release. **Future build/deployment must re-verify the source and rights pages a second time before any image is linked into a page.**

---

## C-01 — BHL page 603998

- **Rights basis**: Public domain per BHL per-page Copyright Status indicator. CC BY-NC-SA subset pages of BHL item 318921 are excluded and remain blocked.
- **Rights URL**: https://about.biodiversitylibrary.org/help/copyright-and-reuse/
- **Per-item vs. policy-level**: Per-page — the page image inherits the item-level BHL status.
- **Attribution expectation**: Page-id + BHL item-id + Public domain.
- **Licence caveat**: CC BY-NC-SA subset pages of the parent item must remain excluded.
- **Import date**: 2026-07-11 (UTC).
- **Repository-only / not-deployed note**: Imported into `second-exhibition/assets/images/bhl-318921-page-603998-c01.webp` only; not deployed.

## C-03 — BHL page 603962

- **Rights basis**: Public domain per BHL per-page Copyright Status indicator. **PD subset only.** CC BY-NC-SA subset pages of BHL item 318921 are excluded and remain blocked-from-import.
- **Rights URL**: https://about.biodiversitylibrary.org/help/copyright-and-reuse/
- **Per-item vs. policy-level**: Per-page — the page image inherits the item-level BHL status.
- **Attribution expectation**: Page-id + BHL item-id + Public domain + explicit "PD subset only" caveat in any future publication.
- **Licence caveat**: CC BY-NC-SA subset pages of the parent item must remain excluded.
- **Import date**: 2026-07-11 (UTC).
- **Repository-only / not-deployed note**: Imported into `second-exhibition/assets/images/bhl-318921-page-603962-c03.webp` only; not deployed.

## C-06 — NMNH Botany catalog 1529703

- **Rights basis**: Smithsonian Open Access / CC0 1.0 — **dataset-level only**. The Smithsonian's Open Access release applies to the entire NMNH Botany dataset; no per-item licence field is rendered on the NMNH Botany record page.
- **Rights URL**: https://www.si.edu/openaccess/faq
- **Per-item vs. policy-level**: Policy-level (dataset-wide). The dataset-level CC0 1.0 statement is the licence basis for this asset; do not invent a per-item licence field that does not exist on the institution's own page.
- **Attribution expectation**: Smithsonian Open Access credit line: US Catalog number + institution + dataset-level CC0 1.0.
- **Licence caveat**: The /media/?i=... endpoint serves a 90x90 PNG thumbnail; a higher-resolution derivative was not exposed by the NMNH Ke Emu API at import time. Re-confirm the dataset-level CC0 1.0 statement on the live si.edu Open Access / Terms page before any publication.
- **Import date**: 2026-07-11 (UTC).
- **Repository-only / not-deployed note**: Imported into `second-exhibition/assets/images/smithsonian-nmnh-1529703.png` only; not deployed.

## C-08 — Met object 285149

- **Rights basis**: The Met Open Access — public domain designation. **Double-confirmation PASS**: (a) Collection API `isPublicDomain: true`; (b) public object page Public Domain indicator.
- **Rights URL**: https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources
- **Per-item vs. policy-level**: Per-item — both indicators (API field + page button) point to this specific object, not a derivation from institution policy.
- **Attribution expectation**: Title + date + The Met + accession number + Public domain.
- **Licence caveat**: Credit line "Gift of Russell C. Vail, 2003" was recorded in v4.4b evidence; not re-confirmed inside v4.5. Page build must verify before publishing.
- **Import date**: 2026-07-11 (UTC).
- **Repository-only / not-deployed note**: Imported into `second-exhibition/assets/images/met-285149.jpg` only; not deployed. Used web-large derivative (1024 px) instead of original.

## C-09 — Rijksmuseum RP-F-F80152

- **Rights basis**: Per-item Rijksmuseum Copyright field on the public object page reads verbatim `Public domain` with a hyperlink to https://creativecommons.org/publicdomain/mark/1.0/deed.en (CC0 1.0).
- **Rights URL**: https://data.rijksmuseum.nl/policy/information-and-data-policy
- **Per-item vs. policy-level**: **Per-item** — the Copyright label rendered on the object page is the licence-of-record for this specific object, not a derivation from institution policy.
- **Attribution expectation**: Title + maker + date + Rijksmuseum + objectNumber + Public domain (CC0 1.0).
- **Licence caveat**: Object type is photogram (cyanotype), not traditional print; page build must label accordingly.
- **Import date**: 2026-07-11 (UTC).
- **Repository-only / not-deployed note**: Imported into `second-exhibition/assets/images/rijksmuseum-rp-f-f80152.jpg` only; not deployed.

## C-10 — Rijksmuseum RP-F-F80313

- **Rights basis**: Per-item Rijksmuseum Copyright field on the public object page reads verbatim `Public domain` with a hyperlink to https://creativecommons.org/publicdomain/mark/1.0/deed.en (CC0 1.0).
- **Rights URL**: https://data.rijksmuseum.nl/policy/information-and-data-policy
- **Per-item vs. policy-level**: **Per-item** — the Copyright label rendered on the object page is the licence-of-record for this specific object, not a derivation from institution policy.
- **Attribution expectation**: Title + maker + date + Rijksmuseum + objectNumber + Public domain (CC0 1.0).
- **Licence caveat**: Object type is photogram (cyanotype), not traditional print. Presentation API `/manifest.json` returned HTTP 404; manifest-based evidence was intentionally omitted from this round. The per-item public object page Copyright field is the authoritative licence source for the credit line.
- **Import date**: 2026-07-11 (UTC).
- **Repository-only / not-deployed note**: Imported into `second-exhibition/assets/images/rijksmuseum-rp-f-f80313.jpg` only; not deployed.

---

## Forbidden status words

The status words `approved`, `deployed`, `live`, `safe for commercial use`, and `cleared for all uses` are intentionally **not used** anywhere in v4.5. Every imported asset carries the status `imported-not-deployed`.

## Re-verification rule

Before any future build round links these assets into a page, the build round must re-open every source URL and rights URL recorded above on the day of the build and confirm the licence basis has not changed. The current evidence is dated 2026-07-11; build rounds must produce a fresh re-verification timestamp.