# Second Exhibition — Rights and Sources Summary

Companion to `SOURCE_AUDIT_MANIFEST.md`. This document is the **rights-side** summary: one entry per asset, recording the rights basis, the exact rights URL, and any per-item vs. policy-level distinction.

Round: **v4.5-asset-import** (partial: 5 of 6 candidates imported; C-06 blocked)

---

## C-01 — BHL page 603998

- **Rights basis:** Public domain, per BHL per-page status indicator.
- **Rights URL:** https://about.biodiversitylibrary.org/help/copyright-and-reuse/
- **Per-item vs. policy-level:** Per-page status — the page image inherits the item-level BHL status. CC BY-NC-SA subset pages of item 318921 are excluded and remain blocked.
- **Source URL:** https://www.biodiversitylibrary.org/page/603998
- **Identifier:** BHL page 603998

## C-03 — BHL page 603962

- **Rights basis:** Public domain, per BHL per-page status indicator.
- **Rights URL:** https://about.biodiversitylibrary.org/help/copyright-and-reuse/
- **Per-item vs. policy-level:** Per-page status — the page image inherits the item-level BHL status. CC BY-NC-SA subset pages of item 318921 are excluded and remain blocked.
- **Source URL:** https://www.biodiversitylibrary.org/page/603962
- **Identifier:** BHL page 603962

## C-06 — NMNH Botany catalog 1529703

- **Rights basis:** Smithsonian Open Access / CC0 1.0 — **dataset-level only**, per https://www.si.edu/openaccess/faq.
- **Rights URL:** https://www.si.edu/openaccess/faq
- **Per-item vs. policy-level:** Policy-level only. No per-item evidence was confirmed during v4.5 because no per-item media URL could be retrieved.
- **Source URL (attempted, not confirmed in v4.5):** https://collections.nmnh.si.edu/search/botany/?irn=2793935
- **Identifier:** NMNH catalog 1529703 (per-item irnstamp not confirmed in v4.5)
- **Status:** blocked-from-import (see `SOURCE_AUDIT_MANIFEST.md` C-06 row).

## C-08 — Met object 285149

- **Rights basis:** The Met Open Access — public domain designation.
- **Rights URL:** https://www.metmuseum.org/about-the-met/policies-and-documents/image-resources
- **Per-item vs. policy-level:** Per-item, double-confirmed via:
  1. Collection API `isPublicDomain=true` (https://collectionapi.metmuseum.org/public/collection/v1/objects/285149)
  2. Public object page Public Domain indicator (https://www.metmuseum.org/art/collection/search/285149)
- **Source URL:** https://www.metmuseum.org/art/collection/search/285149
- **Identifier:** Met object 285149 / accession 2003.562.3

## C-09 — Rijksmuseum object RP-F-F80152

- **Rights basis:** Per-item Rijksmuseum Copyright field — `Public domain` (verbatim), with a CC0 1.0 link on the same page.
- **Rights URL:** https://data.rijksmuseum.nl/policy/information-and-data-policy
- **Per-item vs. policy-level:** **Per-item** — the Copyright label rendered on the object page is the licence-of-record for this specific object, not a derivation from the institution-wide policy.
- **Source URL:** https://www.rijksmuseum.nl/en/collection/RP-F-F80152
- **Identifier:** RP-F-F80152 (persistent URL https://id.rijksmuseum.nl/200408261)

## C-10 — Rijksmuseum object RP-F-F80313

- **Rights basis:** Per-item Rijksmuseum Copyright field — `Public domain` (verbatim), with a CC0 1.0 link on the same page.
- **Rights URL:** https://data.rijksmuseum.nl/policy/information-and-data-policy
- **Per-item vs. policy-level:** **Per-item** — the Copyright label rendered on the object page is the licence-of-record for this specific object, not a derivation from the institution-wide policy.
- **Source URL:** https://www.rijksmuseum.nl/en/collection/RP-F-F80313
- **Identifier:** RP-F-F80313 (persistent URL https://id.rijksmuseum.nl/200408260)
- **Note:** Presentation API `/manifest.json` for this object returned HTTP 404. Manifest-based evidence intentionally omitted from this round.