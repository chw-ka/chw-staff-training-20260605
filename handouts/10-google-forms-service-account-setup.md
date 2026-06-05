# 課後回饋問卷 — Google Forms（Service Account 自動建立）

> **對象：** 講者／資訊科技組（非一般學員講義）  
> **用途：** 以 GCP Service Account 透過 API 建立 Google Forms，再將編輯權分享予您的 Google 帳戶。  
> **帳戶：** `staff-training-form-creation@staff-training-498501.iam.gserviceaccount.com`  
> **GCP Project：** `staff-training-498501`

---

## 您須準備什麼？

| 項目 | 說明 |
|------|------|
| GCP 專案 | 已有 `staff-training-498501` |
| Service Account | 已有上述電郵；尚需 **下載 JSON 金鑰** |
| 本機 | Python 3.10+、`pip` |
| 學校 Google Workspace（建議） | 設定 **網域範圍授權**，問卷將出現於您帳戶的 Drive |
| 個人 Gmail（進階） | 可不設授權，但問卷屬機械帳戶，須依分享連結編輯 |

⚠️ **切勿** 將 JSON 金鑰 commit 至 Git、貼至 WhatsApp 或傳予學員。

---

## 與 OAuth／API Key 的分別（講者速查）

| 方式 | 何時用 | 本問卷 |
|------|--------|--------|
| **API Key**（Gemini 等） | 呼叫 AI 模型 | ❌ 不適用 |
| **OAuth**（`06` Drive MCP） | 以**您本人**登入操作 Drive | 可整理檔案；Forms MCP 不包含 |
| **Service Account** | 伺服器／腳本代為呼叫 Google API | ✅ 本指南 |

---

## Step 1：啟用 API

1. 開啟 https://console.cloud.google.com → 選擇 project **`staff-training-498501`**
2. **APIs & Services** → **Library**
3. 啟用：
   - **Google Forms API**
   - **Google Drive API**（用於將表格**分享**予您編輯）

---

## Step 2：確認 Service Account 並下載金鑰

1. **IAM & Admin** → **Service Accounts**
2. 點選 `staff-training-form-creation@staff-training-498501.iam.gserviceaccount.com`
3. **Keys** → **Add key** → **Create new key** → **JSON** → 下載
4. 將檔案複製為（檔名固定方便腳本讀取）：

   ```
   config/gcp-service-account.json
   ```

5. 對照 [`config/gcp-service-account.example.json`](../config/gcp-service-account.example.json) 確認 `client_email` 正確

---

## Step 3：學校 Google Workspace — 網域範圍授權（強烈建議）

若您使用 **學校 @chw.edu.hk**（或同網域）帳戶管理問卷，請校內 Google **超級管理員**執行一次：

1. Google Admin → **安全性** → **存取權和資料控制** → **API 控制** → **網域範圍授權**
2. **新增** → Client ID 填 Service Account 的 **數字 Client ID**（於金鑰 JSON 的 `client_id` 欄位，並非電郵）
3. OAuth 範圍（逐行貼上）：

   ```
   https://www.googleapis.com/auth/forms.body
   https://www.googleapis.com/auth/drive
   ```

4. **授權**

完成後，腳本將以您的帳戶身份建立問卷（見 Step 5 環境變數 `GOOGLE_FORMS_DELEGATED_USER`）。

---

## Step 4：安裝 Python 套件

於培訓資料夾開啟終端機：

```powershell
cd C:\Users\localadmin\Projects\chw-staff-training-20260605
pip install -r scripts/requirements-google-forms.txt
```

---

## Step 5：執行建立問卷

### 5a. Workspace（有網域授權）

PowerShell：

```powershell
$env:GOOGLE_APPLICATION_CREDENTIALS = "$PWD\config\gcp-service-account.json"
$env:GOOGLE_FORMS_DELEGATED_USER = "您的學校Gmail@chw.edu.hk"
python scripts/create_feedback_form.py
```

### 5b. 無網域授權（問卷在 Service Account 名下）

```powershell
$env:GOOGLE_APPLICATION_CREDENTIALS = "$PWD\config\gcp-service-account.json"
$env:GOOGLE_FORMS_SHARE_WITH = "您的Gmail@chw.edu.hk"
python scripts/create_feedback_form.py
```

腳本將嘗試把**編輯權**分享予 `GOOGLE_FORMS_SHARE_WITH`（可與上述 delegated 相同）。

成功後終端機將顯示：

- **填寫連結**（`responderUri`）→ 提供予同事
- **編輯連結** → 供您修改題目、設定「每人限填一次」等

---

## Step 6：表單設定（建議手動補一次）

API 目前較難設定「每人限填一次」。請於 Google Forms 網頁：

1. 開啟編輯連結
2. **設定** → 開啟 **限制每人回應次數 1 次**（需登入 Google）
3. 確認 **不收集電郵**（若希望匿名）
4. **傳送** → 短連結 → 放於簡報最後一頁

---

## 常見問題

| 問題 | 可能原因 | 處理 |
|------|----------|------|
| `403`／`Permission denied` | 未啟用 Forms API；或無網域授權 | 檢查 Step 1、3 |
| `invalid_grant`／delegation | Client ID 或 scope 錯誤 | 核對 Admin 授權範圍 |
| 找不到 `gcp-service-account.json` | 金鑰未放至 `config/` | 見 Step 2 |
| 同事無法開啟填寫連結 | 未發佈／權限不足 | 於 Forms 按「傳送」取得公開連結 |
| 問卷出現於「陌生」帳戶 | 未完成 Step 3 | 設定 `DELEGATED_USER` 或依 `SHARE_WITH` 分享 |

---

## Plan B：Admin 無法 Authorize（你而家嘅情況）

若 **View Google Workspace Admin console** 只見 **Manage Google services**／**Manage app access**，冇 **Add new**／**Authorize**：

- 你**唔係 Super Admin**，或學校**隱藏** Domain-wide delegation  
- **Service Account 路線暫時走唔通**（唔係你做錯）

### 改用 OAuth（你自己登入一次，建議）

1. GCP project `staff-training-498501`：
   - 啟用 **Google Forms API**
   - **OAuth consent screen** → Internal（Workspace）或 External + Test user
   - **Credentials** → **OAuth client ID** → **Desktop app** → 下載 JSON → `config/gcp-oauth.keys.json`
   - Consent screen 加 scopes：`forms.body`、`drive`（或執行時會請求）
2. 本機執行：

```powershell
pip install -r scripts/requirements-google-forms.txt
python scripts/create_feedback_form_oauth.py
```

3. 瀏覽器用 **`kalun.chan@chw.edu.hk`** 登入並允許  
4. 問卷會出現在你自己 Drive，唔使 Admin Authorize

### Plan C：手動開表（最快）

https://forms.google.com → 照 `create_feedback_form.py` 內題目逐條加入

---

## 安全提示

- JSON 金鑰等同密碼；外洩即他人可代您建立表單
- 課後若不再使用，可於 GCP **刪除該金鑰** 並重新建立
- 已列入 `.gitignore`：`config/gcp-service-account.json`

---

## 下一步

- 修改題目：編輯 `scripts/create_feedback_form.py` 內 `QUESTIONS`，再執行腳本（將**新建**另一份表單；舊表單保留）
- 收集結果：Forms → **回應** → 連結試算表
