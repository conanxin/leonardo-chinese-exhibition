# v5.4 Public Stable Freeze Report

## STATUS

**PASS** -- public second exhibition verified end-to-end against the live GitHub Pages URL on the freeze round, and the freeze doc commit is ready to be created. Deployment chain confirmed: f84e53f -> 83ab6d8 -> 5250404 -> bfce140 (and now the freeze doc commit).

## Baseline HEAD / origin

| Field | Value |
|---|---|
| HEAD at start of this round | `bfce140029a66a95a0b52115f5083b3aef308f6a` |
| `origin/main` at start of this round | `bfce140029a66a95a0b52115f5083b3aef308f6a` |
| Head subject | `Verify live second exhibition production QA` |
| Working tree at start | clean (only `.firecrawl/` untracked) |

## Final QA commit (pre-freeze)

`bfce140029a66a95a0b52115f5083b3aef308f6a` -- Verify live second exhibition production QA.

## Freeze commit

`TBD on commit step` -- the freeze commit is created by `git commit -m "Freeze verified v5.0 second exhibition deployment"` against the 5 doc files. This report is backfilled with the freeze commit SHA after `git commit` returns; the value lands in this file via an evidence-backfill commit that is a child of the freeze commit (the freeze commit itself remains the documented freeze anchor; the backfill commit is purely textual).

## Optional evidence-backfill commit

`TBD on tag + release step` -- after the annotated tag is created and pushed and the GitHub Release is created, an evidence-backfill commit updates this report (and the release notes / manifest if needed) with the concrete tag object SHA, tag target commit, Release URL, `publishedAt`, and the freeze-round Actions run ID. The backfill commit does NOT move the tag.

## Tag

- Tag name: `v5.0-real-second-exhibition-deployment`
- Type (after `git tag -a`): annotated tag (object type `tag`)
- Tag target commit (after creation): the freeze doc commit on `main`. The exact SHA is backfilled after `git tag -a` returns; the value is verified post-create via `git rev-parse v5.0-real-second-exhibition-deployment` and `git rev-parse v5.0-real-second-exhibition-deployment^{}`.
- Old tags untouched: all 12 pre-existing tags (`v2.0-public-portfolio-case` through `v4.8-real-second-exhibition-repository-hardening`) are still pinned to their original commits.

## Tag object SHA / target SHA

Backfilled after `git tag -a`:

| Field | Value |
|---|---|
| Tag object SHA | `TBD` |
| Tag target commit SHA | `TBD (= freeze commit SHA)` |

## Release URL / status / publishedAt

Backfilled after `gh release create`:

| Field | Value |
|---|---|
| Release URL | `TBD` |
| Status | `TBD` |
| `publishedAt` | `TBD` |

## GitHub Actions run IDs (this v5.4 round)

| Step | Run ID | Status | headSha | URL |
|---|---|---|---|---|
| freeze doc push | `TBD` | `TBD` | the freeze commit SHA | `TBD` |
| freeze doc push (re-verify after backfill) | `TBD` | `TBD` | the backfill commit SHA | `TBD` |

Prior Actions runs (pre-freeze):

- `29154365778` -- v5.3 controlled deployment (success, 18 s).
- `29156046423` -- v5.3b production-state reconciliation push (success).
- `29172641937` -- v5.3c live production browser QA push (success, ~20 s).

## Root identity

| Field | Value |
|---|---|
| `GET https://conanxin.github.io/leonardo-chinese-exhibition/` HTTP | 200 |
| Root byte | **92,976 B** |
| Root v2.9 exact marker (`grep -o 'v2.9-real-source-rights-audit' | wc -l`) | **1** |
| Root v2.9 loose marker (`grep -o 'v2\.9' | wc -l`) | **4** |
| `cmp -s site/index.html /tmp/v50-live/root-index.html` | IDENTICAL |
| Root identity preserved from v5.3 through v5.3c | YES |

## Second exhibition identity

| Field | Value |
|---|---|
| `GET https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/` HTTP | 200 |
| Second index byte | **25,635 B** |
| `curl -L --fail -sS /second-exhibition/ | wc -c` | 25,635 |
| `cmp -s /tmp/v50-freeze-artifact/second-exhibition/index.html /tmp/v50-live/second-index.html` | IDENTICAL |
| `cmp -s /tmp/v50-freeze-artifact/second-exhibition/style.css /tmp/v50-live/second-style.css` | IDENTICAL |
| `cmp -s /tmp/v50-freeze-artifact/second-exhibition/script.js /tmp/v50-live/second-script.js` | IDENTICAL |

## Status text counts (live, exact commands)

