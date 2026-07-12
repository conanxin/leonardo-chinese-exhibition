# 策展短文 / Curatorial Essay

> 本文是《植物图谱与视觉分类》展览的中文策展短文，面向第一次访问者。它不替代实物观察，也不替代机构元数据本身；它的作用是为观众提供一个可以把 6 件资产放进去的坐标系。
>
> 全文约 2400 中文字，按四个分节（观察 / 分类 / 复制 / 再组织）展开。
> 全文明确区分三类陈述：**事实**（来自机构元数据 / 引用源）、**策展假设**（本页内的解释）、**可研究方向**（参见 DEEP_RESEARCH_NOTES_ZH.md）。

---

## 一句话总结

自然史图像的生命周期由四个动作组成：观察、分类、复制、再组织。这四个动作决定了一张植物图谱能不能、怎样、以何种权威被后人看见。

## 第一节：观察——一种保留什么、舍弃什么的判断

十八、十九世纪之交的水彩植物图谱看起来"客观"，但每一幅画都是一系列取舍的结果：花要画多大、叶脉要不要画出阴影、果实是否写实、背景留不留白。本展览选择的第一件资产 C-01 来自 Biodiversity Heritage Library（BHL）馆藏的《Album of watercolors of Asian fruits and flowers》第 603998 页（Pistillaria plate），parent item 为 BHL item 318921，介乎 1798—1850 年之间，作者佚名。

当我们把这张图谱放在屏幕上放大，它能给出颜色与笔触的细节；但当我们把它缩到一页之中，它只能给出"这是某种 Pistillaria"的视觉印象。换句话说，水彩植物图谱保留的不仅是植物本身，还有一段"在某一刻、某一种灯光下、某一位观察者愿意投入多少时间"的事实。

**策展假设**：观察从来不是中性的视觉采集，它是一组关于"哪些信息值得保留"的判断。这组判断本身就是图像的一部分。

## 第二节：分类——图像如何获得位置

分类学让一张图谱有了位置：它对应哪个属、哪个种、哪一段采集信息、哪一份机构记录。本展览用两件跨机构的资产做对照样本：

- **C-06**：Smithsonian National Museum of Natural History / NMNH Botany 馆藏的 US Catalog 1529703，标识为 *Aconitum bulbilliferum* Hand.-Mazz.（毛茛科，Type fragment），采集人 Handel-Mazzetti, H. R.，日期 1914 年 9 月 17 日。该资产由 Smithsonian Open Access / CC0 1.0 数据级授权。**重要**：本资产当前可获得的图像仅为 NMNH `/media/?i=1529703&ph=yes&thumb=yes` 端点直接返回的 90×90 PNG 缩略图。它的作用是"机构元数据与命名秩序的对照点"，而非视觉证据。
- **C-08**：The Metropolitan Museum of Art 馆藏 object 285149 / accession 2003.562.3，标题 *[Botanical Specimen: Fern]*，年代 1855–60，作者佚名。Met Collection API 返回 `isPublicDomain: true`，且公开页面显示了 Public Domain 指示——即"double-confirmation PASS"。

把这两件资产并排阅读，可以看到机构政策如何影响图像的命运：Smithsonian 提供"数据集级 CC0 1.0"，但当前公开端点只给出 90×90 缩略图；Met 提供更完整的 JPEG（web-large 派生 449×624），并且在公开页面就标明了 Public Domain。两家机构在"开放"这件事上的差异，并不是关于版权的法律差异，而是关于图像服务基础设施的工程差异。

**策展假设**：分类秩序的可靠性来自元数据层与图像层的同时开放。当其中一层缺失，分类秩序在视觉传播上就会失稳——这正是 C-06 当前的状态。

## 第三节：复制——技术决定传播半径

植物图谱的命运在很大程度上由"复制技术"决定：手稿只能在书房里被翻阅，雕版与石印可以让它走出本土，照相制版（photomechanical reproduction）可以让它进入百科全书，扫描与 IIIF 可以让它进入数字馆藏。本展览在第三节集中处理"复制"问题，挑选了三件资产：

