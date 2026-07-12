# v5.6d Live Browser QA Reproducibility

## Problem (v5.6c → v5.6d handoff)

The v5.6c post-deploy round (commit `fff6e78`) used a temporary runner
at `/tmp/v56c-live-browser-qa.mjs` to perform the public 5-viewport
browser QA. The temporary runner carried several fixes that were not
in the repository's official runner
`scripts/second_exhibition_browser_qa.mjs`. The freeze requirement is
that the QA must be reproducible from **repository content only** — no
`/tmp` scripts, no user-specific hardcoded paths.

## Baseline (this round)

- Pre-v5.6d HEAD: `96bef6a4c16745dc420630a6df081c663c440929` (v5.6d
  promotion commit; tracked tree clean)
- Production identity (live, this round):
  - root: 92,976 B / SHA `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`
  - second: 31,452 B / SHA `00894e8dfa0fa1e40ed3df803afa0036a2a070bee8f42cdfb636cd31d68b3aa2`
  - marker `second-exhibition-v0.2` count = 3, stale v0.1 count = 0
  - 6/6 image checksums OK
- Browser / Playwright:
  - chromium 148.0.7778.96 via `playwright-core` (resolved through
    `PLAYWRIGHT_NODE_PATH=/home/conanxin/.local/node_modules/playwright-core`)
  - Node 22 / `~/.local/node_modules/playwright-core` available
- Staging build (v5.6d this round):
  - root 25 files, second 9 files, path rewrite count 6
  - source SHA `662bee42799a5e92fb7407a37d2fe57d02bfd123a344cbeada0cb51b99c5030e` / staged SHA `00894e8d…`
- Dry run PASS:
  - allowlist probes 14/14
  - forbidden probes 16/16
  - roundtrip 34 byte-identical
  - schema 2.0

## Initial official runner result (this round, before further edits)

`SECOND_EXHIBITION_QA_URL=https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/ \
 PLAYWRIGHT_NODE_PATH=… node scripts/second_exhibition_browser_qa.mjs`

- Run 1: **FAIL** — 1440×1000 viewport, `images loaded = 5` (expected 6)
- Run 2 (immediate retry, hot cache): **PASS** — 5/5 viewports, imgsLoaded `[6, 6, 6, 6, 6]`

The official runner (as of commit `96bef6a`) is **non-deterministic** on
the public URL's cold cache: scroll-to-bottom + 800 ms tail wait + 3 s
per-image timeout is sometimes not enough for BHL's 2 lazy `webp`
images to complete fetch + decode before the page sample. The freeze
requirement is "QA reproducible from repository content only", which
implicitly requires deterministic PASS.

## Differences audited (vs. v5.6c temporary runner)

| Category | v5.6c temporary | v5.6d official (this round, after edits) | Notes |
|---|---|---|---|
| **Playwright module resolution** | hardcoded `~/.local/...` + `/tmp/playwright-test/...` | env `PLAYWRIGHT_NODE_PATH` + `require("playwright")` + `require("playwright-core")` | hardcoded paths explicitly forbidden by brief §4 B; kept env-driven |
| **HTTPS pre-flight** | implicit (no pre-flight) | explicit `https.request` (added in v5.6d commit `96bef6a`) | same behavior on success, better failure message |
| **Origin-aware request tracking** | `url.startsWith(TARGET_URL.split("/s")[0])` | `url.startsWith(ORIGIN)` helper (added in `96bef6a`) | same behavior, cleaner expression |
| **Lazy image scroll** | `scrollIntoView()` per-image + 1500 ms hydration | scroll-to-bottom + **1500 ms tail wait** (this round) | tail wait bumped 800 → 1500 ms |
| **Per-image load timeout** | 3000 ms (in `checkPage`) | **5000 ms** (this round) | bumped 3 s → 5 s |
| **Selectors** | identical | identical | no change |
| **Interactions** | identical (guided/lightbox/esc/focus/C-06/section nav/tab) | identical | no change |
| **Result serialization** | `JSON.stringify` | `JSON.stringify` | no change |
| **Default URL** | hardcoded public URL | preserves `http://127.0.0.1:8770/site/` (v4.8 compat) | no change |
| **Exit codes** | none explicit | 0/1/2 (v4.8) | no change |

**Items explicitly NOT ported** (per brief §3 forbidden list):

- absolute user paths (`/home/conanxin/...`, `~/.local/...`)
- ad-hoc `/tmp/playwright-test/...` location
- machine-specific Chromium executable path
- unbounded `setTimeout` waits
- silent `try/catch` around failures
- "FAIL → WARN" downgrades

## Changes (this round)

`scripts/second_exhibition_browser_qa.mjs` — only file changed:

1. `runViewport()` lazy-load tail wait: `setTimeout(800)` →
   `setTimeout(1500)` after the scroll-to-bottom step, with an
   inline comment explaining why (cold-cache `loading="lazy"` images
   need a few extra hundred ms after the IntersectionObserver fires
   to complete the fetch + decode).
2. Per-image `setTimeout` cap in the load poll: `3000` → `5000`, with
   an inline comment explaining the bound (a slow cold-cache 404
   should still surface as not-loaded rather than hanging the whole
   viewport).

