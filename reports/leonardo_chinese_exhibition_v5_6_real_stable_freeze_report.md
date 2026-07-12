# v5.6 Real Stable Freeze Report

- **Round**: v5.6 Real Stable Freeze
- **Date**: 2026-07-12
- **Outcome**: PASS

## 1. Identity

- **Pre-freeze HEAD**: `f43c5479f8cee50e95435766e63bb5fb1e6ecfb9`
  (`Make live browser QA reproducible`)
- **Pre-freeze origin/main**: `f43c5479f8cee50e95435766e63bb5fb1e6ecfb9`
- **FREEZE_COMMIT**: `ffd0976a1f52858f8445044fc64cf9c19c40cba9`
  (`Freeze verified second exhibition v0.2 release`)
- **FREEZE_COMMIT Actions run**: `29187257609` (conclusion: `success`,
  23s, headSha `ffd0976a1f52858f8445044fc64cf9c19c40cba9`)
- **BACKFILL_COMMIT**: not yet created at the time of this report
- **CURRENT_HEAD**: `ffd0976a1f52858f8445044fc64cf9c19c40cba9` (this
  report is the next commit; see §16)

## 2. Annotated tag

- **Tag name**: `v5.1-real-second-exhibition-v0.2`
- **Tag type**: `tag` (annotated)
- **Tag object SHA**: `47155d3e2b504e6b98620946c27cd080df4b80a1`
- **Tag target SHA**: `ffd0976a1f52858f8445044fc64cf9c19c40cba9` =
  **FREEZE_COMMIT** (verified via `git rev-parse …^{}`) ✓
- **Tag message**: `Stable release: second exhibition v0.2`
- **Push status**: pushed to `origin/v5.1-real-second-exhibition-v0.2`

The tag does **not** point at the next (backfill) commit; it
points at the freeze commit. The backfill commit will be the
next commit on `main` and will be created in §16.

## 3. GitHub Release

- **URL**: `https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v5.1-real-second-exhibition-v0.2`
- **Name**: `v5.1 Real Second Exhibition v0.2`
- **TagName**: `v5.1-real-second-exhibition-v0.2`
- **targetCommitish**: `main`
- **publishedAt**: `2026-07-12T09:21:07Z`
- **isDraft**: `false` ✓
- **isPrerelease**: `false` ✓
- **Assets**:
  - `v5.1-real-second-exhibition-v0.2-manifest.md` (7,651 B,
    digest `sha256:8c86797b7d9269e0b8fe71c6cb16c9e718a79d3f53bb8cbe7f166a16a9a9986b`,
    state `uploaded`,
    URL `https://github.com/conanxin/.../download/v5.1-real-second-exhibition-v0.2/v5.1-real-second-exhibition-v0.2-manifest.md`)
- **Release notes source**: `release-assets/v5.1-real-second-exhibition-v0.2-release-notes.md`
  (uploaded as the GitHub Release "body" via `--notes-file`)

## 4. Commit chain

| Role | Commit | Subject |
|---|---|---|
| content deployment | `6b7ee068b1cd50ae4c9c9613b1106ba65c4b0071` | Implement second exhibition v0.2 content iteration (v5.6b) |
| production health baseline | `fff6e785db8c86e06ecad823a3e3ba4c28301cb8` | Promote v0.2 production health baseline |
| browser QA reproducibility | `f43c5479f8cee50e95435766e63bb5fb1e6ecfb9` | Make live browser QA reproducible |
| **FREEZE_COMMIT (tag target)** | `ffd0976a1f52858f8445044fc64cf9c19c40cba9` | Freeze verified second exhibition v0.2 release |
| **BACKFILL_COMMIT (this report)** | (next commit) | Backfill v5.1 stable freeze evidence |

## 5. Production identity (this round, post-freeze)

### Root

- URL: `https://conanxin.github.io/leonardo-chinese-exhibition/`
- HTTP: `200`
- bytes: **92,976**
- SHA256: `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`
- exact marker `v2.9-real-source-rights-audit`: 1

