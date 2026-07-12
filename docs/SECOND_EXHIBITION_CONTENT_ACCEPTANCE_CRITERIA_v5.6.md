# v5.6 Second Exhibition Content Acceptance Criteria

> These criteria define the gate that the **v0.2 implementation**
> round (the round that follows the current planning round, named
> in the V5_ROADMAP as `v5.6b-content-iteration-implementation-prep`)
> must pass before its commit can be pushed.

> Every "PASS" line must come from a tool run in this round — not
> from previous-round evidence. The post-push verification is the
> last and most important check.

## Content

| # | Criterion | Source row | Required value |
|---|---|---|---|
| C-01 | Factual blockers | F-17 / I-01 | **0** (CHG-01 must be applied; Rijksprentenkabinet must NOT be misdescribed as a herbarium anywhere in `data/glossary.json`, `data/sections.json`, `data/assets.json`, or the four narrative docs) |
| C-02 | Unsupported claims | F-17 | **0** in  `data/glossary.json` `glossary-herbarium` |
| C-03 | Terminology blockers | I-02, I-03, I-04 | **0** (`glossary-print` cyanotype disambiguation present; `glossary-cyanotype` and `glossary-photogram` entries exist; `glossary-iiif` scopes the C-10 caveat) |
| C-04 | Section structure | — | = **4** (观察 / 分类 / 复制 / 再组织) |
| C-05 | Artifact roster | — | = **6** (C-01, C-03, C-06, C-08, C-09, C-10) |
| C-06 | Section → artifact mapping | `data/sections.json` `artifact_candidate_ids` | unchanged from v0.1 (S1={C-01}; S2={C-06,C-08}; S3={C-03,C-09,C-10}; S4={C-01,C-03,C-06,C-08,C-09,C-10}) |
| C-07 | Glossary count | `data/glossary.json` `items` length | in **12 – 16** (12 baseline, +2 if CHG-12 lands, up to 14; +2 more only if explicitly approved) |
| C-08 | Source notes (per asset) | `data/assets.json` `source_note` field | = **6** (one per asset; never empty) |
| C-09 | Credit lines (per asset) | `data/assets.json` `credit_line` field | = **6** (one per asset; never empty) |
| C-10 | Status phrase counts (live second-exhibition page) | rendered HTML | `production-deployed-v5.3 = 5` · `published-in-v5.3 = 8` · `imported-not-deployed = 8` · `repository-only-not-deployed = 0` (the four counts MUST match v0.1 exactly) |
| C-11 | Hero misdescription | I-10 / F-25 | the three deployment-status phrases are no longer in the hero region (CHG-09); status counts preserved elsewhere |
| C-12 | Section 1 disambiguation (watercolour ≠ specimen) | I-06 / CHG-02 | "水彩图版 ≠ 标本" distinction appears in Section 1 body |
| C-13 | Section 2 disambiguation (NMNH herbarium ≠ Met object) | I-07 / CHG-03 | distinction appears in Section 2 body |
| C-14 | Section 3 disambiguation (4 reproduction media) | I-08 / CHG-04 | distinction appears in Section 3 body |
| C-15 | Section 4 concrete examples | I-09 / CHG-05 | at least 4 concrete identifier examples appear in Section 4 body |
| C-16 | IVY APIs distinguished | I-04 / CHG-08 | `glossary-iiif` defines Image API vs. Presentation API explicitly |

## Data consistency

| # | Criterion | Required value |
|---|---|---|
| D-01 | `data/exhibition.json.version` | `second-exhibition-v0.2` |
| D-02 | `data/exhibition.json.marker` | `second-exhibition-v0.2` (matches D-01) |
| D-03 | HTML ↔ JSON candidate-ID consistency | every `C-NN` referenced in `site/index.html` must equal a `candidate_id` in `data/assets.json` and a candidate-id heading in `docs/SOURCE_AUDIT_MANIFEST.md` |
| D-04 | Titles ↔ identifiers ↔ institutions | unchanged per asset: each `data/assets.json.title`, `.identifier`, `.institution` matches the same-named `SOURCE_AUDIT_MANIFEST.md` row's "Source note" verbatim or expanded-wording only |
| D-05 | Status model (`production-deployed-v5.3` / `published-in-v5.3` / `imported-not-deployed` / `repository-only-not-deployed`) | per-asset values must remain `published-in-v5.3` (current) and `imported-not-deployed` (historical); status counts unchanged |
| D-06 | Forbidden-status discipline | none of `repository-only-not-deployed`, `approved`, `pending`, `draft` may appear as positive labels; they remain explicitly enumerated as "not used" |

## Assets

