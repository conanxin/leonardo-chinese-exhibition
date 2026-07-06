# v2.6 Content Stable Release

> 达·芬奇手稿展览 — 内容审校稳定封版

## 概览

| 项 | 值 |
| --- | --- |
| **Live URL** | https://conanxin.github.io/leonardo-chinese-exhibition/ |
| **Stable commit** | `d71b0e8a245f040d7b44358e6cdaa8b079dc0d13` |
| **Tag** | `v2.6-content-stable`（本轮新增） |
| **Stable base** | v2.6 content copy polish |
| **Baseline** | v2.5-real guided accessibility recovery |
| **历史起点** | v2.4 artifact annotation upgrade |

## 真实版本线

| 版本 | 内容 | commit |
| --- | --- | --- |
| **v2.4 artifact annotation upgrade** | 展品注释面板、glossary 术语表、annotation panel ×4 | `c3c3e0b` |
| **v2.5-real guided accessibility recovery** | 完整重建 guided mode、focus 管理、section-nav、tour progress | `c512dbd` |
| **v2.6 content copy polish** | 全站中文文案审校、术语统一、图注 / source note 统一 | `d71b0e8` |
| **v2.6 content stable** | 稳定封版、release notes、final audit、清理残留 v2.7 标记 | 待 tag commit |

## 已修正的历史问题

- 早前 v2.5 / v2.6 阶段曾有功能误报（例如 live 缺 guided mode 入口、section-nav 数量口径混乱）
- 后续通过 v2.5-real recovery 真实补回导览、focus、键盘导航、section-nav 全部功能
- v2.6 完成真实的中文文案审校、术语统一、图注/source note 打磨
- v2.6-content-stable 阶段清理了上一次迭代遗留的 v2.7 重复 marker，统一版本字符串

## 当前能力（v2.6 stable）

- 真实图像（温莎皇家收藏高清 + 安布罗西安图书馆大西洋手稿）
- 真实平台截图（Leonardo//thek@ 模块界面）
- Lightbox 浏览 + 键盘导航 + focus 返回
- Guided mode（导览模式）+ 退出
- Runtime section-nav（11 项，跨 8 个主展区 + intro + 展品索引 + 参观路线）
- Tour progress（顶部进度指示）
- Annotation panels ×4（温莎手稿四张关键图版）
- Platform interface notes ×5（平台模块说明）
- Glossary ×14（中英对照术语表）
- Content copy polish（展览墙文语气，术语一致，标点统一）

## 验证结果

| 项 | 值 |
| --- | --- |
| **Live Playwright** | **14/14 PASS** |
| **section-nav (runtime DOM)** | **11** |
| **section-takeaway** | 9 |
| **glossary** | 14 |
| **annotation panels** | 4 |
| **platform interface notes** | 5 |
| **image-placeholder-pro** | 0 |
| **script.js HTTP** | 200 |
| **Live byte size** | 82,787 B（v2.6 阶段） |
| **markers on live** | 9（旧 8 + v2.6 stable 新 1） |

## No-touch（按 spec 严格遵守）

- v2.0 tag（`v2.0-public-portfolio-case` → `9e6233ab2b2c5aa3e1243565583f8f66c7df34b4`）**未触碰**
- 旧 GitHub Release **未触碰**
- `posts/` `case-study/` `release-assets/` **未触碰**
- Hermes 生产配置 **未触碰**
- untracked `.firecrawl/` **未处理**

## 已知小问题（按事实记录）

- 之前报告中曾出现 section-nav 口径混乱（"9+" / "10 generated" / "9+ in DOM"）
  - **本轮统一为 11**（Playwright 实地确认 = 11，无重复，无遗漏）
- 本地 HTML byte size（82,797 B）与 live byte size（82,787 B）有 10 字节差异
  - 原因：GitHub Pages 部署时对静态 HTML 的标准化处理（不影响功能与展示）

## 下一步建议

- v2.6-content-stable 为当前稳定基线
- 后续如做 v2.7+，建议聚焦在：图像替换为更高分辨率版本、annotation panel 扩写、英文导览副本、移动端 UX 微调
- 旧 GitHub Release 资产（`release-assets/`）保留作为 portfolio 历史，**不删**

---

*Released: v2.6 content stable — 真实达·芬奇手稿数字展览，导览 + 无障碍 + 内容审校完整。*