Net diff: `1 file changed, 12 insertions(+), 2 deletions(-)`.

## Local exact-base-path result (this round, after edits)

Server: `python3 -m http.server` over `/tmp/v56d-artifact` (the v5.6d
staging artifact), base path `/leonardo-chinese-exhibition`.

URL: `http://127.0.0.1:8772/leonardo-chinese-exhibition/second-exhibition/`

3 consecutive runs:

| Run | Status | viewports | imgsLoaded per vp | errors (ext/fail/con/page) |
|---|---|---|---|---|
| 1 | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 |
| 2 | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 |
| 3 | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 |

- interactions: guidedToggle / lightboxOpen / lightboxRole=dialog /
  lightboxAccessibleName=lightbox-title / closeButtonFocused /
  escClose / focusReturn / c06LightboxOpen=false / sectionNav /
  tabFocusable — all true
- a11y: h1=1, imgMissingAlt=0, buttonMissingName=0, headingJump=false
- no-JS: 6 cards / 6 source notes / 6 credit lines / repo status
  visible / body text
- reduced-motion: lightboxOpen + escClose

## Production result (this round, after edits)

URL: `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`

3 consecutive runs:

| Run | Status | viewports | imgsLoaded per vp | errors (ext/fail/con/page) |
|---|---|---|---|---|
| 1 | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 |
| 2 | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 |
| 3 | PASS | 5/5 | [6, 6, 6, 6, 6] | 0/0/0/0 |

Identical interaction / a11y / no-JS / reduced-motion to local. Browser:
chromium 148.0.7778.96 (via `PLAYWRIGHT_NODE_PATH`).

## Reproduction command (canonical, both surfaces)

### Public (the freeze reference)

```bash
PLAYWRIGHT_NODE_PATH="$(npm root -g)/playwright-core" \
SECOND_EXHIBITION_QA_URL=https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/ \
  node scripts/second_exhibition_browser_qa.mjs
```

If `$(npm root -g)/playwright-core` does not exist on the host,
set `PLAYWRIGHT_NODE_PATH` to any absolute path containing
`playwright-core`. The runner's default fallback is
`require("playwright")` then `require("playwright-core")`, which
covers global installs and `NODE_PATH`-configured installs without
hardcoding any user home or `/tmp` location.

### Local exact-base-path

```bash
python3 scripts/second_exhibition_staging_build.py \
  --output /tmp/v56d-artifact --audit /tmp/v56d-audit
python3 scripts/second_exhibition_staging_gate.py \
  --artifact /tmp/v56d-artifact --audit /tmp/v56d-audit
python3 scripts/second_exhibition_deployment_dry_run.py \
  --artifact /tmp/v56d-artifact --audit /tmp/v56d-audit \
  --dry-run-dir /tmp/v56d-dry-run --roundtrip-dir /tmp/v56d-roundtrip \
  --tar /tmp/v56d-artifact.tar.gz \
  --repo-base /leonardo-chinese-exhibition --server-port 8772
# Keep the staging server up by re-running it manually if needed:
python3 -c "
import http.server, socketserver, os
class H(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        base = '/leonardo-chinese-exhibition'
        if path.startswith(base): path = path[len(base):] or '/'
        return os.path.join('/tmp/v56d-artifact', path.lstrip('/'))
socketserver.TCPServer.allow_reuse_address = True
socketserver.TCPServer(('127.0.0.1', 8772), H).serve_forever()
" &

PLAYWRIGHT_NODE_PATH="$(npm root -g)/playwright-core" \
SECOND_EXHIBITION_QA_URL=http://127.0.0.1:8772/leonardo-chinese-exhibition/second-exhibition/ \
  node scripts/second_exhibition_browser_qa.mjs
```

`/tmp/v56d-*` is a per-run temp directory; the runner itself has no
dependency on it. The artifact, audit, and dry-run directories are
git-ignored / outside the repository.

### Local v4.8 default (no staging)

```bash
python3 -m http.server 8770 --directory second-exhibition --bind 127.0.0.1 &
PLAYWRIGHT_NODE_PATH="$(npm root -g)/playwright-core" \
  node scripts/second_exhibition_browser_qa.mjs
```

The default URL is `http://127.0.0.1:8770/site/`, matching the v4.8
invocation shape. No env override needed.

## No drift

- `site/` `second-exhibition/site/` `second-exhibition/data/`
  `second-exhibition/assets/` `second-exhibition/docs/` — **unchanged**
- `.github/workflows/` — **unchanged**
- `_template/` `_pilots/` `posts/` `case-study/` `release-assets/` —
  **unchanged**
- All other `scripts/*.py` — **unchanged**
- No `__pycache__` in working tree
- Stable v5.0 tag `v5.0-real-second-exhibition-deployment` →
  `ac0f19e2c03b…` — **unchanged**
- Stable Release — **unchanged**
- 34/34 public artifact files: byte-identical to v5.6c (root 92,976 B,
  second 31,452 B)
- 6/6 image checksums — **unchanged**

## What this round removed

- `/tmp/v56c-live-browser-qa.mjs` is **no longer the QA entry point**.
  It was kept on disk for audit; the in-repo runner covers everything.
  The `diff -u` between the two files (this round) is now limited to
  the style differences listed in the table above; the substance is
  unified.