### Second exhibition (v0.2)

- URL: `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`
- HTTP: `200`
- marker: `second-exhibition-v0.2` (count = 3)
- stale v0.1 marker: 0
- live bytes: **31,452**
- live SHA256: `00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2`
- source bytes / SHA: 31,458 / `662bee42799a5e92fb7407a37d2fe57d02bfd123a344cbeada0cb51b99c5030e`
  (differs by 6 bytes from staged/live due to the staging builder's
  6 path rewrites; expected and audited)

### Content identity

- sections: 4
- artifact cards: 6
- glossary entries: 14
- public images: 6 / 6
- source notes: 6
- credit lines: 6
- C-06 lightbox: disabled (low-resolution NMNH 90×90 thumbnail)

## 6. Gate results (this round, pre-freeze + post-freeze)

| Gate | Pre-freeze | Post-freeze (Pages workflow success) |
|---|---|---|
| `template_quality_gate.py` | PASS | (unchanged) |
| `second_exhibition_build_gate.py` | PASS | (unchanged) |
| `second_exhibition_repository_qa.py` | 166 / 0 / 0 | (unchanged) |
| `second_exhibition_production_healthcheck.py` (default) | 70 / 0 | 70 / 0 (post-push) |
| 6 asset SHA-256 | 6 / 6 OK | 6 / 6 OK (unchanged) |
| `node --check` (script.js + browser_qa) | OK | (unchanged) |
| JSON (exhibition / sections / glossary / assets) | 4 / 4 valid | (unchanged) |
| `second_exhibition_staging_build.py` | PASS (25 + 9, 6 rewrites) | (re-run not needed; artifact content identical) |
| `second_exhibition_staging_gate.py` | PASS (schema 2.0) | (re-run not needed) |
| `second_exhibition_deployment_dry_run.py` | PASS (allowlist 14/14, forbidden 16/16, roundtrip 34/34) | (re-run not needed) |
| local exact-base-path browser QA | 3 / 3 PASS, 5/5 viewports, imgsLoaded `[6,6,6,6,6]`, 0 errors | (unchanged) |
| production browser QA | 3 / 3 PASS, 5/5 viewports, imgsLoaded `[6,6,6,6,6]`, 0 errors | 1 / 1 PASS, 5/5 viewports, imgsLoaded `[6,6,6,6,6]`, 0 errors |

## 7. Browser QA matrix (production, post-freeze)

| Run | Status | viewports | imgsLoaded per vp | err (ext/fail/con/page) | overflow |
|---|---|---|---|---|---|
| post-freeze (Actions-run 29187257609 succeeded first) | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 | 0 |

Interactions PASS: guidedToggle / lightboxOpen / lightboxRole=dialog /
lightboxAccessibleName=`lightbox-title` / closeButtonFocused / escClose
/ focusReturn / c06LightboxOpen=false / sectionNav / tabFocusable.

A11y PASS: h1=1 / imgMissingAlt=0 / buttonMissingName=0 /
headingJump=false.

No-JS PASS: 6 cards / 6 source notes / 6 credit lines /
repo status visible / body text.

Reduced-motion PASS: lightboxOpen + escClose.

## 8. Public inventory and forbidden boundary (this round)

- Public inventory: **25 root + 9 second = 34 files**
- Forbidden paths probed on `https://conanxin.github.io/.../leonardo-chinese-exhibition/`:
  - `/_template/` → 404
  - `/_pilots/` → 404
  - `/scripts/` → 404
  - `/posts/` → 404
  - `/case-study/` → 404
  - `/release-assets/` → 404
- No internal docs, manifests, audits, or scratch paths exposed

## 9. Scope guard (this round)

### Freeze commit `ffd0976a` (5 files added/modified)

- `docs/SECOND_EXHIBITION_V0_2_STABLE_FREEZE_v5.6.md` (new)
- `release-assets/v5.1-real-second-exhibition-v0.2-manifest.md` (new)
- `release-assets/v5.1-real-second-exhibition-v0.2-release-notes.md` (new)
- `docs/V5_ROADMAP.md` (freeze section appended)
- `README.md` (freeze section appended)

