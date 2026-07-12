# v5.5 Public Deployment Maintenance Report

This report records the v5.5 maintenance round: a manual, repeatable
production health check, a frozen production baseline, an operations
runbook, and an incident-response / rollback reference.

- **STATUS**: PASS
- **Baseline HEAD / origin**: `2ff17094904af23757643be4424f17f7f6a35770` (pre-push)
- **V5.5 commit (post-push HEAD / origin)**: `355a049703056a0834c69c6b283e1f28a4df306c`
- **V5.5 commit message**: `Add second exhibition production maintenance checks`
- **V5.5 Actions run**: `29174730791` (success, 22 s)
- **Stable tag object**: `c8871f09e4003675d5796c76058d589a08541f45`
- **Stable tag target (freeze commit)**: `ac0f19e2c03b09738ae49b4a15c629a1f2177068`
- **Tag pinned to freeze target**: confirmed (`git rev-parse v5.0-real-second-exhibition-deployment^{}` → `ac0f19e2c03b09738ae49b4a15c629a1f2177068`)
- **Release URL**: https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v5.0-real-second-exhibition-deployment
- **Release publishedAt**: `2026-07-12T00:29:43Z`

## Root baseline

- URL: https://conanxin.github.io/leonardo-chinese-exhibition/
- HTTP: **200**
- Byte size: **92,976 B**
- SHA-256: `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` (live byte-identical to `site/index.html`)
- Exact marker: `grep -o 'v2.9-real-source-rights-audit' | wc -l` → **1**
- Loose marker: `grep -o 'v2.9' | wc -l` → **4** (informational)

## Second exhibition baseline

- URL: https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/
- HTTP: **200**
- Byte size: **25,635 B**
- SHA-256: `7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c` (live byte-identical to staging artifact; the staging builder rewrites `./assets/images/` → `../assets/images/`, so live SHA differs from local `second-exhibition/site/index.html`)
- Title fragment present: `植物图谱与视觉分类`
- Phrase counts (live):

  | Phrase | Count | In historical context? |
  |---|---:|:---:|
  | `production-deployed-v5.3` | 5 | n/a (current) |
  | `published-in-v5.3` | 8 | n/a (current) |
  | `imported-not-deployed` | 8 | yes (Import record / asset-import-manifest) |
  | `repository-only-not-deployed` | 0 | n/a |

## Production healthcheck result

`python3 scripts/second_exhibition_production_healthcheck.py --json-output /tmp/v55-production-health.json` → **PASS** (exit 0)

- `total=73  pass=68  fail=0  warn=0  info=5  env_err=0`
- Root latency: 1580 ms
- Second-exhibition latency: 1334 ms
- Downloaded bytes: root 92,976 / second 25,635
- All 7 sections PASS:
  - A. Root production identity (HTTP 200, byte 92,976, SHA match, exact marker 1, byte-identical to `site/index.html`)
  - B. Second-exhibition identity (HTTP 200, byte 25,635, SHA match, all 4 phrase counts correct, `imported-not-deployed` only in historical context)
  - C. Public static files (8 / 8 — root `/`, `/index.html`, `/style.css`, `/script.js`, plus `second-exhibition/` and its three siblings)
  - D. Image integrity (18 / 18 — 6 images × {HTTP 200, MIME OK, SHA match})
  - E. Forbidden exposure boundary (17 / 17 — all forbidden paths 404)
  - F. Workflow static safety (8 / 8 — staging builder + gate, `--output`/`--audit`, `leonardo-pages-artifact`, configure/deploy, no audit upload, no root upload)
  - G. Stable release identity (3 / 3 + 1 INFO — tag exists, type `tag`, target `ac0f19e2c03b…`)

JSON output: valid (8 top-level keys: `timestamp_utc`, `root_url`, `second_url`, `counts`, `latency_ms`, `downloaded_bytes`, `groups`, `final_ok`).

## Browser viewport result

Public-URL browser QA (Chromium headless shell `148.0.7778.96`, ≥5 viewports, ≥4 environments) — re-run for v5.5 against
`https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`:

| Viewport | Sections | Cards | Glossary | Source notes | Credits | Imgs loaded | Overflow | console / page / failed / external |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1440×1000 | 4 | 6 | 12 | 6 | 6 | 6 / 6 | none | 0 / 0 / 0 / 0 |
| 1280×900 | 4 | 6 | 12 | 6 | 6 | 6 / 6 | none | 0 / 0 / 0 / 0 |
| 768×1024 | 4 | 6 | 12 | 6 | 6 | 6 / 6 | none | 0 / 0 / 0 / 0 |
| 390×844 | 4 | 6 | 12 | 6 | 6 | 6 / 6 | none | 0 / 0 / 0 / 0 |
| 320×700 | 4 | 6 | 12 | 6 | 6 | 6 / 6 | none | 0 / 0 / 0 / 0 |

