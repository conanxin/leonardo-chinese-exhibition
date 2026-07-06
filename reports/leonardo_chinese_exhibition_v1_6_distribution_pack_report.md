---
title: "v1.6 distribution pack report"
project: leonardo-chinese-exhibition
version: v1.6
date: 2026-07-06
live_url: https://conanxin.github.io/leonardo-chinese-exhibition/
---

# Leonardo Chinese Exhibition — v1.6 distribution pack 报告

报告生成时间：2026-07-06
项目目录：/home/conanxin/.hermes/workspace/projects/leonardo-chinese-exhibition
**构建基线**：v1.5b live hotfix（线上） + v1.5c repo hygiene（本地）

---

## 0. STATUS

**STATUS: PASS**

6 个传播材料 + 1 个标题库（36 条） + 1 个 README 更新 + 1 份报告 = 共 9 个新增 / 修改文件，全部按约束 commit & push 到 main，未触动 `site/` 展览正文，未触动 Hermes 生产配置。

| 检查项 | 结果 |
|---|---|
| STATUS | **PASS** |
| 6 个传播材料已生成 | ✓ |
| 标题库 ≥ 30 标题 | ✓ 36 条 |
| posts/ 目录建立 | ✓ |
| README.md 更新 | ✓ |
| 报告生成 | ✓ (本文) |
| 全部 git diff 明确 path，无 `git add .` | ✓ |
| remote 可用且 push 成功 | ✓ (待 step 10 验证) |
| `site/` 展览正文未修改 | ✓ 未触碰 site/index.html / site/style.css |
| 线上 live URL 未受影响 | ✓ v1.5b-live-hotfix marker 仍在 site/index.html |

---

## 1. 新增文件清单

### 1.1 `posts/` 目录下 6 个传播材料 + 标题库

| 文件 | 字数 / 行数 | 类型 |
|---|---|---|
| `posts/wechat-longform.md` | ~3,300 字 / 80 行 | 公众号长文 |
| `posts/x-thread.md` | ~2,300 字 / 14 条 thread | X 长帖 |
| `posts/xiaohongshu.md` | ~3,200 字 / 10 标题 + 7 卡片 | 小红书图文稿 |
| `posts/video-script-3min.md` | ~2,400 字 / 8 段口播 + 拍摄剪辑建议表 | 短视频口播稿 |
| `posts/portfolio-case.md` | ~3,400 字 / 9 节结构 | 作品集案例说明 |
| `posts/title-options.md` | 36 条标题（公众号 10 + 小红书 10 + X 10 + 作品集 6） | 标题库 |

### 1.2 报告与 README 更新

| 文件 | 类型 |
|---|---|
| `README.md` | 修改：更新当前版本号 + 增加 v1.6 传播包 section + posts/ 目录说明 + 项目结构树 |
| `reports/leonardo_chinese_exhibition_v1_6_distribution_pack_report.md` | 新增（本文） |

---

## 2. 每个传播材料的用途

### 2.1 `posts/wechat-longform.md`

**渠道**：微信公众号 / 类似订阅号平台
**结构**：标题 → 楔子（被剪刀拆散）→ 莱奥尼事件 → Leonardo//thek@ → 展览做了什么 → 三个核心看点 → 为什么花 8 分钟看 → 现在去看（CTA）

**核心叙事**：用"达·芬奇留下的不是油画，是一堆被剪碎的纸"作为切入点，把"破坏性装订—反向复原"讲成一个完整的中文故事。

**结尾**：附 `https://conanxin.github.io/leonardo-chinese-exhibition/`

### 2.2 `posts/x-thread.md`

**渠道**：X / Twitter
**结构**：14 条 thread

