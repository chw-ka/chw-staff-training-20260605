# 講者腳本：@Folder 與 Context — 「超快實習老師」比喻

> 不必講 vector database、embedding、RAG。用學校場景，30 秒講清。

---

## 核心比喻（投影時可唸）

> 「想像 Cursor 是一位**無限體力、閱讀速度 0.5 秒**的實習老師。
> 你平時教書要逐份看作文、對照評核準則 — 很花時間。
> 當你用 **`@Folder`** 指定一個資料夾，就等於告訴實習老師：
> **『請先讀完這個櫃桶裡面所有文件，再答我問題。』**
> 它不必真的『記住整個學校』 — 你只給它這次需要的文件就可以。」

---

## 與「Context Window」如何解釋

> 「AI 一次可以處理的文字量有限 — 好像一張桌面那麼大。
> 你不會把整個倉庫的書一次搬上桌；你會**選擇這次要用的 folder**。
> `@Folder` 就是幫它整理好這次要放上桌的文件。」

---

## 現場 Demo 腳本：30 份作文 × 教育局寫作評核準則

### 準備（課前）

1. 建立資料夾 `demo-student-compositions/`（可放 3–5 份**虛構**短文作示範，不必真 30 份）
2. 放入 `edb-writing-criteria-excerpt.md`（評核準則摘錄）

### 講者步驟

1. **`Ctrl + I`** 開 Agent
2. 輸入 `@`，選 **`demo-student-compositions`** folder（或整個 project 內該 folder）
3. 貼以下 Prompt（可投影）：

```
我 @ 了 demo-student-compositions 資料夾，裡面有學生作文與 edb-writing-criteria-excerpt.md。

請你：
1. 用 edb-writing-criteria-excerpt.md 做準則
2. 為每份作文寫一段「評語草稿」（繁中，各 80 字內）
3. 用表格列出：學生代號、符合準則的優點、建議改善一項

注意：全部是示範虛構資料，不要當真實學生。
```

4. **Approve** 讀檔 → 展示表格 output

### 話術（生成前）

> 「我沒有 copy 30 份作文入 Prompt — 我只 `@` 了那個 folder。
> AI 自己開櫃桶拿文件，再對照準則 — 這就是今日要記的 `@Folder`。」

### 話術（生成後）

> 「評語是**草稿**，老師一定要覆核 — 與改作文一樣。
> 敏感真實學生資料要用校內核准工具；今日只用虛構示範。」

---

## 常見問題（即場答）

| 同事問 | 你可以答 |
|--------|----------|
| 它真的讀完整個 folder？ | 會讀你 `@` 指定範圍內的文字檔；太大就要分 folder 或分批 |
| 會不會漏文件？ | 可以 Prompt 寫明「列出你讀了哪幾份檔名」 |
| 與 Google Drive MCP 有什麼分別？ | `@Folder` 是本機 project 檔；Drive MCP 是雲端 — 活動二教的那個 |

---

## 下一步

→ 延伸練習：用 `@activity-1-minutes/sample-meeting-transcript.txt` + `@.cursor/skills/meeting-minutes/SKILL.md` 做 minutes demo
