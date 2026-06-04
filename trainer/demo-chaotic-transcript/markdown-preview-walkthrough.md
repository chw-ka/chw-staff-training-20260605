# Markdown Preview 講解 — 講者逐字稿

> 配合 [`chaotic-open-day-transcript.txt`](chaotic-open-day-transcript.txt) → [`expected-minutes-output.md`](expected-minutes-output.md) demo。

---

## 場景

Agent 剛生成 `expected-minutes-output.md`，投影 Cursor 編輯器。

---

## 講者話術（約 1 分鐘）

### 1. 指著原始符號

> 「大家看到 `#`、`##`、`| | |` 這些符號 — 不是壞了，不是亂碼。
> 它們與 Word 裡面的**標題 1、標題 2、插入表格**一樣，只是用**文字**寫下排版規則。
> 這種格式叫 **排版文字**（Markdown），Cursor 與很多學校工具都識讀。」

### 2. 開 Preview

> 「我現在按 **`Ctrl + Shift + V`** — 或者右上角這個**分屏預覽**圖示。」

**動作：** 開啟 Markdown Preview（與編輯器並排）

### 3. 對比左右

> 「左邊：給電腦與 AI 讀的**原稿**。
> 右邊：人眼看的**正式格式** — 標題、表格、粗體，一目了然。
> 同一份文件，兩種視圖。」

### 4. 連結會議紀錄

> 「剛才那段 1 分鐘錄音 — 口語、搶話、booth 7 重複 — AI 幫我整理成**學校慣用的會議紀錄表**：
> 議項、內容摘要、跟進人員、限期。
> 你的工作變成**覆核**，不是由零開始打字。」

### 5. 貼至 Word

> 「要交 admin？**Copy** 右邊預覽或者整份 file，貼至 Word 即可。
> 表格會保留；若格式有少少走樣，用 Word「貼上 → 保留來源格式」。」

---

## Demo Prompt（可投影）

```
請讀 @trainer/demo-chaotic-transcript/chaotic-open-day-transcript.txt，
整理成學校正式會議紀錄，用表格列出：議項、內容摘要、跟進人員/部門、限期。
輸出繁體中文書面語，存去 trainer/demo-chaotic-transcript/expected-minutes-output.md
```

---

## 常見反應

| 同事 | 回應 |
|------|------|
| 「一定要學這些符號？」 | 不必 — 叫 Agent 寫，你只需要識 Preview 與 Copy |
| 「與 Word 有什麼分別？」 | Word 用按鈕排版；這裡用文字標記 — AI 寫文字標記較方便，人就用 Preview 看 |
