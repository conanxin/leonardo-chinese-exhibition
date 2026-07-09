# 发布与封版工作流

本工作流定义从一次内容更新到稳定 release 的完整流程。
本工作流基于 v2.0 → v3.1 的真实 release 经验，包含多次踩坑教训，特别是 v3 之前的 phantom-success 教训。

---

## 推荐版本阶段

每个有意义的版本应经过以下阶段：

1. **content build**：内容构建与数据填充
2. **polish**：文案打磨、术语统一、视觉微调
3. **source audit**：来源与权利核验（必须经过完整 checklist）
4. **template extraction**（可选）：如果本版本沉淀了可复用结构，抽出为模板
5. **pilot**（可选）：如果本版本是新主题或新结构，先做不部署的 pilot
6. **stable freeze**：封版（写入 release notes / manifest / freeze report）
7. **GitHub Release**：打 tag + 写 release notes
8. **post-release maintenance**：发布后维护（部署验证、链接修复、内容更新）

不是每个版本都要走完所有阶段。最低要求是 stable freeze + GitHub Release。

---

## 每个版本必须记录

每个 release 必须有以下记录，缺一项视为不完整：

- **commit**：本次 release 封版的 commit SHA
- **tag**：tag 名称
- **tag target commit**：tag 指向的具体 commit（必须是 freeze commit，不能是中间 commit）
- **live byte size**：发布后 live 页面的字节数（实测值，不是估算值）
- **live marker**：live 页面中可以 grep 出的版本标记字符串
- **Playwright check**（如果适用）：自动化渲染检查结果
- **placeholder count**：未替换的 placeholder 数量（应为 0）
- **source-note / credit-line count**：来源与权利核验计数（应与上一 release 对比一致或增加）
- **no-touch confirmation**：旧 tag、旧 release、live 站未被本 release 修改

任何一项缺失，禁止宣告 PASS。

---

## 禁止事项

明确禁止：

- **不移动旧 tag**：tag 一旦创建，永远指向当时的 freeze commit
- **不覆盖旧 release**：每个 release 在 GitHub 上是历史记录，不可重新发布覆盖
- **不在未验证 live 时宣布 PASS**：必须 live URL 抓取验证通过
- **不用 `git add .`**：必须显式 add 需要提交的文件，避免 untracked 内容误入 commit
- **不把 draft / pilot 当 stable**：pilot 必须有独立命名与独立目录
- **不把 phantom memory 当真实起点**：v3 之前的教训——不要在没有 commit / 没有 live 验证的情况下宣布 PASS

特别注意：

- 不要在没有 freeze 的情况下部署
- 不要在没有 tag 的情况下发布
- 不要在没有 release notes 的情况下打 tag
- 不要在没有 source audit 的情况下增加新图

---

## Stable freeze checklist

每次 stable freeze 之前：

- [ ] release notes（说明本次 release 的内容、变化、限制）
- [ ] manifest（结构化清单：commit / tag / live byte / marker）
- [ ] freeze report（详细报告，含过程与回滚说明）
- [ ] annotated tag（`git tag -a` 写明 freeze commit + 简述）
- [ ] GitHub Release（push tag 后到 GitHub 上写 release notes）
- [ ] live verification（push 后 live URL 抓取验证）
- [ ] no-touch verification（确认旧 tag、旧 release、旧 live 未变）

### 标准的 2-commit freeze 模式

本项目从 v3.0 开始采用 2-commit freeze 模式：

1. **第一次 commit**：freeze 本体（写入 release notes / manifest / freeze report，但 commit SHA 字段先留空或用占位符）
2. **第二次 commit**：backfill commit SHA（用 `git rev-parse HEAD~0` 或类似方式回填上一次 commit 的 SHA）

这样做的原因是：freeze 报告需要写明"freeze commit = HEAD"，但写报告时 HEAD 还没确定，所以先 freeze 再 backfill。

如果项目不采用这个模式，也可以：

- 在 freeze 前预留 commit SHA 字段，freeze 时 `git commit --amend` 写入
- 或在 freeze 后另起一个 backfill commit

---

## Reality recovery rule

本项目最重要的硬规则。

> **任何阶段必须有 commit SHA + verified live byte + verified tag 三件套；缺一项则标为 unverified。**

具体含义：

- **commit SHA**：本次变更的 git commit 标识
- **verified live byte**：发布后从 live URL 实际抓取的字节数
- **verified tag**：tag 的 object SHA 与 target SHA 都通过 `git rev-parse` 验证

缺少任意一项，相关报告与 memory 必须标记为 unverified，禁止作为下一阶段的起点。

### 为什么需要这条规则

v3 之前发生过 phantom-success 教训：

- 报告写"已 freeze v2.7"，但 `git reflog` 是空的
- 报告写"已 deploy"，但 live URL 没动
- 报告写"`git fetch` 完成"，但 `git fetch` 从未真正运行

这些教训导致后续 round 需要做 phantom recovery，反而消耗更多时间。

### 如何应用这条规则

- 每次完成 freeze，必须在 24 小时内独立校验三件套
- 校验方法：`git rev-parse HEAD` + `curl -L -s <live-url> | wc -c` + `git rev-parse <tag>^{}`
- 如果校验失败，立刻标 unverified，不要把报告向上游传递
- 在 README / reports / memory 中，unverified 状态必须可见

---

## 发布后维护

发布后维护包括但不限于：

- 部署验证（Pages 是否真的更新）
- 链接修复（外部链接失效后如何补救）
- 内容更新（错误修正、补充说明）
- 旧 release 链接维护（确保旧 release 在 GitHub 上仍可访问）

每次维护都要经过完整的 stable freeze 流程，不能"小改直接部署"。

---

## 复盘 checklist

每次发布后，回答以下问题：

- 三件套（commit SHA + live byte + tag）是否都校验？
- 旧 tag 是否未动？
- 旧 release 是否未动？
- live 站是否在 freeze 后才更新？
- release notes 是否写明权利边界？
- 报告是否记录了 unverified 项？