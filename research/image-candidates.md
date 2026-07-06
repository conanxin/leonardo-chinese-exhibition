# 展品图像候选清单（v1.8 · 含字段 schema）

**目的**：用于"达·芬奇的纸上宇宙"中文数字展览的展陈。

**字段约定**（每项候选的字段）：

| 字段 | 含义 |
|---|---|
| `id` | 候选编号（A1..An / B1..Bn / C1..Cn / X1..Xn） |
| `name` | 中文/英文名 |
| `source_url` | 资源原始地址 |
| `type` | `real-image` / `screenshot-candidate` / `original-svg` |
| `final_use` | hero / exhibit-index / section-2 / section-3 / section-4 / section-5 / section-6 / section-7 / unused |
| `asset_path` | 在仓库中的相对路径 |
| `source_page` | 馆藏条目页 URL |
| `credit_line` | 显示在 `<figcaption>` 中的署名 |
| `download_status` | downloaded-v1 / screenshot-needed / svg-generated / pending |
| `integration_status` | integrated / planned / not-used |

---

## A · Royal Collection Trust 温莎绘图（real-image · Wikimedia 公共域）

> 当前共 8 个候选；其中 4 个已在 v1.8 下载为本地 JPG，4 个仍为外链候选。

### A1（v1.8 · downloaded）

- id: `A1`
- name: Studies of a horse (c.1490)
- 中文: 马的研究（1490 年前后）
- source_url: `https://upload.wikimedia.org/wikipedia/commons/e/e3/Leonardo_da_Vinci_-_RCIN_912310%2C_Studies_of_a_horse_c.1490.jpg`
- type: real-image (Wikimedia · public domain)
- final_use: exhibit-index（C 卡片）+ section-3（C 画廊）
- asset_path: `site/assets/images/royal-collection/royal-horse-studies-rcin-912310.jpg`
- source_page: https://www.rct.uk/collection/912310
- credit_line: "Leonardo da Vinci · Studies of a horse · c.1490 · Royal Collection Trust / RCIN 912310 · public domain (Wikimedia Commons)"
- download_status: downloaded-v1
- integration_status: integrated

### A2（v1.8 · downloaded）

- id: `A2`
- name: Studies of water (c.1510-12)
- 中文: 水的研究（1510-1512 年）
- source_url: `https://upload.wikimedia.org/wikipedia/commons/3/38/Leonardo_da_Vinci_-_RCIN_912660%2C_Studies_of_water_c.1510-12.jpg`
- type: real-image (Wikimedia · public domain)
- final_use: exhibit-index（D）+ section-3（D）
- asset_path: `site/assets/images/royal-collection/royal-water-studies-rcin-912660.jpg`
- source_page: https://www.rct.uk/collection/912660
- credit_line: "Leonardo da Vinci · Studies of water · c.1510-12 · Royal Collection Trust / RCIN 912660 · public domain"
- download_status: downloaded-v1
- integration_status: integrated

### A3（v1.8 · downloaded）

- id: `A3`
- name: The muscles of the shoulder (Verso) (c.1510-11)
- 中文: 肩臂肌肉（背面，1510-1511 年）
- source_url: `https://upload.wikimedia.org/wikipedia/commons/f/f4/Leonardo_da_Vinci_-_RCIN_919003%2C_Verso_The_muscles_of_the_shoulder_c.1510-11.jpg`
- type: real-image (Wikimedia · public domain)
- final_use: exhibit-index（E）+ section-3（E）
- asset_path: `site/assets/images/royal-collection/royal-shoulder-arm-rcin-919003.jpg`
- source_page: https://www.rct.uk/collection/919003
- credit_line: "Leonardo da Vinci · Verso: The muscles of the shoulder · c.1510-11 · Royal Collection Trust / RCIN 919003 · public domain"
- download_status: downloaded-v1
- integration_status: integrated

### A4（v1.8 · downloaded）

