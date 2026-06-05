# 靜態網站發佈指南 — 活動三【teacher.chw.edu.hk】

> 配合「活動三：生成 HTML + CSS + JS」。  
> 學校已提供 **teacher.chw.edu.hk**：您將靜態檔放入 NAS 上的 `_web` 資料夾，網站即會對外提供 HTTPS 網址。

---

## 說明：為何不是 Google Drive？

- Google Drive **本身不會**作為網站執行 HTML／JS（通常僅預覽或下載）
- CHW 教師網站架構為：**NAS 共享資料夾 → 校內伺服器 nginx → 公開網址**
- 因此您只需準備 **一個資料夾內僅含靜態檔**（HTML／CSS／JS／圖片）

---

## 架構一覽

```
您的電腦（P:\KA\_web\）
        ↓  儲存檔案
NAS（//10.10.0.13/staff/KA/_web/）
        ↓  伺服器自動讀取
公開網址（https://teacher.chw.edu.hk/KA/）
```

| 公開網址 | NAS 實際路徑 |
|----------|--------------|
| `https://teacher.chw.edu.hk/KA/index.html` | `//10.10.0.13/staff/KA/_web/index.html` |
| `https://teacher.chw.edu.hk/ka/index.html` | 同一檔案（網址**不分大小寫**） |

> NAS 上的資料夾名請保持**大寫**（例如 `KA`），網址大小寫均可。

---

## 您需要什麼？

- 學校 NAS 存取權（`//10.10.0.13/staff`）
- 您的**教師代碼資料夾**（例如 `KA`、`LC` — 即 staff share 內屬於您的資料夾）
- 名為 `_web` 的子資料夾（網站根目錄）
- 活動三產出的靜態檔（`index.html` 等）

---

## Step 1：連接 NAS（Windows）

1. 開啟 **檔案總管**
2. 上方選 **⋯** → **連線網路磁碟機**（或右鍵「本機」→「連線網路磁碟機」）
3. 資料夾輸入：
   ```
   \\10.10.0.13\staff
   ```
4. 勾選「使用不同的認證連線」（如學校要求）
5. 完成後可能顯示為 `P:\` 或其他磁碟代號

> 若您平時已 map 好 `P:\`，可直接使用現有連線。

---

## Step 2：建立 `_web` 資料夾

於您的教師資料夾內建立 `_web`（若尚未存在）：

```
\\10.10.0.13\staff\{您的代碼}\_web\
```

Windows 已 map 者，例如：

```
P:\KA\_web\
```

**重要：** 必須命名為 `_web`（底線 + web）。若無此資料夾 → 伺服器不會為您建立公開網址。

---

## Step 3：標準輸出格式

將網站檔案直接放入 `_web`（無需再包多一層資料夾）：

```
_web/
├── index.html      ← 入口（必須有）
├── styles.css
├── app.js
└── assets/
    ├── logo.png
    └── illustration.png
```

> 瀏覽器開啟 `https://teacher.chw.edu.hk/{您的代碼}/` 時，會自動載入 `index.html`。

---

## Step 4：發佈前 Checklist

- [ ] 以瀏覽器開啟本機 `index.html`，確認可運作
- [ ] 所有檔案路徑使用**相對路徑**（例如 `styles.css`、`./assets/logo.png`）
- [ ] **避免**使用 `/styles.css` 這類以 `/` 開頭的路徑（會指向網站根目錄，而非您的資料夾）
- [ ] 無需 build、無需 Node server（純靜態）
- [ ] **切勿放入任何 API key**（前端公開檔案不可存放密鑰）

---

## Step 5：上線

1. 將 `index.html`、`styles.css`、`app.js`、`assets/` 等複製至 `_web`
2. 儲存後，NAS 上的檔案會**即時**被伺服器讀取（無需額外 sync）
3. 若您**新建立** `_web` 資料夾，可能須等候最多 **1 小時**（伺服器定時掃描）；急用請聯絡資訊科技組
4. 以瀏覽器開啟：

   ```
   https://teacher.chw.edu.hk/{您的代碼}/index.html
   ```

   或直接：

   ```
   https://teacher.chw.edu.hk/{您的代碼}/
   ```

---

## 活動三完整流程（課堂 + 上線）

1. 依 [`activity-3-web/sample-prompts.md`](../activity-3-web/sample-prompts.md) 以 Agent 產出網站至 `activity-3-web/output/`
2. 於本機開啟 `output/index.html` 預覽
3. **上線（二擇一）：**
   - **Agent 一句話：** 設定好 `activity-3-web/publish.config.json` 後，於 Agent 輸入 **「publish」** 或 **「上線」**
   - **手動：** 將 `output/` 內所有檔案複製至您的 `_web`
4. 以公開網址驗證

### 首次設定 publish（課前或課後做一次）

1. 複製 `activity-3-web/publish.config.example.json` → `activity-3-web/publish.config.json`
2. 填入 `teacher_code`（例如 `KA`）
3. 若已 map NAS 為 `P:\`，可改填 `publish_target_override`：`P:\\KA\\_web`
4. 測試：`python scripts/publish_web.py --dry-run`

---

## 常見問題

| 問題 | 原因／解決 |
|------|-------------|
| 網址顯示 **404** | 未建立 `_web`；或 `_web` 內無 `index.html`；或新資料夾尚未掃描 — 請等候 1 小時或聯絡 IT |
| 改完檔案但網站未更新 | 請嘗試 hard refresh（`Ctrl + Shift + R`）；Cloudflare 可能有 cache，請稍候或聯絡 IT |
| CSS／圖片無法載入 | 請檢查 HTML 是否使用 `/style.css` 等絕對路徑；請改為相對路徑 |
| `/ka/` 與 `/KA/` 有何分別？ | 無分別，均指向同一網站 |
| 為何不可將 API key 寫入 JS？ | 靜態網站為公開檔案，任何人可檢視原始碼；須透過後端或 proxy 使用 API |
| 欲加登入保護？ | 目前 teacher.chw.edu.hk 為公開靜態網站；如有需要請與資訊科技組商討 |

---

## 快速參考卡

```
NAS 路徑：  \\10.10.0.13\staff\{代碼}\_web\
公開網址：  https://teacher.chw.edu.hk/{代碼}/index.html
入口檔：    index.html（必須）
路徑規則：  使用相對路徑，勿以 / 開頭
新 _web：   最多等候 1 小時；急用請聯絡 IT
```

---

## 下一步

→ 課後可請 Agent 產出更多教學小工具，放入 `_web` 即可上線  
→ 技術細節（IT／管理員）見 [`references/TEACHER-WEB-SERVER-SPEC.md`](../references/TEACHER-WEB-SERVER-SPEC.md)
