# Pilot QA Checklist

## Identity

- **Pilot path**: `_pilots/second-exhibition-pilot/`
- **Pilot title**: 一件作品的旅程
- **Pilot version**: `pilot-v0.1`
- **Deployment status**: repository only, not deployed
- **Source template**: [`_template/`](../../template/)
- **Source release**: `v3.0-real-template-extraction-audit` (template base) + `v3.1-real-second-exhibition-pilot` (this pilot's own freeze)

## Structural checks

- [ ] Hero exists
- [ ] 3-minute guide exists
- [ ] Exhibition map exists
- [ ] Sections >= 4
- [ ] Artifact cards >= 4
- [ ] Glossary items >= 6
- [ ] Deep-reading block exists
- [ ] Material-evidence block exists
- [ ] Visual-thinking block exists
- [ ] Research-model block exists

## Data checks

- [ ] `data/exhibition.json` valid
- [ ] `data/sections.json` valid
- [ ] `data/glossary.json` valid
- [ ] `data/assets.json` valid
- [ ] assets `sourceType = project-generated`
- [ ] no forbidden terms in content layer

## Rights and source checks

- [ ] No real collection images
- [ ] No platform screenshots
- [ ] All diagrams are project-generated
- [ ] Rights doc exists (`docs/RIGHTS_AND_SOURCES.md`)
- [ ] Source audit doc exists (`docs/SOURCE_AUDIT_MANIFEST.md`)
- [ ] No external reuse claim beyond project-generated diagrams

## Render checks

- [ ] Local static server works
- [ ] Desktop no console errors (under `file://`)
- [ ] Mobile 390 no horizontal overflow
- [ ] SVG diagrams load (under `file://`)
- [ ] Lightbox / guided mode do not error if present

## Deployment checks

- [ ] Pilot title absent from live HTML
- [ ] `pilot-v0.1` absent from live HTML
- [ ] live byte unchanged
- [ ] no Pages deployment path changed

## How to run this checklist

1. Confirm structural counts with `python3 scripts/template_quality_gate.py` (this checks pilot structure as part of its 37 checks).
2. Open the pilot directly in a browser via `file://` URL, OR serve via `python3 -m http.server 8770 --directory _pilots/second-exhibition-pilot/site` and open `http://localhost:8770/`.
3. Record results in [`docs/PILOT_QA_REPORT.md`](docs/PILOT_QA_REPORT.md).
4. Do not deploy; do not modify the live site.

## See also

- [`PILOT_HANDOFF.md`](PILOT_HANDOFF.md) — handoff guide for turning this pilot into a real exhibition
- [`docs/PILOT_QA_REPORT.md`](docs/PILOT_QA_REPORT.md) — last QA report (v3.4 round)
- [`README.md`](README.md) — pilot overview