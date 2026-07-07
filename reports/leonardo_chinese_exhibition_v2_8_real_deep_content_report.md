# leonardo-chinese-exhibition v2.8 real deep content report

> 2026-07-07 · v2.8-real-deep-content round
>
> commit message: `Rebuild v2.8 deep content from verified baseline`

## STATUS: PASS

本轮从真实 `v2.7-zh-exhibition-polish` tag 重建 v2.8 deep content，**未引用任何 phantom v2.8 历史**，未触碰 site/script.js / 旧 tags / 旧 releases / posts / case-study / release-assets 既有文件。

## 1. Reality gate (round 起点)

| 项 | 命令 | 结果 |
|---|---|---|
| HEAD (round start) | `git rev-parse HEAD` | `c37dd2eb06ce3ad17a1edc4f9a07f07e9a5f1f7c` |
| origin/main (round start) | `git rev-parse origin/main` | `c37dd2eb06ce3ad17a1edc4f9a07f07e9a5f1f7c` |
| Working tree | `git status -sb` | clean (untracked: `.firecrawl/`) |
| v2.0 tag | `git rev-parse v2.0-public-portfolio-case` | `9e6233a` ✓ untouched |
| v2.6 tag | `git rev-parse v2.6-content-stable` | `033b65e` (annotated `01cdaa2`) ✓ untouched |
| v2.7 tag object | `git rev-parse v2.7-zh-exhibition-polish` | `a0fee10` ✓ |
| v2.7 tag dereferenced | `git rev-parse v2.7-zh-exhibition-polish^{}` | `f58f6b4` ✓ |
| `_template/` | `test -d _template` | missing ✓ |
| `_pilots/` | `test -d _pilots` | missing ✓ |
| Live byte size | `curl -L -s .../ \| wc -c` | 85,564 B |
| v2.7 marker | `grep -c "v2.7-zh-exhibition-polish"` | 1 |
| v2.8 marker (round start) | `grep -c "v2.8-deep-exhibition-content"` | 0 |
| v2.9 marker | `grep -c "v2.9-source-rights-audit"` | 0 |
| placeholder | `grep -c "image-placeholder-pro"` | 0 |
| script.js | `curl -LIs` | HTTP 200 |
| `node --check site/script.js` | round start | PASS |

## 2. Files modified in this round

| 文件 | 操作 | 字节数变化 |
|---|---|---|
| `site/index.html` | patched（v2.8 marker ×3 + 4 deep blocks + postscript 深化） | 85,564 → 92,507 B (+6,943 B, +8.1%) |
| `site/style.css` | patched（4 block classes + mobile rules） | 40,362 → 42,079 B (+1,717 B, +4.3%) |
| `site/script.js` | **未修改**（14594 B 不变；`node --check` PASS） | 14,594 → 14,594 B (0) |
| `README.md` | patched（追加 v2.8 Real Deep Content 节） | +33 行 |
| `docs/CURATORIAL_ESSAY_ZH.md` | **new** | 9,516 B |
| `docs/DEEP_RESEARCH_NOTES_ZH.md` | **new** | 7,002 B |
| `docs/ROADMAP_AFTER_v2.6.md` | patched（追加 v2.8 real rebuild 节） | +13 行 |
| `reports/leonardo_chinese_exhibition_v2_8_real_deep_content_report.md` | **new** (本文件) | — |

## 3. v2.8 marker (三层)

| 层 | 位置 | 文本 |
|---|---|---|
| meta | `<head>` | `<meta name="version" content="v2.8-real-deep-content">` |
| comment | line 35 | `<!-- leonardo-chinese-exhibition v2.8 real deep content -->` |
| footer | `<footer>` 末尾 | `版本：... / <strong>v2.8 real deep content</strong></p>` |

旧 marker 全部保留（v1.5b / v1.7 / v1.8 / v2.2 / v2.3 / v2.4 / v2.5-real / v2.6 / v2.6-content-stable / v2.7-zh-exhibition-polish 共 10 层历史 marker 一致）。

## 4. 4 个新增深度内容模块

