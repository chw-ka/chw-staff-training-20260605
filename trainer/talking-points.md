# 講者 Talking Points — 各時段核心概念

---

## 00–10 min｜引入：AI 2026 變革

### 要講的三個重點

1. **從 Chatbot 到 Agent** — 舊：一問一答；新：多步驟、自動執行
2. **Agentic Workflow** — 老師做「工作流設計師」
3. **今日三個 Activity** — Minutes（API）→ Drive 整理（雲端 MCP）→ MARP（多模態）

---

## 10–20 min｜環境準備

- Gemini + DeepSeek Key 填入 Cursor
- **加多一步：** Google Drive MCP OAuth（06 handout）
- DeepSeek 填「OpenAI 欄」是兼容接口，不是 OpenAI

---

## 20–40 min｜活動一：Minutes

- API 打破字數限制
- SKILL = reusable 規則
- Model：**deepseek-v4-flash**
- AI 起草，你覆核

---

## 40–65 min｜活動二：【雲端神蹟】

### 核心概念

| 概念 | 解釋 |
|------|------|
| **MCP** | 隨意門 — 今次連 **Google Drive**，不是本機 |
| **雲端 Automation** | Agent 直接 rename / move 雲端檔 |
| **Approve** | 每次改 Drive 前你批准 — 安全又可即時觀看 |

### 教學節奏

1. （3 min）MCP 概念 + 對比「本地執 file vs 雲端」
2. （2 min）並排開 Cursor + drive.google.com
3. （3 min）確認垃圾崗有 4 個亂碼檔
4. （12 min）貼 Prompt → 逐次 Approve → 全班驚呼
5. （5 min）討論：Shared Drive、學校政策、私隱

### Wow 話術

> 「你不用寫一行 code。按 Approve，回去 browser — 檔案自己動。這就是雲端 MCP。」

### 與本地 Watchdog 分別

| | 本地 Watchdog | Google Drive MCP |
|--|---------------|------------------|
| 視覺 | Terminal 輸出 | **Browser 即時見** |
| 範圍 | 本機 folder | 雲端 Drive |
| 設定 | Python + pip | OAuth 一次 |
| 衝擊力 | 中 | **滿分** |

---

## 65–85 min｜活動三：MARP

- Model：**gemini-2.5-flash**
- 讀活動一 minutes → 出簡報

---

## 85–90 min｜總結

- 私隱：敏感資料用 Ollama；Drive MCP 只用測試 folder
- 老師 = 工作流總設計師