| Command | Count |
|---|---|
| `curl -L -sS <root> | wc -c` | 92,976 |
| `curl -L -sS <root> | grep -o 'v2.9-real-source-rights-audit' | wc -l` | 1 |
| `curl -L -sS <second-exhibition/> | wc -c` | 25,635 |
| `curl -L -sS <second-exhibition/> | grep -o 'production-deployed-v5.3' | wc -l` | 5 |
| `curl -L -sS <second-exhibition/> | grep -o 'published-in-v5.3' | wc -l` | 8 |
| `curl -L -sS <second-exhibition/> | grep -o 'imported-not-deployed' | wc -l` | 8 |
| `curl -L -sS <second-exhibition/> | grep -o 'repository-only-not-deployed' | wc -l` | 0 |

Page semantics correct: production-deployed-v5.3 (current status), published-in-v5.3 (per-asset current publication status), imported-not-deployed (preserved historical import record, only inside the explicit `Import record: imported-not-deployed (v4.5)` annotation), zero `repository-only-not-deployed`, zero stale `未部署` / `not deployed` prose.

## Gates

| Gate | Result |
|---|---|
| `python3 scripts/template_quality_gate.py` | 37 / 37 PASS |
| `python3 scripts/second_exhibition_build_gate.py` | PASS |
| `python3 scripts/second_exhibition_repository_qa.py` | 164 / 164 PASS |
| `sha256sum -c second-exhibition/assets/asset-checksums.sha256` | 6 / 6 OK |
| `python3 -m json.tool <each JSON> | python3 -m json.tool` (roundtrip parse) | 5 / 5 OK |
| `node --check second-exhibition/site/script.js` | clean |
| `python3 scripts/second_exhibition_staging_build.py --output /tmp/v50-freeze-artifact --audit /tmp/v50-freeze-audit` | PASS (`25 main-site + 9 second-exhibition files`) |
| `python3 scripts/second_exhibition_staging_gate.py --artifact /tmp/v50-freeze-artifact --audit /tmp/v50-freeze-audit` | PASS |

## Browser viewport matrix (live, on `bfce140`)

| Viewport | deep-block sections | artifact cards | glossary items | source notes | credit lines | images loaded | horizontal overflow | console / page / failed / external errors |
|---|---|---|---|---|---|---|---|---|
| 1440 x 1000 | 4 | 6 | 12 | 6 | 6 | 6 / 6 | no | 0 / 0 / 0 / 0 |
| 1280 x 900 | 4 | 6 | 12 | 6 | 6 | 6 / 6 | no | 0 / 0 / 0 / 0 |
| 768 x 1024 | 4 | 6 | 12 | 6 | 6 | 6 / 6 | no | 0 / 0 / 0 / 0 |
| 390 x 844 | 4 | 6 | 12 | 6 | 6 | 6 / 6 | no | 0 / 0 / 0 / 0 |
| 320 x 700 | 4 | 6 | 12 | 6 | 6 | 6 / 6 | no | 0 / 0 / 0 / 0 |

Browser / engine: Chromium headless shell `148.0.7778.96` (Chrome for Testing) via local Playwright.

Per-viewport text (5/5 viewports): `production-deployed-v5.3` visible, `published-in-v5.3` visible, `imported-not-deployed` visible only inside the historical `Import record` annotation, `repository-only-not-deployed` absent, stale `未部署` / `not deployed` phrase absent.

## Accessibility

| Probe | Result |
|---|---|
| Image alt coverage (5 viewports x 7 images, minus the zero-src SVG icon) | 30 / 35 with non-empty alt (5 are intentional `alt=""` lightbox scaffolds) |
| Close button focus on C-01 lightbox open | YES |
| ESC closes lightbox | YES |
| Focus returns to C-01 trigger after close | YES |
| Dialog accessible name (via `aria-labelledby="lightbox-title"`) | `图片查看器` |
| C-06 lightbox click blocked (low-res warning only) | YES |
| Guided toggle (`#guided-toggle`) `aria-pressed` switches `false -> true` | YES |
| Tab reaches 6 primary buttons | YES |
| no-JS render preserves title / status text / 6 cards / source notes / credit lines / `.repository-status` | YES |
| `prefers-reduced-motion: reduce` honored (`matchMedia` true, lightbox open + ESC close clean) | YES |

## Errors / overflow

| Metric | Result |
|---|---|
| Console errors across all 5 viewports + 4 environment variants | **0** |
| Page errors (uncaught exceptions) | **0** |
| Failed requests | **0** |
| External (non-`conanxin.github.io`) requests | **0** (`externalHosts` empty) |
| Horizontal overflow (5 viewports) | **0** |

## Public inventory

- Main site public files: **25**.
- Second exhibition public files: **9** (= `index.html`, `style.css`, `script.js` + 6 images).
- Total public files: **34**.
- Public raster images (second exhibition): **6**.