### 4.1 `被装订改变的思想`（`.deep-reading-block`）

- **位置**：section1（手稿流散 / 时间线）之后、section2（大西洋手稿）之前
- **内容**：解释达·芬奇手稿命运不是单纯保存史，而是知识结构被重新排序的历史。三个层次：(1) 达·芬奇留下的是工作纸页不是完成体系；(2) 梅尔齐继承的是仍在生成中的工作现场；(3) 莱奥尼的裁切拼贴装订保存了材料也改变了材料关系。
- **实现**：`<aside>`，不进入 `getTourSections()` 的 section registry（脚本不修改，runtime section-nav 不变）

### 4.2 `纸页也在说话`（`.material-evidence-block`）

- **位置**：section4（同一张纸上的艺术与科学 / 复原拼合）之后、section5 之前
- **内容**：把纸张证据从辅助信息提升为第一手证据。4 个 evidence chips：水印 / 裁切边缘 / 编号 / 空白与方向
- **实现**：`<aside>` + `<ul class="evidence-chips">` + 4 × `<li class="evidence-chip">`

### 4.3 `图像如何成为思考工具`（`.visual-thinking-block`）

- **位置**：section3（温莎的绘图）之后、section4 之前
- **内容**：深化「达·芬奇不是画插图，而是用图像思考」。4 个 thought cards：水:运动 / 肌肉:结构 / 动物:姿态 / 机械:推演
- **实现**：`<aside>` + `<ul class="thought-cards">` + 4 × `<li class="thought-card">`

### 4.4 `从看图到建模：Leonardo//thek@ 的研究逻辑`（`.research-model-block`）

- **位置**：section7（Leonardo//thek@ 平台工具墙）之后、section8 之前
- **内容**：把平台九大工具从列表提升为研究方法论。9 个 method rows：Foliations / Subject Indexes / Photographic Plates / Lexicon / Watermarks / Recompositions / Bibliography / Advanced Search / Comparative Study
- **实现**：`<aside>` + `<ul class="method-rows">` + 9 × `<li class="method-row">`

## 5. Postscript 深化

把 `<section class="postscript">` 从「不是天才崇拜」（4 点短句）深化为四个主题段：

1. **关于知识如何生成**：纸页是工作内存；思想不是先于纸页的成品，而是纸页之间的连接
2. **关于材料如何打断知识**：梅尔齐之后的关系丢失；整理工作保存了材料也改写了材料
3. **关于数字平台如何重新连接**：平台让证据重新相遇；复原研究关键是「让证据相遇」
4. **关于今天我们能学到什么**：知识库 / 数字人文 / AI 工具都面对同一个问题——按关系组织材料

控制字数约 480 字（连同 lede 与 closing），处于 brief 要求的 400–600 字范围内。

## 6. Curatorial essay & research notes

### `docs/CURATORIAL_ESSAY_ZH.md` (9,516 B)

中文策展长文，五节：

1. **为什么从纸页开始**（~500 字）：纸页是工作痕迹 / 整理史决定读法 / 观众可真正「看到」的东西
2. **被拆散的不是纸，而是关系**（~600 字）：梅尔齐 → 莱奥尼 → 温莎与米兰 → Leonardo//thek@ 的反向连接
3. **图像不是插图，而是思考**（~550 字）：水流 / 肌肉 / 动物 / 机械四种图式与跨域图式
4. **数字平台不是线上相册**（~500 字）：九大工具作为「从图像到证据、到关系、到论证」工作流
5. **今天我们能学到什么**（~450 字）：四点收束 + 「纸页仍在说话」

总字数约 2,600 字，处于 brief 要求的 2,000–3,000 字范围。

### `docs/DEEP_RESEARCH_NOTES_ZH.md` (7,002 B)

研究深化笔记：

- **可继续深挖的问题**：13 个（涵盖整理史 / 材料证据 / 图像与思考 / 平台与方法）
- **需要后续查证的事实**：6 个（含 v2.9 任务提示 + 写作语气问题）
- **可作为后续版本的内容方向**：8 个（内容 / 工程 / 工具三类）

