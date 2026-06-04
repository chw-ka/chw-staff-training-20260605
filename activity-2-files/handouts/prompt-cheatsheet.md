# Prompt 懶人包 — 文件整理

> `Ctrl + I` 開 Agent，Model 用 **Auto**。  
> 用 **`@`** 引用檔案或資料夾。

---

## 階段 A：傾談（唔搬檔）

```
@.cursor/skills/file-organizer/SKILL.md

我個下載 folder 好亂，想整理，但唔想打長篇指示。

請用繁體中文書面語同我傾：
1. 我係中學老師，有教學、行政、eLearning、ICT、STEAM 等工作
2. 我想點分類、學年同跨學年點分、舊檔點處理
3. inbox/ 大約有 100 個檔，你會點樣讀內容再分類

呢個階段只傾，唔好搬任何檔。
```

---

## 階段 B：定規則

```
根據剛才傾談，請：
1. 以 @my_organization_profile.example.md 為底，寫 my_organization_profile.md
2. 確認 @folder_structure.md 同 sorted/ 子資料夾一致
3. 列出規則等我確認，確認後先至執行
```

---

## 階段 C：一句執行

```
@.cursor/skills/file-organizer/SKILL.md
@my_organization_profile.md
@folder_structure.md

請按 SKILL 階段 C：讀 @inbox/ 每個檔內容（唔好只睇副檔名），
搬入 sorted/<類別>/<學年>/ 或 sorted/<類別>/跨學年/。
逐步等我批准。完成後俾摘要表。
```

（未建立 profile 時，將 `@my_organization_profile.md` 改為 `@my_organization_profile.example.md`）

---

## 驗收

- `sorted/教學/2025-2026/`、`sorted/行政/跨學年/` 等有檔
- `inbox/` 應清空或只剩少量 `待確認`
- 總數約 100 個檔
