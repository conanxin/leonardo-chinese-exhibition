# v5.6c Post-deploy Verification Report

- **Round**: v5.6c — Post-deploy verification + production health baseline promotion
- **Date**: 2026-07-12
- **Trigger**: v5.6b deployment of `second-exhibition-v0.2` to public Pages
- **Status**: PASS

## 1. Deployment baseline

- Pre-v5.6c HEAD: `6b7ee068b1cd50ae4c9c9613b1106ba65c4b0071`
- Pre-v5.6c origin/main: `6b7ee068b1cd50ae4c9c9613b1106ba65c4b0071`
- v5.6b deployment commit: `6b7ee068b1cd50ae4c9c9613b1106ba65c4b0071`
- v5.6b GitHub Actions run: `29181008324` (conclusion: success)
- Stable v5.0 tag: `v5.0-real-second-exhibition-deployment` → `ac0f19e2c03b09738ae49b4a15c629a1f2177068` (unchanged)
- Stable Release: https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v5.0-real-second-exhibition-deployment (unchanged)

## 2. Reality gate

| Check | Result |
|---|---|
| HEAD == origin/main | PASS (`6b7ee06`) |
| template_quality_gate | PASS |
| second_exhibition_build_gate | PASS |
| second_exhibition_repository_qa | PASS (166 / 0 / 0) |
| asset checksums | PASS (6/6) |
| tracked tree clean before edits | PASS |
| `.firecrawl/` ignored as expected | PASS |
| `.tmp-*` cleanup | PASS (none present) |
| `__pycache__` cleanup | PASS (none present) |

## 3. Healthcheck baseline promotion

| Aspect | Before v5.6c | After v5.6c |
|---|---|---|
| Default target version | v0.1 | **v0.2** |
| `SECOND_EXPECTED_BYTES` | `25635` | **`31452`** |
| `SECOND_EXPECTED_SHA256` | `7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c` | **`00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2`** |
| `SECOND_EXACT_MARKER` | n/a | `"second-exhibition-v0.2"` (count = 3) |
| `SECOND_STALE_MARKER` | n/a | `"second-exhibition-v0.1"` (count = 0; regression guard) |
| `--candidate-v0.2` flag | required for v0.2 | **deprecated alias** (one migration round, emits stderr `DEPRECATION NOTICE`) |
| `--legacy-v0.1` flag | n/a | supported only for explicit historical-fixture checks; **do not** point at current live |
| Daily maintenance flag | required | none (default mode) |

## 4. Default healthcheck result (live production)

- **PASS** (exit 0)
- 70 PASS / 0 FAIL / 0 WARNINGS / 5 INFO
- latency root: 1705 ms, latency second: 1360 ms
- downloaded bytes root: 92,976, downloaded bytes second: 31,452
- SHA match: root `e2be1077…`, second `00894e8d…`
- marker `second-exhibition-v0.2` count = 3
- stale marker `second-exhibition-v0.1` count = 0
- 14 glossary entries
- 6/6 image checksums OK
- 17/17 forbidden paths non-200 (audit)
- JSON: `/tmp/v56c-recheck-default.json`

## 5. Deprecated alias result

- `python3 scripts/second_exhibition_production_healthcheck.py --candidate-v0.2` → **PASS** (exit 0)
- 70 PASS / 0 FAIL — same numbers as default
- stderr: `DEPRECATION NOTICE: --candidate-v0.2 is a no-op alias since v5.6c. v0.2 is now the default production baseline (commit 6b7ee06). Running default v0.2 baseline.`
- JSON: `/tmp/v56c-recheck-alias.json`

## 6. Legacy mode result

- `python3 scripts/second_exhibition_production_healthcheck.py --legacy-v0.1` against current v0.2 production → correctly **FAIL** with 4 expected FAILs:
  - byte (25635 vs 31452)
  - SHA (`7c05f39d…` vs `00894e8d…`)
  - exact marker `second-exhibition-v0.1` (live count 0)
  - stale marker `second-exhibition-v0.2` (live count 3, expected 0)
- Proves dual-rail design: legacy mode is self-consistent for v0.1 historical fixtures, intentionally incompatible with current production.
- **Not** used for current production monitoring.

## 7. Production identity (verified live)

### Root

- bytes: **92,976**
- SHA256: `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`
- exact marker `v2.9-real-source-rights-audit`: 1

### Second exhibition

- marker: `second-exhibition-v0.2` (count = 3)
- bytes: **31,452**
- SHA256: `00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2`
- sections: 4
- artifact cards: 6
- glossary: 14
- images: 6

## 8. Public 5-viewport browser QA

Target: `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`

| Viewport | Result | Cards | Glossary | Images | Overflow | Console | Page | Failed | External |
|---|---|---|---|---|---|---|---|---|---|
| 1440×1000 | PASS | 6 | 14 | 6 | 0 | 0 | 0 | 0 | 0 |
| 1280×900 | PASS | 6 | 14 | 6 | 0 | 0 | 0 | 0 | 0 |
| 768×1024 | PASS | 6 | 14 | 6 | 0 | 0 | 0 | 0 | 0 |
| 390×844 | PASS | 6 | 14 | 6 | 0 | 0 | 0 | 0 | 0 |
| 320×700 | PASS | 6 | 14 | 6 | 0 | 0 | 0 | 0 | 0 |

### Interactions (all 5 viewports)

- guided toggle: PASS
- lightbox open: PASS
- lightbox accessible dialog name: PASS
- ESC close: PASS
- focus return: PASS
- C-06 lightbox exclusion: PASS (last card, no body image, no lightbox)
- section navigation: PASS

### Accessibility

- h1 count: 1
- img missing alt: 0
- button missing accessible name: 0
- dialog role + accessible name on lightbox: PASS

### Behavior

- no-JS: 6 cards, 14 glossary entries, 6 source notes, 6 credit lines, repo status visible, body text — PASS
- reduced-motion: lightbox open + ESC close under `prefers-reduced-motion: reduce` — PASS

## 9. No-touch confirmation

- `site/` — unchanged
- `second-exhibition/site/`, `second-exhibition/data/`, `second-exhibition/assets/`, `second-exhibition/docs/` — unchanged
- `.github/workflows/` — unchanged
- `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/` — unchanged
- Source / rights evidence — unchanged
- 6/6 image checksums identical
- Stable tag `v5.0-real-second-exhibition-deployment` — unchanged (still points at `ac0f19e2c03b…`)
- Stable Release — unchanged

## 10. Files modified by this round

- `scripts/second_exhibition_production_healthcheck.py` (v0.2 default + flags)
- `docs/SECOND_EXHIBITION_POST_DEPLOY_VERIFICATION_v5.6c.md` (new)
- `docs/PRODUCTION_HEALTH_BASELINE_v5.5.md` (v0.1 historical preserved + v0.2 current appended)
- `docs/PUBLIC_DEPLOYMENT_MAINTENANCE_RUNBOOK_v5.5.md` (default mode v0.2 + deprecation notes)
- `docs/V5_ROADMAP.md` (v5.6c section appended)
- `README.md` (v5.6c section appended)
- `reports/leonardo_chinese_exhibition_v5_6c_post_deploy_verification_report.md` (this file, new)

## 11. Production before / after this docs push

- **Before docs push**: live is already v5.6b-deployed v0.2 (31,452 B / `00894e8d…`).
- **After docs push** (this commit, no site/data/asset edits): live root and second-exhibition HTML are **byte-identical** to before — Pages workflow will only re-emit the same artifact. Healthcheck + 5-viewport QA must continue to PASS.

## 12. Next recommended task

- **v5.6-real-stable-freeze**
