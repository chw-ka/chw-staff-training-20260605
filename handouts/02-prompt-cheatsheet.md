# Prompt 懶人包 — 三個活動實操指令

> 直接複製貼上到 Agent 視窗（`Cmd/Ctrl + I`）。  
> **Model 用 Auto** 即可。  
> 想 Agent 讀某份檔，輸入 **`@`** 再揀檔名（例如 `@sample-meeting-transcript.txt`）。

---

## 活動一：錄音 → 會議紀錄（20–40 min）

> **目標：** 學懂完整流程 — 錄音 → 文字 → 加議程同範本 → 出紀錄。  
> 詳解：[`activity-1-minutes/README.md`](../activity-1-minutes/README.md)

### 三個步驟

```
第一步  錄音 → 文字        （課堂用短錄音示範）
第二步  逐字稿 + 議程 + 通用範本 → 紀錄（.md 草稿 + .docx）
第三步  逐字稿 + 議程 + 上學年格式 → 今年紀錄（.md 草稿 + .docx，可選）
```

> **交付格式：** 老師日常用 **Word（.docx）** 開檔；**排版文字（.md）** 留喺 Cursor 內改稿同接觸新格式，唔使驚。

---

### 第一步 — 錄音轉文字

```
我有一份會議錄音，想轉做文字。

請讀 @activity-1-minutes/samples/demo-short-clip.m4a，
幫我寫好轉文字嘅程式，跑完之後將結果儲存到
activity-1-minutes/output/transcript-from-audio.txt。

每一步請等我批准先再做。如果部機缺軟件，請話我知點搞。
```

**對照結果：** `activity-1-minutes/samples/demo-short-clip-expected-transcript.txt`

> 💡 若轉寫太慢，可直接用 `@activity-1-minutes/sample-meeting-transcript.txt` 跳去第二步。

---

### 第二步 — 寫會議紀錄（通用範本）

> 用 `minutes-template.md` 學基本 workflow。

```
@.cursor/skills/meeting-minutes/SKILL.md

請跟 SKILL 嘅格式，幫我寫會議紀錄：

- 會議內容：@activity-1-minutes/sample-meeting-transcript.txt
- 議程：@activity-1-minutes/議程_視藝科組會_20260528.docx
- 格式範本：@activity-1-minutes/minutes-template.md

用繁體中文書面語。

請先寫排版文字：activity-1-minutes/output/meeting-minutes-draft.md
再轉成 Word：activity-1-minutes/output/會議紀錄_草稿.docx（老師用 Word 開呢份）

決議、跟進人、截止日期唔可以漏。我會覆核 .docx 後才作正式版本。
```

**對照：** `.md` 見 `expected-output-sample.md`；正式檔為 `.docx`

---

### 第三步 — 用上學年格式寫今年紀錄（可選）

> 科組日常做法：**上學年紀錄**做格式參考（版面、欄位、語氣），內容來自**今年議程**同**今年逐字稿**。  
> **唔係**把兩份紀錄合併。

```
@.cursor/skills/meeting-minutes/SKILL.md

請幫我寫今年嘅會議紀錄：

- 會議內容（逐字稿）：@activity-1-minutes/sample-meeting-transcript.txt
- 議程：@activity-1-minutes/議程_視藝科組會_20260528.docx
- 格式參考（跟足上學年紀錄嘅版面同欄位）：@activity-1-minutes/會議紀錄_視藝科組_20250522_上學年.docx

內容只可以來自今年逐字稿同議程，唔好抄上學年嘅舊內容。
用繁體中文書面語。

請先寫排版文字：activity-1-minutes/output/meeting-minutes-final.md
再轉成 Word：activity-1-minutes/output/會議紀錄_視藝科組_20260528.docx（跟足上學年紀錄版面）

我會覆核 .docx 後才作正式版本。
```

**對照：** `.md` 見 `expected-output-sample.md`；正式檔為 `.docx`

---

## 活動二：本機文件整理（40–60 min）

> Open Folder → **`activity-2-files`**（內附 SKILL、RULES）。  
> `inbox/` 約 100 個示範下載檔；**按內容分類**，唔按副檔名。

