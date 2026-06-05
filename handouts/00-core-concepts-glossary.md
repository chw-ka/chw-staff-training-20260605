# 核心概念速查 — 課堂用語對照

> **無需背誦英文術語。** 以下以學校行政文書語氣說明課堂常見詞彙。  
> 實操請以 [`02-prompt-cheatsheet.md`](02-prompt-cheatsheet.md) 為主；本頁供課前預習或課後查閱。

---

## 一覽表（五項概念與本日活動）

| 概念 | 摘要說明 | 本日活動對應 |
|------|----------|--------------|
| **Workflow（工作流）** | 並非單次問答，而是 **輸入 → 多個步驟 → 產出**；您擔任設計者，AI 協助執行 | 活動一：錄音→文字→紀錄；活動二：商討→訂規則→整理檔案；活動三：描述需求→產出網頁 |
| **SKILL（專用指引）** | 某類工作的 **部門標準作業程序（SOP）**，存於檔案內，供 Agent 依循 | 活動一 `@.cursor/skills/meeting-minutes/`；活動二 `file-organizer` |
| **Rules（長期規範）** | 整個專案須遵守的 **語氣與格式**（例如繁體中文書面語） | 培訓包 `.cursor/rules/`；活動二資料夾內亦有 |
| **MCP（連線服務）** | 供 AI **標準化** 讀寫本機檔案、Google Drive 等；可理解為「標準化連接介面」 | 課堂活動二 **無需** 使用；課後可試 Filesystem／Drive（見 04、06、09） |
| **Model（模型）** | 背後運算引擎；課堂請選 **Auto** | 全課 Agent；活動一轉錄使用 **Whisper**（本機程式，與聊天模型不同） |

**總結：** 本培訓並非培養程式開發人員，而是培養 **工作流設計** 能力 — Cursor 為目前適用的操作平台。

---

## 排版文字（`.md`）是什麼？

| 所見符號 | 實際意義 | 相當於 Word 的 |
|----------|----------|----------------|
| `# 標題` | 一級標題 | 標題 1 |
| `## 小標` | 二級標題 | 標題 2 |
| `**粗體**` | 粗體 | 粗體 |
| `\| 欄 \| 欄 \|` 表格 | 表格 | 插入表格 |

- 副檔名 **`.md`** 即 **排版文字**（Markdown），以文字符號標示版面，並非檔案損壞或亂碼。
- **活動一：** Agent 先產出 `.md` 草稿以便修訂；再轉為 **Word（`.docx`）** 供正式開啟、簽署及歸檔。
- **建議掌握的操作（無需背誦符號）：**
  1. 於編輯區開啟 `.md` 檔
  2. 按 **`Ctrl + Shift + V`**（Mac：`Cmd + Shift + V`）→ **預覽**，右側呈現近似正式文件
  3. 確認無誤後 **複製** 預覽內容 → 貼至 Word；或直接使用 Agent 產出的 `.docx`

> 💡 **貼至 Word／Excel：** 點擊右上方 **Copy**，直接開啟 Word 貼上即可；表格可先貼至 Word 再複製至 Excel。

---

## Workflow（工作流）與 Agentic Workflow

**傳統做法（Chatbot）：** 提問一句 → 回覆一句 → 自行抄錄至 Word。

**工作流做法（Workflow）：** 清楚說明 **輸入、步驟、產出**，由 Agent 逐步執行，**每一步均須您批准**。

```
範例（活動一）：
  輸入：錄音 + 議程 + 範本
  步驟：轉文字 → 依 SKILL 撰寫紀錄 → 轉為 Word
  產出：會議紀錄 .docx（由您覆核）
```

活動二另增：**先商討、不移動檔案** → 訂立規則 → **一次執行整理** — 均屬同一工作流思維。

---

## SKILL 是什麼？為何 Prompt 要 `@` 引用？

- **SKILL** = 存放於 `.cursor/skills/某名稱/SKILL.md` 的 **專用工作指引**（類似科組「撰寫會議紀錄 SOP」）。
- Prompt 寫 `@.cursor/skills/meeting-minutes/SKILL.md` 即要求 Agent：**依該 SOP 執行**，無需每次重複說明欄位與語氣。
- **您無需自行撰寫 SKILL** 亦可完成活動；培訓包已預先備妥。課後可請 Agent 協助編寫科組專用 SKILL。

