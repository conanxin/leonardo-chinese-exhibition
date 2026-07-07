# Release Notes / 版本发布说明（模板）

> 本文件是 v3.0 中文数字展览模板的版本发布说明模板。每次 freeze 一个版本时复制一份并填入。
> 占位符：`{{TAG_NAME}}` / `{{LIVE_URL}}` / `{{BYTE_SIZE}}` / `{{AUDIT_COMMIT}}` / `{{FREEZE_COMMIT}}`

---

# {{TAG_NAME}}

## Live

`{{LIVE_URL}}`

## Tag

`{{TAG_NAME}}`

## Verified live byte size

`{{BYTE_SIZE}}` B

## Source tag

`{{SOURCE_TAG}}` @ `{{SOURCE_TAG_TARGET}}`

## Audit commit

`{{AUDIT_COMMIT}}`

## Freeze commit

`{{FREEZE_COMMIT}}`

## What changed in this version

（用 5–10 个 bullet 说明本版本相对上一版改了什么。诚实记录，包括 follow-up。）

- 新增 `{{NEW_THING_1}}`
- 新增 `{{NEW_THING_2}}`
- 修正 `{{FIX_THING}}`
- 文档更新 `{{DOC_UPDATE}}`

## What did NOT change

- 上游 tag `{{UPSTREAM_TAG_1}}` 未触碰
- 上游 tag `{{UPSTREAM_TAG_2}}` 未触碰
- 旧 GitHub Releases 未触碰
- live 站点代码 `site/index.html` / `style.css` / `script.js` 在本 round **{{SITE_TOUCHED_OR_NOT}}**

## Verification checklist

| 项 | 命令 | 实测 |
|---|---|---|
| Live byte size | `curl -s URL \| wc -c` | `{{BYTE_SIZE}}` B |
| `{{TAG_NAME}}` marker | `grep -c "{{TAG_NAME}}"` | `{{MARKER_COUNT}}` |
| `{{PHANTOM_TAG}}` marker | `grep -c "{{PHANTOM_TAG}}"` | `0` |
| `image-placeholder-pro` | `grep -c` | `0` |
| `script.js` HTTP | `curl -LIs` | HTTP 200 |
| `source-note` | `grep -c` | `{{SOURCE_NOTE_COUNT}}` |
| `credit-line` | `grep -c` | `{{CREDIT_LINE_COUNT}}` |
| `figcaption` | `grep -c` | `{{FIGCAPTION_COUNT}}` |

## No-touch confirmation

- 上游 `{{UPSTREAM_TAG_1}}` 未移动
- 上游 `{{UPSTREAM_TAG_2}}` 未移动
- 旧 GitHub Releases 未触碰
- `posts/` 未触碰（如适用）
- `case-study/` 未触碰（如适用）

## Follow-up items

- `{{FOLLOW_UP_1}}`
- `{{FOLLOW_UP_2}}`

## Known notes

（说明本版本已知的限制、未验证的假设、phantom history 等。）

---

> 本模板由 v3.0-real-template-extraction-audit 创建，来源案例 `v2.9-real-source-rights-audit`。