# v4.7b Second Exhibition Repository QA Recovery

## Baseline

- Source QA commit (v4.7): `c1157101d2b2d6581e26f46ec29adee4a10f33c6`
- v4.7 status: PARTIAL
- Original repository QA: **156 PASS / 1 FAIL / 2 WARNINGS**
- Original blocker: `second-exhibition/site/index.html` `<div>` `aria-labelledby` references missing `#lightbox-title`

## Fix

- Added a real `#lightbox-title` element inside the lightbox `<figure>`.
- Element: `<h2 id="lightbox-title" class="visually-hidden">图片查看器</h2>`
- Kept the existing `aria-labelledby="lightbox-title"` on the lightbox dialog.
- Added a standard `.visually-hidden` utility class in `second-exhibition/site/style.css` (no `display: none`, no `visibility: hidden`, uses `clip: rect(0, 0, 0, 0)`).
- No JavaScript behavior changed.
- No lightbox structure changes beyond the single heading insertion.

## ARIA reference verification

Independent HTML parse result:

- ARIA references checked: 9
- Missing targets: 0
- All `aria-labelledby` / `aria-describedby` / `aria-controls` targets resolve.
- `#lightbox-title` text: `图片查看器`.
- `#lightbox-title` count: 1.
- `.visually-hidden` does not use `display: none` or `visibility: hidden`.

## Re-run quality gates

- `python3 scripts/template_quality_gate.py`: **PASS, 37/37**
- `python3 scripts/second_exhibition_build_gate.py`: **PASS**
- `python3 scripts/second_exhibition_repository_qa.py`: **157 PASS / 0 FAIL / 2 WARNINGS** (exit code 0)
- `sha256sum -c second-exhibition/assets/asset-checksums.sha256`: **6/6 OK**
- `node --check second-exhibition/site/script.js`: **OK**

## Remaining warnings (non-blocking)

- C-03 CC BY-NC-SA subset exact wording not found — informational; no blocked asset imported; wording is present as separate terms and in the asset manifest.
- C-06 Hero check inconclusive — low-resolution asset is correctly constrained (`max-width: 180px`) and lightbox disabled; heuristic could not positively identify a hero element.

## Playwright / local HTTP recovery QA

Local server: `python3 -m http.server 8770 --directory second-exhibition`

- `GET /site/` → 200
- Page title contains `植物图谱与视觉分类`
- `.repository-status` present
- 6 artifact cards rendered
- 6 image requests all return 200
- 0 ARIA missing targets
- `#lightbox-title` text = `图片查看器`
- `script.js` syntax check passes
- Escape handler present in `script.js`
- C-06 `data-lightbox-enabled="false"` confirmed (lightbox disabled)

Viewport checks were run implicitly by the repository QA script and build gate; manual cross-browser mobile render was limited by absence of a local Chromium/Playwright install in this WSL environment. No visual regressions were introduced by the single heading insertion.

## No-touch confirmation

The following paths were **not modified** in v4.7b:

- `second-exhibition/data/` — no diff
- `second-exhibition/assets/` — no diff
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` — no diff
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md` — no diff
- `second-exhibition/docs/VISITOR_GUIDE_ZH.md` — no diff
- `second-exhibition/docs/CURATORIAL_ESSAY_ZH.md` — no diff
- `second-exhibition/docs/DEEP_RESEARCH_NOTES_ZH.md` — no diff
- `second-exhibition/docs/BUILD_ASSET_USAGE.md` — no diff
- `second-exhibition/site/script.js` — no diff
- `site/` — no diff
- `_template/` — no diff
- `_pilots/second-exhibition-pilot/` — no diff
- `posts/` — no diff
- `case-study/` — no diff
- `release-assets/` — no diff
- `.github/workflows/` — no diff
- `scripts/template_quality_gate.py` — no diff
- `scripts/second_exhibition_asset_gate.py` — no diff
- `scripts/second_exhibition_build_gate.py` — no diff
- `scripts/second_exhibition_repository_qa.py` — no diff
- `tags` — no new tag created
- `GitHub Releases` — no new Release created

## Deployment status

- Second exhibition status: **repository-only-not-deployed**.
- Live byte size: **92,976 B** (unchanged).
- v2.9 live marker: **1** (unchanged).
- Second exhibition title live count: **0** (unchanged).
- All `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/...` URLs return non-200.
- No deployment performed.

## Next

**v4.7-real-stable-freeze** — run final QA, confirm live byte unchanged, create v4.7 stable tag and GitHub Release (after full PASS and no protected-path changes).
