# v5.0 Second Exhibition Deployment Planning Report

## STATUS: PASS

**Date:** 2026-07-12
**Baseline HEAD / origin/main:** `01bebd87c2d109b2e549430436fe91c8ff2d3720`
**Source release:** `v4.8-real-second-exhibition-repository-hardening`
**Source tag object:** `1c868b054424c348f273be4148a6a3f184e374ba`
**Source tag target:** `a70c8430a8e3d01153153e54f055d9907340d6b7`
**Live URL:** https://conanxin.github.io/leonardo-chinese-exhibition/
**Live byte size:** **92,976 B**
**Round:** v5.0 — Second Exhibition Deployment Planning
**Next:** `v5.1-staging-artifact-build`

---

## Quality gates (this round)

| Gate | Result |
|------|--------|
| Template quality gate | **PASS, 37/37** |
| Second exhibition build gate | **PASS** |
| Repository QA | **161 PASS / 0 FAIL / 0 WARNINGS** (exit 0) |
| Asset checksums | **6/6 OK** |
| JavaScript syntax (site) | OK |
| JavaScript syntax (browser QA) | OK |
| Data JSON | all valid |
| Browser QA (this round, before v5.0 work) | **PASS, 5/5 viewports**, 0 console / page errors / failed requests / external requests |
| Deployment preflight (this round, new script) | **PASS** |

## Workflow analysis

- File: `.github/workflows/pages.yml`
- Artifact source: `path: site` (top-level only)
- Publish directory: GitHub Pages (per `actions/deploy-pages@v4`)
- Only deploys top-level `site/` — does NOT publish repository root
- No path collision risk for `/second-exhibition/` (not in artifact)
- No root artifact leakage risk
- No second workflow, no CNAME

## Options reviewed

| Option | Result |
|--------|--------|
| A — Existing GitHub Pages subpath (`/second-exhibition/`) | **Selected** |
| B — Separate GitHub Pages repository | Fallback (isolation / rollback) |
| C — Custom subdomain on Cloudflare Pages | Out of scope (separate platform audit needed) |

## Selected architecture

- Existing GitHub Pages site + isolated staging artifact under `/second-exhibition/`
- One repository, one workflow, one Release stream
- Staging directory lives outside the repository (e.g., `/tmp/leonardo-pages-artifact/`), is never committed
- Top-level site copy is byte-identical to source
- Second-exhibition page is path-rewritten in the staging tree only (`../assets/images/` → `./assets/images/`)

## Proposed public URL

- `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`

## Artifact strategy

```
/tmp/leonardo-pages-artifact/
├── index.html             (byte-identical to site/index.html)
├── style.css              (byte-identical to site/style.css)
├── script.js              (byte-identical to site/script.js)
└── second-exhibition/
    ├── index.html         (path-rewritten staging copy)
    ├── style.css          (byte-identical to second-exhibition/site/style.css)
    ├── script.js          (byte-identical to second-exhibition/site/script.js)
    └── assets/
        └── images/        (6 raster images, copied from second-exhibition/assets/images/)
```

## Path rewrite strategy

- Tracked source unchanged: `second-exhibition/site/index.html` retains `../assets/images/`.
- During staging assembly, rewrite is applied **only** to the staging copy of `second-exhibition/index.html`:
  - `../assets/images/` → `./assets/images/`
- 6 references found in source page, all covered by the rewrite plan.

## Publish allowlist

- HTML (`.html`)
- CSS (`.css`)
- JavaScript (`.js`)
- Raster images: `.webp`, `.png`, `.jpg`, `.jpeg`

## Forbidden files / paths (must NOT appear in artifact)

- `*.md`, `*.json`, `*.sha256`
- Any `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`, `docs/`, `reports/`, `scripts/`, `.git/`, `.firecrawl/`
- `second-exhibition/data/`
- `second-exhibition/docs/`
- `second-exhibition/assets/asset-import-manifest.json`
- `second-exhibition/assets/asset-checksums.sha256`

## Risk summary

- Total named risks: **15** (D-01 through D-15)
- High risks: **7** (D-01, D-02, D-03, D-04, D-06, D-09, D-11, D-12, D-13, D-14, D-15) — **all closed by staging isolation + preflight + checklist**
- Blocked risks: **1** (D-05) — **closed** by the workflow-only-uploads-staging rule + preflight check
- Medium risks: **2** (D-08, D-10)
- Low risks: **1** (D-07)
- **Open High / Blocked at end of v5.0: 0** → no deployment blocker.

## Rollback plan

- Rollback baseline: live byte 92,976 B, v2.9 marker 1, second exhibition URLs 404, Pages workflow uploads `site/` only.
- Trigger conditions: top-level regression, internal files reachable, browser QA failure on public URL, external requests > 0, checksum mismatch, source / rights blocker, GitHub Actions deploy failure × 2.
- Method: one revert commit restores the workflow to `path: site`; no force-push; no tag movement; no Release deletion.
- Verification: live byte 92,976 B, v2.9 marker 1, second exhibition URLs back to 404, top-level script.js still 200.

## Deployment checklist

- Five phases: Pre-build, Artifact assembly, Staging QA, Deployment, Post-deployment
- Each phase has an explicit exit gate
- Rollback gate: any trigger observed at any phase aborts the round

## Preflight result

- `python3 scripts/second_exhibition_deployment_preflight.py` → **PASS**
- A. Verified baseline: **PASS**
- B. Source build (checksums): **PASS** (6/6)
- C. Deployment planning (6 v5.0 docs + V5_ROADMAP + risk register + rollback + checklist): **PASS**
- D. Source path analysis (6 references, no external / absolute / file:// / Windows paths): **PASS**
- E. Publish allowlist (defined and printed): **PASS**
- F. Workflow safety (`path: site`, no root upload, no second-exhibition / _template / _pilots reference): **PASS**

## Current workflow unchanged?

- Yes. `.github/workflows/pages.yml` was not modified in this round.

## Protected content unchanged?

- Yes. All checks against `site/`, `second-exhibition/site/`, `second-exhibition/data/`, `second-exhibition/assets/`, source / rights evidence, `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`, `.github/workflows/`, and gate scripts are empty.

## Second exhibition still unavailable?

- Yes. All tested `second-exhibition/` Pages URLs return HTTP 404.

## Tags / Releases unchanged?

- Yes. No new tag, no new Release. Latest tag remains `v4.8-real-second-exhibition-repository-hardening`.

## Next recommended task

**v5.1-staging-artifact-build** — build the staging tree, run browser QA against staging server, do not push to `main`.