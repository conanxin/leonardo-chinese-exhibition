# Roadmap after v2.6 Content Stable

> v2.6 Content Stable 之后的中长期路线

本路线描述的是**未来可能的方向**，不是承诺。所有项目应在 GitHub Issue 中先讨论，再以独立分支实施，并以新 tag 收口。

## 2026-07-06 状态更新

- **v2.7 Bilingual Edition 暂缓**。当前 v2.7 已改为 **Chinese Exhibition Polish**：专注中文展览体验精修（typo / 重复 / 3 分钟摘要 / 中文观展手册 / 观众动作提示）。详见 [GitHub Issue #1](https://github.com/conanxin/leonardo-chinese-exhibition/issues/1)。
- Bilingual Edition 后移到 v2.7+ 的未来版本。在 bilingual 之前先把中文体验打磨到位。

## v2.7 Bilingual Edition（暂缓）

**目标**（保留，未来版本实施）：

- 中英双语切换
- 保留中文主站
- 不破坏现有导览与 lightbox
- 中英文案同步审校

**当前状态**：Postponed。Issue #1 已评论说明。中文体验先在 `v2.7 zh exhibition polish` 中打磨。

**关键风险**：

- 双语切换不应改变当前 v2.6 stable 的 `script.js` 行为
- 文案量翻倍，需提前规划 review 流程
- 切换状态的本地化存储

## v2.8 Education / Teacher Guide

**目标**：

- 课堂导览
- 讨论问题
- 15 分钟课程脚本
- 学生观察任务

**关键风险**：

- Education 模式不应干扰现有导览
- 教师 / 学生视角的 UI 区分
- 课堂用 PDF / 打印版的可访问性

## v2.9 More Manuscript Images

**目标**：

- 增补更多 Codex Atlanticus / Royal Collection 图像
- 明确版权与 source note
- 不回到 placeholder

**关键风险**：

- 严格遵守 Wikimedia Commons 公共域授权
- 每张图必须有 RCIN 编号 / page number
- 任何 image 增补必须配合 figcaption 审校

## v3.0 Reusable Digital Exhibition Template

**目标**：

- 抽象出中文数字展览模板
- 支持其他艺术家 / 文献 / 档案项目复用
- 保留 OpenAI-style editorial + artifact cards + glossary + guided mode

**关键风险**：

- 这是**破坏性重构**，必须独立分支独立 tag
- v2.6 stable 必须保持原状可访问
- 模板的可配置性 vs 当前 v2.6 的硬编码

## Backlog

不进入 v2.7 / v2.8 / v2.9 计划，但可作为远期探索：

- 更好的移动端导览体验
- 更精确的图版注释
- 更好的站内搜索 / index
- Static JSON data layer（让展览内容可被外部查询）
- Screenshot refresh（v2.6 release 截图重制）
- 多语言扩展（英 / 日 / 法）
- 离线 / 打印版

---

## Verified reality reset (2026-07-07)

> 本节为对账 + 恢复标记，不删除上文任何历史。

- **真实 live 当前版本**：v2.7 zh exhibition polish（commit `71c7403` · HEAD）。Live byte size 85,564 B，HTML 含 `v2.7-zh-exhibition-polish` footer marker，无 placeholder，`script.js` HTTP 200。
- **真实 tag 集合**：`v2.0-public-portfolio-case` (9e6233a), `v2.6-content-stable` (01cdaa2)。**仅此两个**。
- **v2.7 的真实状态**：内容已上线，commit 链存在（`31e5126` / `c3c3e0b` / `988ebb9` / `e1ca01f` / `71c7403` 等），但**尚未 freeze** —— 没有 v2.7 tag / release / release notes / release-assets manifest。
- **v2.8 / v2.9 / v3.0 / v3.1 / v3.2 / v3.3**：当前**不可视为已完成**。具体 phantom 内容见 [`docs/REALITY_CHECK_AFTER_PHANTOM_V3.md`](REALITY_CHECK_AFTER_PHANTOM_V3.md)。

### 后续推荐顺序（基于真实状态）

1. **v2.7-real-stable-freeze**：把已上线的 v2.7 内容独立 tag + release。这是「把真实状态记录成可验证状态」，无破坏性。Issue #1（v2.7 Bilingual Edition）目前仍 OPEN，但实际做的不是 bilingual —— 在 freeze round 里需要重新审视 issue 标题。
2. **v2.8 + v2.9**：在 v2.7 freeze 之后，按原有 roadmap（deep content → source rights audit）逐步推进。每一步都基于前一步真实 freeze，不允许 phantom 跳跃。
3. **v3.x template**：必须先真实创建 `_template/site/` 骨架（在 `_template/` 下独立子目录），与 live `site/` 物理隔离。完成 v3.0 template extraction audit 之后才有 v3.1 / v3.2 / v3.3 讨论基础。

### 历史保留

上文「v2.7 Bilingual Edition（暂缓）/ v2.8 Education / Teacher Guide / v2.9 More Manuscript Images / v3.0 Reusable Digital Exhibition Template / Backlog」段落**全部保留**，作为「方向记录」存在；本节是「真实状态校正」，两者并存。

---

*Roadmap 是**方向**，不是时间表。任何项目进入实施前，应在 GitHub Issue 中先讨论，并通过 `v2.6-content-stable` tag 派生新分支。*
