# Release Asset Manifest — v2.0 (leonardo-chinese-exhibition)

> Generated 2026-07-06 for tag `v2.0-public-portfolio-case` (commit `9e6233a`).
> All assets produced by Playwright + Chrome-for-Testing from the **live** URL
> `https://conanxin.github.io/leonardo-chinese-exhibition/`.

## Screenshots (release-assets/screenshots/)

All 6 screenshots were generated **from the live URL** using the locally-installed
Playwright + Chrome-for-Testing 149 stack. Each shot is anchored to a real page
section (`#hash`) so it lands at the right spot; viewport sizes match the spec.

| File | Section target | Viewport | Bytes | Real? |
|---|---|---|---|---|
| `desktop-hero.png` | Root / hero (`<header>`) | 1440×900 | 131,788 | ✓ |
| `desktop-exhibit-index.png` | `#exhibit-index` (「本展展品索引」) | 1440×900 | 77,883 | ✓ |
| `desktop-real-image-gallery.png` | `#section2` (《大西洋手稿》) | 1440×900 | 165,566 | ✓ |
| `desktop-platform-tools.png` | `#section7` (Leonardo//thek@ 如何工作) | 1440×900 | 140,233 | ✓ |
| `mobile-hero.png` | Root / hero (390-wide) | 390×844 | 87,548 | ✓ |
| `mobile-section.png` | `#section2` mobile view | 390×844 | 108,906 | ✓ |

**Total**: 6 files, ~712 KB combined.

### Suggested usage

| Destination | Files to attach |
|---|---|
| **GitHub Release hero** (top of release page) | `desktop-hero.png` |
| **GitHub Release body** (inline gallery) | all 4 desktop shots in order |
| **README.md** (visual hero at top) | `desktop-hero.png` |
| **X / Twitter post** | `desktop-hero.png` (or 1×1 mobile crop) |
| **LinkedIn / 个人作品集** | `desktop-real-image-gallery.png` + `desktop-platform-tools.png` |
| **小红书图文** | `mobile-section.png` (vertical frame) |
| **Case study** (`case-study/portfolio-case-study.md`) | `desktop-real-image-gallery.png` |
| **One-pager** (`case-study/project-onepager.md`) | `desktop-hero.png` as inline cover |

### Re-capture

```bash
# inside /tmp/pwtool with the venv
source .venv/bin/activate
python3 capture6.py    # ~30s, overwrites the 6 PNGs
```

(Browser binary lives at
`/home/conanxin/.cache/ms-playwright/chromium-1228/chrome-linux64/chrome`.)

## Other release artifacts (not generated here)

| Wanted | Where it lives | Notes |
|---|---|---|
| OG cover image | `site/assets/og-cover.svg` | Already shipped with v1.8 |
| Favicon | `site/assets/favicon.svg` | Already shipped with v1.8 |
| Real-image hero | `site/assets/codex-atlanticus-*.jpg` (6 files) | Already shipped with v1.7/v1.8 |
| SVG diagrams | `site/assets/*.svg` (9 files) | Already shipped with v2.0 |

## What is NOT in this v2.1 kit (deferred)

- **Video walkthrough** (45–60s screencast) → planned for v2.2
- **iPad / tablet 768-wide** viewport → not requested
- **Translated captions** (English legend burn-in) → case-study already has
  English version separately, captions stay Chinese-only on screenshots by design
- **PDF export of all 6 screenshots** → not requested; PNGs only is the
  cross-platform norm