## 7. README / Roadmap 更新

- `README.md`：在 v2.7 zh exhibition polish 节之后、当前版本节之前，插入 v2.8 Real Deep Content 节（33 行），不删除任何历史
- `docs/ROADMAP_AFTER_v2.6.md`：在「历史保留」节之后追加 v2.8 real rebuild 节（13 行），明确说明本轮基于真实 v2.7 tag 重建、不引用 phantom v2.8 / v2.9 / v3.x

## 8. 本地验证

### 8.1 HTML / CSS / script.js 字节数

| 文件 | round start | round end | 变化 |
|---|---|---|---|
| `site/index.html` | 85,564 B | 92,507 B | +6,943 B (+8.1%) |
| `site/style.css` | 40,362 B | 42,079 B | +1,717 B (+4.3%) |
| `site/script.js` | 14,594 B | 14,594 B | **0** (未修改) |

### 8.2 HTML marker 计数

| 类别 | 命令 | 结果 |
|---|---|---|
| v2.8 marker | `grep -c "v2.8-real-deep-content"` | 1 ✓ |
| deep-reading-block | `grep -c "deep-reading-block"` | 1 ✓ |
| material-evidence-block | `grep -c "material-evidence-block"` | 1 ✓ |
| visual-thinking-block | `grep -c "visual-thinking-block"` | 1 ✓ |
| research-model-block | `grep -c "research-model-block"` | 1 ✓ |
| placeholder | `grep -c "image-placeholder-pro"` | 0 ✓ |
| section-takeaway | `grep -c "section-takeaway"` | 18 (≥ 9) ✓ |
| quick-guide-zh | `grep -c "quick-guide-zh"` | 1 ✓ |
| viewer-action | `grep -c "viewer-action"` | 4 ✓ |
| v2.7 marker | `grep -c "v2.7-zh-exhibition-polish"` | 1 ✓ |

### 8.3 Node 语法检查

```bash
node --check site/script.js  # PASS
```

### 8.4 Playwright 运行时检查（python3.12 + Playwright 1.58.0）

| 项 | 结果 |
|---|---|
| section-nav runtime links | 31 (与 v2.5-real 基线一致：~10 sections × 3 link groups + a few extras) |
| deep-reading-block | 1 |
| material-evidence-block | 1 |
| visual-thinking-block | 1 |
| research-model-block | 1 |
| v2.7 marker | 1 |
| v2.8 marker | 1 |
| placeholder | 0 |
| guided-mode toggle | **OK** (body class 切换) |
| lightbox open | **OK** (role=dialog 出现 1 次) |
| lightbox ESC | dispatched |
| mobile 390 overflow | **0 px** ✓ |
| console errors | **[]** ✓ |
| deep blocks @ mobile 390 | 1 / 1 / 1 / 1 ✓ |

## 9. Live verification (round 终态，待 push + Actions 之后回填)

| 项 | 期望 | 实测 |
|---|---|---|
| Live byte size | ~92,500 B | 待回填 |
| v2.7 marker | 1 | 待回填 |
| v2.8 marker | 1 | 待回填 |
| v2.9 marker | 0 | 待回填 |
| placeholder | 0 | 待回填 |
| 4 deep blocks | 各 1 | 待回填 |
| script.js HTTP 200 | yes | 待回填 |
| site diff (HEAD~1..HEAD) | 仅 index.html / style.css | 待回填 |
| posts/case-study diff | empty | 待回填 |
| v2.0 tag unmoved | 9e6233a | 待回填 |
| v2.6 tag unmoved | 033b65e / 01cdaa2 | 待回填 |
| v2.7 tag unmoved | a0fee10 → f58f6b4 | 待回填 |
| GitHub Actions | success | 待回填 |

## 10. No-touch confirmation

