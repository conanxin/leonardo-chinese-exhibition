# Second Exhibition Rollback Plan — v5.2 (Dry-Run Rehearsal)

**Round:** v5.2-deployment-dry-run
**Date:** 2026-07-11
**STATUS:** **PASS** — rollback path is one `git revert` of one line

This document is the v5.2-specific rollback rehearsal that complements the master
plan in `docs/SECOND_EXHIBITION_ROLLBACK_PLAN_v5.0.md`. v5.0 documents the policy;
v5.2 verifies it against the current workflow file.

---

## Rollback baseline (verified in v5.2)

| Item | Verified value | Source |
|------|----------------|--------|
| Production live byte | **92,976 B** | `curl https://conanxin.github.io/leonardo-chinese-exhibition/ | wc -c` |
| Production v2.9 marker count | **1** | `curl … | grep -c v2.9-real-source-rights-audit` |
| `/second-exhibition/` Pages URL | **404** | direct `curl` |
| `/second-exhibition/index.html` Pages URL | **404** | direct `curl` |
| All sub-URLs under `/second-exhibition/` | **404** | direct `curl` |
| v4.8 tag target | `a70c8430a8e3d01153153e54f055d9907340d6b7` | `git rev-parse v4.8-real-second-exhibition-repository-hardening^{}` |
| Current workflow `path:` line | `          path: site` (occurs exactly once) | `grep -c 'path: site' .github/workflows/pages.yml` |
| Current workflow file | `.github/workflows/pages.yml` | v4.8 freeze |

All twelve tags from v2.0 through v4.8 are intact. All GitHub Releases are unchanged.

---

## Proposed change (the future deployment commit)

A single-line edit to `.github/workflows/pages.yml`:

```diff
-          path: site
+          path: __STAGING_ARTIFACT_DIR__
```

(Where `__STAGING_ARTIFACT_DIR__` is the v5.1 staging artifact at
`/tmp/leonardo-pages-artifact`, copied to the deployer's working directory.)

In v5.2 we did NOT execute this edit. The diff shown here is the **proposed** change
for the future v5.3 controlled deployment.

---

## Rollback method

| Step | Command | Expected result |
|------|---------|-----------------|
| 1 | Identify the future deployment commit SHA | `<deployment-commit>` |
| 2 | `git revert --no-edit <deployment-commit>` | Creates a new commit whose diff is exactly `-          path: __STAGING_ARTIFACT_DIR__` / `+          path: site` (1 line) |
| 3 | `git push origin main` | New revert commit reaches `main` |
| 4 | Wait for GitHub Actions success | Pages workflow runs with `path: site` again |
| 5 | `curl -L -sS https://conanxin.github.io/leonardo-chinese-exhibition/ \| wc -c` | 92,976 B |
| 6 | `curl … \| grep -c v2.9-real-source-rights-audit` | 1 |
| 7 | `curl … \| grep -c 植物图谱与视觉分类` | 0 |
| 8 | `curl … -o /dev/null -w "%{http_code}" /second-exhibition/` | 404 |
| 9 | Verify all 6 image URLs under `/second-exhibition/assets/images/` return 404 | 6/6 |
| 10 | Document incident in `reports/` if any step fails | n/a |

The revert is **1 line**. The Pages artifact source reverts to `site/`. The existing
production Leonardo site is restored because the `site/` directory is unchanged on
disk — the only thing the workflow flips is which directory is uploaded.

---

## Rollback triggers (from v5.0, restated)

Any one of the following triggers a rollback:

- Main URL non-200 after deployment.
- Live byte ≠ 92,976 B AND cannot be explained.
- v2.9 marker count ≠ 1.
- Second-exhibition assets 404 (i.e. deployment did not actually publish
  `/second-exhibition/`).
- Workflow accidentally published an internal file (e.g. `data/`, `docs/`,
  `_template/`, `_pilots/`, `reports/`, `scripts/`, `.firecrawl/`, top-level
  `README.md`, `V4_ROADMAP.md`, `V5_ROADMAP.md`).
- Browser QA against public URL FAILS.
- External requests > 0.
- Asset checksum mismatch.
- Source / rights blocker (e.g. accidental edit to `second-exhibition/docs/`).

---

## Things the rollback must NOT do

- Force-push `main`.
- Move or delete any existing tag (`v2.0` through `v4.8`).
- Delete any GitHub Release.
- Edit the `site/` directory contents (only the workflow line changes).
- Re-deploy the staging artifact manually via the GitHub UI / drag-and-drop.
- Edit `second-exhibition/docs/` or `second-exhibition/data/` (those are not on
  the publish path anyway, but editing them is out of scope for this round and
  could pollute the rollback narrative).

---

## Rollback rehearsal verification (v5.2)

| Check | Method | Result |
|-------|--------|--------|
| Current workflow has exactly one `path: site` line | `grep -c 'path: site' .github/workflows/pages.yml` | **1** |
| Proposed change is one line | text diff in this document | **1 line** |
| Revert is one line | reverse of proposed change | **1 line** |
| Workflow was NOT modified by v5.2 | `git status -- .github/workflows/` and re-read of file | **unmodified** |
| Dry-run did NOT push to `main` | `git rev-parse origin/main` before and after dry-run | **unchanged (`0bc9c99`)** |
| Dry-run did NOT call `actions/deploy-pages` | no workflow run triggered by this round | **none** |

The rollback path is verified to be a 1-line revert. The rehearsal is complete.

---

## After v5.3 deploys, the rollback contract will look like

```
production state            <- git revert <v5.3 deployment commit>
                            <- live byte = 92,976; v2.9 marker = 1
                            <- /second-exhibition/ = 200, then back to 404 after revert
```

In v5.2 we have only verified the contract: 1-line revert, no other state mutation.
The actual rollback will be exercised for the first time when v5.3 ships and we
need to undo it.