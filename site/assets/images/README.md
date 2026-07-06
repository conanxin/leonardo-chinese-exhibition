# 展品图像资源（v1.8）

本目录用于存放"达·芬奇的纸上宇宙"中文数字展览所引用的真实展品图像。

---

## 目录结构

```
site/assets/images/
├── README.md                          # 本说明
├── royal-collection/                  # 温莎皇家收藏（Royal Collection Trust · 公共域）
│   ├── royal-horse-studies-rcin-912310.jpg        # C 马的研究
│   ├── royal-water-studies-rcin-912660.jpg        # D 水的研究
│   ├── royal-shoulder-arm-rcin-919003.jpg         # E 肩臂肌肉
│   └── royal-cats-lions-dragon-rcin-912363.jpg    # F 猫、狮子与龙
├── codex-atlanticus/                  # 《大西洋手稿》（米兰 · 安布罗西安 · 公共域）
│   ├── codex-atlanticus-f719-recto.jpg            # 机械 / 飞行相关页面
│   └── codex-atlanticus-f21-recto.jpg             # 早期混合主题页面
└── platform/                          # Leonardo//thek@ 平台截图占位
    └── （暂无 · 见 research/image-candidates.md 中 B 系列）
```

## 命名规则

`<source>-<subject>-rcin-<NNNNNN>.<ext>`

- `source`：所属馆藏（royal-collection / codex-atlanticus / platform）
- `subject`：图中主体（horse / water / shoulder-arm / cats-lions-dragon / f719-recto / f21-recto）
- `rcin-XXXXXX`：原馆藏编号（Royal Collection Trust 用 RCIN；Codex Atlanticus 用 folio 编号，不带前缀）
- `ext`：文件扩展名（小写）

## 来源 / 版权

所有当前文件均来自 **Wikimedia Commons**，作者为**公共域（Public Domain）**——Royal Collection Trust 与米兰安布罗西安图书馆已公开达·芬奇手稿的高清数字拷贝，作为学术与教育用途免费使用。 Wikimedia 上传者为 Wikimedia Commons 用户 "Siccard" 等。

每张图像对应的源页面（用于追溯与致谢）：

| 文件 | 源页面 |
|---|---|
| royal-horse-studies-rcin-912310.jpg | https://commons.wikimedia.org/wiki/File:Leonardo_da_Vinci_-_RCIN_912310,_Studies_of_a_horse_c.1490.jpg |
| royal-water-studies-rcin-912660.jpg | https://commons.wikimedia.org/wiki/File:Leonardo_da_Vinci_-_RCIN_912660,_Studies_of_water_c.1510-12.jpg |
| royal-shoulder-arm-rcin-919003.jpg | https://commons.wikimedia.org/wiki/File:Leonardo_da_Vinci_-_RCIN_919003,_Verso_The_muscles_of_the_shoulder_c.1510-11.jpg |
| royal-cats-lions-dragon-rcin-912363.jpg | https://commons.wikimedia.org/wiki/File:Leonardo_da_Vinci_-_RCIN_912363,_Cats,_lions,_and_a_dragon_c.1517-18.jpg |
| codex-atlanticus-f719-recto.jpg | https://commons.wikimedia.org/wiki/File:Leonardo_da_Vinci_-_Ambrosiana-Codice-Atlantico-Codex-Atlanticus-f-719-recto.jpg |
| codex-atlanticus-f21-recto.jpg | https://commons.wikimedia.org/wiki/File:Leonardo_da_Vinci_-_Ambrosiana-Codice-Atlantico-Codex-Atlanticus-f-21-recto.jpg |

## 使用位置

| 文件 | 集成位置 |
|---|---|
| royal-horse-studies-rcin-912310.jpg | 展区 3 画廊（C · 马的研究）+ 展品索引（C 卡片） |
| royal-water-studies-rcin-912660.jpg | 展区 3 画廊（D · 水的研究）+ 展品索引（D 卡片） |
| royal-shoulder-arm-rcin-919003.jpg | 展区 3 画廊（E · 肩臂肌肉）+ 展品索引（E 卡片） |
| royal-cats-lions-dragon-rcin-912363.jpg | 展区 3 画廊（F · 猫、狮子与龙）+ 展品索引（F 卡片） |
| codex-atlanticus-f719-recto.jpg | 展区 2 · 《大西洋手稿》代表页插图 |
| codex-atlanticus-f21-recto.jpg | 展区 2 · 早期混合主题页（机械 + 解剖 + 几何） |

## 后续替换方式

若需要替换或新增：

1. 在 Wikimedia Commons 用文件名搜索更高分辨率版本。
2. 下载到本目录对应子目录，文件名遵循上述命名规则。
3. 在 `research/image-candidates.md` 中更新对应行的 `download_status` 为 `downloaded-v2` / `downloaded-v3` 等。
4. 在 `site/index.html` 更新 `<img src="…">` 路径。
5. 在 commit message 中注明图像版本。

## 已下载图像统计

- 温莎皇家收藏：**4 / 8**（C / D / E / F），其余 4 项（A5/A6/A7/A8）仍为外链候选
- 《大西洋手稿》：**2** 代表页（f.719 / f.21）
- 平台截图：**0**（B 系列均标记为 screenshot-needed，仍由原创 SVG 工具墙承担）

总计：6 张 JPG / 3.4 MB。