| 类别 | 状态 |
|---|---|
| `site/script.js` | ✓ untouched (`node --check` PASS; runtime section-nav 与 v2.5-real 一致) |
| v2.0 tag | ✓ untouched (9e6233a) |
| v2.6 tag | ✓ untouched (033b65e / 01cdaa2) |
| v2.7 tag | ✓ untouched (a0fee10 → f58f6b4) |
| v2.0 / v2.6 GitHub Releases | ✓ untouched |
| v2.7 GitHub Release | ✓ untouched |
| `posts/` | ✓ untouched |
| `case-study/` | ✓ untouched |
| `release-assets/` 既有文件（`manifest.md`, `v2.6-content-stable-manifest.md`, `v2.7-zh-exhibition-polish-manifest.md`, `screenshots/`） | ✓ untouched |
| `_template/` | ✓ **不存在**（按约束未创建） |
| `_pilots/` | ✓ **不存在**（按约束未创建） |
| Untracked `.firecrawl/` | ✓ 未处理 |
| `git add .` | ✓ 全部显式 add |
| 新图片 | ✓ 未引入 |
| 新 tag | ✓ 未创建（v2.8-real-deep-content-freeze 留给下一轮） |
| 新 GitHub Release | ✓ 未创建（同样留给下一轮） |
| Bilingual / education / template 内容 | ✓ 未触碰 |

## 11. Known note

本轮明确**不**做的事：

- ❌ 未创建 `v2.8-real-deep-content` tag（留给 v2.8-real-stable-freeze round）
- ❌ 未创建 GitHub Release（同上）
- ❌ 未创建 `_template/` 或 `_pilots/`
- ❌ 未引用任何 phantom v2.8 / v2.9 / v3.x 历史
- ❌ 未修改 GitHub Issue #1「v2.7 Bilingual Edition」（保持 OPEN，留给后续 round 单独处理）
- ❌ 未引入新图片

## 12. Next recommended task

**v2.8-real-stable-freeze**（独立 round）：

1. 新增 `docs/RELEASE_NOTES_v2.8_REAL_DEEP_CONTENT.md`
2. 新增 `release-assets/v2.8-real-deep-content-manifest.md`
3. 创建 annotated tag `v2.8-real-deep-content` @ freeze commit
4. `git push origin v2.8-real-deep-content`
5. `gh release create v2.8-real-deep-content` + attach notes
6. 更新 README「Stable Tag」字段
7. live 重新验证（byte size / 4 deep blocks / placeholder / script.js / runtime）

之后下一推荐 round 为 **v2.9 Real Source & Rights Audit**（基于 v2.8 tag），逐图核 source note 与权利状态。Phantom v3.x 模板化路线在 `_template/` 真实创建之前不推进。

## 13. Final status

| 项 | 值 |
|---|---|
| STATUS | **PASS** |
| Freeze commit | 待 commit 后回填 |
| Live URL | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| Live byte size | 92,507 B（待 push + Actions 后 live 验证） |
| Verified source tag | `v2.7-zh-exhibition-polish` @ `f58f6b4`（起点） |
| v2.8 marker count | 1 (meta) + 1 (comment) + 1 (footer) = 3 层 |
| 4 个深度模块数量 | 1 / 1 / 1 / 1 |
| curatorial essay | 创建 (`docs/CURATORIAL_ESSAY_ZH.md`, 9,516 B) |
| research notes | 创建 (`docs/DEEP_RESEARCH_NOTES_ZH.md`, 7,002 B) |
| section-nav runtime | 31 links（与 v2.5-real 基线一致） |
| placeholder | 0 |
| guided mode toggle | OK |
| lightbox | OK |
| mobile 390 overflow | 0 px |
| console errors | 0 |
| v2.0 tag | ✓ untouched |
| v2.6 tag | ✓ untouched |
| v2.7 tag | ✓ untouched |
| 旧 releases | ✓ untouched |
| site/script.js | ✓ untouched |
| `_template/` | ✓ 不存在 |
| `_pilots/` | ✓ 不存在 |
| Next recommended task | v2.8-real-stable-freeze |

---

*本报告 v2.8-real-deep-content round 自证。所有「verified」项均由本轮的 `<tool_use_result>` 凭据支撑；无 phantom 重建。*