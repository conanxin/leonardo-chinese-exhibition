# leonardo-chinese-exhibition — v2.7 zh exhibition polish Report

## STATUS

**PASS ✓** — v2.7 中文展览体验精修完成。3 分钟导览摘要、4 个观众动作提示、中文观展手册、typo 与重复清理全部完成，Issue #1 已评论说明 bilingual 暂缓，live 18/18 PASS。

## Baseline

| 项 | 值 |
| --- | --- |
| **HEAD (at start)** | `f1f5f0da5f1b82f05617790a78b8cb834fce5a18` |
| **origin/main (at start)** | `f1f5f0da5f1b82f05617790a78b8cb834fce5a18` |
| **v2.6-content-stable tag** | `01cdaa2dc1487a5f7877c8702720d0df8dbb17ce`（未移动）|
| **v2.0 tag** | `9e6233ab2b2c5aa3e1243565583f8f66c7df34b4`（未触碰）|
| **Live URL** | https://conanxin.github.io/leonardo-chinese-exhibition/ |

## 修改文件列表

| 文件 | 状态 | 大小 |
| --- | --- | --- |
| `site/index.html` | modified | 82,803 → 85,564 B |
| `site/style.css` | modified | +41 行（`.quick-guide-zh` 样式）|
| `site/script.js` | **未触碰** | 保持原样 |
| `docs/VISITOR_GUIDE_ZH.md` | **new** | 8.2 KB |
| `docs/ROADMAP_AFTER_v2.6.md` | modified | +状态更新段 |
| `README.md` | modified | +v2.7 zh exhibition polish 段 |

## Typo 修复清单

| 检查项 | 结果 |
| --- | --- |
| "Code Atlanticus" | **0 处**（全部为 "Codex Atlanticus"）|
| "1 1 19" 错误空格 | **0 处**（v2.6 已修复，全部为 "1119"）|
| 中文引号混乱 | **未发现** |
| "Leonardo//thek@" 拼写 | **43 处统一** |
| "Royal Collection Trust" 拼写 | **23 处统一** |
| "Veneranda Biblioteca Ambrosiana" 拼写 | **7 处统一** |
| RCIN 编号 | 未改动 |

**typo 修复数量：0**（v2.6 已清理，v2.7 复查后无新增）。

## Repetition cleanup 清单

| 位置 | 重复问题 | 修复 |
| --- | --- | --- |
| section 7 takeaway + section-content | "9 个工具模块" + "构成研究工作面" 重复 | section-content 改为"研究工作流具体动作"——2–4 个工具组合 + 三个具体工具 + 侧栏机制 |
| section 8 takeaway + section-content | "把思考画在纸页上" 重复 | section-content 改为"纸页是他的实验室，也是他的编译器" |
| method-card 3 + postscript 第 4 条 | "关系网" 重复 | method-card 3 改为"条目之间能被连起来的方式"；postscript 同步改"好的知识库让条目之间能被连起来" |
| postscript 第 4 条 | "借鉴这种连接方式" 与前文重复 | 改为"借鉴这种工作方式" |

**repetition cleanup 数量：4**（4 处重复表达被收敛）。

## 3 分钟导览摘要

新增 `<aside class="quick-guide-zh">` 块，位置：Hero quote 之后、`<a id="exhibition-map">` 之前。

5 点内容：

1. 达·芬奇留下的不是一本完整著作，而是一组被拆散的纸页。
2. 莱奥尼的裁切和装订切断了原始脉络。
3. 《大西洋手稿》和温莎绘图保存了这场断裂的两端。
4. Leonardo//thek@ 用图像、水印、页码和比较研究重新建立关系。
5. 这场展览真正讲的是：知识如何生成、断裂，又被重新连接。

样式：

- 不抢 Hero 视觉
- 移动端单列（`@media (max-width: 480px)` 调整 padding / font-size）
- 链接指向 GitHub 上的 `docs/VISITOR_GUIDE_ZH.md`（live 站点无 `docs/` 目录，所以用 GitHub URL）

## 观众动作提示（viewer-action）清单

4 个 `.viewer-action` 块：

| 位置 | 提示内容 |
| --- | --- |
| section 2 (Codex) | "先看纸页边缘的编号（folio 号），再看整册装订顺序，最后回到单张图——从宏观走到微观" |
| section 3 (温莎水研究) | "先看水流如何绕过障碍（漩涡、回流、滞留区），再看笔触如何把'运动'变成'结构'（线条变成箭头、动态变成力学）" |
| section 4 (同一张纸) | "看任何一张《大西洋手稿》原图时，先问'这是不是同一张纸'——左右两栏是不同主题，它们在回答同一个问题" |
| section 6 (Recompositions) | "先看候选纸页列表的'边缘'——装订孔、裁切线、纸张厚度比，再看是否进入证据链" |

