# Prompt 實操指令速查 — 活動一：錄音 → 會議紀錄

> 請直接複製貼上至 Agent 視窗（`Cmd/Ctrl + I`）。  
> **Model 使用 Auto** 即可。  
> 若需 Agent 讀取某份檔案，請輸入 **`@`** 再選擇檔名。

> **交付格式：** 正式檔使用 **Word（.docx）**；**排版文字（.md）** 保留於 Cursor 內修訂及學習。

---

## 三個步驟

```
第一步  錄音 → 文字
第二步  逐字稿 + 議程 + 通用範本 → .md 草稿 + .docx
第三步  逐字稿 + 議程 + 上學年格式 → .md 草稿 + .docx（可選）
```

---

### 第一步 — 錄音轉文字

```
我有一份會議錄音，需要轉換為文字。

請讀取 @samples/demo-short-clip.m4a，
協助撰寫轉文字程式，執行完成後將結果儲存至
output/transcript-from-audio.txt。

每一步請待我批准後再進行。若本機缺少軟件，請告知處理方法。
```

**對照結果：** `samples/demo-short-clip-expected-transcript.txt`

> 💡 若轉寫耗時過長，可直接使用 `@sample-meeting-transcript.txt` 進入第二步。

---

### 第二步 — 撰寫會議紀錄（通用範本）

```
@.cursor/skills/meeting-minutes/SKILL.md

請依 SKILL 所訂格式，協助撰寫會議紀錄：

- 會議內容：@sample-meeting-transcript.txt
- 議程：@議程_視藝科組會_20260528.docx
- 格式範本：@minutes-template.md

請使用繁體中文書面語。

請先撰寫排版文字：output/meeting-minutes-draft.md
再轉為 Word：output/會議紀錄_草稿.docx（供教師以 Word 開啟）

決議、跟進人員、截止日期均不可遺漏。我將覆核 .docx 後方作為正式版本。
```

---

### 第三步 — 依上學年格式撰寫今年紀錄（可選）

> **上學年紀錄**僅作格式參考；內容僅來自**今年議程**及**今年逐字稿**。

```
@.cursor/skills/meeting-minutes/SKILL.md

請協助撰寫本年度會議紀錄：

- 會議內容（逐字稿）：@sample-meeting-transcript.txt
- 議程：@議程_視藝科組會_20260528.docx
- 格式參考（依循上學年紀錄之版面與欄位）：@會議紀錄_視藝科組_20250522_上學年.docx

內容僅可來自本年度逐字稿及議程，請勿抄錄上學年舊內容。
請使用繁體中文書面語。

請先撰寫排版文字：output/meeting-minutes-final.md
再轉為 Word：output/會議紀錄_視藝科組_20260528.docx（依循上學年紀錄版面）

我將覆核 .docx 後方作為正式版本。
```

---

### 課後延伸

- 更換為本科組錄音、議程、上學年紀錄試做
- 較長錄音 `@samples/新錄音 2.m4a` 可於放工後慢慢轉寫
