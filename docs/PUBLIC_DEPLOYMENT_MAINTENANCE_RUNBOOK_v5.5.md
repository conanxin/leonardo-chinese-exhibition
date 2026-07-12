# Public Deployment Maintenance Runbook

This runbook is the standard operating procedure for keeping the second
exhibition production surface stable after the v5.0-stable-freeze cycle.
It pairs with:

- `scripts/second_exhibition_production_healthcheck.py` (manual health check)
- `docs/PRODUCTION_HEALTH_BASELINE_v5.5.md` (frozen baselines)
- `docs/INCIDENT_RESPONSE_AND_ROLLBACK_v5.5.md` (incident response)

## Daily / manual quick check

Run before anything that touches `main`, and right after a Pages deploy
completes:

```bash
python3 scripts/second_exhibition_production_healthcheck.py
```

Exit codes:

- `0` — PASS
- `1` — check failure
- `2` — environment / network failure (cannot reach the host)

Optional machine-readable artefact:

```bash
python3 scripts/second_exhibition_production_healthcheck.py \
  --json-output /tmp/health.json
```

JSON keys:

- `timestamp_utc`, `root_url`, `second_url`
- `counts`: `{PASS, FAIL, WARN, INFO, ENV-ERR, TOTAL}`
- `latency_ms`: `{root, second}`
- `downloaded_bytes`: `{root, second}`
- `groups`: ordered map of check-group → array of per-check results
- `final_ok`: boolean

> **Status update — 2026-07-12 (v5.6c)**: default mode of the healthcheck
> now validates `second-exhibition-v0.2` (commit `6b7ee06`) directly. The
> `--candidate-v0.2` flag is a **deprecated alias** kept for one migration
> round (emits stderr `DEPRECATION NOTICE` and runs the default v0.2
> baseline). `--legacy-v0.1` is supported ONLY for explicit historical-fixture
> checks — do not point it at the current live URL. Each content iteration
> must perform a post-deploy verification round that promotes the default
> baseline.

A passing run should report:

- 1 root exact marker (`v2.9-real-source-rights-audit`)
- SHA-256 of live root = `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`
- SHA-256 of live second-exhibition index = `00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2` (**v0.2**, since v5.6c; was `7c05f39d…` under v0.1)
- `second-exhibition-v0.2` marker count = 3 (body data-marker + badge + footer-marker)
- `second-exhibition-v0.1` (stale) marker count = 0 (regression guard)
- 5 `production-deployed-v5.3`, 8 `published-in-v5.3`,
  8 `imported-not-deployed` (all in historical context), 0 `repository-only-not-deployed`
- 6 / 6 image SHA-256 matches
- 17 / 17 forbidden paths returning non-200
- Workflow safety checks all PASS
- Stable tag `v5.0-real-second-exhibition-deployment` is annotated and
  pinned to `ac0f19e2c03b09738ae49b4a15c629a1f2177068`

## Full verification before content changes

Before any change to `main` that touches the second exhibition (HTML, CSS,
JS, data, asset, manifest, workflow):

```bash
python3 scripts/template_quality_gate.py
python3 scripts/second_exhibition_build_gate.py
python3 scripts/second_exhibition_repository_qa.py
sha256sum -c second-exhibition/assets/asset-checksums.sha256

python3 scripts/second_exhibition_staging_build.py \
  --output /tmp/staging-artifact \
  --audit /tmp/staging-audit

python3 scripts/second_exhibition_staging_gate.py \
  --artifact /tmp/staging-artifact \
  --audit /tmp/staging-audit
```

For visual / interaction verification against the live surface (or a
local server that mirrors it), run the browser QA over the live URL:

```bash
SECOND_EXHIBITION_QA_URL="https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/" \
  node scripts/second_exhibition_browser_qa.mjs
```

Finally run the production health check.

## Any main push warning

Pushing to `main` triggers the Pages deploy workflow. The workflow:

1. Rebuilds the staging artifact into `runner.temp/leonardo-pages-artifact`.
2. Runs the staging gate.
3. Uploads the artifact and deploys via `actions/deploy-pages`.

