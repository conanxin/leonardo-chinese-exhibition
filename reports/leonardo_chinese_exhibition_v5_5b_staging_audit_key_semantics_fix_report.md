# v5.5b Staging Audit Key Semantics Fix — Report

## STATUS

**PASS** — staging audit schema v2 has been tightened: schema-version
field renamed to canonical `schema_version`, per-block identity fields
now use the explicit `*_index_*` infix, and the v1 ambiguous key has
been renamed to `legacy_second_exhibition_source_index_html_sha256`
with scope baked into the field name. Bare `source_index_html_sha256`
and `source_index_html_sha256_scope` are now absent (fail-loud policy).
Public artifact output is byte-identical to the v5.5a-baseline build;
production surface (live root + second-exhibition + 6 images) is
byte-identical to the post-v5.5a freeze; stable tag and Release are
unchanged.

## Baseline

- baseline HEAD: `92f14e95190bf247b902822d08db9450acdf5025`
  (v5.5a-stable-second-exhibition-content-iteration-prep)
- baseline origin/main: `92f14e95190bf247b902822d08db9450acdf5025`
- pre-round working-tree HEAD: `7462dc42bd3d9e1fb26b8714e54a8bf2ebc1da24`
  (intermediate v5.5b reconciliation round, in-scope carry-over)
- post-round HEAD: `e2eba50f6d6483bcc6f9d5f373e744c2271430ad`
  (Clarify staging audit root and exhibition hashes)

## Original ambiguous field

The v5.5a-baseline builder emitted a key named
`source_index_html_sha256` that actually stored the SHA of
`second-exhibition/site/index.html` (the rewritten-source SHA inside
the builder), not the SHA of the top-level `site/index.html`. This
ambiguous name led the v5.0 release manifest line 61 to misattribute
that value as the root index SHA. The carry-over was preserved in the
v5.5b reconciliation round (commit `7462dc4`) under the same name plus
a `_scope` companion field, but the naming remained ambiguous and
left a soft-compat fallback.

## Original actual value

```
source_index_html_sha256 = f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda
```

(= `second-exhibition/site/index.html`, NOT `site/index.html`)

## Canonical root SHA

```
SHA-256 = e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc
bytes   = 92976
path    = site/index.html
```

## Canonical second-exhibition source SHA

```
SHA-256 = f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda
bytes   = 25641
path    = second-exhibition/site/index.html
```

## Canonical second-exhibition staged SHA (post 6 rewrites)

```
SHA-256 = 7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c
bytes   = 25635
path    = second-exhibition/index.html  (after /assets/images → ./assets/images rewrite)
```

## Affected scripts (production-side)

- `scripts/second_exhibition_staging_build.py` — emitter of the
  audit JSON; renamed constant `AUDIT_SCHEMA_VERSION` →
  `SCHEMA_VERSION`; renamed top-level audit key
  `audit_schema_version` → canonical `schema_version` with
  `audit_schema_version` retained as deprecated alias; added
  `_index_` infix to all 6 identity fields inside `root_site` and
  `second_exhibition` blocks; renamed
  `source_index_html_sha256` → `legacy_second_exhibition_source_index_html_sha256`;
  removed `source_index_html_sha256_scope`.
- `scripts/second_exhibition_staging_gate.py` — main consumer;
  switched to canonical `schema_version` key (deprecated alias
  accepted); switched to `*_index_*` field names; added explicit
  fail-loud on missing canonical fields; reject bare v1 keys.
