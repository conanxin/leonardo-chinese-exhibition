# v5.6 Second Exhibition Content Iteration Plan

> Goal of the v0.2 iteration: address the **single high-severity**
> fact (Rijksprentenkabinet ≠ herbarium) and the **medium-severity**
> terminology / narrative findings from
> [`SECOND_EXHIBITION_CONTENT_AUDIT_v5.6.md`](SECOND_EXHIBITION_CONTENT_AUDIT_v5.6.md),
> without changing the section structure, status model, asset
> roster, image roster, deployment URL, or any source / rights
> evidence file. This document is the design-level plan; the
> exact per-file edits are in the changeset draft.

## Target version

```
second-exhibition-v0.2
```

Bumping the `marker` in `data/exhibition.json` from
`second-exhibition-v0.1` to `second-exhibition-v0.2`. All six
images, all six asset candidate IDs, the four-section structure,
the four-section deep-block types, the twelve-term glossary (to
be expanded to 14 terms in v0.2), and the existing status
model must remain byte-identical or semantically equivalent.

## Scope boundary (do-not-touch list)

The v0.2 implementation **must not**:

- change `second-exhibition/site/index.html` byte-identical —
  only modify it in the named paragraphs below.
- change any image file under `second-exhibition/assets/images/`.
- change `asset-import-manifest.json` or `asset-checksums.sha256`.
- change `docs/SOURCE_AUDIT_MANIFEST.md` or
  `docs/RIGHTS_AND_SOURCES.md`.
- change the deployment URL (`/second-exhibition/`) or the
  base path on GitHub Pages.
- change the four section IDs, the six artifact IDs, the four
  deep-block types, the four-section kicker strings.
- change the four status phrases or their counts
  (`production-deployed-v5.3 = 5`,
  `published-in-v5.3 = 8`,
  `imported-not-deployed = 8`,
  `repository-only-not-deployed = 0`).
- change the public inventory file count (34 files); new HTML/CSS/JS
  *additions* are fine if they don't add new files to the Pages
  artifact.
- change the production drift gate or the post-push verification
  surface.

The v0.2 implementation **may**:

- edit named paragraphs of `second-exhibition/site/index.html`,
  `data/exhibition.json`, `data/sections.json`,
  `data/glossary.json`, `data/assets.json`.
- edit the four narrative `docs/*.md` (CURATORIAL_ESSAY,
  VISITOR_GUIDE, DEEP_RESEARCH_NOTES, BUILD_ASSET_USAGE).
- rebuild `docs/V5_ROADMAP.md` and `README.md` to record the v0.2
  release.
- add (not change) new entries to the glossary (limit 12 → 14).
- emit a new round report under `reports/`.

## Content changes (high-level)

### 1. Hero

**Current**: subtitle + 3 status strings + URL, packed into
1,331 B.

**Proposed v0.2 (blocker: NO, recommended: YES, scope: site/index.html
hero region only)**:

- Move the three deployment-status phrases out of the hero into
  a footer-rail or sidebar. The hero carries the *core question*
  (already in `data/exhibition.json.core_question`) and a
  single-sentence framing.
- The status strings are **kept** in the page — just relocated
  — so the v5.3 controlled-deployment count discipline is
  preserved.

**Risk**: low — strictly a layout/relocation.

### 2. 3-minute guide

**Current**: 5-step "visitor action" list.

**Proposed v0.2 (recommended: YES, scope: site/index.html 3-minute
guide block)**:

- Switch lead sentence from "what to do" to "what to look for";
  keep the 5 steps but reframe each to anchor a *viewing
  method* (watercolour vs. specimen vs. cyanotype vs. record).

**Risk**: low — wording-only.

### 3. Section 1 · 观察 / Observation

**Current**: watercolour intro, viewer-action "把两张水彩图像并排放
在一起".

**Proposed v0.2 (recommended: YES, scope: section body + Section 1
deep-block prompt)**:

- Foreground the difference between watercolour-on-paper (drawn
  representation) and herbarium specimen (preserved physical
  object). Use "保留什么、舍弃什么" as the rubric but make
  the visual/non-physical contrast explicit.
- Vary the Section 1 deep-block prompt verb so it does not
  read like a restatement of the body (I-15).

**Risk**: low — wording-only.

### 4. Section 2 · 分类 / Classification

**Current**: bundles C-06 and C-08 as "对照样本".

**Proposed v0.2 (recommended: YES, scope: section body + asset cards
in Section 2)**:

- Disambiguate: NMNH C-06 is a herbarium specimen (image of a
  specimen); Met C-08 is a curatorial object record (image of
  a botanical specimen photograph).