**This means a documentation-only or script-only commit still redeploys
production Pages.** The deployed bytes come from the staging builder —
if the production HTML / CSS / JS / data / assets have not changed since
freeze, the deployed surface is byte-identical.

Before pushing to `main`:

- Confirm staging builder + gate are PASS.
- Confirm no file under `site/`, `second-exhibition/site/`,
  `second-exhibition/data/`, `second-exhibition/assets/`,
  `second-exhibition/docs/`, `second-exhibition/site/README.md`,
  `.github/workflows/`, or any of the six images / manifest /
  checksums file has been touched unless that was the *intended*
  content round.

After pushing to `main`:

- Wait for the Actions run to complete (`success`).
- Re-run the production health check. Exit 0 required.
- If the run's `downloaded_bytes` for root or second-exhibition index
  differ from baseline, **stop** and treat as P1.

## Stable baseline comparison

Cross-check the live surface against the frozen baseline after any deploy.

| Field | Baseline | Live at healthcheck |
|---|---|---|
| Root URL | https://conanxin.github.io/leonardo-chinese-exhibition/ | same |
| Root byte | 92,976 | must match |
| Root SHA-256 | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` | must match |
| Root exact marker count | 1 | must be 1 |
| Root loose `v2.9` count | 4 | informational |
| Second-exhibition URL | …/second-exhibition/ | same |
| Second-exhibition index byte | 25,635 | must match |
| Second-exhibition index SHA-256 | `7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c` | must match |
| `production-deployed-v5.3` | 5 | must match |
| `published-in-v5.3` | 8 | must match |
| `imported-not-deployed` | 8 (all in historical context) | must match |
| `repository-only-not-deployed` | 0 | must remain 0 |
| Six image SHA-256 | see baseline doc | must match |

## Allowed maintenance actions

These edits are routine and do not require a new controlled deployment
round. They should still pass all gates and the production health check
before pushing:

- Documentation additions / corrections (this runbook, the baseline doc,
  reports under `reports/`).
- QA-script and health-check improvements (under `scripts/`).
- New reports under `reports/` that summarise past activity.
- Non-destructive source / rights file review
  (`second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`,
  `second-exhibition/docs/RIGHTS_AND_SOURCES.md`).
- Adding / fixing safe-links in markdown.
- Updating `docs/V5_ROADMAP.md` and `README.md` to reflect completed
  maintenance rounds.

After any of the above changes, re-run the production health check, push,
wait for Actions success, then re-run the health check.

## Actions requiring a new controlled round

The following categories of change must go through a full round (analogous
to v5.3 / v5.3b / v5.3c) before becoming part of the live surface:

- Edits to any file under `second-exhibition/site/` (HTML / CSS / JS).
- Edits to `second-exhibition/data/*.json` (data structure or content).
- Adding, replacing, or removing an image asset under
  `second-exhibition/assets/images/`.
- Edits to `second-exhibition/assets/asset-import-manifest.json` or
  `second-exhibition/assets/asset-checksums.sha256`.
- Edits to `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` or
  `second-exhibition/docs/RIGHTS_AND_SOURCES.md`.
- Edits to `site/`.
- Edits to the Pages workflow under `.github/workflows/`.
- Any change to the public inventory shape or count.
- Any change to the status phrase semantics
  (`production-deployed-v5.3` / `published-in-v5.3` /
  `imported-not-deployed` / `repository-only-not-deployed`).
- Any change to URL paths (root, `/second-exhibition/`).

Such changes need their own dedicated deployment round (e.g. v5.6),
each with its own commit chain, freeze-style reconciliation, optional
browser QA, optional annotated tag, optional Release.

## Tag and Release rule

- Never move a stable tag. If the freeze needs to be retracted, publish a
  new tag pointing to the new commit; the old tag stays as a permanent
  record of the prior state.
- Never overwrite an existing Release. Add a new Release per stable tag.
- Backfill commits that evidence a freeze come **after** the freeze
  commit and **do not** modify the tag target.
- The health-check script does not require `gh` to PASS — its tag
  verification uses `git rev-parse` only. Use `gh release view` manually
  to confirm the GitHub Release if needed for an incident report.
