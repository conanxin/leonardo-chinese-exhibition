# V3 Template Roadmap / v3 模板路线图

> 本文件记录从 v2.9-real-source-rights-audit 出发的 v3.x 路线图。
> 起点：v2.9-real-source-rights-audit 已封版（live 92,976 B）
> phantom v3.x 历史（v3.0-source-rights-audit / v3.1-template-audit / v3.2-second-exhibition-pilot 等）**不**作为基线。

## v3.0 Real Template Extraction Audit

| 项 | 值 |
|---|---|
| 状态 | **Done**（v3.0-real-template-extraction-audit @ `dd7d589`，tag + GitHub Release + freeze report 全部落地） |
| 起点 | v2.9-real-source-rights-audit @ a1e667e |
| 交付物 | `_template/` 真实创建（17 文件，freeze round 实测；extraction round 误写 18 已 patch 修正） |
| 范围 | docs/TEMPLATE_EXTRACTION_AUDIT.md + docs/REUSABLE_EXHIBITION_COMPONENTS.md + _template/ |
| 不做的事 | 不创建 `_pilots/`，不部署模板，tag 已封版 |
| 下一步 | v3.1 Second Exhibition Pilot（当前 round） |

## v3.0 Real Stable Freeze

| 项 | 值 |
|---|---|
| 状态 | **Done**（`v3.0-real-template-extraction-audit` tag 已 push，Release 已发布 Latest 2026-07-07T22:48:44Z） |
| 起点 | v3.0 extraction round HEAD `9aea3ae` |
| 交付物 | freeze commit `beb2d7b` + SHA-backfill `dd7d589` + tag `v3.0-real-template-extraction-audit` (`3b5404f`) + GitHub Release |
| 范围 | 冻结 `_template/` 骨架 + docs/ + reports/ |
| 不做的事 | 不创建 `_pilots/`，不修改 live |
| 下一步 | v3.1 Second Exhibition Pilot（当前 round） |

## v3.1 Second Exhibition Pilot

| 项 | 值 |
|---|---|
| 状态 | **Done**（`v3.1-real-second-exhibition-pilot` @ `c5e93d0`，tag + GitHub Release + freeze report 全部落地） |
| 起点 | 已封版的 `v3.0-real-template-extraction-audit` @ `dd7d589` |
| 交付物 | `_pilots/second-exhibition-pilot/`（18 文件，pilot 验证模板真正可复用） |
| 范围 | 主题《一件作品的旅程》 + 自制 SVG（3 张） + 4 section + 4 artifact card + 6 glossary + source/rights docs + 5 内部 docs + README/manifest/notes |
| 不做的事 | 不部署到 GitHub Pages，不引入真实馆藏图片，不修改 `_template/`，不修改旧 tag |
| 下一步 | v3.1-real-stable-freeze（已完成，与本 round 同 commit 链） |

## v3.1 Second Exhibition Pilot — stable freeze

| 项 | 值 |
|---|---|
| 状态 | **Done**（与 v3.1 pilot 同步完成，2-commit freeze：pilot 创建 `ae1a54e` → freeze `de017f9` → SHA backfill `c5e93d0`） |
| tag | `v3.1-real-second-exhibition-pilot` (`f839187` / target `c5e93d0`) |
| 范围 | 冻结 pilot 数据 / 站点 / 文档 + 写 freeze report |
| 不做的事 | 不创建第二个 pilot，不部署 |

## v3.2 Template Documentation

| 项 | 值 |
|---|---|
| 状态 | **Done**（`v3.2-real-template-documentation` @ `5a89fb2`，tag + GitHub Release + freeze report 全部落地） |
| 起点 | 已封版的 `v3.1-real-second-exhibition-pilot` @ `c5e93d0` |
| 交付物 | 五份中文模板使用手册（usage / authoring / rights checklist / pilot workflow / release workflow） + `_template/README.md` 追加"使用文档"小节 |
| 范围 | `_template/USAGE_GUIDE_ZH.md` + `_template/CONTENT_AUTHORING_GUIDE_ZH.md` + `_template/SOURCE_RIGHTS_CHECKLIST_ZH.md` + `_template/PILOT_WORKFLOW_ZH.md` + `_template/RELEASE_WORKFLOW_ZH.md` |
| 不做的事 | 不修改 `site/index.html` / `site/style.css` / `site/script.js`，不修改 `_template/site/`，不修改 `_template/data/`，不修改 `_pilots/second-exhibition-pilot/` 内容，不创建新 pilot，不部署，不移动任何旧 tag，不修改旧 GitHub Releases，不新增真实馆藏图片 |
| 下一步 | v3.3 Template Quality Gate（本 round）或 v3.3-real-stable-freeze |

## v3.3 Template Quality Gate

| 项 | 值 |
|---|---|
| 状态 | **In progress**（本 round 进行中） |
| 起点 | 已封版的 `v3.2-real-template-documentation` @ `5a89fb2` |
| 交付物 | `scripts/template_quality_gate.py`（37 项检查：A required paths / B JSON validity / C forbidden terms / D pilot structure / E release workflow rule / F no accidental deployment signal / G summary） + `docs/TEMPLATE_QUALITY_GATE.md` |
| 范围 | 自动化质量门禁脚本 + 文档说明；不修改 `_template/`、`_pilots/`、`site/` 内容 |
| 不做的事 | 不修改 `site/index.html` / `site/style.css` / `site/script.js`，不修改 `_template/site/`，不修改 `_template/data/`，不修改 5 个手册正文，不修改 `_pilots/second-exhibition-pilot/` 内容，不创建新 pilot，不部署，不移动任何旧 tag，不修改旧 GitHub Releases |
| 下一步 | v3.3-real-stable-freeze 或 v3.4-real-second-exhibition-hardening |

## v3.4 Optional Real Second Exhibition

| 项 | 值 |
|---|---|
| 状态 | **Optional**（只有 v3.3 quality gate 验证通过后才做） |
| 起点 | v3.0 / v3.1 / v3.2 / v3.3 都封版后 |
| 交付物 | 第二个真实展览（独立项目） |
| 范围 | 全新主题、新数据、新图像、新文档流 |
| 不做的事 | 不复用 Leonardo 资产，不影响 Leonardo live |

## 不接受的 phantom 状态

本路线图**不接受**任何 phantom v3.x 历史：

- ✗ phantom `v3.0-source-rights-audit`
- ✗ phantom `v3.1-template-audit`
- ✗ phantom `v3.2-second-exhibition-pilot`
- ✗ phantom `_template/` / `_pilots/` 已创建
- ✗ phantom Issue #16 已创建并关闭
- ✗ phantom "v2.0 / v2.6 / v2.7 / v2.8 / v2.9 tags 均稳定共存"（实际 live 在 v2.9 之前只到 v2.7-zh-exhibition-polish；v2.8 / v2.9 在本 round 才真实存在）

任何 v3.x 工作必须**真实地从 verified v2.9 出发**，不能从 phantom 历史推断。

---

## 路径示意

```
v2.9-real-source-rights-audit  (verified, freeze)
    ↓
v3.0-real-template-extraction-audit  (Done — tag + Release)
    ↓
v3.1-real-second-exhibition-pilot  (Done — pilot + tag + Release, freeze 同步)
    ↓
v3.2-real-template-documentation  (Done — tag + Release)
    ↓
v3.3-template-quality-gate  (In progress — 本 round)
    ↓
v3.4+ optional real second exhibition
```

---

> 本文件由 v3.0-real-template-extraction-audit 真实创建。