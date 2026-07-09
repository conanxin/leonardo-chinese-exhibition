# Pilot Handoff

## What this pilot proves

This pilot demonstrates that the [`_template/`](../../template/) framework can be instantiated end-to-end:

- **`_template/` can be instantiated** — the four sections, four artifact cards, six glossary items, four deep-block types (deep-reading / material-evidence / visual-thinking / research-model), source / rights / curatorial docs all reproduce correctly.
- **A generic theme works without Leonardo-specific content** — the pilot uses a generic theme "一件作品的旅程" with no source-case dependencies.
- **Project-generated SVG can lower rights risk** — all three diagrams (`object-journey.svg`, `evidence-chain.svg`, `viewing-map.svg`) are CC0 1.0 project-generated, with explicit `template-source-note` and `template-credit-line` markings.
- **Source / rights / curatorial docs can be generated alongside the pilot** — `docs/RIGHTS_AND_SOURCES.md`, `docs/SOURCE_AUDIT_MANIFEST.md`, `docs/CURATORIAL_ESSAY_ZH.md`, `docs/DEEP_RESEARCH_NOTES_ZH.md` are present.
- **The template quality gate can check basic structure** — `scripts/template_quality_gate.py` runs 37 checks; this pilot passes structural sub-checks (4 sections, 4 artifact cards, 6 glossary items, 4 deep blocks, pilot-v0.1 marker).

## What this pilot does not prove

This pilot is a structural demonstration, not a publishable exhibition. It does **not** prove:

- **Real collection image rights have been resolved** — there are no real collection images; the pilot uses only project-generated SVG.
- **Formal exhibition content is deep enough** — body copy is generic and short, suitable for demonstration only.
- **Direct deployment readiness** — the pilot is repository-only; deploying it would require an explicit deployment round.
- **Replacement for formal source audit** — the `SOURCE_AUDIT_MANIFEST.md` here is a self-audit, not an independent third-party audit.
- **Replacement for formal release freeze** — the pilot's freeze (v3.1-real-second-exhibition-pilot) is a milestone, not a substitute for the live release freeze (v2.9-real-source-rights-audit on the live site).

## If turning into a real exhibition

A real exhibition must add the following on top of this pilot:

1. **Real subject research** — pick a concrete theme (artist / period / collection) and do primary research.
2. **Real sources** — collect image sources with institution, URL, identifier, license for each.
3. **Image authorization / source note / credit line** — for each image, fill `data/assets.json` with real `sourceType`, `sourceNote`, `creditLine`, `license`, `reusePermission`.
4. **More complete curatorial text** — body copy per section should reach 200–500 字 per USAGE_GUIDE_ZH.md guidance, with kicker / title / body / takeaway / viewer-action per section.
5. **Playwright UI check** — full Playwright suite covering desktop + mobile + lightbox + guided mode, with screenshots saved as evidence.
6. **Release notes / manifest / freeze report** — produce all three, matching the pattern in `docs/RELEASE_NOTES_v3.1_REAL_SECOND_EXHIBITION_PILOT.md` etc.
7. **Source rights audit** — independent audit of all sources, per `_template/SOURCE_RIGHTS_CHECKLIST_ZH.md`.

## Safe reuse instructions

When copying this pilot as a starting point for a new project:

1. **Change title / data / docs first** — replace "一件作品的旅程" with the new theme; rewrite `data/*.json` with new content; rewrite `docs/*.md` with new curatorial text.
2. **Keep source-rights checklist** — `docs/RIGHTS_AND_SOURCES.md` and `docs/SOURCE_AUDIT_MANIFEST.md` are the audit trail; keep them updated for any new image source.
3. **Re-run `template_quality_gate.py`** — `python3 scripts/template_quality_gate.py` must still PASS (37/37).
4. **Do not deploy un-audited pilots** — only deploy after a separate deployment round that includes a full source audit and freeze workflow.

## Quick links

- [README.md](README.md) — pilot overview
- [PILOT_QA_CHECKLIST.md](PILOT_QA_CHECKLIST.md) — QA checklist
- [docs/PILOT_QA_REPORT.md](docs/PILOT_QA_REPORT.md) — last QA report
- [docs/RELEASE_NOTES_PILOT.md](docs/RELEASE_NOTES_PILOT.md) — pilot release notes
- [../../template/USAGE_GUIDE_ZH.md](../../template/USAGE_GUIDE_ZH.md) — template usage guide
- [../../template/SOURCE_RIGHTS_CHECKLIST_ZH.md](../../template/SOURCE_RIGHTS_CHECKLIST_ZH.md) — source rights checklist
- [../../scripts/template_quality_gate.py](../../scripts/template_quality_gate.py) — quality gate script