- id: `A4`
- name: Cats, lions, and a dragon (c.1517-18)
- 中文: 猫、狮子与龙（1517-1518 年）
- source_url: `https://upload.wikimedia.org/wikipedia/commons/1/10/Leonardo_da_Vinci_-_RCIN_912363%2C_Cats%2C_lions%2C_and_a_dragon_c.1517-18.jpg`
- type: real-image (Wikimedia · public domain)
- final_use: exhibit-index（F）+ section-3（F）
- asset_path: `site/assets/images/royal-collection/royal-cats-lions-dragon-rcin-912363.jpg`
- source_page: https://www.rct.uk/collection/912363
- credit_line: "Leonardo da Vinci · Cats, lions, and a dragon · c.1517-18 · Royal Collection Trust / RCIN 912363 · public domain"
- download_status: downloaded-v1
- integration_status: integrated

### A5（外链候选）

- id: `A5`
- name: A map of southern Tuscany (c.1503)
- 中文: 南托斯卡纳地图（约 1503 年）
- source_url: `https://www.rct.uk/collection/912278`
- type: real-image (Royal Collection Trust · 公共域，但未下载)
- final_use: section-4 (作为候选链接 · 提供 RCIN)
- asset_path: unused
- source_page: https://www.rct.uk/collection/912278
- credit_line: "Leonardo da Vinci · A map of southern Tuscany · RCIN 912278 · public domain · link only"
- download_status: pending (目前未下载；Wikimedia 仍有更高画质版本，可在 v1.9 补)
- integration_status: not-used (作为 RCIN 外链候选保留)

### A6（外链候选）

- id: `A6`
- name: A star-of-Bethlehem and other plants (c.1506-12)
- 中文: 虎眼万年青与其他植物
- source_url: `https://www.rct.uk/collection/912406`
- type: real-image
- final_use: section-4
- asset_path: unused
- source_page: https://www.rct.uk/collection/912406
- credit_line: "Leonardo da Vinci · RCIN 912406 · public domain · link only"
- download_status: pending
- integration_status: not-used

### A7（外链候选）

- id: `A7`
- name: The head of Leda
- 中文: 丽达的头部
- source_url: `https://www.rct.uk/collection/912594`
- type: real-image
- final_use: section-4
- asset_path: unused
- source_page: https://www.rct.uk/collection/912594
- credit_line: "Leonardo da Vinci · RCIN 912594 · public domain · link only"
- download_status: pending
- integration_status: not-used

### A8（外链候选）

- id: `A8`
- name: Designs for gun-barrels and mortars
- 中文: 枪管与臼炮设计
- source_url: `https://www.rct.uk/collection/912478`
- type: real-image
- final_use: section-4
- asset_path: unused
- source_page: https://www.rct.uk/collection/912478
- credit_line: "Leonardo da Vinci · RCIN 912478 · public domain · link only"
- download_status: pending
- integration_status: not-used

---

## B · Leonardo//thek@ 平台截图候选（screenshot-candidate · 暂无下载）

> v1.7 / v1.8 阶段不下载平台截图，改由原创 SVG 工具墙承担视觉。每个平台模块都给出最终页面栏目（CV-1..CV-7），便于日后直接补图。

### B1

- id: `B1`
- name: home（首页）
- 中文: Leonardo//thek@ 首页 9 功能入口
- source_url: `https://teche.museogalileo.it/leonardo/home/index_en.html`
- type: screenshot-candidate
- final_use: section-7
- asset_path: `site/assets/images/platform/leadk-home-screenshot.jpg`（待补）
- source_page: https://teche.museogalileo.it/leonardo/
- credit_line: "Screenshot courtesy of Museo Galileo / Leonardo//thek@"
- download_status: screenshot-needed
- integration_status: planned

### B2

- id: `B2`
- name: Foliations
- final_use: section-7
- asset_path: `site/assets/images/platform/leadk-foliations-screenshot.jpg`
- source_page: https://teche.museogalileo.it/leonardo/
- credit_line: "Screenshot courtesy of Museo Galileo / Leonardo//thek@"
- download_status: screenshot-needed
- integration_status: planned

