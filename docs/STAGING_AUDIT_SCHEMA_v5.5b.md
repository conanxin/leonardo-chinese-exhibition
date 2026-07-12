# v5.5b Staging Audit Schema (key-semantics-fix)

This document defines the staging audit JSON produced by
`scripts/second_exhibition_staging_build.py` and consumed by
`scripts/second_exhibition_staging_gate.py` and
`scripts/second_exhibition_deployment_dry_run.py`.

The schema version in force is **`"2.0"`**, recorded in the audit
summary as `schema_version: "2.0"`. The deprecated alias
`audit_schema_version: "2.0"` is also emitted for one round of
forward compatibility. v5.5b introduced this schema; earlier rounds
produced schema version `1` with an ambiguous key
(`source_index_html_sha256`).

This document was tightened in the **v5.5b-key-semantics-fix** round:

- The schema-version key is canonicalised to `schema_version`
  (`audit_schema_version` is now a deprecated alias).
- All per-source / per-staged identity blocks now use the explicit
  `_index_` infix on path / bytes / sha256 keys
  (`source_index_path`, `source_index_bytes`, `source_index_sha256`,
  `staged_index_path`, `staged_index_bytes`, `staged_index_sha256`).
- The ambiguous v1 key is renamed to
  `legacy_second_exhibition_source_index_html_sha256` (scope is baked
  into the field name itself; the `source_index_html_sha256_scope`
  companion key is removed).
- Bare `source_index_html_sha256` and `source_index_html_sha256_scope`
  keys are now treated as a fail-loud stale-audit signal.

## Problem

The v1 audit summary contained a key named
`source_index_html_sha256` whose **name** implied "the SHA of the root
site's `index.html`" but whose **value** was actually the SHA of the
second-exhibition source file `second-exhibition/site/index.html`.
The naming came from a stale variable inside the builder (`src_index`
referring to the rewritten source, not the root site).

The v1 schema also did not separately record:

- the explicit per-file source SHA for `site/index.html`,
- the staged-side SHA for the rewritten `second-exhibition/index.html`,
- the `source_equals_staged` boolean for either subtree,
- the `_scope` annotation that would have made the deprecated key
  unambiguous.

The misattribution propagated into at least one human-facing
historical document (the v5.0 release manifest, see the v5.5a
reconciliation report). v5.5b replaces the ambiguous key with
explicit per-source / per-staged nested blocks; v5.5b-key-semantics-fix
renames the carry-over key so its scope is self-evident and adds the
fail-loud policy on bare v1 keys.

## Correct identity model

```
root source     ──┐
                  │ byte-identical (no rewrite for site/*)
root staged     ──┤
                  │
root live       ──┘
                  │
                  ┌─ same SHA seen at: site/index.html,
                  │   staging-artifact/index.html,
                  │   https://conanxin.github.io/leonardo-chinese-exhibition/

second source   ──┐
                  │ differs (the builder performs 6 rewrites of
                  │   ../assets/images/ → ./assets/images/ in
                  │   the second-exhibition index only)
second staged   ──┤
                  │
second live     ──┘
                  │
                  ┌─ same SHA seen at: second-exhibition/site/index.html,
                  │   staging-artifact/second-exhibition/index.html,
                  │   https://conanxin.github.io/.../second-exhibition/
                  │
                  └─ different SHA from second source (because of
                      the 6 path rewrites)
```

The "identity equality" rules are therefore:

| Subtree                                       | `source_equals_staged` | Reason                                                |
|---|:---:|---|
| `root_site` (top-level `site/`)               | `true`  | Builder copies bytes without rewriting.               |
| `second_exhibition` (subtree under `second-exhibition/`) | `false` | Builder rewrites 6 image paths in `index.html`.       |

These two booleans are the canonical answer to the question "is the
source identical to the staged output for this subtree?". Misreading
either as `true` for the second-exhibition would mean the builder
silently regressed the rewrite step.

## Canonical identities (current freeze)

- **Root**
  - path: `site/index.html`
  - bytes: `92976`
  - SHA-256: `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`
- **Second-exhibition source**
  - path: `second-exhibition/site/index.html`
  - bytes: `25641`
  - SHA-256: `f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda`
- **Second-exhibition staged** (after 6 image-path rewrites)
  - path: `second-exhibition/index.html`
  - bytes: `25635`
  - SHA-256: `7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c`

## Schema v2 — full JSON shape (current)

