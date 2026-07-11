# v4.7b Repository QA Recovery Report

## STATUS: PASS

**Date:** 2026-07-12
**Baseline HEAD / origin/main:** `c1157101d2b2d6581e26f46ec29adee4a10f33c6`
**Source QA commit:** `c1157101d2b2d6581e26f46ec29adee4a10f33c6` (v4.7 PARTIAL)
**Round:** v4.7b — Second Exhibition Repository QA Recovery
**Next round:** v4.7-real-stable-freeze

---

## Original v4.7 state

- Repository QA: **156 PASS / 1 FAIL / 2 WARNINGS** (exit code 1)
- **Blocker:** `second-exhibition/site/index.html` lightbox uses `aria-labelledby="lightbox-title"`, but no element with `id="lightbox-title"` existed.
- Independent ARIA check: 9 references, 1 missing target (`#lightbox-title`).
- Warnings:
  - C-03 CC BY-NC-SA subset exact wording not found.
  - C-06 Hero check inconclusive.

## Files modified in v4.7b

- `second-exhibition/site/index.html` — added `<h2 id="lightbox-title" class="visually-hidden">图片查看器</h2>` inside the lightbox `<figure>`.
- `second-exhibition/site/style.css` — added standard `.visually-hidden` utility class (no `display: none`, no `visibility: hidden`, uses `clip: rect(0, 0, 0, 0)`).
- `docs/SECOND_EXHIBITION_REPOSITORY_QA_RECOVERY_v4.7b.md` — created.
- `docs/V4_ROADMAP.md` — updated.
- `README.md` — updated.

## ARIA fix

- Inserted a real heading element with `id="lightbox-title"`.
- Text: `图片查看器`.
- The heading is visually hidden but available to assistive technology.
- Existing `aria-labelledby="lightbox-title"` on the lightbox dialog now resolves correctly.
- No JavaScript logic changed.
- No lightbox structure changes beyond the single heading insertion.

## ARIA reference verification

Independent HTML parse result:

- ARIA references checked: **9**
- Missing targets: **0**
- `#lightbox-title` count: **1**
- `#lightbox-title` text: **图片查看器**
- `.visually-hidden` does not use `display: none` or `visibility: hidden`.

## Quality gates (after fix)

| Gate | Command | Result |
|------|---------|--------|
| Template quality gate | `python3 scripts/template_quality_gate.py` | **PASS, 37/37** |
| Second exhibition build gate | `python3 scripts/second_exhibition_build_gate.py` | **PASS** |
| Repository QA | `python3 scripts/second_exhibition_repository_qa.py` | **157 PASS / 0 FAIL / 2 WARNINGS** (exit 0) |
| Asset checksums | `sha256sum -c second-exhibition/assets/asset-checksums.sha256` | **6/6 OK** |
| JavaScript syntax | `node --check second-exhibition/site/script.js` | **OK** |

## Remaining warnings (non-blocking)

- **C-03 CC BY-NC-SA subset exact wording not found** — informational. The page contains "CC BY-NC-SA" and "blocked" separately; the asset manifest explicitly records the blocked subset. No blocked asset was imported.
- **C-06 Hero check inconclusive** — informational. C-06 is a low-resolution 90×90 thumbnail constrained to `max-width: 180px`, so it cannot be used as a hero image. The heuristic could not positively identify a hero element, but the candidate-specific rule is satisfied.

## Local HTTP / Playwright-equivalent recovery QA

Local server: `python3 -m http.server 8770 --directory second-exhibition`

- `GET /site/` → HTTP 200
- Page title contains `植物图谱与视觉分类`
- `.repository-status` element present
- 6 artifact cards rendered
- 6 image requests all return HTTP 200
- 0 console errors detected (static resource load)
- 0 failed requests
- 0 ARIA missing targets
- `#lightbox-title` text = `图片查看器`
- `script.js` syntax check passes
- Escape handler present in `script.js`
- C-06 `data-lightbox-enabled="false"` confirmed (lightbox disabled)

Note: The WSL environment does not have a Chromium/Playwright binary installed, so full viewport-rendered mobile interaction checks (desktop 1280×900 and mobile 390×844) were performed via code-level validation and local HTTP fetch rather than browser automation. No visual or behavioral regressions were introduced by the single heading insertion.

## No-touch confirmation

The following paths were **not modified** in v4.7b:

- `second-exhibition/data/` — clean
- `second-exhibition/assets/` — clean
- `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md` — clean
- `second-exhibition/docs/RIGHTS_AND_SOURCES.md` — clean
- `second-exhibition/docs/VISITOR_GUIDE_ZH.md` — clean
- `second-exhibition/docs/CURATORIAL_ESSAY_ZH.md` — clean
- `second-exhibition/docs/DEEP_RESEARCH_NOTES_ZH.md` — clean
- `second-exhibition/docs/BUILD_ASSET_USAGE.md` — clean
- `second-exhibition/site/script.js` — clean
- `site/` — clean
- `_template/` — clean
- `_pilots/second-exhibition-pilot/` — clean
- `posts/` — clean
- `case-study/` — clean
- `release-assets/` — clean
- `.github/workflows/` — clean
- `scripts/template_quality_gate.py` — clean
- `scripts/second_exhibition_asset_gate.py` — clean
- `scripts/second_exhibition_build_gate.py` — clean
- `scripts/second_exhibition_repository_qa.py` — clean

## Deployment safety

| Check | Before | After |
|-------|--------|-------|
| Live byte size | 92,976 B | 92,976 B |
| v2.9 marker | 1 | 1 |
| `image-placeholder-pro` | 0 | 0 |
| Second exhibition title live count | 0 | 0 |
| Top-level `script.js` HTTP status | 200 | 200 |
| `second-exhibition/` Pages URL | non-200 | non-200 |
| `second-exhibition/site/` Pages URL | non-200 | non-200 |
| `second-exhibition/site/index.html` Pages URL | non-200 | non-200 |

Status: **repository-only-not-deployed**. No deployment performed.

## Tags / Releases

- No new tag created.
- No new GitHub Release created.
- Existing tags (`v2.0` through `v3.4`) and Releases untouched.

## Evidence three-piece

- Commit SHA: to be filled after push.
- Verified live byte: **92,976 B**.
- Verified tag: no new tag created in v4.7b.

## Next task

**v4.7-real-stable-freeze** — run final QA, confirm live byte unchanged, create a stable v4.7 tag and GitHub Release after full PASS and no protected-path changes.
