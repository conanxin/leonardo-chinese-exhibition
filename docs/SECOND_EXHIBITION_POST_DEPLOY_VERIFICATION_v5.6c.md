# v5.6c Second Exhibition v0.2 Post-deploy Verification

## Deployment identity

- v5.6b deployment commit: `6b7ee068b1cd50ae4c9c9613b1106ba65c4b0071`
- v5.6b GitHub Actions run: `29181008324` (conclusion: success)
- Root URL: https://conanxin.github.io/leonardo-chinese-exhibition/
- Second exhibition URL: https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/
- Stable v5.0 tag: `v5.0-real-second-exhibition-deployment` → `ac0f19e2c03b09738ae49b4a15c629a1f2177068` (unchanged initial-deployment anchor)
- Stable Release: https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v5.0-real-second-exhibition-deployment (unchanged)

## Production identity (post v5.6b / pre v5.6c docs push)

### Root

- HTTP 200
- bytes: **92,976**
- SHA256: `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`
- exact v2.9 marker: 1

### Second exhibition (v0.2)

- HTTP 200
- version marker: `second-exhibition-v0.2` (count = 3: body data-marker + badge + footer-marker)
- bytes: **31,452**
- SHA256: `00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2`
- sections: 4
- artifact cards: 6
- glossary entries: 14
- images: 6/6
- stale v0.1 marker: 0 (regression guard)
- status counts: production live (no errors)

## Healthcheck baseline promotion

### Before v5.6c

- `scripts/second_exhibition_production_healthcheck.py` default mode validated `second-exhibition-v0.1`:
  - `SECOND_EXPECTED_BYTES = 25635`
  - `SECOND_EXPECTED_SHA256 = 7c05f39d…`
  - no `--candidate-v0.2` flag existed
- Running default against current v0.2 production would FAIL (byte/SHA mismatch by definition).

### After v5.6c

- Default mode validates **`second-exhibition-v0.2`**:
  - `SECOND_EXPECTED_BYTES = 31452`
  - `SECOND_EXPECTED_SHA256 = 00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2`
  - `SECOND_EXACT_MARKER = "second-exhibition-v0.2"` (count = 3)
  - `SECOND_STALE_MARKER = "second-exhibition-v0.1"` (count = 0) — regression guard
- `--candidate-v0.2` retained as **deprecated alias** — identical behavior to default, emits stderr `DEPRECATION NOTICE`.
- `--legacy-v0.1` retained ONLY for explicit historical-fixture checks. Do not point at current live.
- Daily maintenance巡检 no longer requires the candidate flag.

## Default healthcheck result (live production)

- **PASS** (exit 0)
- 70 PASS / 0 FAIL / 0 WARNINGS / 5 INFO
- latency root: 1705 ms
- latency second: 1360 ms
- downloaded bytes root: 92,976
- downloaded bytes second: 31,452
- SHA match: root `e2be1077…`, second `00894e8d…`
- marker `second-exhibition-v0.2` count = 3
- stale marker `second-exhibition-v0.1` count = 0
- glossary = 14
- image checksums: 6/6 OK
- forbidden paths: all 404 (path-scoped privacy audit)

## Deprecated alias result

- `python3 scripts/second_exhibition_production_healthcheck.py --candidate-v0.2` → **PASS** (exit 0)
- 70 PASS / 0 FAIL — same numbers as default
- stderr emits: `DEPRECATION NOTICE: --candidate-v0.2 is a no-op alias since v5.6c. v0.2 is now the default production baseline (commit 6b7ee06). Running default v0.2 baseline.`
- Kept for one round to allow external scripts to migrate; will be removed in a future cleanup round (not in v5.6c).

## Legacy mode result

- `python3 scripts/second_exhibition_production_healthcheck.py --legacy-v0.1` against current v0.2 production → **correctly FAIL** (4 expected FAILs: byte 25635 vs 31452, SHA `7c05f39d…` vs `00894e8d…`, marker v0.1 absent, stale v0.2 present)
- Proves dual-rail design: legacy mode is self-consistent for v0.1 historical fixtures, intentionally incompatible with current production.
- **Not** used for current production monitoring.

## Live browser QA (5 viewports, public URL)

Target: https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/

| Viewport | Result | Cards | Glossary | Images | Overflow | Console Err | Page Err | Failed Req | External Req |
|---|---|---|---|---|---|---|---|---|---|
| 1440×1000 | PASS | 6 | 14 | 6 | 0 | 0 | 0 | 0 | 0 |
| 1280×900 | PASS | 6 | 14 | 6 | 0 | 0 | 0 | 0 | 0 |
| 768×1024 | PASS | 6 | 14 | 6 | 0 | 0 | 0 | 0 | 0 |
| 390×844 | PASS | 6 | 14 | 6 | 0 | 0 | 0 | 0 | 0 |
| 320×700 | PASS | 6 | 14 | 6 | 0 | 0 | 0 | 0 | 0 |

### Interactions (5/5 viewports)

- guided toggle: PASS
- lightbox open: PASS
- lightbox accessible dialog name: PASS
- ESC close: PASS
- focus return: PASS
- C-06 lightbox exclusion: PASS (last card; no body image, no lightbox)
- section navigation: PASS

### Accessibility

- h1 count: 1
- img missing alt: 0
- button missing accessible name: 0
- dialog role + accessible name on lightbox: PASS

### Behavior

- no-JS: 6 cards, 14 glossary entries, 6 source notes, 6 credit lines, repo status visible, body text rendered — PASS
- reduced-motion: lightbox opens + ESC closes correctly under `prefers-reduced-motion: reduce` — PASS
- overflow: 0 across all 5 viewports
- console errors: 0
- page errors: 0
- failed requests: 0
- external requests: 0 (all assets served from same origin)

## No-touch confirmation

- `site/` — unchanged
- `second-exhibition/site/` — unchanged
- `second-exhibition/data/` — unchanged
- `second-exhibition/assets/` — unchanged (6/6 checksums identical)
- `second-exhibition/docs/` — unchanged
- `.github/workflows/` — unchanged
- `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/` — unchanged
- Source / rights evidence — unchanged
- Stable tag `v5.0-real-second-exhibition-deployment` — unchanged (still points at `ac0f19e2c03b…`)
- Stable Release — unchanged

## Next

- v5.6-real-stable-freeze
