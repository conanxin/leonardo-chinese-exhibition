# v5.6d Second Exhibition Live Browser QA Reproducibility

## Problem (v5.6c → v5.6d handoff)

The v5.6c post-deploy round (commit `fff6e78`) used a temporary runner at
`/tmp/v56c-live-browser-qa.mjs` to perform the public 5-viewport browser
QA. The temporary runner carried several fixes that were not in the
repository's official runner `scripts/second_exhibition_browser_qa.mjs`:

- HTTPS support in the pre-flight `checkServer()` (the official runner
  used `node:http` only, which fails against `https://` URLs)
- Origin-aware request tracking (the official runner treated anything
  outside `http://127.0.0.1`/`http://localhost` as "external", which
  incorrectly flagged same-origin subresource fetches on a public URL
  as external)
- Per-image lazy-load triggering via `scrollIntoView()` and a 1500 ms
  hydration wait (the official runner's `scrollTo(0, scrollHeight)` +
  800 ms is also correct on the current page, but the temporary
  runner's per-image pattern is more explicit)
- A 1200 ms hydration wait after `goto({waitUntil: "networkidle"})`

The freeze requirement is that the QA must be reproducible from
**repository content only** — no `/tmp` scripts, no user-specific
hardcoded paths, no environment-dependent `~/.local/...` lookups.

## What v5.6d changed (in the official runner)

`scripts/second_exhibition_browser_qa.mjs` is now the single source of
truth for both local and public QA. Changes are minimal and
additive — the v4.8 design (default URL, env vars, exit codes,
viewport matrix) is preserved.

1. **HTTPS support in `checkServer()`** — switched from `http.get`
   to `https.request` (or `http.request` for `http://`), with the
   correct default port (443 / 80). A 5 s timeout and a 2xx
   status check are unchanged.
2. **Origin-aware request tracking** — `trackRequests()` now skips
   any request whose URL starts with the **origin of TARGET_URL**
   (`{protocol}://{host}`). This means:
   - Local server (`http://127.0.0.1:8770`) → in-page `/site/...` and
     `/site/assets/...` are first-party, never external.
   - Public site (`https://conanxin.github.io/leonardo-chinese-exhibition/`)
     → in-page `/.../second-exhibition/assets/...` and
     `/.../second-exhibition/script.js` are first-party, never external.
   - `data:` and `blob:` URLs are also skipped (not network).
3. **Better error message on `checkServer()` failure** — when the
   unreachable URL is local, the message still suggests
   `python3 -m http.server 8770 --directory second-exhibition`. When
   the unreachable URL is non-local, the message is neutral
   ("check network/proxy") so it doesn't mislead on a real outage.
4. **Updated docstring** — documents both invocation patterns
   (local server, public URL) and explicitly states the file is
   **the** QA entry point for both surfaces.

What v5.6d **did not** change:

- The Playwright module loader (`loadPlaywright`) is unchanged. The
  official mechanism — `PLAYWRIGHT_NODE_PATH` env var, fallback
  `require("playwright")`, fallback `require("playwright-core")` —
  is what the script has used since v4.8. v5.6d does **not** hardcode
  any user home or absolute install path. The v5.6c temporary
  runner's `~/.local/node_modules/playwright-core` lookup was a
  per-environment invocation decision (exported via env var), not
  a script constant.
- Lazy-image scroll handling is unchanged (still `scrollTo(scrollHeight)`
  + 800 ms). This is correct on the v0.2 page; v5.6c temporary
  runner's `scrollIntoView()` was equivalent in result.
- Selectors, viewport matrix, interaction checks, a11y checks,
  no-JS check, reduced-motion check, request filter, and PASS/FAIL
  aggregation are all byte-identical to v4.8.

## Verification (post-edit)

Both surfaces were verified using the **official runner** in this round:

### Public 5-viewport QA (https://conanxin.github.io/.../second-exhibition/)

```bash
PLAYWRIGHT_NODE_PATH=/home/conanxin/.local/node_modules/playwright-core \
SECOND_EXHIBITION_QA_URL=https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/ \
  node scripts/second_exhibition_browser_qa.mjs
```

- status: **PASS**
- 5 viewports × 16 checks each = 80/80 PASS, 0 fail
- 1440×1000 / 1280×900 / 768×1024 / 390×844 / 320×700 — all pass
- interactions: guided toggle, lightbox open, lightbox role=dialog,
  accessible name=`lightbox-title`, close button focused, ESC close,
  focus return, C-06 lightbox disabled, section nav, tab focusable —
  all true
- a11y: h1=1, imgMissingAlt=0, buttonMissingName=0, headingJump=false,
  lightbox title not hidden from AT
- no-JS: 6 cards, 6 source notes, 6 credit lines, repo status visible,
  body text rendered
- reduced-motion: lightbox opens + ESC closes under
  `prefers-reduced-motion: reduce`
- errors: external=0, failed=0, console=0, page=0
- browser: chromium 148.0.7778.96 (from `~/.local/node_modules/playwright-core`)

### Local 5-viewport QA (default URL, no env override)

```bash
python3 -m http.server 8770 --directory second-exhibition --bind 127.0.0.1 &  # background
PLAYWRIGHT_NODE_PATH=/home/conanxin/.local/node_modules/playwright-core \
  node scripts/second_exhibition_browser_qa.mjs
```

- status: **PASS** (no `SECOND_EXHIBITION_QA_URL` env)
- 5 viewports × 16 checks = 80/80 PASS
- identical interaction / a11y / no-JS / reduced-motion / errors to public
- default URL `http://127.0.0.1:8770/site/` works as before
- bytes served locally: 31,458 B (source build; live is 31,452 B after
  Pages path-rewriting)

## How to run the QA (canonical invocation)

### Local

```bash
# from the repository root
python3 -m http.server 8770 --directory second-exhibition --bind 127.0.0.1 &
PLAYWRIGHT_NODE_PATH="$(npm root -g)/playwright-core" \
  node scripts/second_exhibition_browser_qa.mjs
```

The runner's default URL is `http://127.0.0.1:8770/site/`, matching
the v4.8 invocation shape.

### Public

```bash
PLAYWRIGHT_NODE_PATH="$(npm root -g)/playwright-core" \
SECOND_EXHIBITION_QA_URL=https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/ \
  node scripts/second_exhibition_browser_qa.mjs
```

If `npm root -g` returns a directory that does not contain
`playwright-core` (e.g. on a machine with only `python -m playwright`),
set `PLAYWRIGHT_NODE_PATH` to the absolute path of the directory that
contains `playwright-core` (the v4.8 escape hatch — `PLAYWRIGHT_NODE_PATH`
is the canonical override).

## Public artifact unchanged

- root: 92,976 B / SHA `e2be1077…` — **unchanged**
- second: 31,452 B / SHA `00894e8d…` — **unchanged**
- `second-exhibition-v0.2` marker count = 3, stale v0.1 marker = 0
- 6/6 image checksums identical
- 70/70 default healthcheck PASS

## Scope guard (this round)

Modified files:

- `scripts/second_exhibition_browser_qa.mjs` — only file changed in
  the working tree

Protected paths (must be empty diffs):

- `site/`, `second-exhibition/site/`, `second-exhibition/data/`,
  `second-exhibition/assets/`, `second-exhibition/docs/`,
  `.github/workflows/`, `_template/`, `_pilots/`, `posts/`,
  `case-study/`, `release-assets/` — all empty
- No other `scripts/*.py` modified
- No `__pycache__` in working tree
- Stable v5.0 tag / Release — unchanged
- No new tag / Release created