- Foreground C-06's `low_resolution: true` and `lightbox_enabled:
  false` in the section body, not only in the asset card.

**Risk**: low — wording-only.

### 5. Section 3 · 复制 / Reproduction

**Current**: reproduction arc anchored by Rijksmuseum cyanotypes.

**Proposed v0.2 (recommended: YES, scope: section body)**:

- Make explicit that Rijksprentenkabinet is a *print room*
  (works on paper), not a herbarium.
- Distinguish the four reproduction media present in this
  exhibition: watercolour-on-paper (C-01, C-03), silver-gelatin
  / photographic print on paper (C-09, C-10 are cyanotype
  *photograms* — i.e. photographic contact prints from the
  biological object itself), institutional photography
  (C-08), digital derivative (C-09, C-10 via IIIF).
- Add the IIIF Image API → Presentation API distinction
  explicitly to the section body.

**Risk**: low — wording-only.

### 6. Section 4 · 再组织 / Reorganization

**Current**: abstract framing of identifier / metadata / rights.

**Proposed v0.2 (recommended: YES, scope: section body)**:

- Anchor each abstract noun with a concrete example:
  identifier resolution (EZID arK for C-06, RP objectNumber for
  C-09/C-10, accession for C-08); rights endpoint (Public
  Domain per-item for C-08/09/10, CC0 link for C-09/10); IIIF
  derivative (Image API for C-09/C-10, missing Presentation API
  manifest for C-10).
- Keep the deep-block `research-model` prompt unchanged.

**Risk**: low — wording-only.

### 7. Artifact cards

**Current**: 6 cards each carry title, alt, caption, viewing-note,
credit-line, source-note, identifier, institution. The
credit/source/identifier triplet is repeated in every card.

**Proposed v0.2 (optional: depends on layout budget, scope:
site/index.html artifact-card markup)**:

- Aggregate credit-line / source-note / identifier into one
  compact line per card. Keep caption and viewing-note at the
  top. The **status counts must not change**.
- The asset metadata stays in `data/assets.json` so the JS
  lightbox modal can still resolve each card to its full
  record.

**Risk**: low — markup-only; if no design budget, defer to v0.3.

### 8. Glossary (12 → 14 entries)

**Current**: 12 entries, see F-17 / F-18 / F-20 above.

**Proposed v0.2 (blocker for F-17: YES, recommended for the rest:
YES, scope: `data/glossary.json`)**:

- **Add** `glossary-cyanotype` (definition anchored on the
  Anna Atkins photograms C-09 / C-10; cross-link to
  `glossary-photogram`).
- **Add** `glossary-photogram` (a contact print where the
  photographic object is the negative itself).
- **Edit** `glossary-herbarium` to *remove* the Rijksprentenkabinet
  example (I-01 / F-17 high-severity).
- **Edit** `glossary-print` to disambiguate cyanotype from
  non-photographic print media.
- **Edit** `glossary-public-domain` to draw the
  Public-Domain-as-legal-status vs. CC0-as-license-instrument
  distinction (F-19).
- **Edit** `glossary-iiif` to surface the Image API →
  Presentation API distinction explicitly and to scope the
  manifest-404 caveat to C-10 only (I-04 / F-04 / F-15).

**Risk**: low — wording + 2-entry addition.

### 9. Deep blocks

**Current**: 4 deep blocks; two of the prompts share the prefix
"如果你只能".

**Proposed v0.2 (optional, scope: `data/sections.json` per-section
`deep_block_prompt`)**:

- Vary the Section 1 and Section 3 prompts so neither begins
  with "如果你只能" (I-15).
- Keep the `deep_block_type` taxonomy unchanged
  (visual-thinking, material-evidence, research-model).

**Risk**: low — wording-only.

## Blockers vs. recommended enhancements vs. deferred

### Blockers (must fix in v0.2; otherwise v0.2 cannot ship)

- **CHG-01** — `glossary-herbarium` references Rijksprentenkabinet
  as a herbarium (F-17, I-01). This is the *only* high-severity
  finding. Fix by removing the Rijksprentenkabinet clause.

### Recommended enhancements (high-value, in scope for v0.2)

- **CHG-02** — Section 1 disambiguation (watercolour vs. specimen).
- **CHG-03** — Section 2 disambiguation (NMNH herbarium vs. Met
  object record).
- **CHG-04** — Section 3 disambiguation (4 reproduction media).
- **CHG-05** — Section 4 concrete identifier-resolution examples.
- **CHG-06** — `glossary-print` cyanotype disambiguation.
- **CHG-07** — `glossary-public-domain` legal-status vs. license
  distinction.
- **CHG-08** — `glossary-iiif` Image API / Presentation API
  distinction.
- **CHG-09** — Hero status-block relocation.
- **CHG-10** — 3-minute guide viewing-method framing.

### Defer to future rounds

- Artifact card credit / source / identifier aggregation
  (deferable to v0.3 if no layout budget).
- Section ordering ("Asset Cards" block appears *after* all 4
  sections in v0.1; optionally move earlier — deferable).
- `glossary-plate` BHL item-layer vs. page-layer note (deferable;
  wording-only polish).
- `data/exhibition.json.forbidden_statuses_not_used` field
  strengthening (deferable; current gate is sufficient for v0.2).

## Acceptance gate before v0.2 implementation

Before any `git add` for v0.2 implementation is allowed, the
following must be true:

1. The changeset draft has been approved by an explicit
   `IMPLEMENT v5.6b` directive from the operator.
2. The fact-check matrix has been read end-to-end and every
   `wording-needs-precision` row is reflected in the changeset
   draft with the proposed new wording recorded verbatim.
3. The acceptance criteria document has been read end-to-end by
   the operator.

These are documented in
[`docs/SECOND_EXHIBITION_CONTENT_ACCEPTANCE_CRITERIA_v5.6.md`](SECOND_EXHIBITION_CONTENT_ACCEPTANCE_CRITERIA_v5.6.md).

## Rollback boundary

If after push, the post-push verification shows any of:

- root bytes / SHA drift,
- second-exhibition SHA drift (other than the expected 6-rewrite
  delta),
- image checksum failure,
- gate, dry-run, healthcheck, or browser-QA failure,
- status-phrase-count change,

the v0.2 push is rolled back via `git revert` of the v0.2 commit,
restoring the v0.1 page byte-identical.
