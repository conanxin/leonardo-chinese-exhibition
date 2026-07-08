# 一件作品的旅程 · 策展人随笔

> 本文件为 v3.1 second exhibition pilot 的策展人随笔中文版。
> 用途：演示模板随笔模块；不参与 live。

## 起点

为什么这场 pilot 选择「一件作品的旅程」？

不是因为某件作品值得被讲，而是因为「单件作品」这个研究单位最容易暴露一个展览的薄弱之处。

一场时代叙事展可以靠宏观叙述撑起来；一件作品展不行。它必须把每条材料、每个流转节点、每段研究者的工作都讲清楚，否则就只剩一张图。pilot 是模板的试金石：它用 4 个 section 把「材料 → 流转 → 阅读 → 展示」走一遍，看看模板骨架在最小规模下是否还能撑住。

## 四个 section 不是四张图

很多展览把 section 当成「图片分组」。本 pilot 不这样。

- **起点**回答的是「为什么从一件作品开始」——是策展判断，不是内容陈列。
- **流转**回答的是「它在世间走过哪些节点」——是源出处链的展开。
- **阅读**回答的是「研究者如何对待它」——是方法论的最小自述。
- **展示**回答的是「它如何被放在观众面前」——是观展体验的最后一公里。

四个 section 因此与「材料 → 流转 → 阅读 → 展示」四步模型一一对应。

## 为什么不引用真实馆藏图

pilot 的所有示意图都是项目自绘。这是有意识的克制。

- 真实馆藏图会立刻把 pilot 拖入「源出处、权利、授权、再使用」一整套问题；
- 这些问题值得单独开轮（v3.2 / 后续）讨论，不应与「模板能否独立跑起来」混在一起；
- 自制示意图让 pilot 聚焦在模板的组件复用性，而不是具体作品。

## 模板真正能复用的部分

跑完这一轮 pilot 后，模板最确定能复用的部分：

1. **JSON schema** — `exhibition / sections / artifacts / glossary / sources / rightsNote` 六字段结构稳定。
2. **section 模式** — `id / kicker / title / body / takeaway / viewerAction` + 四个可选模块（deepReading / materialEvidence / visualThinking / researchModel）。
3. **artifact card 模式** — `id / title / image / alt / caption / sourceNote / creditLine / origin` 八字段结构稳定。
4. **footer marker 模式** — 每个 pilot 在 footer 打印自己的版本号（pilot-v0.1），便于审计。

模板还需要人工写作的部分：

- **正文（200–600 字）** — schema 不能替代写作。
- **策展视角** — 4 个 section 的 kicker / title / body 都需要策展判断。
- **术语定义** — 50–200 字，不能靠模板生成。

## 接下来

- 跑通 pilot 后，下一步是 v3.1-real-stable-freeze：冻结 pilot，给 pilot 自身打 tag。
- 长期看，pilot 演示了模板可以独立组织一个小型研究型展览；下一个 pilot 可以尝试不同主题。
