# v5.0 Real Second Exhibition Deployment

## Public URLs

- Existing Leonardo exhibition:
  https://conanxin.github.io/leonardo-chinese-exhibition/
- Second exhibition:
  https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/

## Release identity

- Tag:
  `v5.0-real-second-exhibition-deployment`
- Freeze commit:
  *filled after freeze doc push; see `reports/leonardo_chinese_exhibition_v5_4_public_stable_freeze_report.md` for the final value*
- Root live byte:
  92,976 B
- Root v2.9 exact marker count (precise command: `curl -sS <root> | grep -o 'v2.9-real-source-rights-audit' | wc -l`):
  1
- Root v2.9 loose marker count (`grep -o 'v2\.9' | wc -l`):
  4
- Second-exhibition index byte (live):
  25,635 B
- Second-exhibition SHA-256 of `index.html` (live):
  `<see freeze report>`
- Source root `site/index.html` SHA-256 (uncompressed `cat site/index.html | wc -c`): 92,976 bytes; byte-identical to live root.

## Deployment chain

| Round | Theme | Commit | Subject |
|---|---|---|---|
| v5.1 | Staging artifact build | — | (no main commit; staging-only artifact built in CI runner scratch space) |
| v5.2 | Deployment dry run | — | (workflow-only rehearsal; no main commit) |
| v5.3 | Controlled deployment | `f84e53f7f1c5fa20fc8fc40e747bbf934cdfdf92` | Wire v5.3 controlled second-exhibition deployment into Pages workflow |
| v5.3 | Controlled deployment | `83ab6d8bc8a3f278d53c72516cf72d1a747e13bd` | Fix v5.3 controlled deploy: pass --audit to staging builder |
| v5.3b | Production-state reconciliation | `52504047a966c0dd9a60b569a63b1857168a498f` | Reconcile second-exhibition production state (v5.3b) |
| v5.3c | Live production browser QA | `bfce140029a66a95a0b52115f5083b3aef308f6a` | Verify live second exhibition production QA |
| v5.4 | Public stable freeze | *TBD* | Freeze verified v5.0 second exhibition deployment (this round) |

The four key commits that materially moved the live surface are `f84e53f`, `83ab6d8`, `5250404`, `bfce140`. The freeze commit added in v5.4 contains only documentation (release notes, release manifest, stable-freeze report, V5_ROADMAP.md update, README.md update) — no live file is touched by the freeze commit.

## Published exhibition

- Working title:
  《植物图谱与视觉分类：从自然史图像到知识秩序》
- Sections: 4
- Artifact cards: 6
- Glossary items: 12
- Source notes: 6
- Credit lines: 6
- Public image assets: 6
- Status (visible on the public page):
  `production-deployed-v5.3`
- Asset publication status (per-asset, visible on every artifact card and in footer):
  `published-in-v5.3`
- Historical import status (preserved, visible only inside the explicit `Import record: imported-not-deployed (v4.5)` annotation on each artifact card):
  `imported-not-deployed`
- Candidates: C-01, C-03, C-06, C-08, C-09, C-10
- C-06 is intentionally rendered at low resolution (Smithsonian NMNH thumbnail 90×90 px) with a visible low-resolution warning; clicking C-06 does NOT open the lightbox (only the warning surfaces). The C-06 lightbox-exclusion behavior is encoded in `second-exhibition/site/script.js` and verified end-to-end by both local and live browser QA runs.

## Verification

| Check | Result |
|---|---|
| Template gate | 37 / 37 PASS |
| Build gate | PASS |
| Repository QA | 164 / 164 PASS |
| Asset checksums | 6 / 6 PASS |
| Live browser QA | 5 / 5 viewports PASS (1440×1000, 1280×900, 768×1024, 390×844, 320×700) |
| Console errors | 0 |
| Page errors | 0 |
| Failed requests | 0 |
| External (non-`conanxin.github.io`) requests | 0 |
| Horizontal overflow | 0 across all 5 viewports |
| Root live / source identity | PASS (`cmp -s` byte-identical, 92,976 B) |
| Second exhibition live / staged identity | PASS (`cmp -s` byte-identical for `index.html`, `style.css`, `script.js`) |
| Public inventory (artifact) | 25 main-site + 9 second-exhibition = 34 files |
| Forbidden public paths | 18 / 18 → HTTP 404 |
| GitHub Actions (last v5.3b push) | success, run `29172641937`, ~20 s |

