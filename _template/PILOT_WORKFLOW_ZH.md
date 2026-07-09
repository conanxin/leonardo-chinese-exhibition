# Pilot 工作流

本工作流说明为什么要做 pilot、pilot 应该包含什么、不应该做什么，以及如何从 pilot 走向正式展览。
本工作流基于 v3.1-real-second-exhibition-pilot 真实经验总结。

---

## 为什么先做 pilot？

在把模板用于正式展览之前，先做一个不部署的 pilot 有四个好处：

- **验证模板是否可复用**：模板是从 v2.9 抽离出来的，结构上稳定，但每个真实项目都会暴露不同的边界问题，pilot 是发现这些问题的最低成本方式
- **降低版权与内容风险**：pilot 不部署，意味着如果发现来源有疑点、权利边界不清、内容判断失误，不会污染 live 站
- **避免直接改 live**：所有模板改动都先在 pilot 验证，确认没问题才合到 main
- **暴露结构问题**：模板里的 section 顺序、artifact card 字段、glossary 术语深度，可能在真实主题下显得不够用，pilot 帮你看清结构是否真的能装下你的内容

---

## Pilot 应该包含什么？

一个最小可用的 pilot 必须包含：

- 小主题（不必是最终展览，可以是"如果做这个展览，第一段会怎么写"）
- 4 个 section
- 4 个 artifact card
- 6 个 glossary terms
- 至少 1 个 deep block
- source / rights docs
- report
- local render check

local render check 用 `python -m http.server` 在 `_pilots/<name>/site/` 启动，确认：

- 页面在浏览器里能打开
- JSON 数据能被前端正确读取
- 没有 console error

---

## Pilot 不应该做什么？

明确禁止：

- **不部署**：pilot 不进入 GitHub Pages，不影响 live URL
- **不使用未经确认图片**：pilot 用 placeholder 或已 audit 的图，不引入新的"待确认"图
- **不影响 live**：pilot 的存在不能改变 `site/` 下任何文件，不能改变任何 tag
- **不移动旧 tag**：pilot 阶段不触碰任何已有 tag 或 release
- **不假装是正式展览**：pilot 的命名、文档、报告都要明确标"pilot"，不要让它读起来像 stable release

特别注意：

- pilot 路径放在 `_pilots/<name>/`，与 `site/` 完全分离
- pilot 的 JSON 与正式展览 JSON schema 必须保持兼容，便于后续合入
- pilot 即使做得很好，也不直接合到 main，必须经过 freeze 流程

---

## 从 pilot 到正式展览

pilot 通过后，进入正式展览路径：

1. 补真实来源（替换 pilot 中的 placeholder）
2. 补权利说明（完整 source note + credit line）
3. 补图像素材（高清版本、lightbox 适配）
4. 补移动端检查（不同分辨率下的 layout）
5. 补交互检查（折叠、tab、scroll 等交互的实际效果）
6. 做 release notes（说明本次 release 与上一版的差异）
7. 做 stable freeze（按 RELEASE_WORKFLOW_ZH.md 的流程封版）

每一步都要留 commit 与验证记录。

---

## v3.1 pilot 经验

基于 `_pilots/second-exhibition-pilot/` 的真实经验：

### 哪些模板结构可直接复用

- `data/*.json` 的字段结构可以直接套用，section / artifact / glossary / asset 的字段命名稳定
- `site/` 下三文件结构（HTML / CSS / JS）足以承载一个完整展览
- `_template/USAGE_GUIDE_ZH.md` 等五份文档提供的写作边界是可执行的

### 哪些地方需要人工写作

- exhibition 的 hero / lede 必须人工写，无法模板化
- artifact 的 viewing note 需要人工判断（这张图值得观众看哪里）
- deep block 的内容选择是策展判断，不是结构能决定的
- glossary 的 why_care 字段尤其需要人工写，因为这是"为什么要学这个术语"的判断

### 哪些字段需要更严格

- `assets.example.json` 的 license 字段需要明确为枚举（pd / cc0 / cc-by / research-only / institutional），不允许空字符串
- `sections.example.json` 的 viewer_action 不允许为空字符串或"无"
- `glossary.example.json` 的 why_care 不允许少于 30 字

### 为什么 pilot 应保持不部署

- v3.1 pilot 的内容是"一件作品的旅程"（虚构示意），如果误部署会污染 live 站的展览主题
- pilot 阶段的来源 / 权利验证是低密度的，不能直接用于正式展览
- pilot 的命名、目录结构、报告格式都还在演进，部署会让外部读者误以为是稳定版本

---

## 复盘 checklist

每次做完一个 pilot，回答以下问题：

- 模板结构是否需要调整？
- 哪些字段暴露了边界不足？
- pilot 是否触犯了禁止事项？
- pilot 的报告是否记录了所有 placeholder 与已知疑点？
- pilot 是否被误部署？（如果误部署，立刻回滚）