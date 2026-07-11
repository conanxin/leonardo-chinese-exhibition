# Second Exhibition Staging Artifact Build — v5.1

**Round:** v5.1-staging-artifact-build
**Date:** 2026-07-11
**STATUS:** **PASS** — staging-only, not deployed

---

## Baseline

| Item | Value |
|------|-------|
| Baseline commit | `5218b43809fa4ab7a78545797e057d72b51e1826` |
| HEAD / origin/main | `5218b43809fa4ab7a78545797e057d72b51e1826` (matches) |
| Source tag | `v4.8-real-second-exhibition-repository-hardening` |
| Source tag object | `1c868b054424c348f273be4148a6a3f184e374ba` (annotated) |
| Source tag target | `a70c8430a8e3d01153153e54f055d9907340d6b7` |
| Existing live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Existing live byte | **92,976 B** (unchanged) |
| Existing v2.9 marker | **1** (unchanged) |
| Second-exhibition Pages paths | all **404** (unchanged) |
| Tags / Releases | unchanged (no new tag, no new Release) |

---

## Quality gates

| Gate | Result |
|------|--------|
| Template quality gate | PASS 37/37 |
| Second-exhibition build gate | PASS |
| Repository QA | 161 PASS / 0 FAIL / 0 WARNINGS |
| Deployment preflight | PASS |
| Asset checksums | 6/6 PASS |
| JavaScript syntax (`script.js`) | PASS |
| JavaScript syntax (`browser_qa.mjs`) | PASS |

---

## Staging architecture

**Staging path:** `/tmp/leonardo-pages-artifact` (outside repository)
**Audit path:** `/tmp/leonardo-pages-artifact-audit` (sibling directory, also outside repo)

```
/tmp/leonardo-pages-artifact/
├── (25 main-site files, byte-identical to site/)
│   ├── index.html                     (92,976 B)
│   ├── style.css                      (42,079 B)
│   ├── script.js                      (14,594 B)
│   └── assets/                        (subtree byte-identical to site/assets/)
│       ├── README.md, og-cover.svg, favicon.svg
│       ├── diagrams/  (7 SVG files)
│       └── images/
│           ├── README.md
│           ├── codex-atlanticus/  (2 JPG)
│           ├── royal-collection/  (4 JPG)
│           └── platform/          (5 JPG)
└── second-exhibition/                 (NEW subtree, only public files)
    ├── index.html                     (24,380 B — PATH REWRITTEN)
    ├── style.css                      (8,261 B)
    ├── script.js                      (4,070 B)
    └── assets/images/                 (6 raster images, byte-identical to source)
```

```
/tmp/leonardo-pages-artifact-audit/   (sibling, NOT in artifact)
├── artifact-files.txt
├── artifact-sha256.txt
├── root-site-sha256.txt
├── second-exhibition-sha256.txt
└── build-summary.json
```

---

## Path rewrite strategy (artifact-only)

Source `second-exhibition/site/index.html` uses `../assets/images/` (relative-up
pattern from local serving). The staging artifact is a sibling subtree rooted at
`/second-exhibition/`, so the pattern is rewritten in the staged copy only:

- `../assets/images/` → `./assets/images/`
- 6 references rewritten (one per artifact card `<img>`)
- Only 6 lines differ between source and staged index.html
- Tracked source `second-exhibition/site/index.html` SHA256 unchanged after the build

Source SHA256 (verified before and after build): `0e7569e69c981ade8e1f1514c370bbe1819d5747c09f8d18c16127bcfeb7fae6`

---

## Publish allowlist (what is allowed in the artifact)

| Extension | Purpose |
|-----------|---------|
| `.html` | Page |
| `.css`  | Stylesheet |
| `.js`   | Script |
| `.webp`, `.png`, `.jpg`, `.jpeg` | Raster images |

Total second-exhibition public files: **9** (exactly matches allowlist count).

---

## Forbidden content (intentionally excluded)

The staging artifact does **not** contain:

- `.md` files
- `.json` files
- `.sha256` checksum files
- `_template/`, `_pilots/`, `reports/`, `scripts/`, `posts/`, `case-study/`
- `second-exhibition/data/`, `second-exhibition/docs/`
- `asset-import-manifest.json`, `asset-checksums.sha256`
- `SOURCE_AUDIT_MANIFEST.md`, `RIGHTS_AND_SOURCES.md`
- `.firecrawl/`
- Top-level `README.md`, `V4_ROADMAP.md`, `V5_ROADMAP.md`
- Repository metadata, hidden files, source maps

