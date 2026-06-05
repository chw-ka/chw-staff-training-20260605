# MARP 語法速查 — 課後延伸（activity-4-marp）

## 基本結構

每個 `---` 分隔一頁 slide：

```markdown
---
marp: true
theme: default
paginate: true
---

# 第一頁：標題

---

# 第二頁：內容
```

## 常用語法

| 語法 | 效果 |
|------|------|
| `# 標題` | 一級標題 |
| `<!-- _class: lead -->` | 置中大字（封面用） |
| `![bg](url)` | 全页背景圖 |
| `![bg left:40%](url)` | 左邊 40% 背景（分欄） |
| `![bg right:35%](url)` | 右邊 35% 背景 |
| `![width:200px](logo.png)` | 指定闊度 |
| `<!-- _paginate: false -->` | 該頁不顯示頁碼 |
| `<!-- _footer: "文字" -->` | 該頁 footer |
| `style` block | 全域 CSS（見 template） |

## 分欄排版示例

```markdown
---
<!-- _class: columns -->
---

![bg left:45%](assets/illustration.png)

# 決議一：展覽安排

- 主題「城市與記憶」
- 三個展示區
- 10月15日截止
```

## 匯出

```bash
# PDF
npx @marp-team/marp-cli output/briefing.md --pdf

# PowerPoint
npx @marp-team/marp-cli output/briefing.md --pptx
```

## Cursor 預覽

1. 安裝擴充：**Marp for VS Code**
2. 開啟 `.md` 檔
3. 右上角點 **Open Preview to the Side**
