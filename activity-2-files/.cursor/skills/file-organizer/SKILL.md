---
name: file-organizer
description: 讀取下載垃圾崗檔案內容，按老師的整理偏好分類入資料夾。適用於 inbox 整理、桌面執檔、下載 folder 歸檔。Use when organizing files, sorting downloads, or cleaning up a messy folder.
---

# 文件整理 SKILL

## 核心原則

- **唔按副檔名分類**（唔好只做 PDF→一個 folder）
- **讀內容**：標題、首段、工作表名、圖片主題等
- **跟用戶偏好**：`my_organization_profile.md`（或 `.example`）
- **先傾清楚，後執行**：未確認規則前，**唔好**大量搬檔

---

## 三階段 Workflow

```
階段 A  傾談 — 了解用戶想點執（可唔改檔）
階段 B  定規則 — 更新 profile / 本 SKILL / folder 清單
階段 C  執行 — 讀 inbox → 分類入 sorted/
```

---

## 階段 A：傾談（唔使打長篇 Prompt）

用繁體中文書面語，問清楚：

1. 你是咩角色？（老師 / 行政 / IT…）
2. 想分幾多類？類別名稱？（例如：教學、行政、eLearning、ICT、STEAM）
3. 每個類別要唔要**學年**子 folder？（例如 `2025-2026/`、`2024-2025/`）
4. 舊檔、重複檔點處理？（`old/`、`trash/`？）
5. 會唔會改名？有咩禁忌？（唔刪、唔改學生檔名…）
6. 示範用 `inbox/` 有幾多檔？可唔可以先抽樣讀 5–10 個睇模式？

**本階段禁止：** 未得用戶確認就搬去 `sorted/`。

---

## 階段 B：定規則

根據傾談結果：

1. 更新或建立 `my_organization_profile.md`（可從 `my_organization_profile.example.md` 複製修改）
2. 確認 `folder_structure.md` 與 `sorted/` 一致：**每個類別下**要有學年子 folder（`2025-2026/`、`2024-2025/` 等）；缺則建立
3. 向用戶**逐條確認**分類規則，等用戶說「可以執行」

---

## 階段 C：執行

必讀：
- `my_organization_profile.md`（若無則用 `my_organization_profile.example.md`）
- `folder_structure.md`
- `@inbox/` 內待整理檔案

### 讀檔方式（按類型）

| 類型 | 做法 |
|------|------|
| PDF | 讀首頁文字／metadata |
| Word | 讀標題、首段、目錄 |
| Excel | 讀工作表名、首行標題 |
| 圖片 | 檔名 + 如可則簡述畫面 |
| 唔識讀 | 入 `待確認/` |

### 搬檔規則

- 來源：`inbox/`
- 目的地（按內容擇一）：
  - **單一學年** → `sorted/<類別>/<學年>/`（`2025-2026`、`2024-2025`…）
  - **跨學年**（多年適用、常年政策、唔綁一屆）→ `sorted/<類別>/跨學年/`
  - **類別根目錄** `sorted/<類別>/` — 僅當 profile 允許且唔適合任何子夾（少用）
- 唔肯定學年但類別清楚 → 優先 `跨學年/`，其次 `待確認/_學年不明/`
- `trash/` 可直接放檔，唔分子學年
- 每批或每個重要操作：**等用戶 Allow**
- 完成後出**摘要表**：類別、學年或「跨學年」、檔名、理由

### 品質

- ❌ 唔好只靠副檔名分類
- ❌ 唔好未讀內容就亂估學生私隱
- ❌ 唔好刪除檔案（除非用戶明確批准）
- ✅ 唔確定類別或學年 → `待確認/…`
- ✅ 跨學年內容 → `跨學年/`，唔好硬塞單一學年 folder
- ✅ 明顯過期／重複 → `old/…` 或 `trash/`（跟 profile）

---

## 課堂一句執行（階段 C）

用戶已確認規則後：

```
@.cursor/skills/file-organizer/SKILL.md
@my_organization_profile.example.md
@folder_structure.md

請按 SKILL 階段 C，讀 @inbox/ 每個檔內容，分類入 sorted/。
逐步批准。
```

---

## 學校示範（CHW 老師）

預設見 `my_organization_profile.example.md`：類別下含學年（`2025-2026/`…）、`跨學年/`、`_學年不明/`。
