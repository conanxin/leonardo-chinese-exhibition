# v5.5a Production Hash Baseline Reconciliation Report

This report records the v5.5a read-only round whose purpose was to
reconcile two conflicting SHA-256 values for `site/index.html` that
appeared across the v5.0 → v5.5 trail. The round is non-deploying: no
production content is touched, no tag is moved, no Release is
overwritten, and the staging builder is deliberately left unmodified
so future reruns reproduce the same misattribution and the same
correction.

## STATUS

**PASS** — five-source binary comparison establishes a single
canonical root SHA-256; the second hash is identified as an
attribution error with a known source; production surface,
stable tag, and GitHub Release are all unchanged.

## Baseline state

| Field | Value |
|---|---|
| Pre-round HEAD / origin | `9bd8107860d3419c0a686f5aa4a4a73de109d364` |
| Stable tag object | `c8871f09e4003675d5796c76058d589a08541f45` (annotated, `type=tag`) |
| Stable tag target (freeze commit) | `ac0f19e2c03b09738ae49b4a15c629a1f2177068` |
| Release URL | https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v5.0-real-second-exhibition-deployment |
| Release publishedAt | `2026-07-12T00:29:43Z` |
| Release status | published, not draft, not prerelease |
| Pages workflow | v5.3 wiring; `git diff 9bd8107..main -- .github/workflows/` empty |

## Five source paths

| Label | Path | Generation command |
|---|---|---|
| current-source | `/tmp/v55a-hash-audit/current-source-index.html` | `cp --preserve=mode,timestamps site/index.html` |
| current-head   | `/tmp/v55a-hash-audit/current-head-index.html`   | `git show HEAD:site/index.html` |
| stable-tag     | `/tmp/v55a-hash-audit/stable-tag-index.html`     | `git show v5.0-real-second-exhibition-deployment^{commit}:site/index.html` |
| staging        | `/tmp/v55a-hash-audit/staging-index.html`        | `python3 scripts/second_exhibition_staging_build.py --output ... --audit ...; cp <out>/index.html ...` |
| live           | `/tmp/v55a-hash-audit/live-index.html`           | `curl -L --fail --silent --show-error -H 'Accept-Encoding: identity' --connect-timeout 20 --max-time 120 https://conanxin.github.io/leonardo-chinese-exhibition/` |

## Five byte counts

All five files = **92,976 B**:

| Label | Bytes |
|---|---:|
| current-source | 92,976 |
| current-head   | 92,976 |
| stable-tag     | 92,976 |
| staging        | 92,976 |
| live           | 92,976 |

## Five SHA-256 results

All five files = **`e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`**:

| Label | SHA-256 |
|---|---|
| current-source | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |
| current-head   | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |
| stable-tag     | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |
| staging        | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |
| live           | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |

## Pairwise `cmp -s` results

All ten unordered pairs exit 0 (byte-identical):

| Pair | exit |
|---|---:|
| current-source ↔ current-head | 0 |
| current-source ↔ stable-tag   | 0 |
| current-source ↔ staging      | 0 |
| current-source ↔ live         | 0 |
| current-head ↔ stable-tag     | 0 |
| current-head ↔ staging        | 0 |
| current-head ↔ live           | 0 |
| stable-tag ↔ staging          | 0 |
| stable-tag ↔ live             | 0 |
| staging ↔ live                | 0 |

## Canonical SHA

`e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`

This hash satisfies the rule that all five sources must agree on
bytes, agree on SHA-256, and be pairwise byte-identical via `cmp -s`.
It is the only value declared canonical.

## Incorrect / inapplicable historical SHA

| Hash | What it actually is | Where it was wrongly attributed |
|---|---|---|
| `f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda` | SHA-256 of `second-exhibition/site/index.html` | `release-assets/v5.0-real-second-exhibition-deployment-manifest.md` line 61 records it as the SHA of "Source `site/index.html`". |

The wrong attribution comes from a misnamed audit key in
`scripts/second_exhibition_staging_build.py`. The variable `src_index`
in section D of the script points at
`src_se_site / "index.html"` (the **second-exhibition** source file),
but its hash is stored in the audit under the key
`source_index_html_sha256` — a name that implies `site/index.html`.
The script is intentionally not modified in this round; renaming the
key is a future improvement. The staging builder does write the correct
root site SHA elsewhere in the same audit (`root_site_sha256`,
`staged_hashes`), and the artifact itself is correct byte-for-byte.