- `scripts/second_exhibition_deployment_dry_run.py` — secondary
  consumer (Section B'); same schema-version + field-rename updates
  + reject bare v1 keys.
- `scripts/test_second_exhibition_staging_audit.py` — regression
  test; updated to use canonical field names, assert bare v1 keys
  absent, assert renamed legacy key.
- `scripts/second_exhibition_production_healthcheck.py` — **not
  changed** (it does not read the staging audit schema; it pulls
  live URLs and SHA-validates the served HTML against the canonical
  values).

## Schema version before / after

| Stage              | `schema_version` / key              | Alias / deprecated key               | Bare v1 keys present? |
|---|---|---|---|
| v5.5a baseline     | `schema_version: 1` (integer)       | `audit_schema_version` not emitted   | `source_index_html_sha256` = second-source SHA (misattributable) |
| v5.5b (7462dc4)    | `audit_schema_version: "2.0"`       | n/a                                 | `source_index_html_sha256` present, `_scope` annotation present |
| **v5.5b-key-semantics-fix (this round)** | `schema_version: "2.0"` (canonical) | `audit_schema_version: "2.0"` (deprecated alias) | renamed to `legacy_second_exhibition_source_index_html_sha256` (bare v1 keys fail-loud) |

## Compatibility decision (per brief §3 option A)

**Chosen decision:** rename `source_index_html_sha256` →
`legacy_second_exhibition_source_index_html_sha256` for one round, keep
the value, remove the `_scope` companion key (scope is now in the
field name), and make the gate fail-loud on the bare v1 keys.

**Rationale:**

- The repo has one active consumer (`staging_gate.py`) and one
  secondary consumer (`deployment_dry_run.py`) plus the regression
  test (3 internal). External consumers are unknown — the v5.0
  release manifest is preserved unmodified under the historical-audit
  rule, so it does not constitute a live consumer.
- Option A (rename) is explicit and self-documenting: an external
  caller seeing the long field name immediately knows it is the
  second-exhibition source SHA, with no need to look up a `_scope`
  companion.
- Option B (delete outright) was rejected for one round to avoid
  silently breaking any untracked out-of-repo consumer.
- Fail-loud on the bare v1 keys means any internal tool, drift
  detector, or future commit that re-introduces the old name will be
  caught at gate time, not silently accepted.

## Audit JSON — before vs after

### BEFORE (v5.5a-baseline) — relevant keys

```json
{
  "schema_version": 1,
  "source_index_html_sha256": "f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda",
  "root_site": null,
  "second_exhibition": null
}
```

(Single ambiguous key, no nested blocks. The misattribution risk is
inherent: a reader who does not know the builder internals would
assume `source_index_html_sha256` is the root site SHA.)

### BEFORE (v5.5b reconciliation, commit `7462dc4`) — relevant keys

```json
{
  "audit_schema_version": "2.0",
  "root_site": {
    "source_path": "site/index.html",
    "source_sha256": "e2be1077...",
    "staged_sha256": "e2be1077...",
    "source_equals_staged": true
  },
  "second_exhibition": {
    "source_path": "second-exhibition/site/index.html",
    "source_sha256": "f31ddcba...",
    "staged_sha256": "7c05f39d...",
    "path_rewrite_count": 6,
    "source_equals_staged": false
  },
  "source_index_html_sha256": "f31ddcba...",
  "source_index_html_sha256_scope": "second-exhibition/site/index.html"
}
```

(Schema-version key renamed to `audit_schema_version`. Nested blocks
introduced. The bare `source_index_html_sha256` carried a companion
`_scope` annotation. Naming still ambiguous: the bare key alone,
absent the `_scope` annotation, conveys nothing about which subtree
it refers to.)

### AFTER (this round) — relevant keys

```json
{
  "schema_version": "2.0",
  "audit_schema_version": "2.0",

  "root_site": {
    "source_index_path":   "site/index.html",
    "source_index_bytes":  92976,
    "source_index_sha256": "e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc",
    "staged_index_path":   "index.html",
    "staged_index_bytes":  92976,
    "staged_index_sha256": "e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc",
    "source_equals_staged": true
  },

  "second_exhibition": {
    "source_index_path":   "second-exhibition/site/index.html",
    "source_index_bytes":  25641,
    "source_index_sha256": "f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda",
    "staged_index_path":   "second-exhibition/index.html",
    "staged_index_bytes":  25635,
    "staged_index_sha256": "7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c",
    "path_rewrite_count":  6,
    "source_equals_staged": false
  },

  "legacy_second_exhibition_source_index_html_sha256":
    "f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda"
}
```

(`schema_version` is canonical; `audit_schema_version` is a
deprecated alias. Each block uses the `*_index_*` field-name convention.
The legacy key's name carries its scope. Bare v1 keys
(`source_index_html_sha256`, `source_index_html_sha256_scope`) are
absent.)

## Artifact before/after (public surface, 0 drift)

| Metric                                          | v5.5a-baseline `/tmp/v55b-before-artifact` | this round `/tmp/v55b-after-artifact` | Match? |
|---|---:|---:|:---:|
| File count                                      | 34                              | 34                            | ✓ |
| Total bytes (sum)                               | 5825174                         | 5825174                       | ✓ |
| File path set                                   | (sorted)                        | (sorted)                      | ✓ identical |
| Per-file SHA-256 (`sha256sum`)                  | `/tmp/v55b-before-artifact.sha256` (34 lines) | `/tmp/v55b-after-artifact.sha256` (34 lines) | **34/34 byte-identical** (verified via `diff -u`, no output) |
| Root `index.html` bytes                         | 92976                           | 92976                         | ✓ |
| Root `index.html` SHA-256                       | `e2be1077…`                     | `e2be1077…`                   | ✓ |
| Second-exhibition `index.html` bytes            | 25635                           | 25635                         | ✓ |
| Second-exhibition `index.html` SHA-256          | `7c05f39d…`                     | `7c05f39d…`                   | ✓ |
| Six image SHA-256 (per `asset-checksums.sha256`) | matches `asset-checksums.sha256` (6/6 OK) | matches `asset-checksums.sha256` (6/6 OK) | ✓ |
| Forbidden leakage (docs / assets / manifests)  | 0                               | 0                             | ✓ |

The artifact's 34 files are byte-identical to the v5.5a-baseline
build. Only the audit JSON metadata has changed (schema version,
field names, deprecated key rename). **No public content drift.**

## Gate results (post-push verification)

| Gate / Tool                                              | Result      |
|---|---|
| `scripts/template_quality_gate.py`                       | PASS        |
| `scripts/second_exhibition_build_gate.py`                | PASS        |
| `scripts/second_exhibition_repository_qa.py`             | PASS (164/164, 0 fail, 0 warn) |
| `scripts/second_exhibition_staging_gate.py`              | PASS — all schema v2 identity checks OK |
| `scripts/second_exhibition_deployment_dry_run.py`        | PASS — base-path probes 14/14 OK, forbidden 16/16 OK, roundtrip 34 byte-identical, schema v2 §B' OK |
| `scripts/second_exhibition_production_healthcheck.py`    | PASS (68/73, fail=0, warn=0, final_ok=True) |
| `scripts/test_second_exhibition_staging_audit.py`        | PASS (30/30, exit 0) |
| `sha256sum -c second-exhibition/assets/asset-checksums.sha256` | 6/6 OK |

Regression test detail:
- `schema_version == 2.0` (or deprecated alias) ✓
- `root_site.source_index_path == "site/index.html"` ✓
- `root_site.staged_index_path == "index.html"` ✓
- `second_exhibition.source_index_path == "second-exhibition/site/index.html"` ✓
- `second_exhibition.staged_index_path == "second-exhibition/index.html"` ✓
- **bare `source_index_html_sha256` absent** ✓ (fail-loud policy)
- **bare `source_index_html_sha256_scope` absent** ✓ (fail-loud policy)
- `root_site.source_index_sha256` matches `sha256sum site/index.html` ✓
- `root_site.staged_index_sha256` matches `sha256sum staged root index.html` ✓
- `second_exhibition.source_index_sha256` matches `sha256sum second-exhibition/site/index.html` ✓
- `second_exhibition.staged_index_sha256` matches `sha256sum staged second-exhibition/index.html` ✓
- `root_site.source_equals_staged == True` ✓
- `second_exhibition.source_equals_staged == False` ✓
- `second_exhibition.path_rewrite_count == 6` ✓
- `root_site.source_index_sha256 != second_exhibition.source_index_sha256` ✓
- `root_site.source_index_sha256 != second_exhibition.staged_index_sha256` ✓
- deprecated `legacy_second_exhibition_source_index_html_sha256` equals `second_exhibition.source_index_sha256` ✓
- deprecated `legacy_*_sha256 != canonical root SHA` ✓
- staging build + gate + bytes / path-rewrite residue all PASS ✓

## Stale-audit fail-loud test

A fake v1 audit (`schema_version: 1`, no nested blocks, bare v1 keys
only) was fed to the staging gate. Result:
- gate exit code **1**
- single visible FAIL: `schema_version in summary = 1, expected '2.0'. v2 schema is required; missing field is fail-loud (no silent fallback).`

Confirms the gate has no silent fallback path.

## Production healthcheck (post-build, post-push)

```
checks: total=73 pass=68 fail=0 warn=0 info=5 env_err=0
latency root: 1658 ms
latency second: 1560 ms
downloaded bytes root: 92976
downloaded bytes second: 25635
FINAL STATUS: PASS
```

(Live root SHA = `e2be1077…`, live second-exhibition SHA = `7c05f39d…`.
All forbidden-boundary and status-phrase checks PASS.)

## Protected paths unchanged?

**YES.**

- `site/`, `second-exhibition/site/`, `second-exhibition/data/`,
  `second-exhibition/assets/`, `second-exhibition/docs/` — no
  changes (git diff shows only scripts + docs + README + V5_ROADMAP).
- `second-exhibition/assets/asset-import-manifest.json`,
  `asset-checksums.sha256` — unchanged.
- 6 image files — unchanged.
- `.github/workflows/` — unchanged.
- `_template/`, `_pilots/`, `posts/`, `case-study/`,
  `release-assets/` — untouched.
- Other scripts that were not in the v5.5b modification scope
  (`template_quality_gate.py`, `second_exhibition_build_gate.py`,
  `second_exhibition_repository_qa.py`,
  `second_exhibition_browser_qa.mjs`,
  `second_exhibition_asset_gate.py`,
  `second_exhibition_deployment_preflight.py`,
  `second_exhibition_deployment_dry_run_browser.mjs`,
  `second_exhibition_production_healthcheck.py`) — unchanged.

## Workflow unchanged?

**YES.** `.github/workflows/` has zero modifications this round.

## Stable tag unchanged?

**YES.** `git rev-parse v5.0-real-second-exhibition-deployment^{}` =
`ac0f19e2c03b09738ae49b4a15c629a1f2177068` (frozen by v5.5a; matches
the expected freeze target).

## Release unchanged?

**YES.** `gh release view v5.0-real-second-exhibition-deployment`
URL: `https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v5.0-real-second-exhibition-deployment`,
`publishedAt`: `2026-07-12T00:29:43Z`, `isDraft`: false,
`isPrerelease`: false.

## Public content drift

**0.** The 34-file staging artifact built this round is byte-identical
to the v5.5a-baseline build. Push triggers the workflow but the served
HTML bytes match the freeze tag's published content exactly.

## Next

```
v5.6-second-exhibition-content-iteration-prep
```
