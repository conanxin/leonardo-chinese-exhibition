# v5.0 Second Exhibition Deployment Options

## Baseline

- HEAD / origin/main: `01bebd87c2d109b2e549430436fe91c8ff2d3720`
- v4.8 release tag: `v4.8-real-second-exhibition-repository-hardening`
- v4.8 tag target: `a70c8430a8e3d01153153e54f055d9907340d6b7`
- Live URL: https://conanxin.github.io/leonardo-chinese-exhibition/
- Live byte: **92,976 B**
- Current Pages workflow: `.github/workflows/pages.yml` — deploys only `site/` (top-level)
- Second exhibition: **repository-only-not-deployed**

## Constraints that apply to every option

- Source / rights evidence is not negotiable: any published copy must pass a second source/rights recheck.
- The existing live Leonardo exhibition (`/`) must not regress.
- Existing Pages URL must remain reachable at exactly `https://conanxin.github.io/leonardo-chinese-exhibition/`.
- Existing tags (`v2.0` through `v4.8`) and Releases must remain immutable.
- All `second-exhibition/` Pages URLs must remain non-200 until a future round explicitly authorizes deployment.

## Option A — Existing GitHub Pages subpath

**Future URL:**
- `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`

**Approach:**
- Continue using the same repository and the same Pages project.
- Re-engineer the Pages workflow to publish an **isolated staging artifact** assembled from `site/` + a copy of `second-exhibition/site/` (path-rewritten) + a copy of `second-exhibition/assets/images/`.
- Do **not** publish the repository root.
- The existing top-level site (`/`) keeps the same byte-for-byte content.

**Pros:**
- One repository, one Pages project, one set of Releases.
- Version control stays unified; the second exhibition can be co-released with future Leonardo updates.
- User entry point stays consistent (single `conanxin.github.io/leonardo-chinese-exhibition` URL).
- No new DNS, no new repo, no new deploy target to audit.
- Backward compatibility: if the second exhibition ever needs to be pulled, the workflow reverts to deploy only `site/`.

**Risks:**
- A workflow regression could damage the existing main site if the staging assembly is misconfigured.
- Path rewriting (`../assets/images/` → `./assets/images/`) must be deterministic and tested.
- A bad artifact can serve content from an unintended directory.
- Requires atomic rollback planning (handled separately).

## Option B — Separate GitHub Pages repository

**Future URL (example):**
- `https://conanxin.github.io/<new-repository>/`

**Approach:**
- Create a second repository that holds a public mirror of the second exhibition's HTML/CSS/JS + raster assets.
- The new repository has its own Pages workflow that publishes the second exhibition at the new URL.

**Pros:**
- Full deployment isolation from the existing site.
- The Leonardo workflow remains untouched.
- Simpler local workflow (one repo = one site).

**Risks:**
- Project history forks: the second exhibition's release tags become harder to align with the source-of-truth repo.
- Asset / documentation duplication or two-way sync overhead.
- Two sets of Releases to maintain, two sets of CI to keep green.
- The new repo must re-do the source/rights audit independently, doubling audit surface.
- Repo creation itself requires GitHub authentication outside the current pipeline.

## Option C — Separate custom subdomain / Cloudflare Pages

**Future URL (example):**
- `https://botanical.conanxin.com/`

**Approach:**
- Deploy the second exhibition to Cloudflare Pages under a custom subdomain.
- DNS managed at the registrar; TLS via Cloudflare.

**Pros:**
- Brand-clear URL.
- Full deployment isolation.
- Independent scaling / edge caching.

**Risks:**
- DNS, TLS certificate, and Cloudflare account all become new dependencies that need audit.
- Adds a separate deployment platform outside the GitHub Pages baseline.
- Cross-platform deployment means cross-platform regression testing.

## Comparison table

| Option | Isolation | Existing-site risk | Operational complexity | URL quality | Rollback | Recommendation |
|--------|-----------|--------------------|------------------------|-------------|----------|----------------|
| **A — Existing Pages subpath** | Medium (artifact isolation) | Low (workflow is currently scoped to `site/` only; new workflow still publishes only the staging artifact) | Low (one workflow, one repo, one Release stream) | Good (`/second-exhibition/` subpath under the existing user-facing site) | Easy (revert the workflow change; main live site unchanged) | **Recommended default** |
| **B — Separate GitHub Pages repo** | High | Very low (no shared deploy) | High (split history, double source/rights audit, two release streams) | Medium (new repo URL) | Medium (need to keep old repo / link) | **Isolation / rollback fallback** |
| **C — Custom subdomain on Cloudflare** | Very high | Very low (separate platform) | Very high (DNS, TLS, Cloudflare account, cross-platform regressions) | High (clean branded URL) | Medium (depends on DNS / platform rollback) | Not recommended now (out of scope) |

## Recommendation

**Option A — Existing GitHub Pages subpath** is the recommended default.

Rationale:
- The existing Pages workflow is already scoped to `site/` only. Reusing this baseline with a strict staging artifact minimizes new surface area.
- A second exhibition co-released with the Leonardo stable line gives one Release stream and one source/rights audit chain.
- Atomic rollback is straightforward: revert the workflow commit and the main live site is unaffected.
- It does not require new DNS, no new authentication, no new repository.

**Option B** remains the fallback when full deployment isolation is later required (e.g., if the second exhibition ever needs a release cadence that conflicts with the Leonardo line).

**Option C** is out of scope for now and would require a separate platform audit before adoption.

## Final architectural choice

- **Default:** Option A.
- **Fallback:** Option B.
- **Future option:** Option C (separate round with its own platform audit).