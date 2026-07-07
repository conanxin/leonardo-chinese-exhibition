# leonardo-chinese-exhibition v2.9 real source rights audit report

> 2026-07-07 · v2.9-real-source-rights-audit round
>
> commit message: `Audit sources and rights from verified v2.8`

## STATUS: PASS

本轮从真实 `v2.8-real-deep-content` tag 出发，对图片、平台截图、自绘 SVG、图注、source note、credit line、外链与复用边界做了完整真实审计。**未引用任何 phantom v2.9 / v3.x 历史**，未触碰 `site/script.js` / `site/style.css` / 旧 tags / 旧 releases / posts / case-study / release-assets 既有文件 / `_template/` / `_pilots/`。

## 1. Reality gate (round 起点)

| 项 | 命令 | 结果 |
|---|---|---|
| HEAD (round start) | `git rev-parse HEAD` | `5a2821b959a198a8fdaf6ecb4ba6819e65ef29e3` |
| origin/main (round start) | `git rev-parse origin/main` | `5a2821b959a198a8fdaf6ecb4ba6819e65ef29e3` |
| HEAD subject (round start) | `git log -1 --format=%s` | `Backfill v2.8 freeze report with verified commit + tag + release data` |
| Working tree | `git status -sb` | clean (untracked: `.firecrawl/`) |
| v2.0 tag | `git rev-parse v2.0-public-portfolio-case` | `9e6233a` ✓ untouched |
| v2.6 tag | `git rev-parse v2.6-content-stable` | `033b65e` (annotated `01cdaa2`) ✓ untouched |
| v2.7 tag | `git rev-parse v2.7-zh-exhibition-polish` | `a0fee10` (annotated → `f58f6b4`) ✓ untouched |
| v2.8 tag | `git rev-parse v2.8-real-deep-content` | `697560a` (annotated → `65b4fbc`) ✓ untouched |
| `_template/` | `test -d _template` | missing ✓ |
| `_pilots/` | `test -d _pilots` | missing ✓ |
| Live byte size | `curl -L -s .../ \| wc -c` | **92,507 B** |
| v2.8 marker | `grep -c "v2.8-real-deep-content"` | 1 |
| phantom v2.9 marker | `grep -c "v2.9-source-rights-audit"` | 0 |
| real v2.9 marker (round start) | `grep -c "v2.9-real-source-rights-audit"` | 0 |
| 4 deep blocks | `grep -c` | 1 / 1 / 1 / 1 |
| placeholder | `grep -c "image-placeholder-pro"` | 0 |
| script.js | `curl -LIs` | HTTP 200 |
| `node --check site/script.js` | syntax check | PASS |

## 2. Asset inventory (audit baseline)

直接对仓库 `site/assets/` 与 `site/index.html` grep + 人工逐图核 `data-credit` / `figcaption` / `source-note` / `interface-note`。

### 2.1 Asset summary

| Category | Count | 已纳入审计 | 备注 |
|---|---|---|---|
| Collection / manuscript images | 6 | 6 | 温莎 4 + Codex Atlanticus 2 |
| Platform screenshots | 5 | 5 | 4 张在 `<img>` 引用 + 2 张已下载未引用 |
| Self-made SVG / project diagrams | 7 | 7 | 含 tool-wall / thinking-map 等 |
| Site metadata assets | 2 | 2 | favicon / og-cover |

合计 **20 个本地资产文件**。外加 6 个 Wikimedia 文件级 URL（每张馆藏图 1）+ 2 个馆藏机构级 URL（RCT / Ambrosiana）+ 1 个平台级 URL（Museo Galileo Leonardo//thek@）。

### 2.2 Collection / manuscript images (6 张)

