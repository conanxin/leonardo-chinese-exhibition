# v5.5 Production Health Baseline

This document freezes the production identity of the second exhibition as
verified after the v5.0-stable-freeze cycle. It is the canonical reference
for the health-check script `scripts/second_exhibition_production_healthcheck.py`
and for any future regression investigation.

## Release identity

| Field | Value |
|---|---|
| Stable tag | `v5.0-real-second-exhibition-deployment` |
| Tag object SHA | `c8871f09e4003675d5796c76058d589a08541f45` (annotated, `type=tag`) |
| Tag target commit | `ac0f19e2c03b09738ae49b4a15c629a1f2177068` |
| Current main HEAD | allowed to advance past the tag target; do **not** move the tag |
| GitHub Release | https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v5.0-real-second-exhibition-deployment |
| Release publishedAt | `2026-07-12T00:29:43Z` |
| Release status | published, not draft, not prerelease |
| Author | `conanxin` |

## Root baseline

- URL: `https://conanxin.github.io/leonardo-chinese-exhibition/`
- HTTP: `200`
- Byte size: `92,976`
- SHA-256: `e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc`
- Exact marker command:
  `grep -o 'v2.9-real-source-rights-audit' <root.html> | wc -l`
- Exact marker count: **1**
- Loose marker command: `grep -o 'v2.9' <root.html> | wc -l`
- Loose marker count: **4** (informational only — does not block the check)
- Live / source identity: live `https://conanxin.github.io/leonardo-chinese-exhibition/`
  is byte-identical to `site/index.html` in the repository at the freeze tag.

## Second exhibition baseline

- URL: `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/`
- HTTP: `200`
- Byte size: `25,635`
- SHA-256: `7c05f39d4d9a49d0ba09d8202ff7ee41e42d67445660510815fb2887cc16324c`
- Title fragment: `植物图谱与视觉分类`

Status phrase counts (live HTML):

| Phrase | Live count |
|---|---|
| `production-deployed-v5.3` | 5 |
| `published-in-v5.3` | 8 |
| `imported-not-deployed` | 8 (historical import record only) |
| `repository-only-not-deployed` | 0 |

Sections: 4
Artifact cards: 6 (C-01 through C-06; C-06 lightbox disabled with low-resolution warning)
Glossary items: 12
Public images: 6

## Public inventory

| Inventory | Count |
|---|---|
| Root public files | 25 |
| Second-exhibition public files | 9 |
| Total public files | 34 |
| Public raster images | 6 |

The 9 second-exhibition public files:
- `index.html`
- `style.css`
- `script.js`
- `assets/images/bhl-318921-page-603998-c01.webp`
- `assets/images/bhl-318921-page-603962-c03.webp`
- `assets/images/smithsonian-nmnh-1529703.png`
- `assets/images/met-285149.jpg`
- `assets/images/rijksmuseum-rp-f-f80152.jpg`
- `assets/images/rijksmuseum-rp-f-f80313.jpg`

## Integrity

Six image SHA-256 values (live ≡ source ≡ staging for all six):

```
10762705aad12906d5d13d4af9afa0e40c6dcceb54708f55eefc361fe74990ba  rijksmuseum-rp-f-f80313.jpg
446d744d9b647f299532fc248e3263f14db818dff591f2c99264beb18c7d881d  bhl-318921-page-603962-c03.webp
75f523b06cc1a62713de51b1ba3a51fc4d43c4ac19268c48478d30c9e2af73a1  smithsonian-nmnh-1529703.png
976b1cbd365a7ddeef961e1b865ba537e5f898487b8984b49eb9cfac33dc47bf  met-285149.jpg
d3832eb3e667065892528f014affab34c2b0c2db632b8e56683826cc3c089502  rijksmuseum-rp-f-f80152.jpg
dc4b292536761be5bdf8a459d5ef82c53c4ecf5e39252ab68d19c233293522b7  bhl-318921-page-603998-c01.webp
```

Notes:
- Live root SHA equals the SHA of `site/index.html` (the root is a static
  file, no staging rewrite).
- Live second-exhibition SHA equals `staging-artifact/second-exhibition/index.html`
  produced by `scripts/second_exhibition_staging_build.py`, NOT
  `second-exhibition/site/index.html`. The staging builder rewrites
  `./assets/images/` → `../assets/images/` so that paths resolve correctly
  under the `/second-exhibition/` URL prefix.