### B3

- id: `B3`
- name: Subject Indexes
- final_use: section-7
- asset_path: `site/assets/images/platform/leadk-subject-indexes-screenshot.jpg`
- source_page: https://teche.museogalileo.it/leonardo/
- credit_line: "Screenshot courtesy of Museo Galileo / Leonardo//thek@"
- download_status: screenshot-needed
- integration_status: planned

### B4

- id: `B4`
- name: Watermarks（关键）
- final_use: section-5
- asset_path: `site/assets/images/platform/leadk-watermarks-screenshot.jpg`
- source_page: https://teche.museogalileo.it/leonardo/
- credit_line: "Screenshot courtesy of Museo Galileo / Leonardo//thek@"
- download_status: screenshot-needed
- integration_status: planned

### B5

- id: `B5`
- name: Recompositions（关键）
- final_use: section-6
- asset_path: `site/assets/images/platform/leadk-recompositions-screenshot.jpg`
- source_page: https://teche.museogalileo.it/leonardo/
- credit_line: "Screenshot courtesy of Museo Galileo / Leonardo//thek@"
- download_status: screenshot-needed
- integration_status: planned

### B6

- id: `B6`
- name: Comparative Study
- final_use: section-7
- asset_path: `site/assets/images/platform/leadk-comparative-study-screenshot.jpg`
- source_page: https://teche.museogalileo.it/leonardo/
- credit_line: "Screenshot courtesy of Museo Galileo / Leonardo//thek@"
- download_status: screenshot-needed
- integration_status: planned

### B7

- id: `B7`
- name: Advanced Search
- final_use: section-7
- asset_path: `site/assets/images/platform/leadk-advanced-search-screenshot.jpg`
- source_page: https://teche.museogalileo.it/leonardo/
- credit_line: "Screenshot courtesy of Museo Galileo / Leonardo//thek@"
- download_status: screenshot-needed
- integration_status: planned

---

## C · 《大西洋手稿》代表页（real-image · Wikimedia 公共域）

### C1（v1.8 · downloaded）

- id: `C1`
- name: Codex Atlanticus f.719 recto（机械 / 飞行相关）
- 中文: 《大西洋手稿》f.719 正面 · 包含机械图与飞行器相关元素
- source_url: `https://upload.wikimedia.org/wikipedia/commons/d/d3/Leonardo_da_Vinci_-_Ambrosiana-Codice-Atlantico-Codex-Atlanticus-f-719-recto.jpg`
- type: real-image (Wikimedia · public domain)
- final_use: section-2
- asset_path: `site/assets/images/codex-atlanticus/codex-atlanticus-f719-recto.jpg`
- source_page: https://www.ambrosiana.it/
- credit_line: "Codex Atlanticus f.719 recto · Veneranda Biblioteca Ambrosiana, Milan · public domain (Wikimedia Commons)"
- download_status: downloaded-v1
- integration_status: integrated

### C2（v1.8 · downloaded）

- id: `C2`
- name: Codex Atlanticus f.21 recto（混合主题页）
- 中文: 《大西洋手稿》f.21 正面 · 早期混合主题
- source_url: `https://upload.wikimedia.org/wikipedia/commons/e/e5/Leonardo_da_Vinci_-_Ambrosiana-Codice-Atlantico-Codex-Atlanticus-f-21-recto.jpg`
- type: real-image (Wikimedia · public domain)
- final_use: section-2
- asset_path: `site/assets/images/codex-atlanticus/codex-atlanticus-f21-recto.jpg`
- source_page: https://www.ambrosiana.it/
- credit_line: "Codex Atlanticus f.21 recto · Veneranda Biblioteca Ambrosiana, Milan · public domain (Wikimedia Commons)"
- download_status: downloaded-v1
- integration_status: integrated

### C3（外链候选）

