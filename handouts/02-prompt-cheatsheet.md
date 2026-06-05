# Prompt 實操指令速查 — 三個活動

> 請直接複製貼上至 Agent 視窗（`Cmd/Ctrl + I`）。  
> **Model 使用 Auto** 即可。  
> 若需 Agent 讀取某份檔案，請輸入 **`@`** 再選擇檔名（例如 `@sample-meeting-transcript.txt`）。  
> 不熟悉 **SKILL、Workflow、.md** 等詞彙？請先閱讀 [`00-core-concepts-glossary.md`](00-core-concepts-glossary.md)。

---

## 活動一：錄音 → 會議紀錄（20–40 分鐘）

> **目標：** 掌握完整流程 — 錄音 → 文字 → 加入議程與範本 → 產出紀錄。  
> 詳解：[`activity-1-minutes/README.md`](../activity-1-minutes/README.md)

### 三個步驟

```
第一步  錄音 → 文字        （課堂以短錄音示範）
第二步  逐字稿 + 議程 + 通用範本 → 紀錄（.md 草稿 + .docx）
第三步  逐字稿 + 議程 + 上學年格式 → 今年紀錄（.md 草稿 + .docx，可選）
```

> **交付格式：** 教師日常以 **Word（.docx）** 開啟；**排版文字（.md）** 保留於 Cursor 內修訂及熟悉新格式。

---

### 第一步 — 錄音轉文字

```
我有一份會議錄音，需要轉換為文字。

請讀取 @activity-1-minutes/samples/demo-short-clip.m4a，
協助撰寫轉文字程式，執行完成後將結果儲存至
activity-1-minutes/output/transcript-from-audio.txt。

每一步請待我批准後再進行。若本機缺少軟件，請告知處理方法。
```

**對照結果：** `activity-1-minutes/samples/demo-short-clip-expected-transcript.txt`

> 💡 若轉寫耗時過長，可直接使用 `@activity-1-minutes/sample-meeting-transcript.txt` 進入第二步。

---

### 第二步 — 撰寫會議紀錄（通用範本）

> 使用 `minutes-template.md` 學習基本工作流。

```
@.cursor/skills/meeting-minutes/SKILL.md

請依 SKILL 所訂格式，協助撰寫會議紀錄：

- 會議內容：@activity-1-minutes/sample-meeting-transcript.txt
- 議程：@activity-1-minutes/議程_視藝科組會_20260528.docx
- 格式範本：@activity-1-minutes/minutes-template.md

請使用繁體中文書面語。

請先撰寫排版文字：activity-1-minutes/output/meeting-minutes-draft.md
再轉為 Word：activity-1-minutes/output/會議紀錄_草稿.docx（供教師以 Word 開啟）

決議、跟進人員、截止日期均不可遺漏。我將覆核 .docx 後方作為正式版本。
```

**對照：** `.md` 見 `expected-output-sample.md`；正式檔為 `.docx`

---

### 第三步 — 依上學年格式撰寫今年紀錄（可選）

> 科組慣常做法：**上學年紀錄**作格式參考（版面、欄位、語氣），內容僅來自**今年議程**及**今年逐字稿**。  
> **並非**合併兩份紀錄。

```
@.cursor/skills/meeting-minutes/SKILL.md

請協助撰寫本年度會議紀錄：

- 會議內容（逐字稿）：@activity-1-minutes/sample-meeting-transcript.txt
- 議程：@activity-1-minutes/議程_視藝科組會_20260528.docx
- 格式參考（依循上學年紀錄之版面與欄位）：@activity-1-minutes/會議紀錄_視藝科組_20250522_上學年.docx

內容僅可來自本年度逐字稿及議程，請勿抄錄上學年舊內容。
請使用繁體中文書面語。

請先撰寫排版文字：activity-1-minutes/output/meeting-minutes-final.md
再轉為 Word：activity-1-minutes/output/會議紀錄_視藝科組_20260528.docx（依循上學年紀錄版面）

我將覆核 .docx 後方作為正式版本。
```

**對照：** `.md` 見 `expected-output-sample.md`；正式檔為 `.docx`

---

## 活動二：本機文件整理（40–60 分鐘）

