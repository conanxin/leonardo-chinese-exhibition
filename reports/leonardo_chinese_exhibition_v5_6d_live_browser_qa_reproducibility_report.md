# v5.6d Live Browser QA Reproducibility Report

- **Round**: v5.6d — Live browser QA reproducibility
- **Date**: 2026-07-12
- **Trigger**: v5.6c used a `/tmp` temporary runner for the public
  5-viewport QA. The freeze requirement is "QA reproducible from
  repository content only", so the v5.6c fixes had to be promoted
  into the official runner.
- **Status**: PASS

## 1. Baseline

- Pre-v5.6d HEAD: `fff6e785db8c86e06ecad823a3e3ba4c28301cb8`
- Pre-v5.6d origin/main: `fff6e785db8c86e06ecad823a3e3ba4c28301cb8`
- Stable v5.0 tag: `v5.0-real-second-exhibition-deployment` →
  `ac0f19e2c03b09738ae49b4a15c629a1f2177068` (unchanged)
- Stable Release: published, unchanged

## 2. Reality gate

| Check | Result |
|---|---|
| HEAD == origin/main | PASS |
| tracked tree clean before edits | PASS |
| `.firecrawl/` ignored as expected | PASS |
| `__pycache__` cleanup | PASS (none present) |

## 3. v5.6c → v5.6d fix list (promoted into official runner)

| Fix | Was in `/tmp/v56c-live-browser-qa.mjs` | Now in `scripts/second_exhibition_browser_qa.mjs` |
|---|---|---|
| `checkServer()` HTTPS support | yes (implicit — no pre-flight, used `goto` directly) | yes (explicit `https.request` for `https://` URLs) |
| `trackRequests` origin-aware (same-origin = first-party) | yes (`url.startsWith(TARGET_URL.split('/s')[0])`) | yes (uses `ORIGIN = targetOrigin()` helper) |
| `data:` / `blob:` skip | partial | yes |
| Lazy-image scroll + 1500 ms hydration | yes | unchanged (v4.8 scroll-to-bottom + 800 ms; already correct on v0.2) |
| `playwright` path lookup | `~/.local/node_modules/playwright-core` hardcoded | unchanged (v4.8 design: `PLAYWRIGHT_NODE_PATH` env + `require("playwright")` + `require("playwright-core")`) |

The two real bugs in the v4.8 runner for the public-URL case are fixed
(HTTPS pre-flight + origin-aware request tracking). The other
"differences" between v5.6c temporary and v4.8 are stylistic /
equivalent — kept the v4.8 shape to honor the freeze requirement.

## 4. Local 5-viewport QA (default URL, no env override)

```bash
python3 -m http.server 8770 --directory second-exhibition --bind 127.0.0.1 &
PLAYWRIGHT_NODE_PATH=/home/conanxin/.local/node_modules/playwright-core \
  node scripts/second_exhibition_browser_qa.mjs
```

- status: **PASS**
- 5 viewports × 16 checks = 80/80 PASS, 0 fail
- 1440×1000, 1280×900, 768×1024, 390×844, 320×700 — all pass
- interactions: guided toggle, lightbox open, lightbox role=dialog,
  accessible name=`lightbox-title`, close button focused, ESC close,
  focus return, C-06 lightbox disabled, section nav, tab focusable —
  all true
- a11y: h1=1, imgMissingAlt=0, buttonMissingName=0, headingJump=false
- no-JS: 6 cards / 6 source notes / 6 credit lines / repo status visible / body text
- reduced-motion: lightboxOpen + escClose — both true
- errors: external=0, failed=0, console=0, page=0
- bytes served locally: 31,458 B (source build; live is 31,452 B after Pages path-rewriting)

## 5. Public 5-viewport QA (real Pages URL)

```bash
PLAYWRIGHT_NODE_PATH=/home/conanxin/.local/node_modules/playwright-core \
SECOND_EXHIBITION_QA_URL=https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/ \
  node scripts/second_exhibition_browser_qa.mjs
```

- status: **PASS**
- 5 viewports × 16 checks = 80/80 PASS, 0 fail
- 1440×1000, 1280×900, 768×1024, 390×844, 320×700 — all pass
- interactions: all 10 true
- a11y: h1=1, imgMissingAlt=0, buttonMissingName=0, headingJump=false
- no-JS: 6 cards / 6 source notes / 6 credit lines / repo status visible / body text
- reduced-motion: lightboxOpen + escClose — both true
- errors: external=0, failed=0, console=0, page=0
- browser: chromium 148.0.7778.96 (via `~/.local/node_modules/playwright-core`)

## 6. Public artifact unchanged (34/34 byte-identity)

| Identity | Pre-v5.6d | Post-v5.6d | Same? |
|---|---|---|---|
| root bytes | 92,976 | 92,976 | yes |
| root SHA256 | `e2be1077…` | `e2be1077…` | yes |
| second bytes | 31,452 | 31,452 | yes |
| second SHA256 | `00894e8d…` | `00894e8d…` | yes |
| `second-exhibition-v0.2` marker count | 3 | 3 | yes |
| stale `second-exhibition-v0.1` count | 0 | 0 | yes |
| 6 image checksums | OK | OK | yes |
| Default healthcheck | 70/0 | 70/0 | yes |

## 7. Scope guard (this round)

Modified files (working tree, this round):

- `scripts/second_exhibition_browser_qa.mjs` (additive only — see §3)
- `docs/SECOND_EXHIBITION_LIVE_BROWSER_QA_REPRODUCIBILITY_v5.6d.md` (new)
- `docs/V5_ROADMAP.md` (v5.6d section appended)
- `README.md` (v5.6d section appended)
- `reports/leonardo_chinese_exhibition_v5_6d_live_browser_qa_reproducibility_report.md` (this file, new)

Protected paths (all empty diffs):

- `site/`
- `second-exhibition/site/`, `second-exhibition/data/`,
  `second-exhibition/assets/`, `second-exhibition/docs/`
- `.github/workflows/`
- `_template/`, `_pilots/`, `posts/`, `case-study/`, `release-assets/`
- All other `scripts/*.py`
- No `__pycache__` in working tree
- No `.gitignore` changes

## 8. No-touch confirmation

- Public production surface — **unchanged**
- 6 image files — **unchanged** (same SHA)
- Source / rights evidence (`second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`,
  `second-exhibition/docs/RIGHTS_AND_SOURCES.md`) — **unchanged**
- Workflow (`.github/workflows/`) — **unchanged**
- Stable v5.0 tag `v5.0-real-second-exhibition-deployment` — **unchanged**
- Stable Release — **unchanged**
- No new tag, no new Release created

## 9. Files modified (final)

1. `scripts/second_exhibition_browser_qa.mjs` — promote v5.6c fixes (HTTPS, origin-aware tracking)
2. `docs/SECOND_EXHIBITION_LIVE_BROWSER_QA_REPRODUCIBILITY_v5.6d.md` (new)
3. `docs/V5_ROADMAP.md` (append v5.6d section)
4. `README.md` (append v5.6d section)
5. `reports/leonardo_chinese_exhibition_v5_6d_live_browser_qa_reproducibility_report.md` (this file, new)

## 10. Next recommended task

- **v5.6-real-stable-freeze**