- **C-03**：BHL item 318921 第 603962 页（Cycas revoluta plate）。与 C-01 同属一个 parent item，但代表"另一个具体页面"——这正是 v4.5 阶段坚持选用两个不同 BHL page ID 的原因：让页面之间的差异（取景、笔触、细节密度）成为可观察的对象。
- **C-09**：Rijksmuseum Rijksprentenkabinet 馆藏 RP-F-F80152，标题 *Zeestreepvaren*，作者 Anna Atkins（英格兰摄影师），年代约 1854。Rijksmuseum 公开页面逐项标注版权为 **Public domain（CC0 1.0）**——这是"逐项 licence"（per-item licence）的范例，不是从机构政策推断出来的。Micrio IIIF Image API 端点（`https://iiif.micr.io/vGipU/full/1024,/0/default.jpg`）给出 1024px 派生图。
- **C-10**：Rijksmuseum Rijksprentenkabinet 馆藏 RP-F-F80313，标题 *Wolfsklauw*，同样为 Anna Atkins 的 cyanotype 蓝晒作品。Rijksmuseum 公开页面同样逐项标注版权为 Public domain（CC0 1.0）。**caveat**：本轮（v4.5）核验时，Rijksmuseum IIIF Presentation API manifest `/manifest.json`（端点 `https://iiif.micr.io/PrcdN/manifest.json`）返回 HTTP 404。因此本展览**不基于 IIIF Presentation API manifest 撰写任何陈述**；licence 依据是 Rijksmuseum 公开页面的"逐项 Copyright 字段"，不是 manifest 内的 license 字段。

C-09 与 C-10 的对象类型是 cyanotype photogram（蓝晒接触印相），不是传统雕版／蚀刻／石印的版画——它们与一般意义上的"版画"在媒介上是不同的。读者如果期待看到雕版线条，会在这里遇到不同的视觉语法。这是 Anna Atkins 的具体作品特征与 cyanotype 的工艺特性，不是 Rijksmuseum 的服务异常。同时，**Rijksprentenkabinet 是 Rijksmuseum 的版画／素描／摄影部门（print room），不是植物标本馆**，因此 C-09 / C-10 的归属关系与 NMNH Botany（C-06）并不属于同一机构类别——C-06 是 herbarium（植物标本馆）中的标本记录，而 C-09 / C-10 是 print room（版画室）中的 cyanotype 摄影印刷。

**策展假设**：复制技术的连续性（手稿 → 雕版 → 蓝晒 → 扫描 → IIIF Image API）与断裂（IIIF Presentation API manifest 404）共同决定了图像的传播半径。今天的数字展览如果想走得比博物馆网页更远，必须把"哪些端点会失败"也写进策展说明——这正是 v4.5 / v4.6 阶段反复核对 source URL 的原因。

## 第四节：再组织——脆弱字段必须被标注

再组织是数字馆藏时代最大的可能：当图像有了稳定的 identifier、可校验的元数据、可机器读取的 rights 字段，它们就不再是孤立的艺术品，而可以与其它图像重新连接。本展览把 6 件资产放回一张"使用图谱"（见 `BUILD_ASSET_USAGE.md`），让观者看到一张关于"脆弱字段"的清单：

- **稳定字段**：identifier（parent item id、page id、object number、persistent URL、EZID）、source URL、rights URL。
- **脆弱字段**：NMNH `/media/?i=...` 端点返回的尺寸（90×90）、Rijksmuseum IIIF Presentation API manifest 的可达性（C-10 上为 404）、机构 Open Access 政策的措辞（随机构主页更新而可能变化）。

脆弱字段之所以脆弱，是因为它们是"工程层"的产物，而不是"法律层"的产物。法律层只要版权不变就不变；工程层则随端点实现、缓存策略、URL 模板变化。再组织的前提是诚实的元数据——每一条脆弱字段都必须被显式标注，不能被静默使用。

**策展假设**：未来研究如果要扩展本展览，第一步不是"找更多图"，而是"重新打开 6 件资产的官方页面重新核对"。这一步应该在每一次外部引用前都做，而不是一次性做完就放在那里。

---

## 元数据层级（事实 / 策展假设 / 可研究方向）

- **事实层**：6 件资产的 identifier、institution、date、rights basis 来自 `second-exhibition/assets/asset-import-manifest.json` 与 `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`，核对时间为 2026-07-11。
- **策展假设层**：四个分节的命题与 takeaway 来自本短文与 `second-exhibition/data/sections.json`。
- **可研究方向层**：见 `second-exhibition/docs/DEEP_RESEARCH_NOTES_ZH.md`。

## 引用规则

任何后续出版物引用本展览中的 6 件资产，必须：

1. 重新打开对应 source URL 与 rights URL 核对现状（不允许引用"v4.6 时的核对"作为长期依据）；
2. 在 credit line 中标注 institution 与 per-item 或 dataset-level 的 rights basis；
3. 在 source note 中标注 source URL 与获取日期；
4. 对低分辨率资产（C-06）必须显式说明"低分辨率缩略图"；
5. 对 404 caveat（C-10 IIIF Presentation API manifest）必须显式说明"本轮 manifest 不可用，licence 依据为公开页面字段"。

不允许：把 6 件资产描述为 "approved" / "deployed" / "live" / "safe for commercial use" / "cleared for all uses" 中的任何一种。