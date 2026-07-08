# Pilot · Rights and Sources

> 本文件为 v3.1 second exhibition pilot 的权利与来源综述。
> 范围：`_pilots/second-exhibition-pilot/` 全部内容。

## 权利综述

本 pilot 的全部示意图、文字、术语定义均为项目自绘 / 自写，不引用任何第三方版权材料。

- **示意图（SVG）**：项目自绘，CC0 1.0 授权。
- **正文文字**：作者撰写，可被复用、修改、引用（建议注明出处：v3.1 second exhibition pilot）。
- **术语定义**：作者撰写，可被复用、修改、引用。
- **站点骨架（HTML / CSS / JS）**：基于 `_template/site/*.template.*` 实例化，作者撰写，可被复用、修改、引用。

## 权利边界

- pilot 本身**不部署**到 live；其权利边界由作者自行声明。
- 任何复用 pilot 内容（包括示意图、文字、站点骨架）的下游项目应：
  1. 在 README / footer 注明「基于 v3.1 second exhibition pilot」；
  2. 保留 sourceNote + creditLine 双字段约定；
  3. 不删除或修改 footer 中的 pilot-v0.1 marker。

## 来源策略

| 类别 | 策略 |
|---|---|
| 真实馆藏图 | **不引用**（本 pilot 不使用） |
| 机构截图 | **不引用**（本 pilot 不使用） |
| 自制示意图 | **使用**（项目自绘，CC0 1.0） |
| 自写文字 | **使用**（作者撰写） |

## 复用许可

- 复用建议：CC0 1.0（与示意图一致）。
- 强制要求：保留 sourceNote + creditLine + pilot-v0.1 marker。

## 与 live site 的关系

- live site（v2.9）的权利政策不影响本 pilot；pilot 的权利政策不影响 live site。
- 二者共享 `_template/`，但 pilot 是 template 的下游实例，不影响 template 本身。

## 已知风险

- pilot 阶段以 `object-journey.svg` 充当 `pilot-curator-model` 的占位图，正式展览中应替换为专属图。
- 替换时需更新 `data/assets.json` 与 `site/index.html` 的两处引用。