- id: `C3`
- name: Codex Atlanticus f.117 recto
- 中文: 《大西洋手稿》f.117 正面
- source_url: `https://upload.wikimedia.org/wikipedia/commons/3/3b/Leonardo_da_Vinci_-_Ambrosiana-Codice-Atlantico-Codex-Atlanticus-f-117-recto.jpg`
- type: real-image
- final_use: section-2
- asset_path: unused
- source_page: https://www.ambrosiana.it/
- credit_line: "Codex Atlanticus f.117 recto · public domain"
- download_status: pending
- integration_status: planned

### C4（外链候选）

- id: `C4`
- name: Codex Atlanticus f.272 verso（与水力相关）
- 中文: f.272 背面 · 与水利相关
- source_url: `https://upload.wikimedia.org/wikipedia/commons/c/ca/Leonardo_da_Vinci_-_Ambrosiana-Codice-Atlantico-Codex-Atlanticus-f-272-verso.jpg`
- type: real-image
- final_use: section-2
- asset_path: unused
- source_page: https://www.ambrosiana.it/
- credit_line: "Codex Atlanticus f.272 verso · public domain"
- download_status: pending
- integration_status: planned

### C5（外链候选）

- id: `C5`
- name: Codex Atlanticus f.455 recto（机械）
- 中文: f.455 正面 · 机械 / 工程
- source_url: `https://upload.wikimedia.org/wikipedia/commons/e/ee/Leonardo_da_Vinci_-_Ambrosiana-Codice-Atlantico-Codex-Atlanticus-f-455-recto.jpg`
- type: real-image
- final_use: section-2
- asset_path: unused
- source_page: https://www.ambrosiana.it/
- credit_line: "Codex Atlanticus f.455 recto · public domain"
- download_status: pending
- integration_status: planned

---

## D · 原创 SVG 图解（original-svg · 已继承 v1.7 · v1.8 不修改）

仅作交叉引用，详细见 reports/leonardo_chinese_exhibition_v1_7_exhibit_image_upgrade_report.md。

- D1 `site/assets/diagrams/manuscript-journey.svg`（v1.7 升级版）
- D2 `site/assets/diagrams/collection-split.svg`（v1.7 新增）
- D3 `site/assets/diagrams/watermark-evidence-chain.svg`（v1.7 新增）
- D4 `site/assets/diagrams/recomposition-triptych.svg`（v1.7 新增）
- D5 `site/assets/diagrams/platform-tool-wall.svg`（v1.7 新增）
- D6 `site/assets/diagrams/thinking-map.svg`（v0.3 继承）
- D7 `site/assets/diagrams/platform-structure.svg`（v0.3 继承 · v1.7 后由 D5 接替）

---

## v1.8 集成清单

| 集成位置 | 真实图像 | 数量 |
|---|---|---|
| 展品索引（A-H 卡片） | A1-A4 4 张（外加 SVG 索引） | 4 |
| 展区 2 《大西洋手稿》 | C1-C2 2 张 | 2 |
| 展区 3 温莎绘图 | A1-A4 4 张（与索引共用） | 4 |
| 展区 4 同一页艺术与科学 | A5-A8 外链候选（不下载） | 0 |
| 展区 5 水印与纸张 | B4 待补 + watermark-evidence-chain.svg | 0 待补 |
| 展区 6 复原拼合 | B5 待补 + recomposition-triptych.svg | 0 待补 |
| 展区 7 平台工具墙 | B1-B3 / B6 / B7 待补 + platform-tool-wall.svg | 0 待补 |
| **本地图像总数** |  | **6** |

## v1.9 待补

- A5-A8（4 张温莎外链候选 → 进一步下载为本地 JPG，可附在展区 4 "同一页艺术与科学"画廊）
- B1-B7（7 个平台截图候选 → 平台或人工截图）
- C3-C5（3 张 Codex Atlanticus 候选页）
- 增加 motion-study、water-flow 等达·芬奇机械 / 工程主题页面
