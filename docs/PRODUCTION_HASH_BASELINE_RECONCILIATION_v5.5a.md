# v5.5a Production Hash Baseline Reconciliation

This document reconciles the **root site** SHA-256 baseline. It was
created after the v5.5 maintenance round exposed two conflicting SHA-256
values in our earlier reports:

| Hash claimed to be `site/index.html` | First-seen in repo |
|---|---|
| `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` | `docs/PRODUCTION_HEALTH_BASELINE_v5.5.md`, all v5.5+ docs |
| `f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda` | `release-assets/v5.0-real-second-exhibition-deployment-manifest.md` (line 61) |

A direct five-source binary comparison (this round) confirms one hash
is canonical and the other is an attribution error.

## Problem

Two different SHA-256 values were recorded as "root `site/index.html`"
across the v5.0 → v5.5 trajectory. Both could not be simultaneously
correct for a byte-identical build of the same source file. We needed:

1. A single canonical root SHA-256.
2. A reproducible procedure anyone can re-run.
3. An attribution-correct mapping of where the wrong SHA came from.

## Method

Five sources were fetched/generated with explicit binary-safe tools.
No HTML parsing, no gzip, no clipboard, no text normalisation.

| Label | Path | How obtained |
|---|---|---|
| current-source | `/tmp/v55a-hash-audit/current-source-index.html` | `cp --preserve=mode,timestamps site/index.html` |
| current-head   | `/tmp/v55a-hash-audit/current-head-index.html`   | `git show HEAD:site/index.html` |
| stable-tag     | `/tmp/v55a-hash-audit/stable-tag-index.html`     | `git show v5.0-real-second-exhibition-deployment^{commit}:site/index.html` |
| staging        | `/tmp/v55a-hash-audit/staging-index.html`        | `python3 scripts/second_exhibition_staging_build.py --output ... --audit ...` then `cp .../index.html ...` |
| live           | `/tmp/v55a-hash-audit/live-index.html`           | `curl -L --fail --silent --show-error -H 'Accept-Encoding: identity' --connect-timeout 20 --max-time 120 https://conanxin.github.io/leonardo-chinese-exhibition/` |

For each file we recorded:

- `wc -c` for raw byte count.
- `sha256sum <file>` for the file-content SHA-256.
- `cmp -s <a> <b>` for every unordered pair (10 pairs total).

Then we declared the canonical SHA only if **all five sources produced
the same SHA-256 and were pairwise identical (`cmp -s` exit 0)**.

## Results

### File-level identity

| Source | Bytes | SHA-256 |
|---|---:|---|
| current-source | 92,976 | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |
| current-head   | 92,976 | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |
| stable-tag     | 92,976 | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |
| staging        | 92,976 | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |
| live           | 92,976 | `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc` |

### Pairwise `cmp -s` exit codes

All ten unordered pairs returned exit code 0 (byte-identical):

| Pair | cmp -s exit |
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

### Identical-to-canonical column

| Source | Identical to canonical |
|---|:---:|
| current-source | ✓ |
| current-head   | ✓ |
| stable-tag     | ✓ |
| staging        | ✓ |
| live           | ✓ |

## Canonical baseline

- **canonical root SHA-256**: `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`
- **canonical root byte size**: 92,976 B
- **exact v2.9 marker count**:
  `grep -o 'v2.9-real-source-rights-audit' <root.html> | wc -l` → **1**
- **loose v2.9 marker count**:
  `grep -o 'v2.9' <root.html> | wc -l` → **4** (informational only)

The canonical SHA is the only one that survives the five-source binary
comparison. The second hash in the table at the top of this document
is wrong, and the audit below documents the source of the error.

## Historical correction

### The second hash is a misattribution

The hash `f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda` was recorded in **one** repo file as the SHA-256 of `site/index.html`:

- `release-assets/v5.0-real-second-exhibition-deployment-manifest.md`, line 61.

```
- Source `site/index.html` SHA-256 (uncompressed) recorded by
  staging build's audit log as `f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda`.
```

That attribution is incorrect. The hash `f31ddcba…` is actually the
SHA-256 of a **different file**:

