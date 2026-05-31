---
marp: true
theme: default
paginate: true
style: |
  section {
    font-family: "PingFang TC", "Microsoft JhengHei", sans-serif;
  }
  section.lead h1 {
    text-align: center;
  }
  footer {
    font-size: 14px;
    color: #666;
  }
  img[alt~="logo"] {
    height: 48px;
  }
footer: '![logo](assets/school-logo.png) 迦密聖道中學 Carmel Holy Word Secondary School'
---

<!-- _class: lead -->
# 標題在這裡

副標題 / 日期

---

# 議程概要

- 第一點
- 第二點
- 第三點

---

![bg left:40%](assets/school-logo.png)

# 分欄排版示例

左邊放 logo 或 AI 插圖（`bg left:40%`），右邊放重點文字。

適合早會簡報每一個決議。

---

![bg right:35%](https://picsum.photos/800/600)

# 決議重點

<!-- _footer: '![logo](assets/school-logo.png) CHW — 視藝科' -->

右邊背景圖可以換成 Gemini 生成嘅插圖。

---

<!-- _class: lead -->
# 謝謝

**Questions?**

<!-- _paginate: false -->

---

## Global Footer 設定說明

在 front matter 加入：

```yaml
footer: '![logo](assets/school-logo.png) 迦密聖道中學'
```

每頁可覆蓋：

```markdown
<!-- _footer: '自訂 footer 文字' -->
```

校徽檔案：`activity-3-marp/assets/school-logo.png`（講者課前放入）