The audit summary (`build-summary.json`) **must** contain, at minimum:

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

  "root_site_file_count": 25,
  "second_exhibition_public_file_count": 9,
  "path_rewrite_count": 6,
  "deployment_status": "staging-only-not-deployed",
  "source_commit": "<git SHA>",
  "build_time": "<ISO-8601 UTC>",
  "output_path": "<absolute path>",
  "audit_path":  "<absolute path>",

  "root_site_sha256": ["<64-hex>", ...],
  "second_exhibition_files": ["second-exhibition/index.html", ...],
  "staged_hashes": [{"path": ..., "sha256": ..., "bytes": ...}, ...],

  "legacy_second_exhibition_source_index_html_sha256":
    "f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda"
}
```

> The schema also re-emits the per-block identity under the un-suffixed
> alias names (`source_path` / `source_bytes` / `source_sha256`,
> `staged_path` / `staged_bytes` / `staged_sha256`) for one round of
> forward compatibility with internal gate code that referenced the
> previous v2 naming. New consumers MUST use the canonical
> `*_index_*` field names. The aliases will be dropped in the next
> schema-version bump.

## Strict invariants

These must hold for any v2 audit under normal build conditions:

- `schema_version == "2.0"` (or `audit_schema_version == "2.0"`).
- `root_site.source_index_path == "site/index.html"`.
- `root_site.staged_index_path == "index.html"`.
- `root_site.source_index_sha256 == root_site.staged_index_sha256`.
- `root_site.source_equals_staged == true`.
- `root_site.source_index_bytes == 92976`
  (under freeze conditions; the value is whatever the source file
  currently is).
- `second_exhibition.source_index_path == "second-exhibition/site/index.html"`.
- `second_exhibition.staged_index_path == "second-exhibition/index.html"`.
- `second_exhibition.source_index_sha256 != second_exhibition.staged_index_sha256`
  (the rewrite step changes bytes).
- `second_exhibition.source_equals_staged == false`.
- `second_exhibition.path_rewrite_count == 6`.
- `second_exhibition.staged_index_sha256 == sha256sum(staging/second-exhibition/index.html)`.
- The value under `root_site.source_index_sha256` is **never equal**
  to the value under `second_exhibition.source_index_sha256` under
  normal conditions (the two files differ by construction).
- The deprecated key `legacy_second_exhibition_source_index_html_sha256`
  (if present) must equal `second_exhibition.source_index_sha256`.
- Bare `source_index_html_sha256` MUST be absent (fail-loud).
- Bare `source_index_html_sha256_scope` MUST be absent (fail-loud).

These invariants are enforced by:

- `scripts/second_exhibition_staging_gate.py` (against the live audit).
- `scripts/second_exhibition_deployment_dry_run.py`
  (`B'. Schema v2 identity from audit` section).
- `scripts/test_second_exhibition_staging_audit.py` (in `/tmp`).

## Compatibility policy

The deprecated key pair is **preserved for one more release** so
any out-of-repo consumer of v1 audits keeps working. The forward path is:

| Field in v1                                                | Status in v2 (current)                          | Replace with |
|---|---|---|
| `schema_version: 1`                                        | replaced                                        | `schema_version: "2.0"` (canonical); `audit_schema_version: "2.0"` (deprecated alias) |
| `source_index_html_sha256`                                 | renamed, deprecated                             | `legacy_second_exhibition_source_index_html_sha256` (scope baked into field name) AND `second_exhibition.source_index_sha256` |
| `source_index_html_sha256_scope`                           | removed                                         | (scope is now baked into the legacy field name) |
| `root_site_sha256`                                         | retained                                        | nested `root_site.staged_index_sha256` covers the same value for the index; the flat list remains for the other 24 site files |
| `second_exhibition_files`                                  | retained                                        | unchanged |
| `path_rewrite_count`                                       | retained                                        | duplicated under `second_exhibition.path_rewrite_count` for tool discoverability |

When the next stage of the project decides to drop v1 support, the
deprecated keys can be removed in a single commit. Until then, the v2
schema (with `*_index_*` field names) is the canonical reference;
v1 keys are read-only compatibility carries, not load-bearing fields
for any new tooling.

## Reporting rule

Future reports and dashboards **must** separately report:

- root source SHA (from `root_site.source_index_sha256`)
- root staged SHA (from `root_site.staged_index_sha256`) — same value
- root live SHA (independently downloaded from
  `https://conanxin.github.io/leonardo-chinese-exhibition/`)
- second-exhibition source SHA (from `second_exhibition.source_index_sha256`)
- second-exhibition staged SHA (from `second_exhibition.staged_index_sha256`)
- second-exhibition live SHA (independently downloaded from
  `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`)

The bare string "source index SHA" with no scope qualifier is
**forbidden** as a unique field. Two distinct SHAs exist; both must
appear under their explicit scope.

## Schema-history rationale

The release manifest
`release-assets/v5.0-real-second-exhibition-deployment-manifest.md`
(line 61, frozen as part of the v5.0 stable release) recorded the
v1 key as "Source `site/index.html` SHA-256". The audit JSON's
explicit `_scope` annotation is the naming correction; the manifest
line itself is preserved unmodified for historical audit, because the
v5.5a reconciliation document is the authoritative source of truth
for the correction.

Future rounds must:

- Use `root_site.source_index_sha256` for the root site SHA.
- Use `second_exhibition.source_index_sha256` for the
  second-exhibition source SHA.
- Never copy `source_index_html_sha256` from a v1 audit and call it
  the root SHA in a new document.

The regression test
(`scripts/test_second_exhibition_staging_audit.py`) enforces both
the structural schema assertions and the
"root SHA ≠ second-exhibition SHA" check, plus the bare-key absence
checks and the schema-version name canonicalisation.