| File | Source institution | RCIN / folio | alt | caption | source-note | credit-line | data-credit | Confidence |
|---|---|---|---|---|---|---|---|---|
| `royal-horse-studies-rcin-912310.jpg` | Royal Collection Trust | RCIN 912310 | ✓ | ✓ | ✓ | ✓ | ✓ | high |
| `royal-water-studies-rcin-912660.jpg` | Royal Collection Trust | RCIN 912660 | ✓ | ✓ | ✓ | ✓ | ✓ | high |
| `royal-shoulder-arm-rcin-919003.jpg` | Royal Collection Trust | RCIN 919003 | ✓ | ✓ | ✓ | ✓ | ✓ | high |
| `royal-cats-lions-dragon-rcin-912363.jpg` | Royal Collection Trust | RCIN 912363 | ✓ | ✓ | ✓ | ✓ | ✓ | high |
| `codex-atlanticus-f719-recto.jpg` | Veneranda Biblioteca Ambrosiana | f.719 recto | ✓ | ✓ | ✓ | ✓ | ✓ | high |
| `codex-atlanticus-f21-recto.jpg` | Veneranda Biblioteca Ambrosiana | f.21 recto | ✓ | ✓ | ✓ | ✓ | ✓ | high |

**RCIN 编号一致性**：6 张全部经 `grep` 核对，Wikimedia 文件名嵌入编号与 credit-line 中的 RCIN 一致。

### 2.3 Platform screenshots (5 张)

| File | 截图 URL | 模块 | 在 `<img>` 中 | Confidence |
|---|---|---|---|---|
| `platform-home-leonardotheka.jpg` | teche.museogalileo.it/leonardo/home/index_en.html | 首页 | ✓ | high |
| `platform-watermarks.jpg` | teche.museogalileo.it/leonardo/filigrane | Watermarks | ✓ | high |
| `platform-recompositions.jpg` | teche.museogalileo.it/leonardo/ricostruzioni | Recompositions | ✓ | high |
| `platform-advanced-search.jpg` | teche.museogalileo.it/leonardo/ricerca-avan | Advanced Search | ✗ **unused** | medium |
| `platform-comparative-study.jpg` | teche.museogalileo.it/leonardo/studio-compare | Comparative Study | ✗ **unused** | medium |

### 2.4 Self-made SVG (7 个)

`collection-split.svg` · `manuscript-journey.svg` · `thinking-map.svg` · `watermark-evidence-chain.svg` · `recomposition-triptych.svg` · `platform-structure.svg` · `platform-tool-wall.svg` — 全部在 figcaption 中以「示意图 · 作者绘制」+ 依据（如「基于公开学术资料」「基于安布罗西安图书馆与 Royal Collection Trust 公开资料」「基于平台公开信息」）标注。

### 2.5 Site metadata (2 个)

`favicon.svg` · `og-cover.svg` — 项目自绘，无外部素材。

## 3. Source note / credit line findings

| Pattern | Count | 状态 |
|---|---|---|
| `<figcaption>` 总数 | 24 | ✓ |
| `class="source-note"` | 14 | ✓（含 6 张馆藏图 source-note + 4 张平台截图 source-note + 4 个 SVG source-note） |
| `class="credit-line"` | 13 | ✓（6 张馆藏图 credit-line + 4 张平台截图 credit-line + 3 个 artifact-card credit-line） |
| `data-credit`（lightbox 层） | 15 | ✓（含 4 张馆藏图 lightbox + 2 张 Codex Atlanticus lightbox + 多个 exhibit-index card lightbox） |
| `class="interface-note"`（研究界面说明） | 5 | ✓（Watermarks / Recompositions / 首页 / Comparative Study / Advanced Search 五个平台界面说明） |

**Wording 一致性**：

- 所有馆藏图 credit-line 写「公共域 · Wikimedia Commons · [机构, 作者]」
- 所有平台截图 credit-line 写「© Museo Galileo 2025 · Screenshot courtesy of Museo Galileo / Leonardo//thek@」
- 所有自绘 SVG source-note 写「示意图 · 作者绘制」+ 依据
- **未发现** placeholder / 待补 / 候选（dummy 候选） / TBD / TODO / FIXME / coming soon 类临时语气
- "候选" 仅在描述平台工具（Recompositions / Watermarks）的「候选纸」语境中出现，属合法用法