### 三階段（詳見 [`activity-2-files/handouts/prompt-cheatsheet.md`](../activity-2-files/handouts/prompt-cheatsheet.md)）

**A 傾談（唔搬檔）**
```
@.cursor/skills/file-organizer/SKILL.md

我個下載 folder 好亂。我係中學老師，有教學、行政、eLearning、ICT、STEAM。
請同我傾想點分類、舊檔點處理；inbox/ 約 100 個檔。
呢個階段只傾，唔好搬任何檔。
```

**B 定規則**
```
根據剛才傾談，以 @activity-2-files/my_organization_profile.example.md 為底寫 my_organization_profile.md，
確認 @activity-2-files/folder_structure.md，列出規則等我確認。
```

**C 一句執行（確認後貼）**
```
@.cursor/skills/file-organizer/SKILL.md
@activity-2-files/my_organization_profile.md
@activity-2-files/folder_structure.md

請讀 @activity-2-files/inbox/ 每個檔內容，分類入 sorted/<類別>/<學年>/ 或 <類別>/跨學年/（跨學年檔唔好硬塞單一學年）。逐步批准。完成後俾摘要表。
```
（未建立 profile 時將 `my_organization_profile.md` 改為 `my_organization_profile.example.md`）

**對照：** `sorted/教學/2025-2026/`、`sorted/行政/跨學年/` 等（唔係 01_PDF）

> **Google Drive 課後自學：** [`09-google-drive-self-study.md`](09-google-drive-self-study.md)

---

## 活動三：生成靜態小工具（60–85 min）

### 主推 Prompt

```
請幫我用純 HTML + CSS + Vanilla JS 寫一個教學用小網站，功能是「功課命名器」。

要求：
1. 輸出到 activity-3-web/output/ 下面，包含：index.html、styles.css、app.js
2. UI 要現代、清晰、mobile responsive（兩欄 → 手機一欄）
3. 表單欄位：學生姓名、科目、原檔名、前綴（預設【功課】）
4. 按「生成」後顯示建議檔名：{prefix}_{student}_{subject}.{ext}
5. 提供「複製到剪貼簿」按鈕（成功/失敗提示）
6. 所有文字用香港繁中書面語
7. 完成後話我點樣用瀏覽器打開 index.html 預覽
```

### 精簡版（時間唔夠）

```
請參考 @activity-3-web/starter/ 的功課命名器，
幫我生成一個改咗色系同標題的版本，輸出到 activity-3-web/output/。
完成後話我點 preview。
```

上線步驟見 [`07-static-site-publish.md`](07-static-site-publish.md)。

---

## 課後延伸：MARP 簡報（可選）

```
請讀 @activity-4-marp/template-tech-with-footer.md 同 @activity-4-marp/sample-minutes-for-slides.md，
幫我寫 5–6 頁早會簡報，儲存為 activity-4-marp/output/morning-briefing.md。圖片位置留空。
```

詳見 [`activity-4-marp/`](../activity-4-marp/)。

---

## 通用技巧

| 技巧 | 用法 |
|------|------|
| `@` 揀檔 | 話 Agent 讀邊份稿，唔使成段複製貼上 |
| 「用繁體中文書面語」 | 控制輸出語言 |
| 「儲存為 xxx」 | 指定輸出位置 |
| **.md 再轉 .docx** | 活動一：先排版文字改稿，再出 Word 正式檔 |
| **Allow / 批准** | Agent 改檔或執行程式前會問你 — 課堂請按批准 |

---

## 課後練習

1. 用自己科組會議錄音同逐字稿，重做活動一
2. 用 `activity-2-files/` 三階段整理練習（先傾、定規則、執行）
3. 用活動三 prompt，整一個教學小工具並 preview
4. （可選）MARP 簡報：`activity-4-marp/`
5. （可選）Google Drive 自學：[`09-google-drive-self-study.md`](09-google-drive-self-study.md)

詳見 [`03-faq-hk-guide.md`](03-faq-hk-guide.md)。
