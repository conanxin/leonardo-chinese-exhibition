# v3.2 Real Template Documentation

## Release identity

- **Tag**: `v3.2-real-template-documentation`
- **Live URL**: https://conanxin.github.io/leonardo-chinese-exhibition/
- **Verified live byte size**: 92,976 B
- **Source tag**: `v3.1-real-second-exhibition-pilot`
- **Documentation commit**: `2f617b1e6dc02f40683c2eb69101c4557670bbc0`
- **Freeze commit**: 本轮 freeze commit 创建后回填（annotated tag 的 target SHA）

## Status

verified template documentation（v3.2 是真实 round，不接受任何 phantom v3.2 历史作为基线）

## What changed

v3.2 Real Template Documentation 补齐可复用中文数字展览模板的使用文档。它不修改 live site，不修改 pilot，不创建新 pilot，不部署任何 pilot。

主要内容：

- 新增 `_template/USAGE_GUIDE_ZH.md`
- 新增 `_template/CONTENT_AUTHORING_GUIDE_ZH.md`
- 新增 `_template/SOURCE_RIGHTS_CHECKLIST_ZH.md`
- 新增 `_template/PILOT_WORKFLOW_ZH.md`
- 新增 `_template/RELEASE_WORKFLOW_ZH.md`
- 在 `_template/README.md` 中链接 5 个手册
- 更新 `docs/V3_TEMPLATE_ROADMAP.md`
- 更新 `README.md`
- 写入 reality recovery rule

## Documentation summary

- Manual files created: 5
- Template usage guide: yes
- Content authoring guide: yes
- Source and rights checklist: yes
- Pilot workflow: yes
- Release workflow: yes
- Reality recovery rule: `commit SHA + verified live byte + verified tag`

## Verification

- Live HTTP 200
- Live byte size: 92,976 B
- v2.9 marker: 1
- image-placeholder-pro: 0
- pilot title in live HTML: 0
- script.js: HTTP 200
- site files unchanged
- pilot unchanged
- old tags untouched
- old releases untouched

## No-touch confirmation

- live site unchanged
- pilot unchanged
- posts/ untouched
- case-study/ untouched
- release-assets existing files untouched
- old tags untouched
- old GitHub Releases untouched
- no new images
- no deployment changes

## Reality recovery rule

本 round 起，所有 release 必须满足三件套：

> 任何阶段必须有 **commit SHA** + **verified live byte** + **verified tag** 三件套；缺一项则标为 unverified。

三件套校验方法：

- commit SHA：`git rev-parse HEAD`
- verified live byte：`curl -L -s <live-url> | wc -c`
- verified tag：`git rev-parse <tag>^{}`

v3.2 当前三件套：

- commit SHA: `2f617b1e6dc02f40683c2eb69101c4557670bbc0`
- verified live byte: 92,976 B
- verified source tag: `v3.1-real-second-exhibition-pilot` → `c5e93d0f6387572e342213737ac1f7e191c2268e`

## Forbidden actions

- 不移动任何旧 tag（v2.0 / v2.6 / v2.7 / v2.8 / v2.9 / v3.0 / v3.1）
- 不覆盖任何旧 GitHub Release
- 不使用 `git add .`
- 不修改 live site
- 不修改 pilot
- 不创建新 pilot
- 不部署 pilot

## Next step

`v3.3-template-quality-gate` 或 `v3.3-real-second-exhibition-hardening`（详见 freeze report）

---

> 本 release notes 由 v3.2-real-stable-freeze 真实创建，所有 live / tag / 文件计数均来自本 round 实测。