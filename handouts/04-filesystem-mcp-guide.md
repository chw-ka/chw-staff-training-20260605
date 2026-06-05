# Filesystem MCP 試玩指南

> 本專案已設定 `@modelcontextprotocol/server-filesystem` 與 **Google Drive MCP**。  
> **課堂活動二**為本機整理 — 見 [`activity-2-files/`](../activity-2-files/)。  
> 本指南供課餘試用 Filesystem MCP；Google Drive 見 [`09-google-drive-self-study.md`](09-google-drive-self-study.md)。

---

## 啟用方法

1. 確認已安裝 **Node.js**（需要 `npx`）
2. 以 Cursor **重新開啟**此專案（或 `Cmd/Ctrl + Shift + P` → **Reload Window**）
3. 開啟 **Cursor Settings → MCP**，確認 `filesystem` 顯示 **Connected**（綠色）
4. 於 Agent 視窗（`Cmd/Ctrl + I`）試用下列 Prompt

---

## Filesystem MCP 有何用途？

它為 Agent 提供一組**標準化**檔案工具，無需依賴終端機亦可：

| 工具 | 功能 | 課堂用途 |
|------|------|----------|
| `list_directory` | 列出資料夾內容 | 檢視 `inbox/` 內檔案 |
| `list_directory_with_sizes` | 列出檔案連同大小 | 找出大型檔案、清理下載項目 |
| `directory_tree` | 整個資料夾樹狀圖 | 快速了解專案結構 |
| `search_files` | 按 pattern 搜尋檔案 | 找出所有 `.jpg`／`IMG_*` |
| `read_text_file` | 讀取文字檔 | 讀取會議逐字稿 |
| `read_multiple_files` | 一次讀取多個檔案 | 同時讀取逐字稿與範本 |
| `read_media_file` | 讀取圖片／音頻（base64） | 檢視學生提交之圖像 |
| `get_file_info` | 查詢檔案大小、修改日期 | 確認下載是否完成 |
| `write_file` | 寫入新檔／覆蓋 | 輸出紀錄草稿 |
| `edit_file` | 精準修改某段文字 | 修訂紀錄某一節 |
| `move_file` | 搬移／重新命名 | 本機檔案整理（補充練習） |
| `create_directory` | 建立資料夾 | 自動建立 `sorted/視覺藝術/` |
| `list_allowed_directories` | 檢視 MCP 可存取範圍 | 確認 sandbox 設定 |

### 與 Cursor 內建能力有何分別？

| | Cursor Agent 內建 | Filesystem MCP |
|--|-------------------|----------------|
| 讀寫專案檔 | ✅ 可以 | ✅ 可以（限定目錄） |
| 標準工具介面 | 混於 Agent 工具中 | 獨立 MCP tools，可接其他 client |
| 安全 sandbox | 依 Cursor 權限 | **明確限定**可讀寫的資料夾 |
| 跨應用程式重用 | ❌ | ✅ 同一 MCP 可接 Claude Desktop 等 |

**培訓重點：** MCP 即標準化連接協議 — 同一套檔案工具，不同 AI 均可使用。

---

## 試玩 Prompt（由淺入深）

### 1. 檢視允許範圍

```
請使用 filesystem MCP 的 list_allowed_directories，告知目前可存取哪些資料夾。
```

### 2. 列出 inbox 示範檔

```
請使用 MCP 列出 activity-2-files/inbox/ 內所有檔案，以及各檔大小。
```

### 3. 搜尋特定檔案

```
請使用 MCP search_files 在 activity-2-files/inbox/ 搜尋所有 .jpg 與 .pdf。
```

### 4. 讀取會議逐字稿

```
請使用 MCP read_text_file 讀取 activity-1-minutes/sample-meeting-transcript.txt 前 20 行，並以繁體中文書面語摘要。
```

### 5. 模擬搬移檔案（無需 Python）

```
請使用 filesystem MCP：
1. 讀取 activity-2-files/my_organization_profile.example.md 前 20 行
2. 於 activity-2-files/sorted/教學/2025-2026/ 建立測試資料夾（若尚未存在）
3. 將 activity-2-files/inbox/ 內任一 .png 複製或移動至上述資料夾（檔名加前綴 test_）
4. 列出目標資料夾以確認結果
```

### 6. 活動二資料夾樹狀圖

```
請使用 MCP directory_tree 顯示 activity-2-files/ 的結構（depth 2 即可）。
```

---

## 安全設定說明

本培訓包的 `.cursor/mcp.json` 將 Filesystem MCP 限於**整個專案資料夾**（`${workspaceFolder}`）。

Agent **無法**透過此 MCP 讀取您電腦上的桌面、個人下載資料夾或校內其他路徑 — 此即 MCP sandbox 之意義。  
課堂活動二整理請使用 [`activity-2-files/`](../activity-2-files/)（Agent 內建讀寫，無需 MCP）。

---

## 常見問題

**問：MCP 顯示紅色／Disconnected**  
答：請檢查 Node.js 是否已安裝（`npx --version`）；Reload Window；查閱 MCP log。

**問：提示找不到 path**  
答：必須使用專案內的相對或絕對路徑；Windows 使用者或須調整 `.cursor/mcp.json` 內的路徑。

**問：與活動二有何分別？**  
答：課堂活動二使用 **Agent 整理專案內 `activity-2-files/`**（無需 MCP）。Filesystem MCP 適合課餘試用；Google Drive 見 [`09-google-drive-self-study.md`](09-google-drive-self-study.md)。

---

## 課堂示範建議（5 分鐘）

1. Settings → MCP → 展示 `filesystem` connected
2. Prompt 2：列出 inbox 內檔案
3. Prompt 5：即場搬移並重新命名一個檔案
4. 對比：「此即 MCP 標準化連接 — 無需開啟檔案總管，無需自行撰寫程式」