Interactions / accessibility / no-JS / reduced-motion:

- Guided toggle: `aria-pressed` flips `false → true` ✓
- C-01 lightbox open, dialog accessible name `植物图谱与视觉分类` (via `#lightbox-title`), ESC closes, focus returns to trigger ✓
- C-06 click blocked (low-resolution warning shown) ✓
- Section-nav: 6 reachable links ✓
- Tab-reachable buttons: 6 ✓
- Alt coverage: 30 / 35 (5 intentional `alt=""` scaffolds for non-informative card icons) ≈ 85.7%
- Close button focused on open ✓
- Focus return after close ✓
- no-JS path: title + status + 6 cards + source notes + 6 credit lines + `.repository-status` all visible ✓
- reduced-motion (`prefers-reduced-motion: reduce`): lightbox open + ESC close ✓

The in-repo `scripts/second_exhibition_browser_qa.mjs` is wired to
`127.0.0.1:8770` and refuses public URLs by design; the public-URL
runner reuses the same logic without modifying the in-repo script.

## Image checksum result

`sha256sum -c second-exhibition/assets/asset-checksums.sha256` → **6 / 6 OK**

| File | SHA-256 (live ≡ source ≡ staging) |
|---|---|
| rijksmuseum-rp-f-f80313.jpg | `10762705aad12906…` |
| bhl-318921-page-603962-c03.webp | `446d744d9b647f29…` |
| smithsonian-nmnh-1529703.png | `75f523b06cc1a627…` |
| met-285149.jpg | `976b1cbd365a7dde…` |
| rijksmuseum-rp-f-f80152.jpg | `d3832eb3e6670658…` |
| bhl-318921-page-603998-c01.webp | `dc4b292536761be5b…` |

Each live image was also re-downloaded in the health check D section;
its SHA matches the source SHA in the checksums file.

## Forbidden boundary result

17 / 17 forbidden paths return HTTP **404**:

| Path | Status |
|---|---:|
| README.md | 404 |
| V4_ROADMAP.md | 404 |
| V5_ROADMAP.md | 404 |
| scripts/ | 404 |
| _template/ | 404 |
| _pilots/ | 404 |
| reports/ | 404 |
| release-assets/ | 404 |
| .github/ | 404 |
| .firecrawl/ | 404 |
| second-exhibition/data/ | 404 |
| second-exhibition/docs/ | 404 |
| second-exhibition/assets/asset-import-manifest.json | 404 |
| second-exhibition/assets/asset-checksums.sha256 | 404 |
| second-exhibition/README.md | 404 |
| second-exhibition/site/README.md | 404 |
| no-such-public-path-please-404/ | 404 |

The health-check script's environment-error guard ensures that any
network-layer failure is **not** mis-classified as a 404.

## Workflow safety result

`scripts/second_exhibition_production_healthcheck.py` section F reads
`.github/workflows/pages.yml` and confirms:

- The staging builder step exists.
- The staging gate step exists.
- The builder invocation uses both `--output` and `--audit`.
- The deploy uploads only `runner.temp/leonardo-pages-artifact`.
- The workflow uses `actions/configure-pages` and `actions/deploy-pages`.
- The audit directory is **not** uploaded as an artifact.
- The repository root is **not** uploaded as an artifact.

All 7 workflow-safety assertions: **PASS**.

## Maintenance docs

The three new documents are the canonical reference for operators
going forward:

- `docs/PRODUCTION_HEALTH_BASELINE_v5.5.md`
- `docs/PUBLIC_DEPLOYMENT_MAINTENANCE_RUNBOOK_v5.5.md`
- `docs/INCIDENT_RESPONSE_AND_ROLLBACK_v5.5.md`

Each document is referenced from `docs/V5_ROADMAP.md` and `README.md`.

## Incident rollback docs

`docs/INCIDENT_RESPONSE_AND_ROLLBACK_v5.5.md` defines:

- Severity levels (P0 / P1 / P2 / P3).
- Immediate checks (Actions, root / second-exhibition HTTP / byte /
  hash, image SHA, forbidden paths, workflow diff, JSON healthcheck).
- Rollback principles (revert commits only, no force push, do not
  move the stable tag, do not overwrite the Release).
- Three named rollback procedures:
  1. Latest content commit (single revert).
  2. Controlled deployment wiring
     (revert `5250404`, then `83ab6d8`, then `f84e53f` in that order).
  3. Freeze commit (single revert `ac0f19e`).