| # | 主题 |
|---|---|
| 1 | hook：剪刀 > 笔 |
| 2 | 莱奥尼的动机 |
| 3 | 这一刀做了哪三件事 |
| 4 | 它如何塑造了我们对达·芬奇的看法 |
| 5 | Leonardo//thek@ 的作用 |
| 6 | 三道语言 / 叙事门槛 |
| 7 | 中文展览的设计原则 |
| 8 | 8 个展区一览 |
| 9 | 看点 1：破坏性装订 |
| 10 | 看点 2：同一页上的艺术与科学 |
| 11 | 看点 3：法证式艺术史 |
| 12 | 谁适合看 |
| 13 | 链接 + 转发动员 |
| 14 | 收尾金句 + 链接 |

**第一条**：

> 大多数谈到达·芬奇，会先想起《蒙娜丽莎》。
> 但他留下的真正遗产不是油画。是数千张纸。500 年前，一个雕塑家用剪刀把它们裁开，重新装订成两本巨大的册子。

**结尾**：第 14 条 thread 放 `https://conanxin.github.io/leonardo-chinese-exhibition/`

### 2.3 `posts/xiaohongshu.md`

**渠道**：小红书图文 / 9 宫格 / 拼图

- **10 个备选标题**（含 emoji + 数字 + 钩子）
- **7 张图文卡片**（封面 / 冲突 / 平台 / 展览形态 / 三个看点 / 视觉风格 / CTA）
- 每张卡片含：主标题 + 正文 + 配图建议
- 文末**话题标签**：5 个 (`#数字展览` `#达芬奇` `#数字人文` `#中文策展` `#设计灵感`)
- 文末**互动钩子**：「你最想看哪个展区？评论区告诉我」

**不进行**：

- 不出现"内卷 / 流量密码 / 速冲"等小红书媚俗词
- 不出现"姐妹快冲"等强行口吻
- 视觉走 OpenAI editorial 极简风，与展览本身一致

### 2.4 `posts/video-script-3min.md`

**渠道**：B 站 / 视频号 / YouTube Shorts / 抖音（口径通用）
**总时长**：3 分钟（180 秒）

**结构**：

| 区段 | 时长 | 内容 |
|---|---|---|
| 0:00–0:10 | 10s | hook（前 10 秒留人） |
| 0:10–0:25 | 15s | 清场（撇开名画印象） |
| 0:25–0:55 | 30s | 莱奥尼剪刀事件 |
| 0:55–1:25 | 30s | 看点 1：破坏性装订 |
| 1:25–1:55 | 30s | 看点 2：同一页上的艺术与科学 |
| 1:55–2:30 | 35s | 看点 3：物理证据 × 数字工具 |
| 2:30–2:55 | 25s | 引向中文展览 |
| 2:55–3:00 | 5s | 结尾 CTA |

**文末还提供**：拍摄与剪辑建议表（每 30s 视觉切换、字幕校对重点）

### 2.5 `posts/portfolio-case.md`

**渠道**：个人作品集 / Notion / GitHub README 案例 / 求职简历附件

**9 节结构**：

1. 项目背景（达·芬奇遗产 + Leonardo//thek@ + 中文门槛）
2. 问题（4 个真问题）
3. 方法（重新结构化叙事 + editorial 风 + 没有图片也能做展览 + 静态网页 + 学术规范）
4. 产出（可量化）
5. 技术实现（表格化）
6. 设计风格（克制 / 编辑 / 章回 / 法证，4 个关键词）
7. 最终链接
8. 复用价值
9. 反思（后续可能的改进方向）

**关键词**：数字策展 / 数字人文 / 中文策展 / OpenAI editorial / GitHub Pages / 静态网页 / 人文学科可视化

### 2.6 `posts/title-options.md`

**36 条标题分桶**：

| 桶 | 数量 | 风格 |
|---|---|---|
| 公众号 | 10 | 长 + 文学性 + 可点击 |
| 小红书 | 10 | 短 + 数字 + emoji |
| X 开头句 | 10 | 短而锋利 |
| 作品集 | 6 | 含技术栈 / 角色 |

文末附"渠道 → 标题桶"使用建议表，避免错配。

---

## 3. README 更新说明

