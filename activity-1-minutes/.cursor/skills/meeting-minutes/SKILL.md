---
name: meeting-minutes
description: 將會議錄音逐字稿或 transcript 轉換為結構化中文會議紀錄。適用於科組會、行政會議、家長會等。Use when the user asks to write meeting minutes, 會議紀錄, or process a meeting transcript.
---

# 會議紀錄 SKILL

## 觸發條件

當用戶要求撰寫會議紀錄、處理 meeting transcript、或將錄音文字整理成 minutes 時，使用此 SKILL。

## 執行流程

### Step 1：讀取輸入

- 讀取用戶提供的 transcript 檔案（`.txt`、`.md`）或貼上的文字
- 若用戶指定範本，讀取 `minutes-template.md` 或同等格式檔案

### Step 2：提取關鍵資訊

從逐字稿中提取：
- 會議名稱、日期、時間、地點
- 出席者、缺席者（含原因）
- 各議程項的討論內容
- **決議**（明確的決定，非一般討論）
- **跟進事項**（負責人 + 截止日期）

### Step 3：撰寫紀錄

- 使用**香港廣東話書面語**（正式但自然）
- 嚴格跟隨範本結構
- 討論摘要：每項 2–4 句，精簡準確
- 決議：用編號列表，每條可獨立執行
- 跟進：必須有負責人及截止日期；若逐字稿未提及，標注「待確認」

### Step 4：輸出

- 儲存為 Markdown 檔案
- 預設路徑：`activity-1-minutes/output/meeting-minutes-draft.md`
- 結尾加註：「本紀錄由 AI 輔助起草，請記錄人覆核後方作正式版本。」

## 品質要求

- ❌ 不可捏造逐字稿中未出現的決議或數字
- ❌ 不可省略任何議程項
- ✅ 人名、日期、金額必須與原文一致
- ✅ 若資訊不完整，在該欄位註明「待確認」

## 學校背景（CHW）

- 學校：迦密聖道中學（Carmel Holy Word Secondary School）
- 語言：繁體中文，香港書面語
- 職稱：老師、主任、校長（不用「教师」等簡體或內地用詞）

## 示例 Prompt（用戶可參考）

```
@.cursor/skills/meeting-minutes/SKILL.md
請處理 @sample-meeting-transcript.txt，輸出會議紀錄。
```