Verification: `python3 scripts/second_exhibition_staging_gate.py` sections F + G both
report **OK** for all forbidden-content checks.

---

## Staging gate result

`python3 scripts/second_exhibition_staging_gate.py`:

| Group | Result |
|-------|--------|
| A. Artifact location | OK (outside repo, no .git, no hidden metadata) |
| B. Main-site identity | OK (25/25 files byte-identical; index 92,976 B; v2.9 marker 1) |
| C. Second-exhibition public tree | OK (9 files, allowlist extensions only) |
| D. Path rewrite | OK (source 6 ../, staged 0 ../ + 6 ./; 6 diff lines; source SHA unchanged) |
| E. Asset integrity | OK (6 images, exact names, source SHA match, checksum file match) |
| F. Forbidden exposure | OK (no forbidden names/paths in second-exhibition subtree or artifact root) |
| G. Audit separation | OK (audit dir exists, files present, counts match, build-summary valid JSON, cross-checks pass) |
| H. Deployment status | OK (staged page carries repository-only / not deployed text) |

**Gate exit: 0 (PASS)**

---

## HTTP QA result

`python3 -m http.server 8771 --directory /tmp/leonardo-pages-artifact`:

| URL | Expected | Actual |
|-----|----------|--------|
| `http://127.0.0.1:8771/` | 200, 92,976 B, v2.9 marker 1 | 200, 92,976 B, v2.9 marker 1 |
| `http://127.0.0.1:8771/second-exhibition/` | 200, title present | 200, title `植物图谱与视觉分类` ×2 occurrences |
| `http://127.0.0.1:8771/second-exhibition/style.css` | 200 | 200, 8,261 B |
| `http://127.0.0.1:8771/second-exhibition/script.js` | 200 | 200, 4,070 B |
| `http://127.0.0.1:8771/second-exhibition/assets/images/*.webp` (×2) | 200 | 200 (306,126 B; 262,498 B) |
| `http://127.0.0.1:8771/second-exhibition/assets/images/*.png` | 200 | 200 (3,550 B) |
| `http://127.0.0.1:8771/second-exhibition/assets/images/*.jpg` (×3) | 200 | 200 (95,001 B; 294,445 B; 191,606 B) |
| `http://127.0.0.1:8771/second-exhibition/data/` | 404 | 404 |
| `http://127.0.0.1:8771/second-exhibition/docs/` | 404 | 404 |
| `http://127.0.0.1:8771/second-exhibition/assets/asset-import-manifest.json` | 404 | 404 |
| `http://127.0.0.1:8771/second-exhibition/assets/asset-checksums.sha256` | 404 | 404 |
| `http://127.0.0.1:8771/reports/` | 404 | 404 |
| `http://127.0.0.1:8771/scripts/` | 404 | 404 |
| `http://127.0.0.1:8771/_template/` | 404 | 404 |
| `http://127.0.0.1:8771/_pilots/` | 404 | 404 |

---

## Browser QA result

`SECOND_EXHIBITION_QA_URL=http://127.0.0.1:8771/second-exhibition/ node scripts/second_exhibition_browser_qa.mjs`

**Final status: PASS, 5/5 viewports**

| Counter | Value |
|---------|------:|
| Console errors | 0 |
| Page errors | 0 |
| Failed requests | 0 |
| External requests | 0 |
| Horizontal overflow | 0 |
| Images loaded per viewport | 6 / 6 |

Full per-viewport and interaction details in
`docs/SECOND_EXHIBITION_STAGING_BROWSER_QA_v5.1.md`.

---

## Production state after v5.1

| Check | Status |
|-------|--------|
| GitHub Pages workflow modified? | **No** — still `path: site` only |
| Existing live byte | **92,976 B** (unchanged) |
| Existing v2.9 marker | **1** (unchanged) |
| Second-exhibition Pages paths | **all 404** (unchanged) |
| Tags / Releases | **unchanged** (no new tag, no new Release) |
| Repository contains staging artifact? | **No** (artifact lives in `/tmp` only) |
| Repository contains audit files? | **No** (audit lives in `/tmp` only) |
| Protected paths modified? | **No** (all `git diff -- <protected-path>` = 0 lines) |

---

## Next task

**v5.2-deployment-dry-run** — exercise the Pages workflow change in dry-run mode,
inspect artifact contents, do not publish to production.