> Open Folder → **`activity-2-files`**（內附 SKILL、RULES）。  
> `inbox/` 約 100 個示範下載檔；**依內容分類**，勿僅依副檔名。

### 三階段（詳見 [`activity-2-files/handouts/prompt-cheatsheet.md`](../activity-2-files/handouts/prompt-cheatsheet.md)）

**A 商討（不移動檔案）**
```
@.cursor/skills/file-organizer/SKILL.md

本人之下載資料夾十分混亂。本人為中學教師，工作涉及教學、行政、eLearning、ICT、STEAM。
請與我商討分類方式及舊檔處理；inbox/ 約有 100 個檔案。
本階段僅商討，請勿移動任何檔案。
```

**B 訂立規則**
```
根據剛才商討內容，以 @activity-2-files/my_organization_profile.example.md 為基礎撰寫 my_organization_profile.md，
確認 @activity-2-files/folder_structure.md，並列出規則供我確認。
```

**C 一次執行（確認後貼上）**
```
@.cursor/skills/file-organizer/SKILL.md
@activity-2-files/my_organization_profile.md
@activity-2-files/folder_structure.md

請讀取 @activity-2-files/inbox/ 各檔案內容，分類至 sorted/<類別>/<學年>/ 或 <類別>/跨學年/（跨學年檔案請勿強行歸入單一學年）。請逐步待我批准。完成後請提供摘要表。
```
（若尚未建立 profile，請將 `my_organization_profile.md` 改為 `my_organization_profile.example.md`）

**對照：** `sorted/教學/2025-2026/`、`sorted/行政/跨學年/` 等（並非 01_PDF）

> **Google Drive 課後自學：** [`09-google-drive-self-study.md`](09-google-drive-self-study.md)

---

## 活動三：生成靜態小工具（60–85 分鐘）

### 主推 Prompt

```
請協助以純 HTML + CSS + Vanilla JS 撰寫教學用小網站，功能為「功課命名器」。

要求：
1. 輸出至 activity-3-web/output/ 目錄，包含：index.html、styles.css、app.js
2. 介面須現代、清晰、支援 mobile responsive（兩欄 → 手機單欄）
3. 表單欄位：學生姓名、科目、原檔名、前綴（預設【功課】）
4. 按「生成」後顯示建議檔名：{prefix}_{student}_{subject}.{ext}
5. 提供「複製至剪貼簿」按鈕（含成功／失敗提示）
6. 所有文字使用香港繁體中文書面語
7. 完成後請說明如何以瀏覽器開啟 index.html 預覽
```

### 精簡版（時間不足時）

```
請參考 @activity-3-web/starter/ 的功課命名器，
協助產出已調整色系與標題之版本，輸出至 activity-3-web/output/。
完成後請說明預覽方法。
```

上線步驟見 [`07-static-site-publish.md`](07-static-site-publish.md)。

---

## 課後延伸：MARP 簡報（可選）

```
請讀取 @activity-4-marp/template-tech-with-footer.md 與 @activity-4-marp/sample-minutes-for-slides.md，
協助撰寫 5–6 頁早會簡報，儲存為 activity-4-marp/output/morning-briefing.md。圖片位置請留空。
```

詳見 [`activity-4-marp/`](../activity-4-marp/)。

---

## 通用技巧

| 技巧 | 用法 |
|------|------|
| `@` 選檔 | 指示 Agent 讀取指定稿件，無需整段複製 |
| 「請使用繁體中文書面語」 | 控制輸出語言 |
| 「儲存為 xxx」 | 指定輸出位置 |
| **.md 再轉 .docx** | 活動一：先以排版文字修訂，再產出 Word 正式檔 |
| **Allow／批准** | Agent 修改檔案或執行程式前會徵詢 — 課堂請按批准 |

---

## 課後練習

1. 以本科組會議錄音及逐字稿，重做活動一
2. 使用 `activity-2-files/` 三階段整理練習（先商討、訂規則、執行）
3. 使用活動三 prompt，製作教學小工具並預覽
4. （可選）MARP 簡報：`activity-4-marp/`
5. （可選）Google Drive 自學：[`09-google-drive-self-study.md`](09-google-drive-self-study.md)

詳見 [`03-faq-hk-guide.md`](03-faq-hk-guide.md)。
