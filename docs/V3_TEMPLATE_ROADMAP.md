# V3 Template Roadmap / v3 模板路线图

> 本文件记录从 v2.9-real-source-rights-audit 出发的 v3.x 路线图。
> 起点：v2.9-real-source-rights-audit 已封版（live 92,976 B）
> phantom v3.x 历史（v3.0-source-rights-audit / v3.1-template-audit / v3.2-second-exhibition-pilot 等）**不**作为基线。

## v3.0 Real Template Extraction Audit

| 项 | 值 |
|---|---|
| 状态 | **In progress**（本 round 进行中） |
| 起点 | v2.9-real-source-rights-audit @ a1e667e |
| 交付物 | `_template/` 真实创建（18 文件） |
| 范围 | docs/TEMPLATE_EXTRACTION_AUDIT.md + docs/REUSABLE_EXHIBITION_COMPONENTS.md + _template/ |
| 不做的事 | 不创建 `_pilots/`，不部署模板，不创建 tag / release |
| 下一步 | v3.0-real-stable-freeze（独立 freeze round） |

## v3.0 Real Stable Freeze

| 项 | 值 |
|---|---|
| 状态 | **Next** |
| 起点 | 本 round 创建的 `_template/` HEAD |
| 交付物 | 创建 `v3.0-real-template-extraction-audit` tag + GitHub Release |
| 范围 | 冻结 `_template/` 骨架 + docs/ + reports/ |
| 不做的事 | 不创建 `_pilots/`，不修改 live，部署影响限于 pages source 上传新文件 |
| 下一步 | v3.1 Second Exhibition Pilot |

## v3.1 Second Exhibition Pilot

| 项 | 值 |
|---|---|
| 状态 | **Planned** |
| 起点 | 已封版的 v3.0 tag |
| 交付物 | `_pilots/second-exhibition-pilot/` |
| 范围 | 小主题 + 自制 SVG + 4 section + 4 artifact + 6 glossary + source / rights docs + report |
| 不做的事 | 不部署到 GitHub Pages，不引入真实馆藏图片，不修改旧 tag |
| 下一步 | v3.2 Template Documentation |

## v3.2 Template Documentation

| 项 | 值 |
|---|---|
| 状态 | **Planned** |
| 起点 | v3.0 tag + v3.1 pilot |
| 交付物 | 完整使用手册（usage / authoring / rights checklist / pilot workflow / release workflow） |
| 范围 | `_template/USAGE_GUIDE_ZH.md` + `CONTENT_AUTHORING_GUIDE_ZH.md` + `SOURCE_RIGHTS_CHECKLIST_ZH.md` + `PILOT_WORKFLOW_ZH.md` + `RELEASE_WORKFLOW_ZH.md` |
| 不做的事 | 不修改 live，不部署 |
| 下一步 | v3.3+ Optional Real Second Exhibition |

## v3.3 Optional Real Second Exhibition

| 项 | 值 |
|---|---|
| 状态 | **Optional**（只有 v3.1 pilot 验证模板真正可复用后才做） |
| 起点 | v3.0 / v3.1 / v3.2 都封版后 |
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
v3.0-real-template-extraction-audit  (本 round) ──→ v3.0-real-stable-freeze
    ↓                                                ↓
v3.1-second-exhibition-pilot                       v3.1 → v3.2
    ↓                                                ↓
v3.2-template-documentation                   v3.3+ optional
    ↓
v3.3 optional real second exhibition
```

---

> 本文件由 v3.0-real-template-extraction-audit 真实创建。