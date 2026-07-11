# 深度研究笔记 / Deep Research Notes

> 本文是《植物图谱与视觉分类》展览的深度研究入口。文中把**可验证事实**、**策展假设**、**可研究方向**三类陈述明确分开，方便后续研究者在引用时不混淆层级。
>
> 核对时间：2026-07-11（v4.5 asset import + v4.6 repository build 阶段）。任何后续引用必须重新核对。

---

## A. 至少 10 个研究问题

1. BHL item 318921（《Album of watercolors of Asian fruits and flowers》）的页级 copyright status 在 2026 年是否发生过回溯变化？哪些页属于 Public-domain 子集、哪些页属于 CC BY-NC-SA 子集？
2. Smithsonian NMNH Botany 馆藏 US Catalog 1529703 的 *Aconitum bulbilliferum* 在 EZID `ark:/65665/31e002158-f911-411b-bbfb-63a2d207e920` 之外是否还有第二条稳定的可达 URL？当前 `/media/?i=…` 端点返回 90×90 PNG，是否存在公开的高分辨率派生？
3. The Metropolitan Museum of Art object 285149 的 "Gift of Russell C. Vail, 2003" credit line 是否在 v4.5 / v4.6 之外的最新公开页面上仍保持一致？是否存在 credit-line 更新历史？
4. Rijksmuseum Rijksprentenkabinet 的 per-item Copyright 字段（CC0 1.0 / CC BY 4.0）在 2026 年是否经历过政策变更？这种变更会同时影响多少已发布的图像？
5. Rijksmuseum IIIF Presentation API manifest `/manifest.json` 在 2026 年 7 月对 RP-F-F80313 返回 404，这是端点暂时不可达还是结构性缺失？其它 Rijksmuseum 对象是否也存在同样问题？
6. Anna Atkins 的 cyanotype 蓝晒作品在不同数字馆藏中的颜色管理：Micrio IIIF Image API 给出的派生 JPG 与机构自托管版本在色彩管理上是否有差异？
7. BHL `/pageimage/<id>` 端点返回 WebP 格式，所有现代浏览器都支持；这对"可访问性 + 文件体积 + 元数据完整性"三者的取舍意味着什么？
8. Smithsonian Open Access / CC0 1.0 的"dataset-level"措辞如何在 credit line 中精确表达？是否应该在 credit line 中区分 "Open Access" 与 "CC0 1.0"，还是直接使用 "CC0 1.0"？
9. Micrio IIIF Image API 端点（`https://iiif.micr.io/<id>/full/1024,/0/default.jpg`）与 Rijksmuseum 自托管 IIIF Image API 端点（如果有）之间的关系：Micrio 是 Rijksmuseum 的官方 IIIF provider 还是第三方？
10. 当一件机构资产的 media URL 在 build 之后失效（如 NMNH `/media/?i=…` 改为仅限登录访问），如何在数字展览中显式降级（degrade gracefully）而不是显示破图？

## B. 至少 6 个可验证事实

下列事实均来自 `second-exhibition/assets/asset-import-manifest.json` 与 `second-exhibition/docs/SOURCE_AUDIT_MANIFEST.md`，核对时间为 2026-07-11。

