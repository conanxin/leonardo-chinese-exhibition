# Source Manifest / 来源清单（模板）

> 本文件是 v3.0 中文数字展览模板的来源清单模板。复制到正式项目后，按以下表格填入真实来源。
> 占位符：`{{TAG_NAME}}` / `{{LIVE_URL}}` / `{{BYTE_SIZE}}` / `{{AUDIT_COMMIT}}` / `{{FREEZE_COMMIT}}`

## 展览元数据

| 字段 | 值 |
|---|---|
| 展览版本 | `{{TAG_NAME}}` |
| Live URL | `{{LIVE_URL}}` |
| Verified live byte size | `{{BYTE_SIZE}}` B |
| 审计 commit | `{{AUDIT_COMMIT}}` |
| 封版 commit | `{{FREEZE_COMMIT}}` |

## 资产总览

| 类别 | 数量 | 备注 |
|---|---|---|
| Collection / manuscript（馆藏/手稿） | {{COLLECTION_COUNT}} | 来自原作机构 |
| Platform screenshots（平台截图） | {{SCREENSHOT_COUNT}} | 引用自第三方平台 |
| Self-made SVG / project-generated（自制） | {{SVG_COUNT}} | 项目自绘 |
| Metadata assets（favicon / og-cover） | {{METADATA_COUNT}} | 站点自身 |

## 资产详细登记

每张图 / 截图 / SVG 都登记一行：

| ID | 标题 | 来源 | URL / 路径 | 类别 | 复用许可 | 访问日期 | 备注 |
|---|---|---|---|---|---|---|---|
| `{{ASSET_ID}}` | `{{ASSET_TITLE}}` | `{{ASSET_ORIGIN_INSTITUTION}}` | `{{ASSET_URL}}` | `{{ASSET_ORIGIN}}` | `{{ASSET_REUSE}}` | `{{ASSET_ACCESSED_AT}}` | `{{ASSET_NOTE}}` |

### 复用许可取值建议

- `official-open-license`：原作机构明确开放（如 CC0 / CC-BY）
- `official-restricted`：原作机构有限制（如仅评论 / 研究 / 教育）
- `platform-screenshot`：第三方平台截图，仅用于说明平台
- `project-generated`：项目自绘
- `unclear`：尚未确认

如果 `unclear`，**该项目不应该进入封版**。

## 平台截图专列

| 截图 | 来源 URL | 截图日期 | 模块说明 | 是否用于说明 |
|---|---|---|---|---|
| `{{SCREENSHOT_TITLE}}` | `{{SCREENSHOT_URL}}` | `{{SCREENSHOT_DATE}}` | `{{SCREENSHOT_MODULE}}` | 是 |

## 自制图解专列

| 自制图 | 依据 | 是否冒充原始资料 | 许可证 |
|---|---|---|---|
| `{{DIAGRAM_TITLE}}` | `{{DIAGRAM_BASIS}}` | 否 | `{{DIAGRAM_LICENSE}}` |

## 引用文献 / 网页

| 标题 | URL | 访问日期 | 用途 |
|---|---|---|---|
| `{{REF_TITLE}}` | `{{REF_URL}}` | `{{REF_ACCESSED_AT}}` | `{{REF_USAGE}}` |

## Follow-up items

- 联系 {{INSTITUTION_NAME}} 取得明确复用许可
- 确认 {{PLATFORM_NAME}} 截图的引用边界
- 决定自制 SVG 的统一 LICENSE（推荐 CC0 1.0 或 CC-BY 4.0）
- 重新审计任何新增 / 替换的资产

---

> 本模板由 v3.0-real-template-extraction-audit 创建，来源案例 `v2.9-real-source-rights-audit`。