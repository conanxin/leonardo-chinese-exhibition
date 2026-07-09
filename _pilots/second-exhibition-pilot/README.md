# _pilots/second-exhibition-pilot/

> v3.1 second exhibition pilot — 基于真实 `_template/` 创建的第一个 second pilot。

## 这是什么

这是本仓库的 **v3.1 second exhibition pilot**（所属项目：leonardo-chinese-exhibition）。

- **主题**：《一件作品的旅程》— 从图像、来源、路径到知识网络
- **目标**：验证中文数字展览模板能否独立组织一个小型研究型展览
- **版本**：pilot-v0.1
- **状态**：repository only（**不部署**到 live）

## 起点

- 源模板：`_template/`（`v3.0-real-template-extraction-audit` @ `dd7d589`）
- live site：v2.9 封版 + v3.0 提取审计，92,976 B 不变
- 本 pilot 不修改 `_template/`，不修改 live，不创建 tag / Release

## 目录结构

```
_pilots/second-exhibition-pilot/
├── README.md                 # 本文件
├── PILOT_MANIFEST.md         # pilot 文件清单
├── PILOT_NOTES.md            # pilot 验证笔记
├── data/
│   ├── exhibition.json       # 展览元数据
│   ├── sections.json         # 4 个 section
│   ├── glossary.json         # 6 个术语
│   └── assets.json           # 4 张示意图 + 1 个 favicon
├── site/
│   ├── index.html            # pilot 站点
│   ├── style.css             # pilot 样式
│   └── script.js             # pilot 脚本（占位）
├── docs/
│   ├── SOURCE_AUDIT_MANIFEST.md
│   ├── RIGHTS_AND_SOURCES.md
│   ├── CURATORIAL_ESSAY_ZH.md
│   ├── DEEP_RESEARCH_NOTES_ZH.md
│   └── RELEASE_NOTES_PILOT.md
└── assets/
    └── diagrams/
        ├── object-journey.svg
        ├── evidence-chain.svg
        └── viewing-map.svg
```

## 不做的事

- 不修改 `site/index.html` / `style.css` / `script.js`
- 不修改 `_template/` 任何文件
- 不创建 tag / GitHub Release
- 不引用任何真实馆藏图
- 不创建第三个 pilot

## 与 live site 的关系

- live site 保持 v2.9 封版 + v3.0 提取审计
- pilot 与 live 共享 `_template/`，但 pilot 是 template 的下游实例
- pilot 的所有路径都在 `_pilots/second-exhibition-pilot/` 下，物理隔离

## 模板可复用性（pilot 内部观察）

跑完这一轮 pilot 后：

**模板真正能复用的部分**

1. JSON schema（`exhibition / sections / artifacts / glossary / sources / rightsNote`）
2. section 模式（`id / kicker / title / body / takeaway / viewerAction` + 4 个可选模块）
3. artifact card 模式（`id / title / image / alt / caption / sourceNote / creditLine / origin`）
4. footer marker 模式（pilot-v0.1）

**模板还需要人工写作的部分**

- 正文（200–600 字）
- 策展视角（4 个 section 的 kicker / title / body）
- 术语定义（50–200 字）

详见 [`PILOT_NOTES.md`](PILOT_NOTES.md)。

## 下一 round

**v3.1-real-stable-freeze**：冻结 pilot，给 pilot 自身打 tag。

---

## Hardening notes

pilot 已经过 v3.4 hardening：

- [`PILOT_QA_CHECKLIST.md`](PILOT_QA_CHECKLIST.md) — pilot QA 检查清单（identity / structural / data / rights / render / deployment）
- [`PILOT_HANDOFF.md`](PILOT_HANDOFF.md) — pilot 交接指南（what this pilot proves / does not prove / if turning into real exhibition / safe reuse）
- [`docs/PILOT_QA_REPORT.md`](docs/PILOT_QA_REPORT.md) — 最近一次 QA 报告（v3.4 round Playwright 实测）

状态：

- pilot 已经过 v3.4 hardening
- repository only
- not deployed
- future formalization needs source audit and release workflow
