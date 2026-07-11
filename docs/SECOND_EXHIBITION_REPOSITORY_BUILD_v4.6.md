# v4.6 — Second Exhibition Repository Build

Round: **v4.6-second-exhibition-repository-build**
Round status: **PASS** — 6 件资产已导入并核验，第二展览 repository-only 网站已构建并通过本地 QA。
Baseline commit: `01923ea9689f509d3547c64339680e8c571952de`
Asset import commit: `2e4cef409d1fbca30b3356aa600c697f0fddc183` (v4.5)
Source tag: `v3.4-real-second-exhibition-hardening` → `81f5e928aefdc4dc92a4dbb5aedecbd3cd564765`

---

## Working title

《植物图谱与视觉分类：从自然史图像到知识秩序》

## Repository-only status

- 部署状态：`repository-only-not-deployed`
- live Leonardo 展览：无变化（byte size 92,976 B，v2.9 marker = 1）
- `second-exhibition/site/` 是 v4.6 新建的 repository-only 副本；它**不**与 GitHub Pages workflow 耦合（workflow 只部署 `site/`，不部署 `second-exhibition/`）
- 6 个 `https://conanxin.github.io/leonardo-chinese-exhibition/second-exhibition/...` URL 全部返回 HTTP 404
- 本轮没有 tag / GitHub Release / 旧 tag / 旧 Release 修改

## Directory structure

```
second-exhibition/
├── assets/
│   ├── asset-checksums.sha256            (v4.5；本轮未修改)
│   ├── asset-import-manifest.json        (v4.5；本轮未修改)
│   └── images/                           (v4.5 6 个图像；本轮未修改)
│       ├── bhl-318921-page-603998-c01.webp
│       ├── bhl-318921-page-603962-c03.webp
│       ├── smithsonian-nmnh-1529703.png
│       ├── met-285149.jpg
│       ├── rijksmuseum-rp-f-f80152.jpg
│       └── rijksmuseum-rp-f-f80313.jpg
├── data/                                 (v4.6 新建)
│   ├── exhibition.json
│   ├── sections.json
│   ├── glossary.json
│   └── assets.json
├── docs/
│   ├── SOURCE_AUDIT_MANIFEST.md          (v4.5；本轮未修改)
│   ├── RIGHTS_AND_SOURCES.md             (v4.5；本轮未修改)
│   ├── VISITOR_GUIDE_ZH.md               (v4.6 新建)
│   ├── CURATORIAL_ESSAY_ZH.md            (v4.6 新建)
│   ├── DEEP_RESEARCH_NOTES_ZH.md         (v4.6 新建)
│   └── BUILD_ASSET_USAGE.md              (v4.6 新建)
└── site/                                 (v4.6 新建，repository-only)
    ├── index.html
    ├── style.css
    ├── script.js
    └── README.md
```

## Six assets used

All 6 imported in v4.5 (commit `2e4cef4`); referenced in v4.6 page via `../assets/images/`:

| ID | File | Institution | Identifier | Status |
|---|---|---|---|---|
| C-01 | `bhl-318921-page-603998-c01.webp` | Biodiversity Heritage Library | BHL item 318921 / page 603998 | imported-not-deployed |
| C-03 | `bhl-318921-page-603962-c03.webp` | Biodiversity Heritage Library | BHL item 318921 / page 603962 | imported-not-deployed |
| C-06 | `smithsonian-nmnh-1529703.png` | Smithsonian NMNH Botany | US Catalog 1529703 | imported-not-deployed |
| C-08 | `met-285149.jpg` | The Metropolitan Museum of Art | Met object 285149 / accession 2003.562.3 | imported-not-deployed |
| C-09 | `rijksmuseum-rp-f-f80152.jpg` | Rijksmuseum | RP-F-F80152 | imported-not-deployed |
| C-10 | `rijksmuseum-rp-f-f80313.jpg` | Rijksmuseum | RP-F-F80313 | imported-not-deployed |

## Four sections

- **01 · 观察**：图像如何抓住植物特征（C-01）
- **02 · 分类**：图像如何服务命名与秩序（C-06、C-08）
- **03 · 复制**：书籍、版画与数字化如何改变传播（C-03、C-09、C-10）
- **04 · 再组织**：数字馆藏如何让图像重新连接（C-01、C-03、C-06、C-08、C-09、C-10）

## Page / content structure

