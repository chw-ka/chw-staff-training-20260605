# Google Drive MCP 設定指南 — 課後自學用

> **90 分鐘課堂不進行此設定。** 課堂活動二為本機文件整理（[`activity-2-files/`](../activity-2-files/)）。  
> 本指南供**課後自學**依 [`09-google-drive-self-study.md`](09-google-drive-self-study.md) 完成（約 20–30 分鐘，僅需設定一次）。完成後 Agent 可直接整理您 Google Drive 內的檔案。

---

## 您需要什麼？

- Google 帳號（個人 Gmail 或學校 Google Workspace）
- Node.js 18+（與 Cursor 同樣需要 `npx`）
- Google Cloud 免費專案（用於 OAuth，無需付費）

---

## Step 1：Google Cloud Project

1. 開啟 https://console.cloud.google.com
2. **Select a project** → **New Project**
3. 名稱例如：`CHW Cursor Training` → Create

---

## Step 2：啟用 Google Drive API

1. **APIs & Services** → **Library**
2. 搜尋 **Google Drive API** → **Enable**
3. （可選）同時啟用：Google Docs API、Sheets API — MCP 套件會用到

---

## Step 3：OAuth 同意畫面

1. **APIs & Services** → **OAuth consent screen**
2. User type：
   - 學校 Google Workspace → 可選 **Internal**（較簡單）
   - 個人 Gmail → 選 **External**，並將自己加為 **Test user**
3. App name：`CHW Drive MCP`（任意）
4. User support email：您的 email
5. Scopes：可先跳過，首次授權時會請求

---

## Step 4：建立 OAuth Client ID

1. **APIs & Services** → **Credentials**
2. **+ CREATE CREDENTIALS** → **OAuth client ID**
3. Application type：**Desktop app**（重要！）
4. Name：`CHW Drive MCP Client` → Create
5. Download JSON

---

## Step 5：放入專案

1. 將下載的 JSON 複製至：
   ```
   config/gcp-oauth.keys.json
   ```
2. 或參考 [`config/gcp-oauth.keys.example.json`](../config/gcp-oauth.keys.example.json) 格式
3. ⚠️ **請勿 commit** 此檔（已在 `.gitignore`）

---

## Step 6：首次 OAuth 登入

於 terminal 執行：

```bash
cd chw-staff-training-20260605
export GOOGLE_DRIVE_OAUTH_CREDENTIALS="$(pwd)/config/gcp-oauth.keys.json"
npx -y @piotr-agier/google-drive-mcp auth
```

1. 瀏覽器將彈出 Google 登入
2. 選擇您的帳號 → 允許存取 Drive
3. 成功後 token 儲存於 `~/.config/google-drive-mcp/tokens.json`

---

## Step 7：確認 Cursor MCP

本專案已包含 `.cursor/mcp.json`。Reload Cursor 後：

1. **Cursor Settings** → **MCP**
2. 確認 **google-drive** 顯示 **Connected**（綠色）
3. 若顯示紅色：請檢查 `config/gcp-oauth.keys.json` 路徑

### mcp.json 設定（參考）

```json
{
  "mcpServers": {
    "google-drive": {
      "command": "npx",
      "args": ["-y", "@piotr-agier/google-drive-mcp"],
      "env": {
        "GOOGLE_DRIVE_OAUTH_CREDENTIALS": "/您的路徑/config/gcp-oauth.keys.json"
      }
    }
  }
}
```

---

## Step 8：建立示範資料夾

1. 開啟 https://drive.google.com
2. 新建資料夾：**CHW_Training_示範整理**
3. 上傳 [`activity-5-gdrive/samples/`](../activity-5-gdrive/samples/) 內 4 個示範檔

---

## Step 9：測試 MCP

於 Agent（`Cmd/Ctrl + I`）輸入：

```
請使用 Google Drive MCP listFolder 列出「CHW_Training_示範整理」內有哪些檔案。
```

若列出 4 個示範檔 → ✅ 準備完成

---

## 常見問題

| 問題 | 解決 |
|------|------|
| `redirect_uri_mismatch` | OAuth client 必須為 **Desktop app** 類型 |
| MCP 紅色／無法連接 | 重新執行 `npx @piotr-agier/google-drive-mcp auth` |
| 「Access blocked」 | External app 須將自己加為 Test user |
| Token 7 日過期 | OAuth app 仍為 Testing 狀態；請重新授權或 publish app |
| 校園封鎖 OAuth | 可嘗試個人 hotspot；或改用本機備用方案 |

---

## 安全提示

- 僅授權**您本人**的 Drive
- 課堂僅使用 **CHW_Training_*** 測試資料夾
- 請勿將 `gcp-oauth.keys.json` 或 token 分享予他人

---

## 下一步

→ 依 [`activity-5-gdrive/sample-prompts.md`](../activity-5-gdrive/sample-prompts.md) 進行雲端整理練習