### Canonical computation command

To reproduce the root values above, run:

```bash
ROOT_URL="https://conanxin.github.io/leonardo-chinese-exhibition/"
curl -L --fail --silent --show-error \
  -H 'Accept-Encoding: identity' \
  --connect-timeout 20 --max-time 120 \
  "$ROOT_URL" \
  -o /tmp/root.html
sha256sum /tmp/root.html          # → e2be1077fa7e601d50e300f7c98ddc19f802b1c38260c5e18e4763c2a1963afc
wc -c /tmp/root.html              # → 92976
grep -o 'v2.9-real-source-rights-audit' /tmp/root.html | wc -l   # → 1
grep -o 'v2.9' /tmp/root.html | wc -l                            # → 4 (informational)
cmp -s site/index.html /tmp/root.html; echo $?    # → 0 (byte-identical to source)
```

The five-source binary comparison is documented in
[`docs/PRODUCTION_HASH_BASELINE_RECONCILIATION_v5.5a.md`](PRODUCTION_HASH_BASELINE_RECONCILIATION_v5.5a.md).
**The hash `e2be1077…` is the canonical root SHA-256.** A different
hash (`f31ddcba…`) was misattributed to `site/index.html` in the v5.0
release manifest; that attribution is the only `f31ddcba…` occurrence
in the repo and is preserved unmodified for history. The
reconciliation document explains the source of the misattribution and
recommends the procedure above as the canonical future baseline.

### Erratum (v5.5a)

A separate hash `f31ddcba5168c8f8fba81498cfd5e259de73452da69eb28a1db4913dffd16fda`
appeared in `release-assets/v5.0-real-second-exhibition-deployment-manifest.md`
line 61 as "Source `site/index.html` SHA-256". That value is the SHA
of `second-exhibition/site/index.html`, **not** `site/index.html`.
The canonical root SHA is `e2be1077…` above; see the reconciliation
document for the full explanation and procedure. **No production
content has drifted.**

Gates at freeze:

| Gate | Result |
|---|---|
| `template_quality_gate.py` | 37 / 37 PASS |
| `second_exhibition_build_gate.py` | PASS |
| `second_exhibition_repository_qa.py` | 164 / 164 PASS |
| `sha256sum -c asset-checksums.sha256` | 6 / 6 OK |
| `node --check second-exhibition/site/script.js` | clean |

## Security boundary

The following paths must return **404** (or 403) at the public root. Forbidden
exposure boundary test list:

- `README.md`
- `V4_ROADMAP.md`
- `V5_ROADMAP.md`
- `scripts/`
- `_template/`
- `_pilots/`
- `reports/`
- `release-assets/`
- `.github/`
- `.firecrawl/`
- `second-exhibition/data/`
- `second-exhibition/docs/`
- `second-exhibition/assets/asset-import-manifest.json`
- `second-exhibition/assets/asset-checksums.sha256`
- `second-exhibition/README.md`
- `second-exhibition/site/README.md`
- `no-such-public-path-please-404/`

Workflow safety:
- `pages.yml` builds staging artifact, runs staging gate, then uploads only
  `runner.temp/leonardo-pages-artifact` to Pages.
- Audit directory and repository root are **not** uploaded.

## Known historical semantics

These phrases appear in the live HTML by design and **must not be removed
mechanically**:

| Phrase | Meaning |
|---|---|
| `production-deployed-v5.3` | Current publication status of the second exhibition. |
| `published-in-v5.3` | Current publication status of the six assets. |
| `imported-not-deployed` | The six assets were *historically imported* under v4.5 (see `second-exhibition/assets/asset-import-manifest.json`). Live occurrences appear only: (a) inside the per-source-note `Import record:` blocks, (b) adjacent to `(v4.5)` and `asset-import-manifest`, as documented in the v5.0 freeze. |
| `repository-only-not-deployed` | Should not appear on the live page; reserved for future "imported into repo but not yet published" entries. |
| `未部署` / `not deployed` / `stale` | Substring checks are informational; the authoritative counts are the four phrase-count rows above. |

The freeze commit intentionally **preserves** the historical import record
on the live page to keep provenance visible to readers. Future content
iterations must keep treating these phrases as part of the historical
record rather than as live status.
