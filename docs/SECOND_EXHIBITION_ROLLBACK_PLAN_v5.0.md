# v5.0 Second Exhibition Rollback Plan

## Rollback baseline

This is the verified state that rollback must restore.

- Live byte size: **92,976 B**
- v2.9 marker live count: **1**
- Second exhibition title live count: **0**
- All `second-exhibition/` Pages URLs return HTTP 404
- Top-level `script.js` HTTP 200
- v4.8 freeze commit: `a70c8430a8e3d01153153e54f055d9907340d6b7`
- v4.8 evidence backfill commit: `01bebd87c2d109b2e549430436fe91c8ff2d3720`
- Pages workflow (current): `.github/workflows/pages.yml` — uploads `site/`

## Rollback triggers

Rollback is initiated when any of the following is observed after a v5.x deploy:

- Top-level Leonardo URL not returning HTTP 200.
- Live byte size changed and cannot be explained.
- `v2.9-real-source-rights-audit` marker count is no longer 1.
- Second exhibition resources return 404 on a path that should serve a file.
- The Pages workflow has published internal files (e.g., `README.md`, `SECOND_EXHIBITION_*`, `_template`, `_pilots`, `posts`, `case-study`, `release-assets`, `docs`, `reports`, `.git`, `.firecrawl`).
- Browser QA fails on the published second exhibition.
- External requests > 0 from the published second exhibition.
- Asset checksum mismatch against `second-exhibition/assets/asset-checksums.sha256`.
- Source / rights evidence has changed on the upstream page since v5.0 was planned.

## Rollback method

The rollback is a one-commit, one-push operation. It does **not** modify any existing tag or Release.

1. **Identify the bad commit.** The bad commit is the workflow change that started publishing the second exhibition.
2. **Revert the deployment commit.** Either revert the commit via `git revert <bad-commit-sha>` or push a new commit that restores the workflow to its pre-v5.x state (`path: site` only).
3. **Confirm the restored workflow.** Inspect `.github/workflows/pages.yml` — `actions/upload-pages-artifact@v3` must have `path: site` only.
4. **Push the rollback commit to `main`.** Do **not** force-push.
5. **Wait for Pages workflow success.** Confirm GitHub Actions run is green.
6. **Re-verify live state.** The checks in the next section must all pass.
7. **Confirm second exhibition URLs are back to 404.** Required.
8. **Create incident report.** Record what triggered the rollback, the timeline, the new commit SHA, and the recovered live byte.

## Things rollback must never do

- Force-push to `main`.
- Delete or move any existing tag (`v2.0` through `v4.8`).
- Delete, overwrite, or modify any existing GitHub Release.
- Manually upload to GitHub Pages outside the workflow.
- Modify source / rights evidence files.
- Re-deploy without a fresh staging assembly and preflight run.

## Rollback verification

After the rollback push and Pages workflow success, the following must all hold:

| Check | Expected value |
|-------|----------------|
| Live URL `https://conanxin.github.io/leonardo-chinese-exhibition/` | HTTP 200 |
| Live byte size | **92,976 B** |
| `v2.9-real-source-rights-audit` count | **1** |
| Top-level `script.js` HTTP status | 200 |
| `/second-exhibition/` HTTP status | 404 |
| `/second-exhibition/index.html` HTTP status | 404 |
| `/second-exhibition/site/index.html` HTTP status | 404 |
| `/second-exhibition/assets/asset-import-manifest.json` HTTP status | 404 |
| Latest local tag (created before rollback) | unchanged |
| Latest GitHub Release (created before rollback) | unchanged |

## Rollback ownership

- **Initiator:** the operator who detects a trigger condition.
- **Approver:** implicit — rollback is a recovery action, not a deploy; no separate approval needed if a trigger is observed.
- **Recorder:** the incident report is committed under `reports/` so the history is preserved.

## Rollback history

- No rollbacks recorded before v5.0.
- This document will be amended after each future deploy round if a rollback occurs.