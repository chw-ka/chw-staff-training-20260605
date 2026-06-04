# Filesystem MCP 試玩指南

> 本 project 已設定 `@modelcontextprotocol/server-filesystem` 與 **Google Drive MCP**。  
> **活動二主線**用 Google Drive — 見 [`06-google-drive-mcp-setup.md`](06-google-drive-mcp-setup.md)

---

## 啟用方法

1. 確認已安裝 **Node.js**（需要 `npx`）
2. 用 Cursor **重新開啟**此 project（或 `Cmd/Ctrl + Shift + P` → **Reload Window**）
3. 開啟 **Cursor Settings → MCP**，確認 `filesystem` 顯示 **Connected**（綠色）
4. 在 Agent 視窗（`Cmd/Ctrl + I`）試下面的 Prompt

---

## Filesystem MCP 有什麼用？

它讓 Agent 一組**標準化**的檔案工具，不必靠 terminal 也可以：

| 工具 | 做什麼 | 課堂用途 |
|------|------|----------|
| `list_directory` | 列出 folder 內容 | 看 `inbox/` 有哪些亂碼檔 |
| `list_directory_with_sizes` | 列出檔案連大小 | 找大檔、清理 Downloads |
| `directory_tree` | 整個 folder 樹狀圖 | 快速了解 project 結構 |
| `search_files` | 按 pattern 搜尋檔案 | 找所有 `.jpg` / `IMG_*` |
| `read_text_file` | 讀文字檔 | 讀 meeting transcript |
| `read_multiple_files` | 一次讀多個檔 | 同時讀 transcript + template |
| `read_media_file` | 讀圖片/音頻（base64） | 看學生交的功課相 |
| `get_file_info` | 查檔案大小、修改日期 | 確認下載是否完成 |
| `write_file` | 寫新檔 / 覆蓋 | 輸出 minutes 草稿 |
| `edit_file` | 精準改某段文字 | 改 minutes 某一節 |
| `move_file` | 搬移 / 重新命名 | 本機檔案整理（補充練習） |
| `create_directory` | 建立 folder | 自動建 `sorted/視覺藝術/` |
| `list_allowed_directories` | 看 MCP 可存取範圍 | 確認 sandbox 設定 |

### 與 Cursor 內建能力有什麼分別？

| | Cursor Agent 內建 | Filesystem MCP |
|--|-------------------|----------------|
| 讀寫 project 檔 | ✅ 可以 | ✅ 可以（限定目錄） |
| 標準工具介面 | 混在 Agent 工具裡面 | 獨立 MCP tools，可接其他 client |
| 安全 sandbox | 靠 Cursor 權限 | **明確限定**可讀寫的 folder |
| 跨 app 重用 | ❌ | ✅ 同一 MCP 可接 Claude Desktop 等 |

**培訓重點：** MCP 就是「隨意門協議」—— 同一套 file 工具，不同 AI 都可用。

---

## 試玩 Prompt（由淺入深）

### 1. 看允許範圍

```
用 filesystem MCP 的 list_allowed_directories，告訴我現在可以存取哪些 folder。
```

### 2. 列出亂碼功課

```
用 MCP 列出 activity-2-watchdog/downloads/ 裡面所有檔案，以及每個檔的大小。
```

### 3. 搜尋特定檔案

```
用 MCP search_files 在 activity-2-watchdog/ 找所有 .jpg 與 .pdf。
```

### 4. 讀取會議逐字稿

```
用 MCP read_text_file 讀 activity-1-minutes/sample-meeting-transcript.txt 的頭 20 行，用繁體中文書面語 summarize。
```

### 5. 模擬自動執檔（不必 Python）

```
用 filesystem MCP：
1. 讀取 activity-2-watchdog/rename_rules.example.json
2. 將 downloads/IMG_8742.jpg move 去 sorted/視覺藝術/【功課】_張小明_視覺藝術.jpg
3. 確認 sorted/ 裡面結果
```

### 6. 整個 project 樹狀圖

```
用 MCP directory_tree 顯示 activity-2-watchdog/ 的結構（exclude __pycache__ 與 .venv）。
```

---

## 安全設定說明

`.cursor/mcp.json` 只允許存取以下目錄：

- 整個培訓 project root
- `activity-2-watchdog/inbox/`
- `activity-2-watchdog/downloads/`
- `activity-2-watchdog/sorted/`

Agent **不能**透過此 MCP 讀你的 Desktop、Downloads 或校內其他路徑 — 這就是 MCP sandbox 的意義。

---

## 常見問題

**Q：MCP 顯示紅色 / Disconnected**  
A：檢查 Node.js 是否已安裝（`npx --version`）；Reload Window；看 MCP log。

**Q：話找不到 path**  
A：必須用 project 內的相對或絕對路徑；Windows 同事要改 `.cursor/mcp.json` 裡面的 path。

**Q：與 Activity 2 有什麼分別？**  
A：活動二用 **Google Drive MCP**（雲端，browser 即時看）。Filesystem MCP 只動本機 project，適合課餘試玩。

---

## 課堂演示建議（5 分鐘）

1. Settings → MCP → 展示 `filesystem` connected
2. Prompt 2：列出 downloads 亂碼檔
3. Prompt 5：即場 move 一個檔改名
4. 對比：「這就是 MCP 隨意門 — 不必開 Finder，不必寫 code」
