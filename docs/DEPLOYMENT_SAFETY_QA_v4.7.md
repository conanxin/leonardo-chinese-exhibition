# Deployment Safety QA v4.7

## Baseline

- Live site: `site/` at the repository root
- Second exhibition repository site: `second-exhibition/site/`
- GitHub Pages workflow: `.github/workflows/pages.yml`
- Current live byte size: 92,976 B

## Workflow scope

- The GitHub Pages workflow (`pages.yml`) is configured to deploy only the top-level `site/` directory.
- It does not reference `second-exhibition/`.
- It does not publish the entire repository root.
- The build artifact path is `site` (root-level), not `second-exhibition/site`.

## Top-level live site unchanged

- `site/index.html`, `site/style.css`, and `site/script.js` have not been modified in v4.7.
- Live byte size remains 92,976 B.
- Live page contains the v2.9 marker (`v2.9-real-source-rights-audit`) exactly once.
- Live page does **not** contain the second exhibition title (`植物图谱与视觉分类`).
- Live `script.js` returns HTTP 200.

## Second exhibition not exposed on Pages

The following URLs all return HTTP 404, confirming the second exhibition is not deployed:

- `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`
- `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/site/`
- `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/site/index.html`
- `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/assets/asset-import-manifest.json`
- All six asset image URLs under `second-exhibition/assets/images/`.

## No deployment configuration

- No second-exhibition-specific GitHub Pages workflow exists.
- No `CNAME` file is present in the repository root.
- No `second-exhibition/CNAME` exists.
- The `second-exhibition/site/` directory is not referenced in any workflow.

## Repository-only status

- `exhibition.json` status: `repository-only-not-deployed`.
- `assets.json` status: `repository-only-not-deployed`.
- The site page shows "repository-only / not deployed" in the repository status banner.
- The main `README.md` does not describe the second exhibition as deployed or live.

## Future deployment must use separate audited round

- Deploying the second exhibition would require:
  - a new v4.x round explicitly authorized for deployment,
  - a new workflow or build step that targets `second-exhibition/site/`,
  - re-verification of all source/rights URLs,
  - a stable live URL path (e.g. `/second-exhibition/` or a separate domain),
  - a new tag or freeze marker before deployment.
- No such round is currently authorized or in progress.

## Result

- All deployment-safety checks in `scripts/second_exhibition_repository_qa.py` PASS.
- The second exhibition remains repository-only and is not exposed on GitHub Pages.

<!-- v4.7-partial-finding -->
## Relationship to the blocking finding

Deployment-safety checks remain valid: the second exhibition is repository-only and its Pages paths remain unavailable. The v4.7 PARTIAL result is caused solely by the missing `#lightbox-title` ARIA target, not by deployment exposure.