**與 Rules 的分別：**

| | SKILL | Rules |
|--|-------|-------|
| 用途 | 某一類任務（會議紀錄、整理檔案） | 全專案語氣、用詞 |
| 位置 | `.cursor/skills/.../SKILL.md` | `.cursor/rules/*.mdc` |
| 比喻 | 科組專用表格範本 | 校內公文書寫規範 |

---

## MCP（Model Context Protocol）是什麼？

- **說明：** 一套 **共通連接標準**，使 AI 能以相同方式讀寫 **本機檔案**、**Google Drive** 等。
- **比喻：** 標準化「連接埠」— 連接至指定位置（通常僅限您授權的資料夾，較具安全性）。
- **本培訓包：**
  - **Filesystem MCP** — 讀寫專案內檔案（課後試用 → [`04-filesystem-mcp-guide.md`](04-filesystem-mcp-guide.md)）
  - **Google Drive MCP** — 讀寫雲端 Drive（課後 → [`06`](06-google-drive-mcp-setup.md) + [`09`](09-google-drive-self-study.md)）
- **課堂活動二** 使用 Agent **內建**讀寫 `activity-2-files/`，**無需啟用 MCP** 即可完成。

**如何確認 MCP 已啟用？** 開啟 Cursor **Settings → MCP** → 顯示 **Connected（綠色）**。

---

## Agent、Chat、Vibe Coding

| 名稱 | 功能 | 本課用途 |
|------|------|----------|
| **Agent** | 可讀寫檔案、執行指令、多步驟作業 | **主要使用**（`Ctrl + I`） |
| **Chat** | 以問答為主，較少自動修改檔案 | 較少使用（`Ctrl + L`） |
| **Vibe Coding** | 以**自然語言**描述所需介面／功能，由 Agent 產出網頁或程式 | 活動三：描述「功課命名器」→ 產出 HTML |

**Allow／批准：** Agent 於修改檔案或執行終端機指令前會徵詢您 — **務必按批准後方繼續**（安全機制）。

**`@` 引用檔案：** 輸入 `@` 選擇檔案 = 將該檔提供予 Agent 查閱，無需整段複製貼上（等同「提供正確卷宗予協理同事」）。

---

## 其他常見檔案與資料夾

| 名稱 | 說明 |
|------|------|
| **Open Folder** | 以 Cursor 開啟**整個培訓資料夾**，Agent 方可讀寫其中檔案 |
| **Project／資料夾** | 本日開啟的 `chw-staff-training-20260605` 資料夾 |
| **`.cursor/`** | 存放 Rules、Skills、MCP 設定的設定目錄 |
| **`.docx`** | Word 正式檔 |
| **`.html`／`.css`／`.js`** | 活動三網頁三件套；以瀏覽器開啟 `index.html` 預覽 |
| **Whisper** | 活動一轉錄所用**本機程式**（非 Cursor 聊天模型） |
| **Auto（Model）** | Cursor 自動選擇合適模型；課堂使用此項即可 |

---

## 課堂與課後 — 講義對照

| 欲了解… | 請查閱 |
|--------|--------|
| 安裝、Demo Login | [`08-appendix-安裝清單.md`](08-appendix-安裝清單.md) |
| 快捷鍵、Auto | [`01-cursor-setup-guide.md`](01-cursor-setup-guide.md) |
| 三項活動 Prompt | [`02-prompt-cheatsheet.md`](02-prompt-cheatsheet.md) |
| MCP 試用 | [`04-filesystem-mcp-guide.md`](04-filesystem-mcp-guide.md) |
| API Key、Ollama | [`03-faq-hk-guide.md`](03-faq-hk-guide.md)、[`05`](05-api-key-application-guide.md) |
| 網站上線 | [`07-static-site-publish.md`](07-static-site-publish.md) |
| 閱讀次序 | [`README.md`](README.md) |

---

*講者開場詳述見 [`trainer/talking-points.md`](../trainer/talking-points.md)；排版文字預覽示範見 [`trainer/demo-chaotic-transcript/markdown-preview-walkthrough.md`](../trainer/demo-chaotic-transcript/markdown-preview-walkthrough.md)。*