## Occurrences audited

Recursive grep of `e2be1077…` and `f31ddcba…` across
`README.md docs reports release-assets scripts`:

- `e2be1077…` appears in 6 places, all consistent with the canonical
  value being the root site SHA: the maintenance runbook, the health
  baseline, the v5.5 maintenance report, and the production health
  check script.
- `f31ddcba…` appears in 1 place: the v5.0 release manifest line 61.
  It was used in that one document and nowhere else in the repo.

No other file claims a different root SHA.

## Root live / byte / marker sanity

| Field | Value |
|---|---|
| `GET /` HTTP | 200 |
| `wc -c` of live root | 92,976 |
| `sha256sum` of live root | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |
| `grep -o 'v2.9-real-source-rights-audit' \| wc -l` | 1 |
| `grep -o 'v2.9' \| wc -l` (loose) | 4 (informational) |

## Gates / healthcheck (re-run this round)

- `template_quality_gate.py`: PASS
- `second_exhibition_build_gate.py`: PASS
- `second_exhibition_repository_qa.py`: PASS (164 / 164)
- `sha256sum -c second-exhibition/assets/asset-checksums.sha256`: 6 / 6 OK
- `node --check second-exhibition/site/script.js`: clean
- `python3 scripts/second_exhibition_production_healthcheck.py`
  → final_ok=True, counts `PASS=68, FAIL=0, WARN=0, INFO=5, ENV-ERR=0, TOTAL=73`,
  downloaded bytes `root=92,976, second=25,635`

The v5.5 production healthcheck script (`scripts/second_exhibition_production_healthcheck.py`)
uses the canonical hash `e2be1077…` directly. Its section A
("Root production identity") reads the live root and compares against
that value; it would FAIL if the live root, the source root, and the
canonical baseline ever diverged.

## Production unchanged

The freeze and all v5.x deploys have kept the live root byte-identical
to `site/index.html`. The misattribution is a label error in the v5.0
release manifest; the underlying production content is the same hash
throughout.

- Live root byte = 92,976 B (= source byte-identical via `cmp -s`)
- Live second-exhibition byte = 25,635 B (= staging-artifact byte-identical via `cmp -s`)
- Six image SHA-256 byte-identical to `asset-checksums.sha256`
- Status phrase counts: `production-deployed-v5.3` = 5,
  `published-in-v5.3` = 8, `imported-not-deployed` = 8,
  `repository-only-not-deployed` = 0
- Forbidden paths: 17 / 17 → 404

## Protected paths unchanged

All paths in the v5.5a allowance list (and the broader protection list
carried over from v5.5) have empty `git diff` against `9bd8107`:

| Path | Diff |
|---|---|
| `site/` | empty |
| `second-exhibition/site/` | empty |
| `second-exhibition/data/` | empty |
| `second-exhibition/assets/` | empty |
| `second-exhibition/docs/` | empty |
| `.github/workflows/` | empty |
| existing `scripts/*` | empty (only existing scripts preserved) |
| `_template/` | empty |
| `_pilots/` | empty |
| `posts/` | empty |
| `case-study/` | empty |
| pre-existing `release-assets/*` | empty (only release manifest line 61 is preserved, but **no edits** are made to it; the manifest line is deliberately not modified; the correction lives in the reconciliation doc) |
| 旧报告正文 (`reports/`) | empty (all pre-existing reports are unchanged; only the new v5.5a reconciliation report is added) |

## Stable tag unchanged

- `v5.0-real-second-exhibition-deployment`
- type: `tag` (annotated)
- object SHA: `c8871f09e4003675d5796c76058d589a08541f45`
- target SHA: `ac0f19e2c03b09738ae49b4a15c629a1f2177068` (the freeze commit, unchanged)

`git rev-parse v5.0-real-second-exhibition-deployment^{}` matches the
freeze commit before the round and matches it after.

## Release unchanged

The GitHub Release `v5.0 Real Second Exhibition Deployment` is
untouched:

- URL: https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v5.0-real-second-exhibition-deployment
- publishedAt: `2026-07-12T00:29:43Z`
- status: `published` (not draft, not prerelease)
- body and binary attachments: unchanged

`gh release list --limit 40` returns the same 13 Releases as before
this round.

## Next recommended task

```
v5.6-second-exhibition-content-iteration-prep
```

(or continued maintenance / bug-fix in the staging builder audit key naming —
deferred to a future round because modifying the builder script is out
of scope for this read-only reconciliation).
