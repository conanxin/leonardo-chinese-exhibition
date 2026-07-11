# v5.0 Second Exhibition URL and Path Plan

## Canonical public URL

`https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`

## Allowed public paths under `/second-exhibition/`

- `/second-exhibition/` (directory)
- `/second-exhibition/index.html` (file)
- `/second-exhibition/style.css`
- `/second-exhibition/script.js`
- `/second-exhibition/assets/images/<one of 6 expected files>`

The 6 expected image files are listed in `second-exhibition/assets/asset-checksums.sha256` and the asset-import manifest.

## Forbidden public paths

All of the following must return HTTP 404 on Pages:

- `/second-exhibition/data/`
- `/second-exhibition/data/*.json`
- `/second-exhibition/docs/`
- `/second-exhibition/docs/*.md`
- `/second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`
- `/second-exhibition/docs/RIGHTS_AND_SOURCES.md`
- `/second-exhibition/docs/VISITOR_GUIDE_ZH.md`
- `/second-exhibition/docs/CURATORIAL_ESSAY_ZH.md`
- `/second-exhibition/docs/DEEP_RESEARCH_NOTES_ZH.md`
- `/second-exhibition/docs/BUILD_ASSET_USAGE.md`
- `/second-exhibition/assets/asset-import-manifest.json`
- `/second-exhibition/assets/asset-checksums.sha256`
- Any path starting with `/second-exhibition/_` (none should exist)
- Any path starting with `/_template/`, `/_pilots/`, `/posts/`, `/case-study/`, `/release-assets/`, `/docs/`, `/reports/`

## Base URL, relative links, fragments

- The published second exhibition uses **path-relative** references only.
- All asset URLs are relative to the page (`./assets/images/...`) after staging path rewrite.
- Fragment-only anchors (e.g., `href="#section-2-classification"`) work because they resolve within the same document.
- Source-note links point to external institution URLs and open via user click only (they do not pre-fetch and do not generate background network requests).
- The page does not include any `<base href>`.

## Trailing slash behavior

- `/second-exhibition/` and `/second-exhibition/index.html` must serve the same byte content.
- The staging artifact places `index.html` directly under `second-exhibition/` so directory resolution works.
- Both URLs must return HTTP 200 with identical content.

## Direct file access

- `/second-exhibition/style.css` and `/second-exhibition/script.js` are served directly. They are referenced by `index.html`.
- The page does not include any inline source-map files.

## 404 behavior

- A request to a non-allowed path under `/second-exhibition/` returns HTTP 404 (Pages default).
- The page does not implement a custom 404 handler.
- The repository's existing 404 page (`site/404.html`, if present) is for the top-level site and is **not** reused under `/second-exhibition/`.

## MIME types

Pages serves all staging files with appropriate MIME types based on file extension. No additional configuration is needed.

## Cache behavior

- HTML: `Cache-Control: max-age=0, must-revalidate` (Pages default for served files).
- CSS / JS / images: `Cache-Control` follows Pages defaults.
- If a future round needs a content-hash in filenames for cache-busting, that is a separate decision and a separate round.

## External network requests

- The page contains **zero** automatic external requests at load time.
- No CDN fonts, no third-party JavaScript, no third-party analytics, no third-party image hosts.
- Source-note links open only via user click.

## Browser refresh / deep linking

- Page reload on any second-exhibition URL produces a fresh GET to Pages; no SPA routing.
- Hash anchors (`#section-1-observation`, `#section-2-classification`, ...) work because the page is plain HTML.

## Backward compatibility with existing top-level site

- The top-level URL `https://conanxin.github.io/leonardo-chinese-exhibition/` remains reachable.
- Live byte size stays at 92,976 B.
- Top-level assets, scripts, and styles are unchanged.
- No new top-level URL or redirect is added.

## Path rewrite summary

The only path rewrite is on the staging copy of `second-exhibition/index.html`:

- `../assets/images/` → `./assets/images/`

This rewrite converts the local serving contract (`../assets/images/` from `/site/`) into the deployed serving contract (`./assets/images/` from `/second-exhibition/`).

The tracked `second-exhibition/site/index.html` is **not** modified. The rewrite happens only in the staging tree.

## Path collision risk

- No collision risk between `/second-exhibition/` and any existing top-level path.
- The existing top-level site has no `/second-exhibition` route, and no other workflow or static file claims that path.