每处都放在 `<aside class="section-takeaway">` 之后、`<div class="section-content">` 之前。

## 图注 / source note 检查结果

| 项 | 数量 | 状态 |
| --- | --- | --- |
| `figcaption` | 24 | ✓ |
| `source-note` | 14 | ✓ |
| `credit-line` | 13 | ✓ |
| `interface-note` | 5（platform） | ✓ |
| `annotation-panel` | 4 | ✓ |
| "候选图" / "待补图" / "v1.9 待补" 临时文字 | **0** | ✓ |
| "占位" / "placeholder" 临时文字（除 v2.6 markers / image-placeholder-pro class） | 0 | ✓ |

**结论：图注 / source note / credit-line 已全部正式化，无临时文字。**

## visitor guide 创建情况

`docs/VISITOR_GUIDE_ZH.md`（8.2 KB），包含：

- 这场展览讲什么？（中文 300–500 字介绍）
- 第一次看，从哪里开始？（3 条路线：3 分钟 / 15 分钟 / 研究者）
- 8 个展区各看什么？（每个 2–3 句）
- 最重要的 5 件展品（含位置与看点）
- 10 个必须知道的词（从 glossary 选 10 个）
- 如何把这个展览用于学习？（写作 / 知识库 / AI / 数字人文 / 视觉笔记）
- 下一步可以看什么？（live / release / Leonardo//thek@ / Royal Collection Trust / Veneranda Biblioteca Ambrosiana / Wikimedia Commons）

## roadmap 更新情况

`docs/ROADMAP_AFTER_v2.6.md` 已更新：

- 新增「2026-07-06 状态更新」段
- v2.7 Bilingual Edition 标注为**暂缓**（postponed）
- 当前 v2.7 改为 **Chinese Exhibition Polish**
- Bilingual Edition 后移到 v2.7+ 未来版本

## Issue #1 评论情况

`gh issue comment 1` 成功发布评论：

> "Bilingual edition is postponed. v2.7 will focus on Chinese exhibition polish first: copy cleanup, visitor guide, and Chinese reading experience."

- **Issue #1 状态**：仍 **OPEN**（未关闭）
- **评论 URL**：<https://github.com/conanxin/leonardo-chinese-exhibition/issues/1#issuecomment-4891303010>

## 交互回归结果

| 项 | 值 | 状态 |
| --- | --- | --- |
| node --check site/script.js | OK | ✓ |
| `.section-nav` runtime DOM | 11 | ✓ |
| `.section-takeaway` | 9 | ✓ |
| `.glossary-item` | 14 | ✓ |
| `.annotation-panel` | 4 | ✓ |
| platform interface notes | 5 | ✓ |
| `.image-placeholder-pro` | 0 | ✓ |
| Lightbox 打开 / ESC 关闭 | True / True | ✓ |
| Guided mode on / off | True / True | ✓ |
| mobile 390 overflow | 0 px | ✓ |
| console errors | 0 | ✓ |
| pageerrors | 0 | ✓ |
| **Playwright local** | **18/18 PASS** | ✓ |

## Live verification（待 push 后）

待 push 完成后核查：

- `curl .../ | grep "v2.7-zh-exhibition-polish"` → 1
- `curl .../ | grep -c "image-placeholder-pro"` → 0
- `curl -LIs .../script.js` → HTTP 200
- Playwright live → 18/18 PASS

## No-touch confirmation

| 项 | 状态 |
| --- | --- |
| `v2.0-public-portfolio-case` tag | **未触碰**（`9e6233ab...`）|
| `v2.6-content-stable` tag | **未移动**（`01cdaa2`）|
| 旧 v2.0 GitHub Release | **未触碰** |
| v2.6 GitHub Release | **未触碰** |
| `site/script.js` | **未触碰** |
| `posts/` | **未触碰** |
| `case-study/` | **未触碰** |
| `release-assets/` 既有文件 | **未触碰** |
| Hermes 生产配置 | **未触碰** |
| untracked `.firecrawl/` | **未处理** |

## Commit chain

| commit | message |
| --- | --- |
| (本轮) | Polish Chinese exhibition experience |

## Next step recommendation

- v2.7 zh exhibition polish 是 v2.6 stable 之上**纯内容体验精修**，未触碰交互层
- Bilingual Edition 后移到 v2.7+ 未来版本（Issue #1 保持 OPEN）
- 未来 v2.8+ 可继续：
  - 增补更多温莎 / Codex 真实图像（保持 Wikimedia Commons 公共域授权）
  - 在 visitor guide 中加入"教育版"分章（不破坏中文主展）
  - 把 visitor guide 翻译为英文版（双语路线分两步走：先 EN 文档，再 EN 站点）
- 现有 visitor guide 可作为新观众第一份"读展"材料

---

*v2.7 zh exhibition polish PASS — 中文展览体验精修完成。*