- Hero（含 3 分钟导览提示）
- 顶部 section nav（4 节 + 术语 + 深度阅读）
- "开启导览模式"按钮（切换 guided banner）
- 4 个 section（每节含 kicker / title / body / takeaway / viewer_action / deep block）
- 6 个 artifact cards（每 card 含 image / caption / source-note / credit-line / viewing-note / artifact-meta；data-candidate-id 全部唯一）
- 12 个 glossary items
- 4 个 deep blocks（deep-reading-block / material-evidence-block / visual-thinking-block / research-model-block）
- 1 个 source-rights-entry 区块（指向 v4.5 docs）
- Footer marker + repository status
- Lightbox（点击图片 / Enter / Space 打开；ESC / 遮罩 / 关闭按钮 关闭；C-06 禁用）
- `prefers-reduced-motion` 关所有 transition / animation

## Build gate result

`python3 scripts/second_exhibition_build_gate.py` → **PASS** (exit 0)。所有 A/B/C/D/E/F 类检查通过。

## Local Playwright result

`/usr/bin/python3.12 /tmp/playwright_v46_qa.py` → **PASS**:

- title 含"植物图谱与视觉分类"
- repository status 可见
- 4 sections / 6 artifact cards / 12 glossary items / 6 source notes / 6 credit lines
- 6 imgs 全部 200 + naturalWidth > 0
- C-06 naturalWidth = 90（与 manifest 一致）
- C-06 lightbox 禁用
- C-01 / C-03 / C-08 / C-09 / C-10 lightbox 可开
- ESC 关闭 lightbox
- guided mode toggle 工作
- desktop (1280×900) 无横向溢出
- mobile (390×844) 无横向溢出
- console errors = 0
- failed requests = 0

## C-06 low-resolution handling

- `data-low-resolution="true"` + `data-lightbox-enabled="false"` 在 C-06 artifact card 上
- CSS：`.artifact-card[data-low-resolution="true"] img { max-width: 180px; width: auto; }`
- 不强制放大；image-rendering 使用浏览器默认值
- viewing-note 内显式标注"低分辨率缩略图" + "不启用 lightbox"
- 页面 / 文档未把 C-06 用作 Hero 或宽屏背景

## BHL distinct pages

- C-01 = BHL page 603998（Pistillaria plate）
- C-03 = BHL page 603962（Cycas revoluta plate）
- 同 parent item (BHL item 318921)，不同 page ID，SHA-256 不同

## C-08 rights confirmation

Double-confirmation PASS：Met Collection API `isPublicDomain=true` + 公开页面 Public Domain 指示。Credit line "Gift of Russell C. Vail, 2003" 在 v4.5 evidence 中已记录；本轮 viewing-note 显式标注 double-confirmation 来源。

## C-10 manifest caveat

- viewing-note 显式说明 Rijksmuseum IIIF Presentation API manifest `/manifest.json` 在 v4.5 阶段返回 HTTP 404
- 本轮不基于 IIIF Presentation API manifest 撰写任何陈述
- licence 依据为 Rijksmuseum 公开页面的"逐项 Copyright 字段"

## No live changes

- `site/index.html`, `site/style.css`, `site/script.js`（顶层）未修改
- `_template/site/`, `_template/data/` 未修改
- `_pilots/second-exhibition-pilot/` 未修改
- `posts/`, `case-study/`, `release-assets/` 未修改
- `scripts/template_quality_gate.py`, `scripts/second_exhibition_asset_gate.py` 未修改
- 6 个图像文件 + `asset-checksums.sha256` + `asset-import-manifest.json` + `SOURCE_AUDIT_MANIFEST.md` + `RIGHTS_AND_SOURCES.md` 未修改
- 现有 git tags (`v2.0` through `v3.4`) 与 GitHub Releases 未触动

## Future deployment requires separate round

任何把 `second-exhibition/` 部署到 GitHub Pages 的尝试都需要单独的、明确的 round。该 round 必须：

1. 重新打开 6 件资产的官方 source URL 与 rights URL 核对现状
2. 在部署前再次运行 `scripts/second_exhibition_asset_gate.py` 与 `scripts/second_exhibition_build_gate.py`
3. 修改 `.github/workflows/pages.yml` 使其部署 `second-exhibition/`（独立 round，不在本轮范围）
4. 重新核对 6 件资产的 IIIF Presentation API manifest 状态（C-10）
5. 重新核对 NMNH Botany 的高分辨率访问（如果可能）
6. 在 live 校验脚本中加入本展览的 status 字段监控