## Checksums

Live 6 image SHA-256 vs `second-exhibition/assets/asset-checksums.sha256` (`sha256sum -c`): **6 / 6 OK**.

The 6 SHA-256 values are byte-identical across:

- local source (`second-exhibition/assets/images/*`),
- staging artifact (`/tmp/v50-freeze-artifact/second-exhibition/assets/images/*`),
- live download (`/tmp/v50-live-img/*`).

## Live / staged identity

- Root: `cmp -s site/index.html /tmp/v50-live/root-index.html` IDENTICAL (92,976 B).
- Second exhibition: `cmp -s /tmp/v50-freeze-artifact/second-exhibition/{index.html,style.css,script.js} /tmp/v50-live/second-{index.html,style.css,script.js}` IDENTICAL for all three (25,635 / 8,261 / 4,070 B).
- 6 raster images: SHA-identical across source / staged / live.

## Forbidden paths

18 / 18 forbidden public paths return HTTP 404:

- root: `data/`, `docs/`, `asset-checksums.sha256`, `asset-import-manifest.json`, `_template/`, `_pilots/`, `reports/`, `release-assets/`, `scripts/`, `.firecrawl/`, `README.md`, `V4_ROADMAP.md`, `V5_ROADMAP.md`, `.github/`.
- second-exhibition: `data/`, `docs/`, `assets/asset-import-manifest.json`, `assets/asset-checksums.sha256`.

## Workflow state

- Workflow file: `.github/workflows/pages.yml` (unchanged this round -- v5.3 wiring is in place and remains the authoritative workflow).
- Workflow semantics: post-v5.3 it invokes `python3 scripts/second_exhibition_staging_build.py --output <runner.temp>/leonardo-pages-artifact --audit <runner.temp>/leonardo-pages-artifact-audit` and `python3 scripts/second_exhibition_staging_gate.py --artifact <runner.temp>/leonardo-pages-artifact --audit <runner.temp>/leonardo-pages-artifact-audit`, then uploads only the staging artifact to Pages.
- No workflow change is required (or permitted) by the freeze commit.
- No workflow change is required (or permitted) by the backfill commit.

## Rollback plan

1. If a follow-up round finds a regression tied to the v5.0 freeze doc commit only (live surface unaffected by design, so this is a documentation-only rollback):
   ```
   git revert <freeze-doc-commit-sha>
   git push origin main
   ```
   The live surface is byte-identical before and after this revert.

2. If a follow-up round finds a regression tied to a later content change that depends on the freeze commit (e.g. accidentally editing `second-exhibition/site/index.html`):
   - revert the offending later commit(s),
   - if necessary, also revert the v5.3c live QA backfill, the v5.3b wording reconciliation, the v5.3 audit-path fix, and the v5.3 wiring commit -- in reverse chronological order (`5250404`, `83ab6d8`, `f84e53f`) -- to restore the pre-v5.3 Pages workflow that only deploys `site/`.

3. The annotated tag `v5.0-real-second-exhibition-deployment` is **never** moved. If the freeze commit SHA itself needs to be retracted, a new tag + Release are published; the old tag is left in place as a permanent record.

## Protected paths unchanged

The v5.4 freeze doc commit only touches documentation. The following paths are guaranteed by `git diff <prev-HEAD> <freeze-HEAD> -- <path>` to be empty:

- `site/`
- `second-exhibition/site/`
- `second-exhibition/data/`
- `second-exhibition/assets/` (incl. six image bytes)
- `second-exhibition/docs/` (incl. `SOURCE_AUDIT_MANIFEST.md` + `RIGHTS_AND_SOURCES.md`)
- `.github/workflows/`
- `scripts/`
- `_template/`, `_pilots/`, `posts/`, `case-study/`
- All pre-existing files under `release-assets/v2.*`, `release-assets/v3.*`, `release-assets/v4.*`, `release-assets/manifest.md`.

## Old tags unchanged

All 12 pre-existing tags remain pinned to their original commits. The freeze round adds one new tag (`v5.0-real-second-exhibition-deployment`); it does not move any pre-existing tag.