| # | Criterion | Required value |
|---|---|---|
| A-01 | Six image files | byte-identical to v4.5 import; SHA-256 unchanged |
| A-02 | Image checksum integrity | `sha256sum -c second-exhibition/assets/asset-checksums.sha256` → **6/6 OK** |
| A-03 | No new external images | no new asset added to `second-exhibition/assets/images/` and no new remote URL in `data/assets.json` |
| A-04 | No-image-data-sheet drift | `second-exhibition/assets/asset-import-manifest.json` byte-identical |

## Tooling gate (all PASS)

| # | Tool                                                         | Required |
|---|---|---|
| T-01 | `python3 scripts/template_quality_gate.py`                   | PASS |
| T-02 | `python3 scripts/second_exhibition_build_gate.py`            | PASS |
| T-03 | `python3 scripts/second_exhibition_repository_qa.py`         | PASS — 164/164 |
| T-04 | `python3 scripts/second_exhibition_staging_gate.py`          | PASS — schema v2, fail-loud absent |
| T-05 | `python3 scripts/second_exhibition_deployment_dry_run.py`    | PASS — §B' schema v2, base-path 14/14 OK, forbidden 16/16 OK, 34-byte roundtrip OK |
| T-06 | `python3 scripts/second_exhibition_production_healthcheck.py` | PASS, `final_ok=True`, 0 drift |
| T-07 | `python3 scripts/test_second_exhibition_staging_audit.py`    | PASS, ≥ 30 assertions, exit 0 |
| T-08 | `python3 scripts/second_exhibition_production_healthcheck.py` (post-push) | PASS, `final_ok=True`, 0 drift |
| T-09 | Live browser QA (5 viewports × 4 environments) | 5/5 PASS |

## Page-render expectations

| # | Criterion | Required value |
|---|---|---|
| P-01 | Live root `index.html` byte count | may change (CHG-09/10 affect page bytes); but live SHA must exactly equal canonical SHA of the just-pushed `site/index.html` |
| P-02 | Live second-exhibition bytes | 25,635 B (only the rewrites-applied shape); live SHA must equal the staged `second-exhibition/index.html` SHA |
| P-03 | Console / page / failed / external errors | 0 |
| P-04 | Overflow (any viewport) | 0 |
| P-05 | Interactions (lightbox, deep-block folding) | all OK |
| P-06 | Accessibility scan | basic (semantic heading hierarchy preserved) |
| P-07 | no-JS | page must remain readable without JS (the `data/*.json` loads via defer but core content lives in `site/index.html`) |
| P-08 | reduced-motion | CSS / no motion logic unchanged |

## Deployment guard

| # | Criterion                                                                                          |
|---|---|
| D-DEP-01 | prep approval before implementation (this planning round is the prep; v0.2 implementation must not begin without an explicit `IMPLEMENT v5.6b` directive). |
| D-DEP-02 | exact diff review before push — every file `git add`'d in the implementation round must be one of the 8 in this round's allowlist, OR explicitly added to the allowlist by the operator. |
| D-DEP-03 | controlled deployment — do not modify `site/` root; do not introduce new public files under `second-exhibition/` unless required by the implementation; do not bypass the staging builder. |
| D-DEP-04 | post-push production QA — the build gate, dry-run, and healthcheck must all be re-run after push; recording the run in the v0.2 implementation report. |
| D-DEP-05 | rollback commit plan — the v0.2 implementation commit must be revert-able with `git revert <commit>` to restore the v0.1 staging artifact byte-for-byte. |

## Source / rights / status boundary

| # | Criterion                                                                  |
|---|---|
| S-01 | `docs/SOURCE_AUDIT_MANIFEST.md` not modified by v0.2.                       |
| S-02 | `docs/RIGHTS_AND_SOURCES.md` not modified by v0.2.                         |
| S-03 | `second-exhibition/assets/asset-import-manifest.json` not modified.        |
| S-04 | `second-exhibition/assets/asset-checksums.sha256` not modified.             |
| S-05 | The "Public Domain" wording in `credit_line` per asset remains verbatim or stricter; do not loosen. |
| S-06 | The C-10 manifest 404 caveat wording in `viewing_note` remains present and reads as a *current-observation* (with implied re-verification cadence), not as a permanent outage. |
| S-07 | The status-phrase counts and forbidden-status discipline remain exactly as v0.1. |

## Authority gate

The v0.2 implementation round **must not start** until the operator
sends an explicit `IMPLEMENT v5.6b` directive. The implementer must
record the exact commit SHA in the round report and link back to
this criteria document.

If any criterion above is not met, the v0.2 implementation round
is **PARTIAL** and must be amended (not pushed) before another
push.
