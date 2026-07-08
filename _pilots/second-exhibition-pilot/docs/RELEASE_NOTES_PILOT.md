# v3.1 Second Exhibition Pilot · Release Notes (Pilot)

> 本文件为 v3.1 second exhibition pilot 的 release notes（pilot 内部）。
> 注意：pilot 不发布 GitHub Release；本文件仅作为 pilot 内部的审计凭证。

## 标识

- **Pilot 名称**：《一件作品的旅程》
- **Pilot 版本**：pilot-v0.1
- **所属项目**：leonardo-chinese-exhibition v3.1
- **源模板**：`_template/`（`v3.0-real-template-extraction-audit` @ `dd7d589`）
- **部署状态**：**不部署**（repository only）
- **Live 影响**：**无**（live site 92,976 B 不变）

## 范围

- 创建 `_pilots/second-exhibition-pilot/` 目录
- 4 个 section：起点 / 流转 / 阅读 / 展示
- 4 张自制示意图：object-journey / evidence-chain / viewing-map / curator-model（占位）
- 6 个术语：单件作品研究 / 流转链 / 源出处 / 权利边界 / 自制示意图 / pilot
- 5 个 docs：SOURCE_AUDIT / RIGHTS_AND_SOURCES / CURATORIAL_ESSAY / DEEP_RESEARCH_NOTES / RELEASE_NOTES
- 3 个 README / manifest / notes：README / PILOT_MANIFEST / PILOT_NOTES

## 不做的事

- 不修改 `site/index.html` / `site/style.css` / `site/script.js`
- 不修改 `_template/` 任何文件
- 不创建 tag / GitHub Release
- 不引用真实馆藏图
- 不创建第三个 pilot

## 验证（pilot 内部）

- JSON validation 4/4 pass
- 4 个 section + 4 张 artifact card + 6 个 glossary + 4 类 block（deep / evidence / thinking / model）均存在
- forbidden terms = 0（Leonardo / Codex Atlanticus / Royal Collection Trust / `thek@`）
- local render check：page title 包含「一件作品的旅程」、artifact cards ≥ 4、glossary items ≥ 6、console errors = 0、mobile 390 no overflow

## 与 live site 的关系

- live site（v2.9 封版 + v3.0 模板提取）完全未受影响
- pilot 与 live 共享 `_template/`，但 pilot 是 template 的下游实例
- pilot 的所有路径（图片 / JSON / 站点）都在 `_pilots/second-exhibition-pilot/` 下，物理隔离

## 已知风险

- `pilot-curator-model` 复用 `object-journey.svg` 作为占位图；正式展览中应替换为专属图。
- 替换时需同步更新 `data/assets.json` 与 `site/index.html` 的两处引用。

## 移交

- 下一 round：`v3.1-real-stable-freeze`（冻结 pilot，给 pilot 自身打 tag）
- 不在 pilot 范围：源出处 / 权利 / 授权细节；具体作品；i18n；服务端
