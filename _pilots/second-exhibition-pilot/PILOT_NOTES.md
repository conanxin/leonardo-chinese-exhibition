# Pilot Notes

> 本文件记录 v3.1 second exhibition pilot 的验证笔记与模板可复用性观察。

## 跑通流程

1. 读 `_template/content.schema.json` 了解六字段结构。
2. 从 `_template/data/*.example.json` 实例化四份 pilot data。
3. 从 `_template/site/*.template.*` 实例化 pilot 站点骨架。
4. 用 `python -m json.tool` 验证四份 pilot JSON。
5. 用本地静态服务（`python3 -m http.server 8770`）+ Playwright 验证渲染。
6. 验证完成后，所有路径在 `_pilots/second-exhibition-pilot/` 下物理隔离。

## 模板组件复用性观察

### 1. JSON schema — 可直接复用 ✓

模板的 `content.schema.json` 定义了六字段顶层结构：

```
{ exhibition, sections, artifacts, glossary, sources, rightsNote }
```

pilot 完全沿用这套结构，未修改 schema，未绕过 required 字段。**模板的 schema 在 pilot 阶段已具备跨展览复用能力。**

### 2. section 模式 — 可直接复用 ✓

模板的 section 模式：

```
{ id, kicker, title, body, takeaway, viewerAction, deepReading?, materialEvidence?, visualThinking?, researchModel? }
```

pilot 4 个 section 中：
- 1 个 section（section-01）使用了全部 4 个可选模块，演示模板最大表达力。
- 3 个 section（section-02 / 03 / 04）仅使用核心 5 字段，演示最小表达力。

两种密度都被验证。**模板的 section 模式在 pilot 阶段已具备跨展览复用能力。**

### 3. artifact card 模式 — 可直接复用 ✓

模板的 artifact 模式：

```
{ id, title, image, alt, caption, sourceNote, creditLine, origin?, viewingNote? }
```

pilot 4 张 artifact 全部为 project-generated，origin = "project-generated"，sourceNote + creditLine 双字段一致。**模板的 artifact 模式在 pilot 阶段已具备跨展览复用能力。**

### 4. footer marker 模式 — 可直接复用 ✓

模板约定：每个 pilot 在 footer 打印自己的版本号（pilot-v0.1），并在 `script.js` console 输出同名 marker。

pilot footer 包含：

```html
<p class="pilot-footer-marker">pilot-v0.1 · v3.1 second exhibition pilot · 基于 _template/ · 不部署到 live</p>
```

**模板的 marker 模式在 pilot 阶段已具备跨展览复用能力。**

### 5. site 骨架（HTML / CSS / JS）— 部分复用

模板的 `_template/site/*.template.*` 提供了占位骨架。pilot 在以下方面需要人工：

- **HTML**：模板骨架是抽象的（nav placeholder / section placeholder / lightbox placeholder），需要具体展览的 sections + artifacts 填充。本 pilot 完成了填充。
- **CSS**：模板骨架有基础 reset + 卡片样式。本 pilot 在此基础上做了 hero / kicker / section / artifact card / glossary / footer 的具体样式。
- **JS**：模板骨架是占位（section nav / lightbox / guided-mode / a11y）。本 pilot 在 5 个占位函数中实现了 section nav + lightbox + a11y + console marker，把 guided-mode 留作可选。

**site 骨架的"骨架部分"可直接复用；"具体表达"需人工写作。**

## 模板还需要人工写作的部分

1. **正文 200–600 字**：schema 不能替代写作。
2. **策展视角**：4 个 section 的 kicker / title / body 都需要策展判断。
3. **术语定义**：50–200 字，不能靠模板生成。
4. **示意图**：虽然本 pilot 用项目自绘 SVG 替代了真实馆藏图，但每个展览的示意图都需要根据具体策展需求绘制。

## 已知风险

- `pilot-curator-model` 复用 `object-journey.svg` 作为占位图；正式展览中应替换为专属图。
- 替换时需同步更新 `data/assets.json` 与 `site/index.html` 的两处引用。

## 留给下一 round

- `v3.1-real-stable-freeze`：冻结 pilot，给 pilot 自身打 tag。
- 长期：跑更多 pilot（不同主题 / 不同策展视角 / 不同 source / rights 状态），验证模板的边界。
