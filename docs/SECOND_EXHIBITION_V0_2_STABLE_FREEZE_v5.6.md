# v5.6 Stable Freeze — Second Exhibition v0.2

> This document is the freeze manifest for the publicly deployed,
> reproducible-verified `second-exhibition-v0.2` surface. It is the
> canonical description of what is being frozen, why it is stable,
> and which previous anchors it preserves.

## Stable release identity

- proposed annotated tag: **`v5.1-real-second-exhibition-v0.2`**
- proposed Release title: **`v5.1 Real Second Exhibition v0.2`**
- the tag **must** target the commit that contains this document
  (the freeze commit, to be recorded in the backfill report)
- previous stable tag `v5.0-real-second-exhibition-deployment` is
  preserved as the initial-deployment anchor; **it is not moved,
  rewritten, or deleted**.

## Commit chain (pre-freeze)

| Role | Commit | Subject |
|---|---|---|
| content deployment | `6b7ee068b1cd50ae4c9c9613b1106ba65c4b0071` | Implement second exhibition v0.2 content iteration (v5.6b) |
| production health baseline | `fff6e785db8c86e06ecad823a3e3ba4c28301cb8` | Promote v0.2 production health baseline |
| browser QA reproducibility | `f43c5479f8cee50e95435766e63bb5fb1e6ecfb9` | Make live browser QA reproducible |
| **freeze commit** | (this commit; recorded in backfill report) | Freeze verified second exhibition v0.2 release |
| evidence backfill | (post-tag; **must not** become tag target) | Backfill v5.1 stable freeze evidence |

The freeze commit is a documentation-only commit. It changes no
production content, no data, no asset, no workflow, no source /
rights evidence, no check manifest.

## Production identity (this round)

### Root

- URL: `https://conanxin.github.io/leonardo-chinese-exhibition/`
- HTTP: `200`
- bytes: **92,976**
- SHA256: `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`
- exact marker `v2.9-real-source-rights-audit`: **1**
- live probe was byte-identical to the staged artifact and to the
  committed `site/index.html` source.

### Second exhibition (v0.2)

- URL: `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`
- HTTP: `200`
- marker: `second-exhibition-v0.2` (count = 3, body data-marker + badge + footer-marker)
- stale v0.1 marker count: **0** (regression guard)
- live bytes: **31,452**
- live SHA256: `00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2`
- staged bytes / SHA: 31,452 / `00894e8d…` (byte-identical to live)
- committed source bytes / SHA: 31,458 / `662bee42799a5e92fb7407a37d2fe57d02bfd123a344cbeada0cb51b99c5030e`
  (differs from live by 6 path rewrites performed by the staging
  builder; the byte-difference is intentional and audited)

## Content identity (this round)

| Field | Value |
|---|---|
| version marker | `second-exhibition-v0.2` |
| sections | 4 |
| artifact cards | 6 |
| glossary entries | 14 |
| public images | 6 / 6 |
| source notes | 6 |
| credit lines | 6 |
| C-06 lightbox | disabled (low-resolution, 90×90 NMNH thumbnail) |

## Quality gates (this round)

| Gate | Result |
|---|---|
| `template_quality_gate` | PASS |
| `second_exhibition_build_gate` | PASS |
| `second_exhibition_repository_qa` | **166 / 0 / 0** (PASS / FAIL / WARNINGS) |
| `second_exhibition_production_healthcheck` (default mode) | **70 / 0** (PASS / FAIL) |
| 6 asset SHA-256 matches | **6 / 6 OK** |
| `node --check second-exhibition/site/script.js` | OK |
| `node --check scripts/second_exhibition_browser_qa.mjs` | OK |
| JSON: `exhibition.json` / `sections.json` / `glossary.json` / `assets.json` | 4 / 4 valid |

## Staging + dry-run (this round)

- `staging_build` PASS
  - root site files: 25
  - second-exhibition files: 9
  - path rewrite count: 6
  - deployment status: `staging-only-not-deployed`
- `staging_gate` PASS (schema 2.0; source `662bee…` → staged `00894e8d…`)
- `deployment_dry_run` PASS
  - base path: `/leonardo-chinese-exhibition`
  - allowlist probes: 14 / 14
  - forbidden probes: 16 / 16
  - roundtrip files: **34 / 34 byte-identical**
  - tar size: 5,804,961 bytes
  - deployment status: `dry-run-only-not-deployed`

## Browser QA (this round, official runner only)

- official runner: `scripts/second_exhibition_browser_qa.mjs`
- local exact-base-path: 3 consecutive runs, **3 / 3 PASS**,
  5/5 viewports, imgsLoaded `[6, 6, 6, 6, 6]`, 0 errors, 0 overflow
- production: 3 consecutive runs, **3 / 3 PASS**, 5/5 viewports,
  imgsLoaded `[6, 6, 6, 6, 6]`, 0 errors, 0 overflow
- interactions PASS in all 6 runs: guidedToggle, lightboxOpen,
  lightbox role=dialog, accessible name `lightbox-title`, close
  button focus, ESC close, focus return, C-06 lightbox exclusion,
  section navigation, tab focusable
- a11y PASS in all 6 runs: h1=1, missing alt=0, button missing
  accessible name=0, no heading jump
- no-JS PASS in all 6 runs: 6 cards, 6 source notes, 6 credit
  lines, repo status visible, body text rendered
- reduced-motion PASS in all 6 runs: lightbox opens + ESC closes

## Security boundary (this round)

- public inventory: 25 root + 9 second = **34 files** (no
  internal docs, manifests, audits, or scratch paths)
- forbidden paths probed on `https://conanxin.github.io/...`:
  - `/_template/` → 404
  - `/_pilots/` → 404
  - `/scripts/` → 404
  - `/posts/` → 404
  - `/case-study/` → 404
  - `/release-assets/` → 404
- workflow: only `staging-builder` → `staging-gate` →
  `upload-pages-artifact` (with allowlist) → `deploy`. No upload
  of repository root, audit dir, or source / rights evidence.

## Preservation (this round)

- 6 image files: **unchanged** (same SHA-256 as v5.6c)
- source / rights evidence (`second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`,
  `second-exhibition/docs/RIGHTS_AND_SOURCES.md`): **unchanged**
- workflow (`.github/workflows/`): **unchanged**
- old tag `v5.0-real-second-exhibition-deployment` (target
  `ac0f19e2c03b…`): **unchanged**
- old Release `v5.0 Real Second Exhibition Deployment` (published
  2026-07-12T00:29:43Z): **unchanged** (not draft, not prerelease)
- check manifests and asset-checksums: **unchanged**

## What this freeze does

This freeze creates a new annotated tag (`v5.1-real-second-exhibition-v0.2`)
and a new GitHub Release (`v5.1 Real Second Exhibition v0.2`)
pointing at this commit. It is the second stable anchor for the
second exhibition — the first (`v5.0-...`) is the initial
v0.1 deployment, and this one is the first fully verified
v0.2 deployment with reproducible public browser QA. The two
anchors are **not interchangeable**; future v0.2.x iterations
may reuse this anchor's tag object name only if their content is
also byte-identical (which future iterations are not expected to
be — they will likely get a new tag).

## What this freeze does NOT do

- it does not modify the v0.2 page, data, or assets
- it does not modify the workflow
- it does not move or rewrite the v5.0 tag / Release
- it does not introduce a new tag until the evidence backfill
  has been recorded
- it does not add any new external request, third-party script,
  or visitor-side dependency
- it does not delete or rewrite any history
