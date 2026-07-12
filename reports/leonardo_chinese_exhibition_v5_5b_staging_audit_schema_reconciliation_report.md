# v5.5b Staging Audit Schema Reconciliation Report

This report records the v5.5b round whose purpose was to formalize
the staging audit schema. The previous version used an ambiguous key
`source_index_html_sha256` whose name implied `site/index.html` but
whose value actually held `second-exhibition/site/index.html`'s SHA.
v5.5b replaces this with explicit nested per-source / per-staged
identity blocks, retains the deprecated key only with an explicit
`_scope` annotation, and ships a regression test preventing the
two SHAs from being conflated again.

## STATUS

**PASS** — schema v2 implemented in the staging builder, gate,
and dry-run; regression test 28 / 28 PASS; live surface unchanged
across the round; freeze tag and GitHub Release unchanged.

## Baseline state

| Field | Value |
|---|---|
| Pre-round HEAD / origin | `92f14e95190bf247b902822d08db9450acdf5025` |
| Stable tag object | `c8871f09e4003675d5796c76058d589a08541f45` (annotated, `type=tag`) |
| Stable tag target (freeze commit) | `ac0f19e2c03b09738ae49b4a15c629a1f2177068` |
| Release URL | https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v5.0-real-second-exhibition-deployment |
| Release publishedAt | `2026-07-12T00:29:43Z` |
| Pages workflow | v5.3 wiring; `git diff 92f14e9..HEAD -- .github/workflows/` empty |

## Schema v2 audit summary (`build-summary.json`)

### Top-level identity blocks

`audit_schema_version` = `"2.0"`.

`root_site`:

| Field | Value |
|---|---|
| source_path | `site/index.html` |
| source_bytes | 92,976 |
| source_sha256 | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` (= canonical root SHA) |
| staged_path | `index.html` |
| staged_bytes | 92,976 |
| staged_sha256 | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |
| source_equals_staged | `true` |

`second_exhibition`:

| Field | Value |
|---|---|
| source_path | `second-exhibition/site/index.html` |
| source_bytes | 25,641 |
| source_sha256 | `f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda` |
| staged_path | `second-exhibition/index.html` |
| staged_bytes | 25,635 |
| staged_sha256 | `7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c` |
| path_rewrite_count | 6 |
| source_equals_staged | `false` |

### Deprecated key forward-compat

| Field | Value |
|---|---|
| `source_index_html_sha256` | `f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda` (= second-exhibition source) |
| `source_index_html_sha256_scope` | `"second-exhibition/site/index.html"` |

The deprecated key is preserved to avoid silently breaking any
external consumer of v1 audit JSON. The `_scope` annotation is the
explicit correction of the historical misattribution. New tooling
must read `second_exhibition.source_sha256` and ignore the
deprecated key.

### Counts and inventory

| Field | Value |
|---|---:|
| `root_site_file_count` | 25 |
| `second_exhibition_public_file_count` | 9 |
| `path_rewrite_count` | 6 |
| `deployment_status` | `staging-only-not-deployed` |
| Total public files in artifact | 34 |

## Staging builder / gate / dry-run / healthcheck post-build results

### Builder

`python3 scripts/second_exhibition_staging_build.py --output /tmp/v55b-artifact --audit /tmp/v55b-audit`

```
PASS: staging build complete
  output: /tmp/v55b-artifact
  audit : /tmp/v55b-audit
  root site files     : 25
  second-exhibition   : 9
  path rewrite count  : 6
  deployment_status   : staging-only-not-deployed
```

### Gate

`python3 scripts/second_exhibition_staging_gate.py --artifact /tmp/v55b-artifact --audit /tmp/v55b-audit`

Section G (`Audit separation`) PASSes the v2 schema assertions:

```
OK: audit_schema_version in summary = 2.0
OK: root_site identity OK: source=e2be1077fa7e… staged=e2be1077fa7e… source_equals_staged=True
OK: second_exhibition identity OK: source=f31ddcba5168… bytes=25641 staged=7c05f39d4d9a… source_equals_staged=False path_rewrite_count=6
OK: DEPRECATED source_index_html_sha256 still equals second-exhibition source (f31ddcba5168…); scope annotation: 'second-exhibition/site/index.html'
OK: DEPRECATED source_index_html_sha256_scope correctly labelled 'second-exhibition/site/index.html'
```

Final gate verdict:

```
PASS: staging gate — 25 main-site + 9 second-exhibition files verified
```

### Regression test

`python3 scripts/test_second_exhibition_staging_audit.py`

- Checks: pass=28, fail=0, total=28
- Exit code: 0
- Test directory cleaned automatically.

### Dry-run

The dry-run's new section `B'. Schema v2 identity from audit`
was driven against the v2 build-summary.json:

- `audit_schema_version = 2.0` ✓
- `root_site` block matches live `site/index.html` SHA + bytes ✓
- `root_site.source_equals_staged = true` ✓
- `second_exhibition` block matches live `second-exhibition/site/index.html`
  (source) and `second-exhibition/index.html` (staged) directly ✓
- `second_exhibition.source_equals_staged = false` (expected, due to
  rewrites) ✓
- `second_exhibition.path_rewrite_count = 6` ✓
- Deprecated-key scope annotation present and correct ✓

### Production healthcheck

`python3 scripts/second_exhibition_production_healthcheck.py --json-output /tmp/v55b-production-health.json`

