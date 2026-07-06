---
title: "Portfolio case (EN) — Leonardo's Paper Universe"
project: leonardo-chinese-exhibition
version: v2.0 (English short case)
date: 2026-07-06
live_url: https://conanxin.github.io/leonardo-chinese-exhibition/
audience: International portfolio / collaborators / academic contact
---

# Leonardo's Paper Universe — A Digital Humanities Case

> An independent Chinese-language digital exhibition built on top of an Italian academic platform — fully static, GitHub Pages hosted, public-domain manuscript imagery.

---

## One-liner

**Translating Museo Galileo's Leonardo//thek@ platform into a complete 8-section Chinese-language exhibition — including 6 real public-domain manuscript images from the Royal Collection Trust and the Codex Atlanticus.**

---

## Live URL

https://conanxin.github.io/leonardo-chinese-exhibition/

---

## What's the project

In the 1580s, Italian sculptor Pompeo Leoni took Leonardo da Vinci's notebooks and **scattered thousands of pages with scissors**, rebinding them into two giant volumes — what we now call the Codex Atlanticus (Milan) and the Windsor Drawings (UK). This act of "destructive binding" shaped 500 years of how we think of Leonardo.

The Italian Museo Galileo launched **Leonardo//thek@** to digitally reverse that process. The platform is brilliant but Italian/English-only, with no continuous Chinese-language narrative.

This exhibition rebuilds it as a complete, audience-ready **8-section Chinese-language digital exhibition** — with primary sources (6 real public-domain manuscript images), editorial structure (策展前言 → 8 节 → 资料来源), and a static deployable build.

## What's the design language

The exhibition adopts an **OpenAI editorial visual system**:

- Warm-paper background `#fbfaf6`
- Dark-grey ink text `#2a2a2a`
- Antique gold accents `#9a7b3b`
- Deep-archive green for emphasis `#1f3a2e`
- Generous whitespace, section-numbered chapters
- No black-on-gold "museum poster" cliché, no soft-skin Xiaohongshu cliché

The visual system is intentionally understated: every section has a *core question*, a *figure*, and a *credit-line* — not a fragment, not a wall art piece.

## What's in the technical box

| Layer | Choice |
|---|---|
| HTML | Static HTML5, no framework |
| CSS | Plain CSS, system fonts (PingFang SC + Helvetica Neue) |
| Imagery | SVG (author-original diagrams) + JPEG (Wikimedia Commons public-domain) |
| Deploy | GitHub Pages + Actions (upload-pages-artifact@v3 + deploy-pages@v4) |
| External dependencies | 0 JS · 0 external CSS · 0 raster bitmaps |
| Total page weight | ~3.6 MB (page + CSS + 9 SVG + 6 JPG) |

> Zero third-party runtime dependencies. The exhibition is reproducible from a single `git clone`.

## What's the content architecture

1. Hero (`manuscript-journey.svg` + dual-column intro)
2. Curatorial prologue (curatorial-statement blockquote)
3. **Exhibit Index** — 8 cards (A–H), giving an "exhibition feel" on first sight
4. Exhibition map (10 navigation tiles)
5–13. Intro + 8 sections, each a `content + figure + meta-cards + viewing-guide` quartet
14. Sources / further reading
15. Footer (version meta + attribution + real-image copyright notes)

Each section carries:

- A **core question** — what is this section really about
- A **250–500 word narrative** — Chinese-language scholarly translation
- A **figure / gallery** — SVG diagram, real JPG, or curated "exhibit-card"
- An **exhibit-card grid** (where appropriate) — with RCIN / folio / year / credit-line
- A **viewing guide** — how to read this section
- A **source note** — where the visual came from

## What's in version control

12 versioned phases from v0.2 to v1.9, with three layered markers (`v1.5b-live-hotfix`, `v1.7-exhibit-image-upgrade`, `v1.8-real-image-integration`) surviving in the deployed HTML — verifiable via `curl + grep` at any time.

## What's the public-good angle

- Uses Wikimedia Commons public-domain images
- Cites Royal Collection Trust, Codex Atlanticus, Leonardo//thek@ platform
- Repo is open-source (https://github.com/conanxin/leonardo-chinese-exhibition)
- Can be forked and translated

## What the keywords are

`digital humanities` · `Chinese localization` · `exhibition design` · `editorial visual system` · `static site` · `GitHub Pages` · `public-domain manuscripts` · `Leonardo da Vinci` · `Codex Atlanticus`

---

## Contact

- Repo: https://github.com/conanxin/leonardo-chinese-exhibition
- Live: https://conanxin.github.io/leonardo-chinese-exhibition/
- Issues: https://github.com/conanxin/leonardo-chinese-exhibition/issues

Last updated: 2026-07-06