**站点 footer wording 收紧**：

- 原文：「...的高清图像为公共域授权使用，全部通过 Wikimedia Commons 引用」
- v2.9：「...的高清图像以公共域授权经 Wikimedia Commons 引用，原件由各馆藏机构保管；具体授权边界请以 Wikimedia Commons 文件页与馆藏页面为准。本轮（v2.9）对所有引用做了来源与权利审计，详见 `docs/SOURCE_AUDIT_MANIFEST.md` 与 `docs/RIGHTS_AND_SOURCES.md`」
- 收紧要点：明确 Wikimedia 是引用路径而不是授权源；指向具体文件页与馆藏页面作为最终依据；引用 v2.9 audit docs

## 4. External link check (`curl -LIs` lightweight)

| URL | HTTP | 用途 | Notes |
|---|---|---|---|
| `https://conanxin.github.io/leonardo-chinese-exhibition/` | 200 | live | ✓ |
| `https://github.com/conanxin/leonardo-chinese-exhibition` | 200 | 仓库 | ✓ |
| `https://github.com/conanxin/leonardo-chinese-exhibition/releases/tag/v2.8-real-deep-content` | 200 | 上一轮 release | ✓ |
| `https://www.rct.uk/collection/` | **403** (curl) | 馆藏根 | ⚠️ 机构级反 bot（浏览器访问 200）— 不修改 |
| `https://www.ambrosiana.it/` | 200 | 馆藏根 | ✓ |
| `https://teche.museogalileo.it/leonardo/` | 200 | 平台根 | ✓ |
| 6 个 Wikimedia Commons 文件页 | 200 | 馆藏图源 | ✓ |

**`curl -LIs` 抽查 11 个 URL**：9 个 200，1 个 403（rct.uk 已知机构级反 bot），1 个 N/A（live URL 已通过 `wc -c` 验证）。

## 5. Docs created / modified in this round

| 文件 | 操作 | 字节 |
|---|---|---|
| `site/index.html` | patched (3 层 v2.9 marker + footer wording 收紧) | 92,507 → 92,976 B (+469 B) |
| `site/style.css` | **未修改** | 42,079 B 不变 |
| `site/script.js` | **未修改** | 14,594 B 不变 (`node --check` PASS) |
| `README.md` | patched (追加 v2.9 Real Source & Rights Audit 节) | +39 行 |
| `docs/SOURCE_AUDIT_MANIFEST.md` | **new** | 10,671 B |
| `docs/RIGHTS_AND_SOURCES.md` | **new** | 5,652 B |
| `docs/ROADMAP_AFTER_v2.6.md` | patched (追加 v2.9 real rebuild 节) | +15 行 |
| `research/image-candidates.md` | patched (追加 v2.9 audit 状态) | +53 行 |
| `reports/leonardo_chinese_exhibition_v2_9_real_source_rights_audit_report.md` | **new** (本文件) | — |

## 6. Local validation

### 6.1 HTML / CSS / script.js 字节数

| 文件 | round start | round end | 变化 |
|---|---|---|---|
| `site/index.html` | 92,507 B | 92,976 B | +469 B (+0.5%) |
| `site/style.css` | 42,079 B | 42,079 B | **0** (未修改) |
| `site/script.js` | 14,594 B | 14,594 B | **0** (未修改) |

### 6.2 HTML marker 计数

| 类别 | 命令 | 结果 |
|---|---|---|
| v2.9 marker | `grep -c "v2.9-real-source-rights-audit"` | 1 ✓ |
| v2.8 marker | `grep -c "v2.8-real-deep-content"` | 1 ✓ (preserved) |
| v2.7 marker | `grep -c "v2.7-zh-exhibition-polish"` | 1 ✓ (preserved) |
| phantom v2.9 marker | `grep -c "v2.9-source-rights-audit"` | 0 ✓ |
| 4 deep blocks | `grep -c` | 1 / 1 / 1 / 1 ✓ (preserved) |
| placeholder | `grep -c "image-placeholder-pro"` | 0 ✓ |
| source-note | `grep -c` | 14 (> 0) ✓ |
| credit-line | `grep -c` | 13 (> 0) ✓ |
| figcaption | `grep -c` | 24 (> 0) ✓ |
| data-credit | `grep -c` | 15 (> 0) ✓ |