Protected paths (all 0 diff):

- `site/`, `second-exhibition/site/`, `second-exhibition/data/`,
  `second-exhibition/assets/`, `second-exhibition/docs/`
- `.github/workflows/`
- `_template/`, `_pilots/`, `posts/`, `case-study/`
- `scripts/` (no script changes this round; the official browser
  QA runner is the v5.6d round 2 state at `f43c5479`)
- existing `release-assets/` files (only the two new
  `v5.1-real-second-exhibition-v0.2-*` files were added)
- No `__pycache__` in working tree

## 10. Old v5.0 tag / Release preserved (verified this round)

- old tag: `v5.0-real-second-exhibition-deployment`
- old tag object SHA: `c8871f09e4003675d5796c76058d589a08541f45` (unchanged)
- old tag target: `ac0f19e2c03b09738ae49b4a15c629a1f2177068` (unchanged)
- old Release: `v5.0 Real Second Exhibition Deployment`
- old Release publishedAt: `2026-07-12T00:29:43Z` (unchanged)
- old Release isDraft: false (unchanged)
- old Release isPrerelease: false (unchanged)
- old Release URL: `https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v5.0-real-second-exhibition-deployment`

## 11. Tag target identity (this round, verified)

- `git rev-parse v5.1-real-second-exhibition-v0.2^{}` = `ffd0976a1f52858f8445044fc64cf9c19c40cba9` = **FREEZE_COMMIT** ✓
- The tag does **not** point at `f43c5479` (browser QA reproducibility) ✓
- The tag does **not** point at any backfill commit (backfill not yet created) ✓
- The tag does **not** point at `6b7ee06` (content deployment) ✓
- The tag does **not** point at `ac0f19e2` (v5.0 anchor) ✓

## 12. Workflow + workflow file unchanged

- `.github/workflows/pages.yml`: **unchanged** (0 diff this round)
- Pages workflow runs `staging builder → staging gate → upload
  pages artifact → deploy`; only the allowlisted artifact is
  uploaded; audit dir + repository root are not.

## 13. Content / data / assets unchanged

- `site/index.html`: 92,976 B / SHA `e2be1077…` (unchanged)
- `second-exhibition/site/index.html`: 31,458 B / SHA `662bee…` (unchanged)
- live root: 92,976 B / SHA `e2be1077…` (unchanged)
- live second: 31,452 B / SHA `00894e8d…` (unchanged)
- 6 image files: SHA-256 unchanged
- `second-exhibition/data/*.json`: unchanged
- `second-exhibition/assets/asset-checksums.sha256`: unchanged
- `second-exhibition/assets/asset-import-manifest.json`: unchanged
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`: unchanged
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md`: unchanged

## 14. Public content drift during the freeze round

- **0 drift in production root (92,976 B)**
- **0 drift in production second (31,452 B)**
- **0 drift in 6 image SHA-256**
- **0 drift in marker `second-exhibition-v0.2` (count = 3) and stale v0.1 (count = 0)**
- The freeze commit itself produces no new Pages bytes (it only
  touches docs and release-assets that are not part of the
  Pages artifact).

## 15. Working tree state at the time of this report

- tracked: clean (only the report file this report is creating
  will be added)
- untracked: `.firecrawl/` (not processed, by policy)
- no `__pycache__` present

## 16. Backfill

- This report will be the next commit (BACKFILL_COMMIT).
- BACKFILL_COMMIT will be created in §16 of the brief; the
  tag `v5.1-real-second-exhibition-v0.2` will continue to point
  at FREEZE_COMMIT (`ffd0976a`), **not** at BACKFILL_COMMIT.
- This is the post-tag evidence backfill as required by the
  brief; it does not modify the freeze commit, the tag, or
  the Release.

## 17. Next recommended task

- Stable maintenance / future v0.3 planning.
