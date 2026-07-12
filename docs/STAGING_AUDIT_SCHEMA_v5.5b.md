# v5.5b Staging Audit Schema

This document defines the staging audit JSON produced by
`scripts/second_exhibition_staging_build.py` and consumed by
`scripts/second_exhibition_staging_gate.py` and
`scripts/second_exhibition_deployment_dry_run.py`.

The schema version in force is **`2.0`**, recorded in the audit
summary as `audit_schema_version: "2.0"`. v5.5b is the round that
introduced this schema; earlier rounds produced schema version `1`
with an ambiguous key (`source_index_html_sha256`).

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
explicit per-source / per-staged nested blocks, while preserving the
deprecated key (with explicit `_scope` annotation) for forward
compatibility.

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

| Subtree | `source_equals_staged` | Reason |
|---|:---:|---|
| `root_site` (top-level `site/`) | `true` | Builder copies bytes without rewriting. |
| `second_exhibition` (subtree under `second-exhibition/`) | `false` | Builder rewrites 6 image paths in `index.html`. |

These two booleans are the canonical answer to the question "is the
source identical to the staged output for this subtree?". Misreading
either as `true` for the second-exhibition would mean the builder
silently regressed the rewrite step.

## Schema v2 — full JSON shape

The audit summary (`build-summary.json`) must contain, at minimum:

```json
{
  "audit_schema_version": "2.0",

  "root_site": {
    "source_path": "site/index.html",
    "source_bytes": <int>,
    "source_sha256": "<64-hex>",
    "staged_path": "index.html",
    "staged_bytes": <int>,
    "staged_sha256": "<64-hex>",
    "source_equals_staged": true
  },

  "second_exhibition": {
    "source_path": "second-exhibition/site/index.html",
    "source_bytes": <int>,
    "source_sha256": "<64-hex>",
    "staged_path": "second-exhibition/index.html",
    "staged_bytes": <int>,
    "staged_sha256": "<64-hex>",
    "path_rewrite_count": 6,
    "source_equals_staged": false
  },

  "root_site_file_count": <int>,
  "second_exhibition_public_file_count": <int>,
  "path_rewrite_count": 6,
  "deployment_status": "staging-only-not-deployed",
  "source_commit": "<git SHA>",
  "build_time": "<ISO-8601 UTC>",
  "output_path": "<absolute path>",
  "audit_path": "<absolute path>",

  "root_site_sha256": ["<64-hex>", ...],
  "second_exhibition_files": ["second-exhibition/index.html", ...],
  "staged_hashes": [{"path": ..., "sha256": ..., "bytes": ...}, ...],

  "source_index_html_sha256": "<64-hex>",
  "source_index_html_sha256_scope": "second-exhibition/site/index.html"
}
```

The first three groups (`audit_schema_version`, `root_site`,
`second_exhibition`) are the canonical identity model. The remaining
fields are auxiliary counts, paths, and forward-compat carryover
from v1.

## Strict invariants

These must hold for any v2 audit under normal build conditions:

- `audit_schema_version == "2.0"`.
- `root_site.source_path == "site/index.html"`.
- `root_site.staged_path == "index.html"`.
- `root_site.source_sha256 == root_site.staged_sha256`.
- `root_site.source_equals_staged == true`.
- `root_site.source_bytes == 92976` (under freeze conditions;
  the value is whatever the source file currently is).
- `second_exhibition.source_path == "second-exhibition/site/index.html"`.
- `second_exhibition.staged_path == "second-exhibition/index.html"`.
- `second_exhibition.source_sha256 != second_exhibition.staged_sha256`
  (the rewrite step changes bytes).
- `second_exhibition.source_equals_staged == false`.
- `second_exhibition.path_rewrite_count == 6`.
- `second_exhibition.staged_sha256 == sha256sum(staging/second-exhibition/index.html)`.
- The value under `root_site.source_sha256` is **never equal** to
  the value under `second_exhibition.source_sha256` under normal
  conditions (the two files differ by construction).
- The deprecated key `source_index_html_sha256` (if present) must
  equal `second_exhibition.source_sha256`, and its companion
  `source_index_html_sha256_scope` must equal
  `"second-exhibition/site/index.html"`.

These invariants are enforced by:

- `scripts/second_exhibition_staging_gate.py` (against the live audit).
- `scripts/second_exhibition_deployment_dry_run.py`
  (`B'. Schema v2 identity from audit` section).
- `scripts/test_second_exhibition_staging_audit.py` (in `/tmp`).

## Compatibility policy

The deprecated key pair is **preserved for at least one release** so
any out-of-repo consumer of v1 audits keeps working. The forward path is:

| Field in v1 | Status in v2 | Replace with |
|---|---|---|
| `schema_version: 1` | replaced | `audit_schema_version: "2.0"` |
| `source_index_html_sha256` | retained, deprecated | `second_exhibition.source_sha256` for the value; `source_index_html_sha256_scope` for the scope |
| `root_site_sha256` | retained | nested `root_site.staged_sha256` covers the same value for the index; the flat list remains for the other 24 site files |
| `second_exhibition_files` | retained | unchanged |
| `path_rewrite_count` | retained | duplicated under `second_exhibition.path_rewrite_count` for tool discoverability |

When the next stage of the project decides to drop v1 support, the
deprecated keys can be removed in a single commit. Until then, the v2
schema is the canonical reference; v1 keys are read-only compatibility
carries, not load-bearing fields for any new tooling.

## Schema-history rationale

The release manifest
`release-assets/v5.0-real-second-exhibition-deployment-manifest.md`
(line 61, frozen as part of the v5.0 stable release) recorded the
v1 key as "Source `site/index.html` SHA-256". The audit JSON's
`_scope` annotation is the explicit naming correction; the manifest
line itself is preserved unmodified for historical audit, because the
v5.5a reconciliation document is the authoritative source of truth
for the correction.

Future rounds must:

- Use the nested `root_site.source_sha256` for the root site SHA.
- Use the nested `second_exhibition.source_sha256` for the second-
  exhibition source SHA.
- Never copy `source_index_html_sha256` from a v1 audit and call it
  the root SHA in a new document.

The regression test
(`scripts/test_second_exhibition_staging_audit.py`) enforces both
the structural schema assertions and the
"root SHA ≠ second-exhibition SHA" check.