1. **BHL item 318921**（《Album of watercolors of Asian fruits and flowers》），parent item URL `https://www.biodiversitylibrary.org/item/318921`；作者佚名，介乎 1798—1850 年之间。
2. **C-01**（Pistillaria plate）来自 BHL page 603998，media URL `https://www.biodiversitylibrary.org/pageimage/603998`，文件大小 306126 B，SHA-256 `dc4b292536761be5bdf8a459d5ef82c53c4ecf5e39252ab68d19c233293522b7`。
3. **C-03**（Cycas revoluta plate）来自 BHL page 603962，media URL `https://www.biodiversitylibrary.org/pageimage/603962`，文件大小 262498 B，SHA-256 `446d744d9b647f299532fc248e3263f14db818dff591f2c99264beb18c7d881d`。C-03 仅属于 Public-domain 子集；CC BY-NC-SA 子集被 blocked-from-import。
4. **C-06**（NMNH US Catalog 1529703）记录为 *Aconitum bulbilliferum* Hand.-Mazz.（毛茛科，Type fragment），采集人 Handel-Mazzetti H. R.，日期 1914-09-17；media URL `https://collections.nmnh.si.edu/media/?i=1529703&ph=yes&thumb=yes` 返回 image/png 90×90 3550 B；rights basis 为 Smithsonian Open Access / CC0 1.0 dataset-level。
5. **C-08**（Met object 285149）标题 *[Botanical Specimen: Fern]*，年代 1855–60，accession 2003.562.3；Met Collection API 返回 `isPublicDomain: true`；公开页面显示 Public Domain 指示（double-confirmation PASS）；media URL `https://images.metmuseum.org/CRDImages/ph/web-large/DP147833.jpg` 返回 image/jpeg 449×624 95001 B。
6. **C-09**（Rijksmuseum RP-F-F80152）标题 *Zeestreepvaren*，作者 Anna Atkins（英格兰摄影师），年代约 1854，cyanotype on paper；Rijksmuseum 公开页面逐项标注版权为 Public domain（CC0 1.0）；media URL `https://iiif.micr.io/vGipU/full/1024,/0/default.jpg` 返回 image/jpeg 1024×1293 294445 B。
7. **C-10**（Rijksmuseum RP-F-F80313）标题 *Wolfsklauw*，同样为 Anna Atkins 的 cyanotype 蓝晒；Rijksmuseum 公开页面同样逐项标注版权为 Public domain（CC0 1.0）；media URL `https://iiif.micr.io/PrcdN/full/1024,/0/default.jpg` 返回 image/jpeg 1024×1291 191606 B。**caveat**：Rijksmuseum IIIF Presentation API manifest `https://iiif.micr.io/PrcdN/manifest.json` 在 v4.5 阶段返回 HTTP 404；本展览不基于 IIIF Presentation API manifest 撰写任何陈述。

## C. 至少 6 个后续研究方向

1. **扩展 NMNH Botany 高分辨率访问**：联系 NMNH 数据团队（Data Manager）申请 US Catalog 1529703 的高分辨率派生；如果可能，写一篇"NMNH 数据访问策略的工程层差异"小论文。
2. **BHL page-level copyright 抽样**：在 BHL item 318921 的全本页范围内做一次抽样（每 10 页抽 1 页）核对 copyright status，把 PD 子集与 CC BY-NC-SA 子集的边界画出来。
3. **Rijksmuseum IIIF 端点稳定性**：在不同时间（24h 间隔）多次访问 Rijksmuseum Micrio IIIF Presentation API manifest，记录返回码的变化趋势；如果是结构性 404，则可以写一篇"机构 IIIF 端点成熟度"的对比研究。
4. **Anna Atkins cyanotype 的色彩管理对比**：取 Micrio IIIF 派生 JPG 与 Met 同一时期 cyanotype 收藏的派生 JPG 做色彩比较；如果两者均使用 sRGB 输出，分析各机构的 ICC profile 差异。
5. **"再组织"算法实验**：用 6 件资产 + 一个检索 query（如 "monocot fern Asia 1850"）在 Met API / Rijksmuseum API / BHL API 之间做跨机构检索，记录检索结果的字段稳定性，验证本展览关于"脆弱字段"的策展假设。
6. **数字展览的伦理边界**：以本展览的 6 件资产为样本，写一篇关于"数字策展如何对待低分辨率 / 404 caveat / PD 子集"的伦理讨论。这一方向与 AUTOMATIC / MANUAL 标注、版权标注、数据级 vs 资产级 CC0 等话题相关。
7. **AI 时代的图像策展**：用 LLM 对 6 件资产的 source note 做自动重写，比较 LLM 输出与人工撰写的 source note 的差异，评估 AI 重写对 source-and-rights 证据完整性的影响。

## D. 显式标注

- 本文 A 部分（10 个研究问题）属于**研究问题**，尚未验证。
- B 部分（7 个可验证事实）属于**已核对事实**，核对时间为 2026-07-11，事实可能被未来发现推翻，必须重新核对。
- C 部分（7 个后续研究方向）属于**研究提案**，并未启动。
- 本展览不构成法律意见；本文不构成法律意见。
- 任何引用本文事实部分的研究者，必须重新打开对应 source URL 与 rights URL 核对现状，不允许直接引用"v4.6 时的核对"作为长期依据。