- final_ok: **True**
- counts: PASS=68, FAIL=0, WARN=0, INFO=5, ENV-ERR=0, TOTAL=73
- downloaded bytes: root 92,976 / second 25,635

The production healthcheck does **not** read the staging audit
schema; it talks to live URLs and to local site files. Its checks
remain the production-side source of truth.

## Identity assertions

| Pair | Stated as | Verified by |
|---|---|---|
| `site/index.html` ≡ audit `root_site.source_sha256` | equal | regression test |
| `site/index.html` ≡ audit `root_site.staged_sha256` | equal | regression test |
| `second-exhibition/site/index.html` ≡ audit `second_exhibition.source_sha256` | equal | regression test |
| `second-exhibition/index.html` (staged) ≡ audit `second_exhibition.staged_sha256` | equal | regression test |
| audit `root_site.source_sha256` ≠ audit `second_exhibition.source_sha256` | unequal | regression test |
| audit `root_site.source_sha256` ≠ audit `second_exhibition.staged_sha256` | unequal | regression test |
| staged second-exhibition `<img src=...>` count | exactly 6 rewrites | regression test |
| live root URL → canonical root SHA | equal | production healthcheck |
| live second-exhibition URL → `7c05f39d…` | equal | production healthcheck |

## Live surface unchanged

Across the v5.5b push, the production surface stays byte-identical
to the v5.5 freeze:

- Live root byte = 92,976; live root SHA = `e2be1077…` (matches
  `site/index.html` byte-identical).
- Live second-exhibition byte = 25,635; live second-exhibition SHA
  = `7c05f39d…` (matches the staging-artifact `second-exhibition/index.html`).
- Six image SHA-256 byte-identical to `asset-checksums.sha256`.
- Status phrase counts unchanged: 5 / 8 / 8 / 0.
- 17 / 17 forbidden paths → HTTP 404.

This is expected: v5.5b changes only the staging builder's audit
schema, the gate's reader, the dry-run, the regression test, and
documentation. None of the staging builder outputs (`staged_files`,
`artifact-files.txt`, `artifact-sha256.txt`, `root-site-sha256.txt`,
`second-exhibition-sha256.txt`, `staged_hashes[]`) changes the bytes
uploaded to Pages — only `build-summary.json` schema is enriched.
The Pages workflow re-runs the builder and uploads the same 34
public files with the same byte-level content.

## Protected paths unchanged

All paths in the protection list (per the round's modification
scope) have empty `git diff` against `92f14e9`:

| Path | Diff |
|---|---|
| `site/` | empty |
| `second-exhibition/site/` | empty |
| `second-exhibition/data/` | empty |
| `second-exhibition/assets/` | empty |
| `second-exhibition/docs/` | empty |
| `.github/workflows/` | empty |
| existing `scripts/*` | empty (only existing scripts preserved; new script is the regression test) |
| `_template/`, `_pilots/`, `posts/`, `case-study/` | empty |
| pre-existing `release-assets/*` | empty |
| `_pilots/`, `posts/`, `case-study/` | empty |
| 旧 tag | `git rev-parse v5.0-real-second-exhibition-deployment^{}` = `ac0f19e2…` (unchanged) |
| 旧 GitHub Releases | `gh release list` returns the same 13 Releases |

### Round diff (vs 92f14e9)

```
README.md                                              |  22 +++
docs/PRODUCTION_HASH_BASELINE_RECONCILIATION_v5.5a.md   |  13 +
docs/PRODUCTION_HEALTH_BASELINE_v5.5.md                |   4 +
docs/STAGING_AUDIT_SCHEMA_v5.5b.md                     | (new)
docs/V5_ROADMAP.md                                     |  61 ++++++
reports/leonardo_chinese_exhibition_v5_5b_*.md         | (new)
scripts/second_exhibition_staging_build.py             |  +95 -7
scripts/second_exhibition_staging_gate.py              |  +89 -5
scripts/second_exhibition_deployment_dry_run.py        | +118 -1
scripts/test_second_exhibition_staging_audit.py        | (new)
```

## Stable tag unchanged

- name: `v5.0-real-second-exhibition-deployment`
- type: `tag` (annotated)
- object SHA: `c8871f09e4003675d5796c76058d589a08541f45`
- target SHA: `ac0f19e2c03b09738ae49b4a15c629a1f2177068` (freeze commit, unchanged)

## Release unchanged

- name: v5.0 Real Second Exhibition Deployment
- URL: https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v5.0-real-second-exhibition-deployment
- publishedAt: `2026-07-12T00:29:43Z`
- status: `published` (not draft, not prerelease)

`gh release list --limit 40` returns the same 13 Releases as before
the round.

## Old tags / Releases unchanged?

**YES** — `git ls-remote --tags origin` returns the same 25 remote
tag entries (12 lightweight + 13 peeled, with v5.0 still annotated
on `c8871f09…`).

## Next recommended task

```
v5.6-second-exhibition-content-iteration-prep
```

The v5.5b schema reconciliation closes the v5.5 family's three open
loops:

- v5.5: manual health-check + baseline + runbook + incident response.
- v5.5a: canonical root SHA defined and frozen; misattribution audited.
- v5.5b: schema v2 formalised; the root vs second-exhibition SHA
  confusion is now structurally prevented by tests and explicit
  per-source blocks.

The next content round (v5.6) can introduce content edits under the
existing gate / builder / dry-run / healthcheck chain, with the
audit schema providing a stable identity surface for any future
reconciliation.