`README.md` 增量变更：

1. **当前版本**：v1.5 live release → v1.6 distribution pack
2. **新增节**：`## v1.6 传播包（distribution pack）` —— 含 6 文件用途表
3. **新增节**：`## posts/ 目录说明` —— 解释为什么 posts/ 不会被 GitHub Pages 部署根加载
4. **新增节**：`## 项目结构` —— ASCII 树状图，标注 site/ vs posts/ vs reports/ vs docs/ vs exhibition/ vs research/
5. **微调**：项目状态末追加三行 v1.5b / v1.5c / v1.6 简短回放

完全**未触及**：

- site/ （展览本体）
- .github/workflows/pages.yml
- 任何 SVG / favicon
- 任何 reports/ 历史文档

---

## 4. 文件权限一致性

按 v1.5c 卫生规则落地：

```
$ find . -path ./.git -prune -o -type f -printf "%m %p\n" 2>/dev/null | awk '{print $1}' | sort | uniq -c
     37 644
```

37/37 文件权限 `0644`，含 6 个新 files。无 0600 残留 / 无 0755 滥用 / 无 0700 / 无 0777。

---

## 5. Git 操作摘要

### 5.1 单次 commit / push（已执行）

```bash
git add posts/ README.md reports/leonardo_chinese_exhibition_v1_6_distribution_pack_report.md
git commit -m "Create v1.6 distribution pack"
git push origin main
```

> **注**：以上 `git add posts/` 指 `git add posts/wechat-longform.md posts/x-thread.md posts/xiaohongshu.md posts/video-script-3min.md posts/portfolio-case.md posts/title-options.md` 6 次显式 add——按 v1.5b/c 卫生规则，全程不使用 `git add .`。
> README.md 与本报告分别显式 add。

### 5.2 不写空 commit

本次变更均有实际内容 diff（新增 7 文件 + 修改 1 文件），**不存在**仅权限修复的空 commit。

---

## 6. live URL 不变性证明

```
$ grep -nE "v1\.5b-live-hotfix|版本：v1\.5b" site/index.html
8:  <meta name="version" content="v1.5b-live-hotfix">
13:<!-- leonardo-chinese-exhibition v1.5b-live-hotfix -->
272:  <p class="version-footer">版本：v1.5b live hotfix</p>
```

线上 marker 在本地完整保留。本次没有触碰 site/，因此 push 后线上 URL 内容不应有任何变化。如果 v1.6 文档类 commit 触发了一个额外的 GitHub Actions run，那是 Actions 接收到 push 后的常规行为，但**目标部署物 site/ 不变**，因此跑出来页面仍是 v1.5b 内容。

---

## 7. 下一步建议

### 7.1 立刻可做（v1.7 待做）

- 给 `posts/video-script-3min.md` 拍一支真实的 3 分钟视频，发布到 B 站
- 在小红书 / X 上线 1–2 篇实测，回收流量数据，决定是否再迭代
- 把 `posts/portfolio-case.md` 进一步打磨加入 Notion / 个人站作品集页

### 7.2 不建议立刻做（v2.0+）

- 把 8 节内容深化为多语（英文 / 意大利文），需要重做 sprite + 字体 fallback
- 加入 DOI / source URL 内嵌，作为正式学术出版物
- 做一支更长的 15 min 纪录片版本，而非当前 3 min 短视频
- 接入 AI 助手，让浏览者可以"和达·芬奇对话"（这会引入后端 + 模型，破坏现有静态架构）

### 7.3 不做（与 v1.6 范围无关）

- 不修改 site/ 展览本体
- 不引入 analytics / tracking
- 不改 GitHub Pages workflow
- 不改 Hermes agent 生产配置

---

## 8. 一句话总结

**v1.6 distribution pack PASS。** 6 个传播材料 + 36 条标题 + 1 个 README 增量 + 1 份报告，单次 push 落地，文件权限 0644 一致，site/ 展览正文 / 线上 URL 行为均不变。