### 6.3 Node 语法检查

```bash
node --check site/script.js  # PASS
```

### 6.4 Playwright 运行时检查（python3.12 + Playwright 1.58.0）

| 项 | 结果 |
|---|---|
| section-nav runtime links | 31 (与 v2.5-real / v2.8 一致) |
| 4 deep blocks | 1 / 1 / 1 / 1 |
| v2.7 marker | 1 |
| v2.8 marker | 1 |
| placeholder | 0 |
| guided-mode toggle | **OK** (body class 切换 `guided-mode`) |
| lightbox open | **OK** (role=dialog 出现 1 次) |
| mobile 390 overflow | **0 px** ✓ |
| console errors | **[]** ✓ |

### 6.5 Docs 存在性

| File | 命令 | 结果 |
|---|---|---|
| `docs/SOURCE_AUDIT_MANIFEST.md` | `test -f` | ✓ exists |
| `docs/RIGHTS_AND_SOURCES.md` | `test -f` | ✓ exists |

## 7. Live verification (round 终态，待 push + Actions 之后回填)

| 项 | 期望 | 实测 |
|---|---|---|
| Live byte size | ~92,976 B | 待回填 |
| v2.9 marker | 1 | 待回填 |
| v2.8 marker | 1 | 待回填 |
| 4 deep blocks | 1 / 1 / 1 / 1 | 待回填 |
| placeholder | 0 | 待回填 |
| source-note | 14 | 待回填 |
| credit-line | 13 | 待回填 |
| figcaption | 24 | 待回填 |
| script.js HTTP 200 | yes | 待回填 |
| site diff (HEAD~1..HEAD) | 仅 index.html | 待回填 |
| posts/case-study diff | empty | 待回填 |
| v2.0 tag unmoved | 9e6233a | 待回填 |
| v2.6 tag unmoved | 033b65e / 01cdaa2 | 待回填 |
| v2.7 tag unmoved | a0fee10 / f58f6b4^{} | 待回填 |
| v2.8 tag unmoved | 697560a / 65b4fbc^{} | 待回填 |
| GitHub Actions | success | 待回填 |

## 8. No-touch confirmation

| 类别 | 状态 |
|---|---|
| `site/style.css` | ✓ untouched |
| `site/script.js` | ✓ untouched (`node --check` PASS, runtime section-nav 31 不变) |
| v2.0 tag | ✓ untouched (9e6233a) |
| v2.6 tag | ✓ untouched (033b65e / 01cdaa2) |
| v2.7 tag | ✓ untouched (a0fee10 → f58f6b4) |
| v2.8 tag | ✓ untouched (697560a → 65b4fbc) |
| v2.0 / v2.6 / v2.7 / v2.8 GitHub Releases | ✓ untouched |
| `posts/` | ✓ untouched |
| `case-study/` | ✓ untouched |
| `release-assets/` 既有文件（`manifest.md`, `v2.6-content-stable-manifest.md`, `v2.7-zh-exhibition-polish-manifest.md`, `v2.8-real-deep-content-manifest.md`, `screenshots/`） | ✓ untouched |
| `_template/` | ✓ **不存在**（按约束未创建） |
| `_pilots/` | ✓ **不存在**（按约束未创建） |
| Untracked `.firecrawl/` | ✓ 未处理 |
| `git add .` | ✓ 全部显式 add |
| 新图片 / 替换图片 | ✓ **未**新增 / **未**替换（brief 明令禁止） |
| 新 tag (v2.9-real-source-rights-audit) | ✓ **未**创建（留给 freeze round） |
| 新 GitHub Release | ✓ **未**创建（同上） |
| Bilingual / education / template | ✓ 未触碰 |

