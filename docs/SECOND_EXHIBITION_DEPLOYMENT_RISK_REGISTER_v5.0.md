# v5.0 Second Exhibition Deployment Risk Register

## Risk levels

- **Low** — observable, easy to recover.
- **Medium** — observable, needs coordinated action.
- **High** — observable, blocks deployment until closed.
- **Blocked** — unobservable or unrecoverable; deployment cannot proceed.

## Release blocker

- Any **High** or **Blocked** risk open → no deployment.
- Two or more open **Medium** risks → no deployment without explicit user authorization.

## Risk table

| ID    | Risk | Level | Trigger | Detection | Mitigation | Rollback |
|-------|------|-------|---------|-----------|------------|----------|
| D-01  | Existing top-level site artifact overwritten by bad staging | High | Staging assembly inadvertently replaces `site/*` files instead of leaving them byte-identical | Pre-deploy diff between staging `index.html` and `site/index.html` (must be byte-identical); live byte check after deploy must equal 92,976 B | Keep top-level `site/*` files copied **byte-identical** to source; never run rewrites against the top-level copy | Revert workflow commit; restore workflow to deploy `site/` only; wait for Pages rebuild; verify live byte |
| D-02  | Path rewrite error breaks second-exhibition image references | High | Path rewrite misses an `../assets/images/` reference, or rewrites in the wrong place (top-level site copy) | Staging QA: serve `/second-exhibition/` and verify all 6 image URLs return 200; visual check | Path rewrite applies **only** to the staging copy of `second-exhibition/site/index.html`; never to `site/index.html`; verify rewrite count after staging | Re-run staging assembly with corrected rewrite; redeploy |
| D-03  | Image resource returns 404 on `/second-exhibition/` | High | Missing or misnamed image file under `second-exhibition/assets/images/` in the staging artifact | Browser QA against staging: all 6 `naturalWidth > 0`; live HTTP probe on each `/second-exhibition/assets/images/<file>` returns 200 | Copy exactly the 6 expected filenames; checksum against `second-exhibition/assets/asset-checksums.sha256` | Re-assemble staging; redeploy |
| D-04  | Second-exhibition internal docs / data exposed on Pages | High | Staging assembly accidentally copies `second-exhibition/data/`, `second-exhibition/docs/`, or `asset-import-manifest.json` into the artifact | Pre-deploy allowlist check: only HTML/CSS/JS + 6 image files appear in the staging tree; live HTTP probes on `/second-exhibition/data/`, `/second-exhibition/docs/`, `/second-exhibition/assets/asset-import-manifest.json` all return 404 | Staging assembly copies a strict allowlist; preflight script blocks any path outside it | Revert workflow; redeploy with corrected allowlist |
| D-05  | Repository root uploaded as Pages artifact | Blocked | Workflow change accidentally points to `.` or the repo root instead of the staging artifact | Pre-deploy staging tree inspection (must show only the allowlisted files); live HTTP probe on `/README.md`, `/SECOND_EXHIBITION_*`, `/_template`, `/_pilots` all return 404 | Workflow uploads the staging directory only; never the repository root | Revert workflow; restore previous workflow that uploaded only `site/` |
| D-06  | Existing live byte / marker changes | High | Top-level site content modified during staging | Post-deploy: `wc -c` of live root must equal 92,976 B; `v2.9-real-source-rights-audit` count must equal 1 | Top-level site copy is byte-identical; no edits to it during staging | Revert workflow; restore previous live |
| D-07  | Browser cache serves stale second-exhibition content | Low | A user revisits `/second-exhibition/` after a previous deploy | Cache-Control headers; manual hard-refresh; compare content hash | Cache-Control: `no-cache` for the staged HTML/CSS/JS files; document expected cache behavior | Roll forward with cache-busting path or query string; not a rollback |
| D-08  | Trailing slash / direct index.html mismatch | Medium | `/second-exhibition/` (directory) vs `/second-exhibition/index.html` (file) return different status codes or different content | HTTP probes for both URLs return 200 with identical byte content | Staging artifact places `index.html` under `second-exhibition/` so the directory URL resolves; verify both probes | Re-assemble; redeploy |
| D-09  | Source / rights page changed in the period between v4.8 freeze and v5.x deploy | High | BHL / Met / Rijksmuseum / NMNH per-page statements change | Post-deploy re-verify each source URL; compare against `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` and `RIGHTS_AND_SOURCES.md` | If a source changed, return to repository-only-not-deployed; treat as a new round | Pull second exhibition back to repository-only |
| D-10  | GitHub Actions deploy job fails or lacks permissions | Medium | `actions/deploy-pages@v4` errors out, or `permissions:` block is wrong | GitHub Actions run logs; `pages` and `id-token` permissions must be present | Confirm workflow permissions block; confirm `concurrency.cancel-in-progress: true` is set | Re-run the workflow; if persistent, revert workflow commit |
| D-11  | Rollback commit cannot recover the prior live state | High | Reverting the workflow commit re-publishes the previous Pages artifact, but a stale branch state may still be referenced | After revert: live byte must return to 92,976 B; v2.9 marker count must return to 1; second exhibition URLs must return to 404 | Rollback plan documented; rollback is one revert commit | Revert again; manually re-pin workflow to the v4.8 freeze commit |
| D-12  | Second exhibition marked `live / deployed / approved` in any document or status field | High | A docs file or status field claims the second exhibition is live before verification is complete | Search of v5.x docs / README for `live`, `deployed`, `approved` on second-exhibition references; live HTTP probes | Keep all second-exhibition status strings as `repository-only-not-deployed` until v5.3 verification passes | Edit document; remove the incorrect status claim |
| D-13  | Asset checksum drift | High | Staging copies of the 6 raster images differ from `second-exhibition/assets/asset-checksums.sha256` | Pre-deploy: `sha256sum -c` on the staging copies against the source checksum file | Staging copies are produced via `cp -p`; verify hashes after copy | Re-stage from source |
| D-14  | External request regression | High | Published second-exhibition page sends requests to third-party domains | Browser QA against public URL: `externalRequests` must equal 0; in particular no CDN fonts, no third-party JS, no external image hosts | Asset allowlist is local-only; document forbids external links except user-click navigation to source institutions | Pull second exhibition back to repository-only |
| D-15  | Accessibility regression | High | Headings jump, images lose alt text, buttons lose accessible names, lightbox focus restoration broken | Browser QA against public URL: a11y checks (h1 count = 1, alt present, button names present, no heading jumps, focus restoration works) | Same script.js fix as v4.8; do not modify tracked files in a way that breaks the existing checks | Revert tracked script changes if any; redeploy staging |

## Open High / Blocked risks at the end of v5.0

- **None open.** v5.0 is a planning-only round. All risks above are mitigated by the staging-isolation design and the preflight script.
- The first actual deploy round (v5.3) must re-run this risk register check before any deployment action.

## Risk tracker note

- This register is a living document. Each future round (v5.1, v5.2, v5.3, v5.4) must add a row or update an existing row when new evidence changes a risk level.
- A risk cannot be downgraded without recorded evidence.