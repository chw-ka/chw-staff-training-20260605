# Prompt 實操指令速查 — 文件整理

> 按 `Ctrl + I` 開啟 Agent，Model 使用 **Auto**。  
> 使用 **`@`** 引用檔案或資料夾。

---

## 階段 A：商討（不移動檔案）

```
@.cursor/skills/file-organizer/SKILL.md

本人之下載資料夾十分混亂，欲整理，但不想撰寫長篇指示。

請使用繁體中文書面語與我商討：
1. 本人為中學教師，工作涉及教學、行政、eLearning、ICT、STEAM
2. 欲了解如何分類、學年與跨學年如何區分、舊檔如何處理
3. inbox/ 約有 100 個檔案，您將如何讀取內容後分類

本階段僅商討，請勿移動任何檔案。
```

---

## 階段 B：訂立規則

```
根據剛才商討內容，請：
1. 以 @my_organization_profile.example.md 為基礎，撰寫 my_organization_profile.md
2. 確認 @folder_structure.md 與 sorted/ 子資料夾一致
3. 列出規則供我確認，確認後方執行
```

---

## 階段 C：一次執行

```
@.cursor/skills/file-organizer/SKILL.md
@my_organization_profile.md
@folder_structure.md

請依 SKILL 階段 C：讀取 @inbox/ 各檔案內容（請勿僅依副檔名），
搬入 sorted/<類別>/<學年>/ 或 sorted/<類別>/跨學年/。
請逐步待我批准。完成後請提供摘要表。
```

（若尚未建立 profile，請將 `@my_organization_profile.md` 改為 `@my_organization_profile.example.md`）

---

## 驗收

- `sorted/教學/2025-2026/`、`sorted/行政/跨學年/` 等應有檔案
- `inbox/` 應清空或僅剩少量「待確認」
- 總數約 100 個檔案
