# Stable Freeze Report / 封版报告（模板）

> 本文件是 v3.0 中文数字展览模板的封版报告模板。每次 freeze 一个版本时复制一份并填入。
> 占位符：`{{TAG_NAME}}` / `{{TAG_OBJECT}}` / `{{TAG_TARGET}}` / `{{LIVE_URL}}` / `{{BYTE_SIZE}}` / `{{AUDIT_COMMIT}}` / `{{FREEZE_COMMIT}}` / `{{SOURCE_TAG}}`

---

## STATUS: PASS / PARTIAL

## Baseline

- HEAD before freeze: `{{HEAD_BEFORE}}`
- origin/main before freeze: `{{ORIGIN_MAIN_BEFORE}}`
- Working tree: clean（允许 untracked `{{UNTRACKED_OK}}`）

## Source tag

- `{{SOURCE_TAG}}` @ `{{SOURCE_TAG_TARGET}}`
- 起点：审计 / 内容 / 上一 freeze round 留下的 verified 状态

## Live verification before freeze

| 项 | 命令 | 实测 |
|---|---|---|
| Live URL | curl | `{{LIVE_URL}}` |
| Live byte size | `wc -c` | `{{BYTE_SIZE}}` B |
| `{{SOURCE_TAG}}` marker | `grep -c` | `{{SOURCE_MARKER_COUNT}}` |
| `{{PHANTOM_TAG}}` marker | `grep -c` | `0` |
| `image-placeholder-pro` | `grep -c` | `0` |
| `source-note` | `grep -c` | `{{SOURCE_NOTE_COUNT}}` |
| `credit-line` | `grep -c` | `{{CREDIT_LINE_COUNT}}` |
| `script.js` HTTP | `curl -LIs` | HTTP 200 |

## Release artifacts created

- `docs/RELEASE_NOTES_{{TAG_NAME_UPPER}}.md`
- `release-assets/{{TAG_NAME}}-manifest.md`
- `reports/{{REPORT_FILE_NAME}}.md`

## Freeze commit

`{{FREEZE_COMMIT}}`

## Tag creation

- Tag name: `{{TAG_NAME}}`
- Tag object SHA: `{{TAG_OBJECT}}`
- Tag target commit: `{{TAG_TARGET}}`
- Tag type: annotated
- Tag annotation: `{{TAG_ANNOTATION}}`
- `git ls-remote --tags origin` 中可见：✓ / ✗

## GitHub Release

- URL: `{{RELEASE_URL}}`
- Title: `{{RELEASE_TITLE}}`
- Published: `{{RELEASE_PUBLISHED_AT}}`
- Notes file: `{{NOTES_FILE_PATH}}`
- 是否 latest：✓ / ✗

## GitHub Actions

- Run ID: `{{ACTIONS_RUN_ID}}`
- Status: success / failure
- Workflow: Deploy GitHub Pages
- Duration: `{{ACTIONS_DURATION}}`

## Asset audit summary

| Category | Count |
|---|---|
| Collection / manuscript | `{{COLLECTION_COUNT}}` |
| Platform screenshots | `{{SCREENSHOT_COUNT}}` |
| Self-made SVG / project-generated | `{{SVG_COUNT}}` |
| Metadata assets | `{{METADATA_COUNT}}` |
| **Total** | `{{TOTAL_COUNT}}` |

## No-touch confirmation

- `site/index.html` untouched in freeze round
- `site/style.css` untouched in freeze round
- `site/script.js` untouched in freeze round
- `posts/` untouched
- `case-study/` untouched
- `release-assets/` 既有文件 untouched（除新增 manifest）
- `{{UPSTREAM_TAG_1}}` untouched
- `{{UPSTREAM_TAG_2}}` untouched
- 旧 GitHub Releases untouched
- `git add .` 未使用

## Follow-up items

- `{{FOLLOW_UP_1}}`
- `{{FOLLOW_UP_2}}`

## Next recommended task

`{{NEXT_TASK_NAME}}`：基于本 freeze 的 tag `{{TAG_NAME}}` 做下一 round。

---

> 本模板由 v3.0-real-template-extraction-audit 创建，来源案例 `v2.9-real-source-rights-audit`。