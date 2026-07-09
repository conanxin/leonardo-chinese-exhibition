# v3.4 Real Second Exhibition Hardening — Release Notes

**Tag**: `v3.4-real-second-exhibition-hardening`
**Date**: 2026-07-09
**Status**: Hardening freeze — pilot only, no live change, no deployment
**Previous tag**: `v3.3-real-template-quality-gate` (object `fb35a5d9`, target `fce2efb`)

---

## What this release is

This release hardens `_pilots/second-exhibition-pilot/` into a **reusable pilot template**. It adds three QA / handoff documents and a hardening-notes appendix to the pilot README. The pilot itself remains **repository-only, not deployed**.

This is the **no-live-touch round**: the live site (`site/index.html`, `site/style.css`, `site/script.js`) is byte-identical to v3.3, `_template/` is byte-identical, and `posts/`, `case-study/`, and `release-assets/` are unchanged.

---

## Scope of change

### New files (3)

| File | Purpose |
|---|---|
| `_pilots/second-exhibition-pilot/PILOT_QA_CHECKLIST.md` | Structural / data / rights / render / deployment checklist for future pilot QA passes |
| `_pilots/second-exhibition-pilot/PILOT_HANDOFF.md` | What this pilot proves, what it does NOT prove, and safe-reuse instructions |
| `_pilots/second-exhibition-pilot/docs/PILOT_QA_REPORT.md` | Playwright Chromium measured QA report (file:// + http.server modes) |

### Modified files (4, append-only)

| File | Change |
|---|---|
| `_pilots/second-exhibition-pilot/README.md` | Appended "Hardening notes" section linking the three new docs |
| `docs/V3_TEMPLATE_ROADMAP.md` | Added `v3.4 Real Second Exhibition Hardening` section; v3.4 marked `Done` |
| `README.md` | Added `v3.4 Real Second Exhibition Hardening` summary block |
| `reports/leonardo_chinese_exhibition_v3_4_real_second_exhibition_hardening_report.md` | Round report |

### Explicitly NOT changed

- `site/index.html`, `site/style.css`, `site/script.js` — byte-identical to v3.3
- `_template/site/`, `_template/data/` — byte-identical to v3.3
- `_pilots/second-exhibition-pilot/site/`, `_pilots/second-exhibition-pilot/data/`, `_pilots/second-exhibition-pilot/assets/` — byte-identical to v3.1
- `posts/`, `case-study/` — unchanged
- All 9 prior tags — untouched
- All 9 prior GitHub Releases — untouched
- `release-assets/` (existing files) — unchanged

---

## Verification at freeze

| Check | Result |
|---|---|
| `python3 scripts/template_quality_gate.py` | **PASS, 37/37, exit code 0** |
| `git rev-parse HEAD == origin/main` | **PASS** (`81f5e92`) |
| working tree clean (`.firecrawl/` untracked) | **PASS** |
| Live byte size | **92,976 B** (unchanged vs v3.3) |
| Live `v2.9-real-source-rights-audit` marker | **1** |
| Live `image-placeholder-pro` count | **0** |
| Live `一件作品的旅程` (pilot title) | **0** |
| Live `script.js` HTTP | **200** |

### Local pilot render (Playwright Chromium, headless)

| Check | `file://` mode | `http://localhost:8770/` mode |
|---|---|---|
| page title contains `一件作品的旅程` | ✓ | ✓ |
| `section` count | 4 | 4 |
| `template-artifact-card` count | 4 | 4 |
| `template-glossary-item` count | 6 | 6 |
| `template-deep-block` count | 4 (1 per type) | 4 |
| `pilot-marker` present | ✓ | ✓ |
| `template-source-note` count | 4 | 4 |
| `template-credit-line` count | 4 | 4 |
| `<img src="*.svg">` natural size | 4 (800×280, 800×360, 800×320, 800×280) | **3 of 4 → 404** *(serving-model caveat)* |
| mobile 390 horizontal overflow | none | none |
| console errors | 0 | 3 *(the 3 SVG 404s)* |

**Serving-model caveat**: The pilot HTML uses `../assets/diagrams/*.svg` paths that resolve correctly under `file://` (where `..` traverses up from `site/` into `_pilots/second-exhibition-pilot/`) but 404 when served via `python3 -m http.server --directory _pilots/second-exhibition-pilot/site/` (where URL root strips the `..`). The pilot is structurally correct under its intended usage; the http.server path is a serving-model mismatch recorded in `PILOT_QA_REPORT.md`, not a pilot bug.

---

## Reality recovery rule

This freeze follows `RELEASE_WORKFLOW_ZH.md`: every claim is anchored by **(commit SHA + verified live byte + verified tag)** triple:

| Anchor | Value |
|---|---|
| freeze commit | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |
| tag name | `v3.4-real-second-exhibition-hardening` |
| tag object SHA | `bf9f5ddb1ce8c08f01b7e0c98fae26ef7f68cb41` |
| verified live byte | 92,976 B |
| verified tag target | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` |

---

## What the pilot proves (post-hardening)

- `_template/` can be instantiated into a new pilot project.
- A non-Leonardo theme (one artifact's journey) works structurally.
- `project-generated` SVG diagrams are sufficient to keep rights risk low.
- Source / rights / curatorial docs can ship with the pilot.
- `scripts/template_quality_gate.py` (37 checks) covers the structural baseline.

## What the pilot does NOT prove

- Real-collection image rights resolution.
- Sufficient depth for a real exhibition.
- Direct deployability.
- Replacement for formal `SOURCE_AUDIT_MANIFEST.md` + `RIGHTS_AND_SOURCES.md`.
- Replacement for formal release freeze on a real exhibition.

---

## Next recommended task

`v3.5-real-second-exhibition-pilot-instantiation` — instantiate the template into a third pilot using a different theme (e.g. 建筑史, 设计史, 手稿学) to prove horizontal template reuse beyond the Leonardo frame. Or, if a real-exhibition direction is chosen, `v4.0-real-second-exhibition-plan` to scope a formal source audit and rights negotiation.

---

## Audit trail

- Round brief: `task brief` for `v3.4-real-second-exhibition-hardening`
- Round report: `reports/leonardo_chinese_exhibition_v3_4_real_second_exhibition_hardening_report.md`
- Pilot QA: `_pilots/second-exhibition-pilot/docs/PILOT_QA_REPORT.md`
- Prior freeze: [`v3.3-real-template-quality-gate`](https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v3.3-real-template-quality-gate)