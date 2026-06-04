# Prompt 懶人包 — 活動一：錄音 → 會議紀錄

> 直接複製貼上到 Agent 視窗（`Cmd/Ctrl + I`）。  
> **Model 用 Auto** 即可。  
> 想 Agent 讀某份檔，輸入 **`@`** 再揀檔名。

> **交付格式：** 正式檔用 **Word（.docx）**；**排版文字（.md）** 留喺 Cursor 改稿同學習。

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
我有一份會議錄音，想轉做文字。

請讀 @samples/demo-short-clip.m4a，
幫我寫好轉文字嘅程式，跑完之後將結果儲存到
output/transcript-from-audio.txt。

每一步請等我批准先再做。如果部機缺軟件，請話我知點搞。
```

**對照結果：** `samples/demo-short-clip-expected-transcript.txt`

> 💡 若轉寫太慢，可直接用 `@sample-meeting-transcript.txt` 跳去第二步。

---

### 第二步 — 寫會議紀錄（通用範本）

```
@.cursor/skills/meeting-minutes/SKILL.md

請跟 SKILL 嘅格式，幫我寫會議紀錄：

- 會議內容：@sample-meeting-transcript.txt
- 議程：@議程_視藝科組會_20260528.docx
- 格式範本：@minutes-template.md

用繁體中文書面語。

請先寫排版文字：output/meeting-minutes-draft.md
再轉成 Word：output/會議紀錄_草稿.docx（老師用 Word 開呢份）

決議、跟進人、截止日期唔可以漏。我會覆核 .docx 後才作正式版本。
```

---

### 第三步 — 用上學年格式寫今年紀錄（可選）

> **上學年紀錄**只係格式參考；內容來自**今年議程**同**今年逐字稿**。

```
@.cursor/skills/meeting-minutes/SKILL.md

請幫我寫今年嘅會議紀錄：

- 會議內容（逐字稿）：@sample-meeting-transcript.txt
- 議程：@議程_視藝科組會_20260528.docx
- 格式參考（跟足上學年紀錄嘅版面同欄位）：@會議紀錄_視藝科組_20250522_上學年.docx

內容只可以來自今年逐字稿同議程，唔好抄上學年嘅舊內容。
用繁體中文書面語。

請先寫排版文字：output/meeting-minutes-final.md
再轉成 Word：output/會議紀錄_視藝科組_20260528.docx（跟足上學年紀錄版面）

我會覆核 .docx 後才作正式版本。
```

---

### 課後延伸

- 換自己科組錄音、議程、上學年紀錄試做
- 長錄音 `@samples/新錄音 2.m4a` 可放工後慢慢轉