- Post-rollback verification (gates + healthcheck + browser QA +
  tag / Release / workflow diff).
- Evidence capture (file checklist + timeline).

## Protected paths

All git-tracked paths under the protection list have empty `git diff`
against the v5.4 head before this commit:

- `site/` — empty diff
- `second-exhibition/site/` — empty diff
- `second-exhibition/data/` — empty diff
- `second-exhibition/assets/` — empty diff (manifest, checksums, six
  images unchanged)
- `second-exhibition/docs/` — empty diff (SOURCE_AUDIT_MANIFEST.md,
  RIGHTS_AND_SOURCES.md unchanged)
- `.github/workflows/` — empty diff (pages.yml unchanged)
- existing `scripts/*` — empty diff for all pre-existing scripts;
  only new `second_exhibition_production_healthcheck.py` is added.
- `_template/`, `_pilots/`, `posts/`, `case-study/` — empty diff
- existing `release-assets/*` — empty diff (no pre-existing release
  asset files were touched)

## Production before push

Verified before staging any changes:

- HEAD = `2ff17094904af23757643be4424f17f7f6a35770`
- Origin/main = `2ff17094904af23757643be4424f17f7f6a35770`
- Tag `v5.0-real-second-exhibition-deployment` annotated, target
  `ac0f19e2c03b09738ae49b4a15c629a1f2177068`
- Live root 92,976 B / SHA `e2be1077…`
- Live second-exhibition 25,635 B / SHA `7c05f39d…`
- Status counts 5 / 8 / 8 / 0
- Six image SHA match `asset-checksums.sha256`
- Forbidden 17 / 17 → 404
- Browser QA 5 / 5 PASS, errors 0, overflow 0

## Production after push

Verified after the v5.5 commit `355a049703056a0834c69c6b283e1f28a4df306c`
pushed and Actions run `29174730791` completed (status: success, 22 s,
01:05:13 → 01:05:35 UTC):

- HEAD = `355a049703056a0834c69c6b283e1f28a4df306c`
- Origin/main = `355a049703056a0834c69c6b283e1f28a4df306c`
- Live root byte: **92,976** (Δ = 0)
- Live root SHA-256: `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`
  (matches pre-push, matches `site/index.html` byte-identical via `cmp -s`)
- Live second-exhibition byte: **25,635** (Δ = 0)
- Live second-exhibition SHA-256: `7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c`
  (matches pre-push)
- Status counts: `production-deployed-v5.3` = 5, `published-in-v5.3` = 8,
  `imported-not-deployed` = 8, `repository-only-not-deployed` = 0 (Δ = 0)
- Six image SHA-256: byte-identical to `asset-checksums.sha256` (Δ = 0)
- Forbidden paths: 17 / 17 → HTTP 404 (Δ = 0)
- Production healthcheck re-run:
  `python3 scripts/second_exhibition_production_healthcheck.py --json-output /tmp/v55-after-health.json`
  → PASS (exit 0), counts: `PASS=68, FAIL=0, WARN=0, INFO=5, ENV-ERR=0, TOTAL=73`
- Browser QA re-run over public URL:
  `node /tmp/qa/v5_3c_browser_qa.mjs`
  → 5 / 5 viewports PASS, console / page / failed / external = 0

## GitHub Actions

V5.5 push Actions run:

| Run ID | headSha | Status | Conclusion | Started | Finished | Duration |
|---|---|---|---|---|---|---|
| `29174730791` | `355a049703056a0834c69c6b283e1f28a4df306c` | completed | success | 2026-07-12T01:05:13Z | 2026-07-12T01:05:35Z | 22 s |

The Pages workflow rebuilt the staging artifact and redeployed via
the v5.3 wiring (unchanged). Because the v5.5 commit changes only
`scripts/`, `docs/`, `reports/`, `README.md`, and `docs/V5_ROADMAP.md`
— none of which feed into the staging artifact — the live surface is
byte-identical to the pre-push state.

## Tags / Releases

- `v5.0-real-second-exhibition-deployment`: unchanged, annotated at
  `c8871f09…`, target `ac0f19e2…`.
- 12 pre-existing tags (`v2.0-public-portfolio-case` through
  `v4.8-real-second-exhibition-repository-hardening`): unchanged.
- 12 pre-existing GitHub Releases: unchanged.
- No new tag or Release created in this round.

## Next recommended task

```
v5.6-second-exhibition-content-iteration
```

or continued maintenance, depending on the next content round. The
health-check, baseline, runbook, and incident-response / rollback
documents together form the durable support layer.

This report finalises v5.5 — see "Final output" further down for the
submitter-facing summary.