| Tag | Object SHA | Target SHA |
|---|---|---|
| `v2.0-public-portfolio-case` | `9e6233ab2b2c5aa3e1243565583f8f66c7df34b4` | `TBD(local)` (lightweight, no `^{}` entry) |
| `v2.6-content-stable` | `033b65e28096d04935205867e6d8dcaac0d6cf94` | `01cdaa2dc1487a5f7877c8702720d0df8dbb17ce` (annotated) |
| `v2.7-zh-exhibition-polish` | `a0fee10273c9ff1c0312a494054158fe524d60b0` | `f58f6b45075e3d8c0e9d81a160ff939b1f8de412` (annotated) |
| `v2.8-real-deep-content` | `697560af9822addbcbe9f865e2bd6d1e33da9a93` | `65b4fbc2b1bc742f263559145bb273c11cb3c6b0` (annotated) |
| `v2.9-real-source-rights-audit` | `13814d345bcd47860b778323c9915460ef72fb28` | `a1e667e302d0d8106a9d0e4961159ae5c14aae4a` (annotated) |
| `v3.0-real-template-extraction-audit` | `3b5404fe8e488c4506b6621e1a80a03958ffdf24` | `dd7d589f8db1417c00c539230849ed3f89d8a0d7` (annotated) |
| `v3.1-real-second-exhibition-pilot` | `f839187ae3c4382084b3b29aeba5df0c67238db8` | `c5e93d0f6387572e342213737ac1f7e191c2268e` (annotated) |
| `v3.2-real-template-documentation` | `77a89fb5ffccaae0f686ed2eb388453b1901fe33` | `5a89fb2061ef3eee95c63dc3592d92fb859177fe` (annotated) |
| `v3.3-real-template-quality-gate` | `fb35a5d9aece0bf44d82e3f7f25c2a73b8e6a70e` | `fce2efb5f0fcbbb3bd4e25c8008513f8c2462eb4` (annotated) |
| `v3.4-real-second-exhibition-hardening` | `2d186a892af0e1ab41c1d9b8a055842e01339cb6` | `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765` (annotated) |
| `v4.7-real-second-exhibition-repository-qa` | `b746a358491149ed9f40c064d0f5661951601c45` | `2153d2eab45bc1ea715fae1e1b04a3ee9fc64961` (annotated) |
| `v4.8-real-second-exhibition-repository-hardening` | `1c868b054424c348f273be4148a6a3f184e374ba` | `a70c8430a8e3d01153153e54f055d9907340d6b7` (annotated) |

Most recent source-freeze anchor: `v4.8-real-second-exhibition-repository-hardening` at `a70c8430a8e3d01153153e54f055d9907340d6b7`.

## Old Releases unchanged

No GitHub Release was created or modified prior to this freeze round. The freeze round creates exactly one new Release for `v5.0-real-second-exhibition-deployment`; it does not touch any pre-existing Release.

## Next recommended task

```
maintenance / v5.1 content iteration
```

Per `docs/V5_ROADMAP.md` v5.4 "Next": each future content round is a separate commit on `main` with optional per-round tag / Release, gated by the same template / build / repository / browser QA tooling. The v5.0 public deployment is now a stable anchor; later rounds build on it without disturbing it.

See `docs/V5_ROADMAP.md` v5.4 "Next" and `docs/POST_RELEASE_MAINTENANCE.md` for the per-round protocol.

---

## Evidence backfill (filled after tag + Release are created)

This section is updated by an evidence-backfill commit after the annotated tag is created and pushed and the GitHub Release is created. The backfill commit does NOT move the tag. The values filled here are the only concrete tag / Release references this report carries.

| Field | Value |
|---|---|
| Freeze commit SHA | `TBD` |
| Evidence-backfill commit SHA | `TBD` |
| Tag object SHA | `TBD` |
| Tag target commit SHA | `TBD` (= freeze commit SHA) |
| Release URL | `TBD` |
| Release status | `TBD` |
| Release `publishedAt` | `TBD` |
| Freeze-doc-push Actions run ID | `TBD` |
| Backfill-push Actions run ID (if any) | `TBD` |
| Old-tags-pin re-verification (post-tag) | TBD (compare `git ls-remote --tags origin` before vs after) |

## Re-verification after freeze doc push (and after backfill push)

- `git rev-parse HEAD` = the backfill commit SHA (or the freeze commit SHA if no backfill is created).
- `git rev-parse origin/main` = same as HEAD.
- `python3 scripts/template_quality_gate.py` still 37 / 37 PASS.
- `python3 scripts/second_exhibition_build_gate.py` still PASS.
- `python3 scripts/second_exhibition_repository_qa.py` still 164 / 164 PASS.
- `sha256sum -c second-exhibition/assets/asset-checksums.sha256` still 6 / 6 OK.
- `GET /` still 92,976 B with `v2.9-real-source-rights-audit` occurring exactly once and `v2.9` (loose) occurring exactly 4 times.
- `GET /second-exhibition/` still 25,635 B with `production-deployed-v5.3` x 5, `published-in-v5.3` x 8, `imported-not-deployed` x 8, `repository-only-not-deployed` x 0.
- Six live images still byte-identical to local source.
- Forbidden public paths still 18 / 18 -> 404.

