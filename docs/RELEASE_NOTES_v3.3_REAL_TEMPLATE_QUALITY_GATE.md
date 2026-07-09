# v3.3 Real Template Quality Gate

## Release identity

- **Tag**: `v3.3-real-template-quality-gate`
- **Live URL**: https://conanxin.github.io/leonardo-chinese-exhibition/
- **Verified live byte size**: 92,976 B
- **Source tag**: `v3.2-real-template-documentation`
- **Quality gate commit**: `497045aa1a3408bd462da0f174a4ef46eb30484f`
- **Freeze commit**: 本轮 freeze commit 创建后回填（annotated tag 的 target SHA）

## Status

verified template quality gate（v3.3 是真实 round，不接受任何 phantom v3.3 历史作为基线）

## What changed

v3.3 Real Template Quality Gate 建立了中文数字展览模板的可重复质量门禁。它不修改 live site，不修改 pilot，不修改 `_template/site/` 或 `_template/data/`。

主要内容：

- 新增 `scripts/template_quality_gate.py`
- 新增 `docs/TEMPLATE_QUALITY_GATE.md`
- 更新 `docs/V3_TEMPLATE_ROADMAP.md`
- 更新 `README.md`
- 生成 v3.3 quality gate report
- quality gate 37/37 checks pass

## Quality gate coverage

- Required paths: 10 checks
- JSON validation: 9 checks
- Forbidden terms in default template content: 4 checks
- Pilot structure: 7 checks
- Release workflow rule: 4 checks
- No accidental deployment signal: 3 checks
- Total: 37 checks

## Verification

- Quality gate: PASS, 37/37, exit code 0
- Live HTTP 200
- Live byte size: 92,976 B
- v2.9 marker: 1
- image-placeholder-pro: 0
- pilot title in live HTML: 0
- script.js: HTTP 200
- site unchanged
- pilot unchanged
- _template/site unchanged
- _template/data unchanged

## No-touch confirmation

- live site unchanged
- pilot unchanged
- _template/site unchanged
- _template/data unchanged
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

v3.3 当前三件套（提交后回填）：

- commit SHA: `497045aa1a3408bd462da0f174a4ef46eb30484f`（quality gate commit）
- verified live byte: 92,976 B
- verified source tag: `v3.2-real-template-documentation` → `5a89fb2061ef3eee95c63dc3592d92fb859177fe`

## Quality gate reusability

`scripts/template_quality_gate.py` 可在以下场景重跑：

- 修改 `_template/` 后
- 修改 `_pilots/` 后
- 准备 release freeze 前
- 新增图片 / 截图 / SVG 前后
- 发现 memory 与 git 状态不一致时

运行命令：

```bash
python3 scripts/template_quality_gate.py
```

exit code：`0` = PASS / `1` = FAIL。

## Forbidden actions

- 不移动任何旧 tag（v2.0 / v2.6 / v2.7 / v2.8 / v2.9 / v3.0 / v3.1 / v3.2）
- 不覆盖任何旧 GitHub Release
- 不使用 `git add .`
- 不修改 live site
- 不修改 pilot
- 不修改 `_template/site/` 或 `_template/data/`
- 不修改 scripts/template_quality_gate.py（除非 reality gate 发现脚本不能运行）

## Next step

`v3.4-real-second-exhibition-hardening`（详见 freeze report）

候选方向：

- 把 quality gate 接入 CI（GitHub Actions step）
- 给 quality gate 加 strict mode（fail on warning）
- 给 quality gate 加 JSON / Markdown 输出便于审计
- 用 quality gate 验证 `_template/data/` 的第二个 example 主题

---

> 本 release notes 由 v3.3-real-stable-freeze 真实创建，所有 live / tag / 文件计数均来自本 round 实测。