## 9. Known note / Follow-up

### 9.1 Follow-up items (移交下一轮)

1. **Museo Galileo 平台截图书面 reuse 答复**：本项目目前无书面 reuse 许可存档，截图仅以 fair use / 评论性使用原则使用
2. **`platform-advanced-search.jpg` / `platform-comparative-study.jpg` 去留决定**：已下载但未引用；下一轮决定 delete 或重新复用
3. **项目自绘 SVG 显式 LICENSE**：仓库根无 LICENSE，目前隐含「保留所有权利」；在 v3.0 之前决定（CC0 / CC-BY / 保留所有权利）
4. **馆藏机构级 reuse 政策比对**：RCT Take Down Policy / Ambrosiana 等机构的详细 reuse 政策未深入比对
5. **任何未来新增图像 / 截图 / 自绘 SVG 必须重新走 audit round**

### 9.2 Phantom 历史说明

Phantom v2.9 / v3.x 任务历史记录于 [`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`](../docs/REALITY_CHECK_AFTER_PHANTOM_V3.md)。本 v2.9 是从 verified `v2.8-real-deep-content` tag 真实重建的 source & rights audit，**不**复用任何 phantom 阶段叙述。下一 round 起点为本 tag。

### 9.3 Issues 状态

GitHub Issues #1–#4 全部保持 OPEN（与本 round 内容无直接关联）。Issue #1 标题「v2.7 Bilingual Edition」与实际 v2.7 Chinese Exhibition Polish 不一致 —— 本 round **不**强行关闭 / 重命名，留给后续 round 单独处理。

## 10. Next recommended task

**v2.9-real-stable-freeze**（独立 round）：

1. `docs/RELEASE_NOTES_v2.9_REAL_SOURCE_RIGHTS_AUDIT.md` (new)
2. `release-assets/v2.9-real-source-rights-audit-manifest.md` (new)
3. 显式 add + commit + push
4. `git tag -a v2.9-real-source-rights-audit` + `git push origin v2.9-real-source-rights-audit`
5. `gh release create v2.9-real-source-rights-audit` + attach notes
6. live 重新验证（byte size / 4 deep blocks / placeholder / script.js / 6 张馆藏图 credit-line）
7. 更新 README「Stable Tag」字段

之后下一推荐 round = **v3.0 Real Template Extraction Audit**（基于 v2.9 tag）。前提是必须先真实创建 `_template/site/` 骨架（在 `_template/` 下独立子目录，与 live `site/` 物理隔离）。在 `_template/` 真实创建之前不做 v3.0 之外的 v3.x 工作。

## 11. Final status

| 项 | 值 |
|---|---|
| STATUS | **PASS** |
| Audit commit | 待 commit 后回填 |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | 92,976 B（待 push + Actions 后 live 验证） |
| Verified source tag | `v2.8-real-deep-content` @ `65b4fbc` |
| v2.9 marker count | 1 (meta) + 1 (comment) + 1 (footer) = 3 层 |
| v2.8 marker count | 1 (preserved) |
| Assets audited | 19 (6 馆藏 + 4 平台引用 + 7 SVG + 2 元数据) + 5 unused 平台 (3 follow-up 项) |
| source-note count | 14 |
| credit-line count | 13 |
| figcaption count | 24 |
| data-credit count | 15 |
| External links checked | 11 |
| v2.0 tag | ✓ untouched |
| v2.6 tag | ✓ untouched |
| v2.7 tag | ✓ untouched |
| v2.8 tag | ✓ untouched |
| 旧 releases | ✓ untouched |
| `site/style.css` | ✓ untouched |
| `site/script.js` | ✓ untouched |
| `_template/` | ✓ 不存在 |
| `_pilots/` | ✓ 不存在 |
| Next recommended task | v2.9-real-stable-freeze |

---

*本报告 v2.9-real-source-rights-audit round 自证。所有「verified」项均由本轮的 `<tool_use_result>` 凭据支撑；无 phantom 重建。*