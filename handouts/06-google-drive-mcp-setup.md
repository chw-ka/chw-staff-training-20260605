# Google Drive MCP 設定指南 — 活動二【雲端神蹟】

> 課前必做（約 20–30 分鐘，只需做一次）。完成後 Agent 可直接整理你 Google Drive 裡面的檔案。

---

## 你需要什麼？

- Google 帳號（個人 Gmail 或學校 Google Workspace）
- Node.js 18+（與 Cursor 一樣需要 `npx`）
- Google Cloud 免費 project（用來做 OAuth，不必付費）

---

## Step 1：Google Cloud Project

1. 開啟 https://console.cloud.google.com
2. **Select a project** → **New Project**
3. 名稱例如：`CHW Cursor Training` → Create

---

## Step 2：啟用 Google Drive API

1. **APIs & Services** → **Library**
2. 搜尋 **Google Drive API** → **Enable**
3. （可選）同時 enable：Google Docs API、Sheets API — MCP 套件會用到

---

## Step 3：OAuth 同意畫面

1. **APIs & Services** → **OAuth consent screen**
2. User type：
   - 學校 Google Workspace → 可選 **Internal**（較簡單）
   - 個人 Gmail → 選 **External**，並加自己做 **Test user**
3. App name：`CHW Drive MCP`（任意）
4. User support email：你的 email
5. Scopes：可先跳過，首次 auth 時會請求

---

## Step 4：建立 OAuth Client ID

1. **APIs & Services** → **Credentials**
2. **+ CREATE CREDENTIALS** → **OAuth client ID**
3. Application type：**Desktop app**（重要！）
4. Name：`CHW Drive MCP Client` → Create
5. Download JSON

---

## Step 5：放入 project

1. 將下載的 JSON 複製到：
   ```
   config/gcp-oauth.keys.json
   ```
2. 或參考 [`config/gcp-oauth.keys.example.json`](../config/gcp-oauth.keys.example.json) 格式
3. ⚠️ **勿 commit** 此檔（已在 `.gitignore`）

---

## Step 6：首次 OAuth 登入

在 terminal 執行：

```bash
cd chw-staff-training-20260605
export GOOGLE_DRIVE_OAUTH_CREDENTIALS="$(pwd)/config/gcp-oauth.keys.json"
npx -y @piotr-agier/google-drive-mcp auth
```

1. 瀏覽器會彈出 Google 登入
2. 選你的帳號 → 允許存取 Drive
3. 成功後 token 儲存在 `~/.config/google-drive-mcp/tokens.json`

---

## Step 7：確認 Cursor MCP

本 project 已包含 `.cursor/mcp.json`。Reload Cursor 後：

1. **Cursor Settings** → **MCP**
2. 確認 **google-drive** 顯示 **Connected**（綠色）
3. 若紅色：檢查 `config/gcp-oauth.keys.json` 路徑

### mcp.json 設定（參考）

```json
{
  "mcpServers": {
    "google-drive": {
      "command": "npx",
      "args": ["-y", "@piotr-agier/google-drive-mcp"],
      "env": {
        "GOOGLE_DRIVE_OAUTH_CREDENTIALS": "/你的路徑/config/gcp-oauth.keys.json"
      }
    }
  }
}
```

---

## Step 8：建立 Demo 垃圾崗

1. 開 https://drive.google.com
2. 新建 folder：**CHW_Training_垃圾崗**
3. 上傳 [`activity-2-gdrive/samples/`](../activity-2-gdrive/samples/) 內 4 個亂碼檔

---

## Step 9：測試 MCP

Agent（`Cmd/Ctrl + I`）輸入：

```
用 Google Drive MCP listFolder 列出「CHW_Training_垃圾崗」裡面有哪些檔案。
```

有列出 4 個亂碼檔 → ✅ 準備完成

---

## 常見問題

| 問題 | 解決 |
|------|------|
| `redirect_uri_mismatch` | OAuth client 必須是 **Desktop app** 類型 |
| MCP 紅色 / 連不到 | 重新跑 `npx @piotr-agier/google-drive-mcp auth` |
| 「Access blocked」 | External app 要加自己做 Test user |
| Token 7 日過期 | OAuth app 仍是 Testing 狀態；重新 auth 或 publish app |
| 校園封 OAuth | 用個人 hotspot 試；或改用本地 Watchdog 備用方案 |

---

## 安全提示

- 只授權**你自己**的 Drive
- 課堂只用 **CHW_Training_*** 測試 folder
- 不要把 `gcp-oauth.keys.json` 或 token 分享給他人

---

## 下一步

→ 課堂跟 [`activity-2-gdrive/sample-prompts.md`](../activity-2-gdrive/sample-prompts.md) 執行【雲端神蹟】