```
$ sha256sum second-exhibition/site/index.html
f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda  second-exhibition/site/index.html
$ sha256sum site/index.html
e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc  site/index.html
```

The hash that ends up under `source_index_html_sha256` in the staging
builder's audit JSON comes from the staging builder's section D. In
that section the variable named `src_index` actually points to
`src_se_site / "index.html"` (i.e. `second-exhibition/site/index.html`).
The same builder does write the correct root site SHA into a
different field of the same audit (`root_site_sha256[]`,
`root_site_files[]`); the root SHA is also exposed directly under
`staged_hashes[?path=="index.html"]`. The misnamed audit key is not a
content bug in the artifact (the staging builder copies
`site/index.html` byte-identical and the per-file hash list records the
correct value), and it is not a production exposure. The bug is in the
label that the audit JSON attaches to the second-exhibition source SHA,
which then propagated into the v5.0 release manifest line 61 as an
attribution to the wrong file.

We do **not** modify the staging builder in this round (out of scope;
deliberately excluded so that any later re-run reproduces the same
attribution and the same correction). Future rounds may rename the
audit key for clarity.

### Effects on live surface

- **stable tag**: `v5.0-real-second-exhibition-deployment` — unchanged
  in this round. Annotated tag object `c8871f09…` continues to point
  to freeze commit `ac0f19e2c03b09738ae49b4a15c629a1f2177068`.
- **GitHub Release v5.0**: unchanged (URL, status, publishedAt,
  body all unchanged).
- **live root content**: 92,976 B, SHA `e2be1077…`, byte-identical
  to `site/index.html` for every one of the v5.3 / v5.3b / v5.3c /
  v5.4 / v5.5 / v5.5a pushes this round checked.
- **live second-exhibition content**: 25,635 B, SHA `7c05f39d…`,
  byte-identical to the staging artifact's `second-exhibition/index.html`.

The hash disagreement is **purely a reporting / attribution error** —
it does **not** indicate production content drift and does **not**
represent any change to the live surface or to the freeze anchor.

### Affected historical documents (one occurrence only)

- `release-assets/v5.0-real-second-exhibition-deployment-manifest.md` (line 61)

The v5.0 manifest does not include a 64-char SHA for `site/index.html`
anywhere else, and the v5.0 release notes (`docs/RELEASE_NOTES_v5_0_REAL_SECOND_EXHIBITION_DEPLOYMENT.md`)
refer only to the byte count (92,976 B), not a SHA. The v5.4 freeze
report does not contain either hash. From v5.5 onwards the correct
`e2be1077…` value is what every reconciliation, health check, and
maintenance report uses.

The misattribution is preserved in the file's git history — we do
not rewrite the manifest in this round; the correction lives in this
reconciliation document, in the updated health baseline, and in the
new v5.5a reconciliation report. Subsequent reports must use the
five-source procedure below and must not copy the mis-named audit
key as `site/index.html` evidence.

## Prevention

To keep future rounds' root SHA clean:

1. **Always run the five-source comparison** before declaring a root
   SHA baseline in any document. The five labels are:

   - `current-source`
   - `current-head`
   - `stable-tag` (peel the annotated tag via `^{commit}`)
   - `staging` (via `python3 scripts/second_exhibition_staging_build.py`)
   - `live` (via `curl ... -H 'Accept-Encoding: identity'`)

2. **Always record these three numbers together** for the root:

   - `wc -c` (raw bytes)
   - `sha256sum` (file-content SHA-256)
   - `grep -o 'v2.9-real-source-rights-audit' | wc -l` (exact marker)

3. **Do not declare canonical** unless all five labels agree on bytes
   and on SHA-256 and all ten unordered `cmp -s` pairs exit 0.

4. **Never copy a hash from a prior report without re-running the
   comparison.** The v5.0 release manifest carried the misattributed
   hash forward exactly because it was inherited from an earlier draft.

5. **Never use the staging builder's `source_index_html_sha256` audit
   key as a stand-in for `site/index.html`'s SHA.** The current build
   stores `second-exhibition/site/index.html`'s SHA there. Use
   `root_site_sha256[]` or `staged_hashes[]` (filtered by
   `path == "index.html"`) instead.