## Accessibility

The published second exhibition was designed and verified for assistive-technology compatibility across the v5.3 → v5.3c rounds:

- One `<h1>` per page; section landmarks are real `<section>` elements with `aria-labelledby` pointing at internal headings (no nested heading-level skips).
- Decorative SVGs / lightbox-scaffold images carry `alt=""` explicitly; the curated candidate images (Rijksmuseum / BHL / Smithsonian / Met) carry non-empty `alt` text describing the source page or specimen (alt coverage 30/35 across the 5-viewport matrix; the 5 misses are intentional `alt=""` decorative icons).
- One `<button>` per interactive control. The guided-mode toggle (`#guided-toggle`) is a `<button>` with `aria-pressed="false"|"true"`; clicking switches the value correctly.
- The lightbox is a `<div role="dialog" aria-modal="true" aria-labelledby="lightbox-title">`; its accessible name resolves to **`图片查看器`** (text content of `<h2 id="lightbox-title">图片查看器</h2>`). Opening the lightbox moves focus to the close button; pressing `Escape` closes it; closing it returns focus to the image trigger that opened it.
- The C-06 click is intentionally blocked (its overlay text says so); the script returns early before opening the dialog, so no dialog-aria side-effect occurs.
- Tab reaches the 6 primary buttons (guided toggle + section-nav links + lightbox close); no focus traps.
- The page remains readable with JavaScript disabled (`html`-only render): the title, all three status phrases, the 6 artifact cards, the source notes, and the credit lines remain visible. The semantic information does not depend on JS.
- The page respects `prefers-reduced-motion: reduce`: under Playwright `emulateMedia({ reducedMotion: "reduce" })`, lightbox open + `Escape` close still work cleanly, and the live media-query match confirms `prefers-reduced-motion` is honoured by the browser.

## Deployment safety

- The combined artifact (root + second-exhibition subtree) is built and gated **before** upload. The Pages workflow invokes `scripts/second_exhibition_staging_build.py` with `--output <runner.temp>/leonardo-pages-artifact` and `--audit <runner.temp>/leonardo-pages-artifact-audit`, then `scripts/second_exhibition_staging_gate.py` validates byte-identity, the 6 image SHA-256, the allowlist (only public allowlisted files), forbidden-leakage (none), and the on-page wording (`production-deployed-v5.3 + published-in-v5.3`, preserved `imported-not-deployed`, no stale prose).
- Only public allowlisted files are deployed. Internal documents (`README.md`, `V4_ROADMAP.md`, `V5_ROADMAP.md`, `docs/`, `data/`, `_template/`, `_pilots/`, `release-assets/`, `reports/`, `scripts/`, `.github/`, `.firecrawl/`, and the second-exhibition `data/` / `docs/` / `assets/asset-import-manifest.json` / `assets/asset-checksums.sha256` paths) return HTTP 404 on the live URL.
- Rollback is by single-commit revert: `git revert <v5.0-doc-commit-sha>` followed by `git push origin main` restores the previous live surface byte-for-byte (since the freeze commit touches only docs/manifest/report/ROADMAP/README, not the live surface). For a deeper pre-v5.4 rollback, `git revert 5250404 83ab6d8 f84e53f` (in reverse order) restores the pre-v5.3 Pages workflow that only deploys `site/`.
- No historical tag was moved in this round. The freeze process creates a new tag `v5.0-real-second-exhibition-deployment` and a new GitHub Release; existing tags `v2.0-public-portfolio-case` through `v4.8-real-second-exhibition-repository-hardening` remain pinned to their original commits.
- No existing GitHub Release was overwritten.

## Next

Maintenance / content iteration under v5.0 (per `docs/V5_ROADMAP.md` v5.4 "Next"):

- Each future content round is a separate commit on `main`, with optional per-round tag / Release, gated by the same template / build / repository / browser QA tooling.
- The `v4.8-real-second-exhibition-repository-hardening` source-freeze anchor remains the most recent pre-v5 milestone tag.
- This release (`v5.0`) is the first public deployment tag.
