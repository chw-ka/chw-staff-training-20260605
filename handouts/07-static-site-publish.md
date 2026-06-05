# 靜態網站發佈指南 — 活動三【teacher.chw.edu.hk】

> 配合「活動三：生成 HTML + CSS + JS」。  
> 學校已提供 **teacher.chw.edu.hk**：你把靜態檔放入 NAS 上的 `_web` folder，網站就會對外提供 HTTPS 網址。

---

## 先講清楚：為什麼不是 Google Drive？

- Google Drive **本身不會**當網站執行 HTML/JS（通常只會預覽/下載）
- CHW 教師網站是：**NAS 共享資料夾 → 校內伺服器 nginx → 公開網址**
- 所以你只需要準備 **一個 folder 裡面只有靜態檔**（HTML / CSS / JS / 圖片）

---

## 架構一覽

```
你的電腦（P:\KA\_web\）
        ↓  儲存檔案
NAS（//10.10.0.13/staff/KA/_web/）
        ↓  伺服器自動讀取
公開網址（https://teacher.chw.edu.hk/KA/）
```

| 公開網址 | NAS 實際路徑 |
|----------|--------------|
| `https://teacher.chw.edu.hk/KA/index.html` | `//10.10.0.13/staff/KA/_web/index.html` |
| `https://teacher.chw.edu.hk/ka/index.html` | 同一個檔案（網址**不分大小寫**） |

> NAS 上的 folder 名請保持**大寫**（例如 `KA`），網址用大寫或小寫都可以。

---

## 你需要什麼？

- 學校 NAS 存取權（`//10.10.0.13/staff`）
- 你的**教師代碼 folder**（例如 `KA`、`LC` — 即 staff share 裡面屬於你的 folder）
- 一個叫 `_web` 的子 folder（網站根目錄）
- 活動三生成的靜態檔（`index.html` 等）

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

> 若你平時已 map 好 `P:\`，可直接用現有連線。

---

## Step 2：建立 `_web` folder

在你的教師 folder 裡面建立 `_web`（若尚未存在）：

```
\\10.10.0.13\staff\{你的代碼}\_web\
```

Windows 已 map 的話，例如：

```
P:\KA\_web\
```

**重要：** 必須叫 `_web`（底線 + web）。沒有這個 folder → 伺服器不會為你建立公開網址。

---

## Step 3：標準輸出格式

把網站檔案直接放入 `_web`（不必再包多一層 folder）：

```
_web/
├── index.html      ← 入口（必須有）
├── styles.css
├── app.js
└── assets/
    ├── logo.png
    └── illustration.png
```

> 瀏覽器打開 `https://teacher.chw.edu.hk/{你的代碼}/` 時，會自動載入 `index.html`。

---

## Step 4：發佈前 Checklist

- [ ] 用瀏覽器打開本地 `index.html`，確認可運作
- [ ] 所有檔案路徑用**相對路徑**（例如 `styles.css`、`./assets/logo.png`）
- [ ] **避免**用 `/styles.css` 這類以 `/` 開頭的路徑（會指向網站根目錄，不是你的 folder）
- [ ] 無需 build、無需 Node server（純靜態）
- [ ] **無放入任何 API key**（前端公開檔案不可放 secret）

---

## Step 5：上線

1. 將 `index.html`、`styles.css`、`app.js`、`assets/` 等複製到 `_web`
2. 儲存後，NAS 上的檔案會**即時**被伺服器讀到（不必額外 sync）
3. 若你**新建立** `_web` folder，可能要等最多 **1 小時**（伺服器定時掃描）；急用可聯絡 IT 協助
4. 用瀏覽器打開：

   ```
   https://teacher.chw.edu.hk/{你的代碼}/index.html
   ```

   或直接：

   ```
   https://teacher.chw.edu.hk/{你的代碼}/
   ```

---

## 活動三完整流程（課堂 + 上線）

1. 跟 [`activity-3-web/sample-prompts.md`](../activity-3-web/sample-prompts.md) 用 Agent 生成網站到 `activity-3-web/output/`
2. 本地打開 `output/index.html` 預覽
3. **上線（二選一）：**
   - **Agent 一句話：** 設定好 `activity-3-web/publish.config.json` 後，在 Agent 講 **「publish」** 或 **「上線」**
   - **手動：** 將 `output/` 裡面所有檔案複製到你的 `_web`
4. 用公開網址驗證

### 首次設定 publish（課前或課後做一次）

1. 複製 `activity-3-web/publish.config.example.json` → `activity-3-web/publish.config.json`
2. 填入 `teacher_code`（例如 `KA`）
3. 若已 map NAS 為 `P:\`，可改填 `publish_target_override`：`P:\\KA\\_web`
4. 測試：`python scripts/publish_web.py --dry-run`

---

## 常見問題

| 問題 | 原因 / 解決 |
|------|-------------|
| 網址顯示 **404** | 未建立 `_web` folder；或 `_web` 裡面沒有 `index.html`；或新 folder 未掃描 — 等 1 小時或聯絡 IT |
| 改完檔案但網站未更新 | 試 hard refresh（`Ctrl + Shift + R`）；Cloudflare 可能有 cache，等一陣或聯絡 IT |
| CSS / 圖片載入不到 | 檢查 HTML 是否用了 `/style.css` 等絕對路徑；改為相對路徑 |
| `/ka/` 與 `/KA/` 有什麼分別？ | 沒有分別，兩個都指向同一個網站 |
| 為什麼不可以直接把 API key 寫入 JS？ | 靜態網站是公開檔案，任何人都可 view source；要用 API 必須加後端或 proxy |
| 想加 Login 保護？ | 目前 teacher.chw.edu.hk 是公開靜態網站；如有需要請與 IT 商討 |

---

## 快速參考卡

```
NAS 路徑：  \\10.10.0.13\staff\{代碼}\_web\
公開網址：  https://teacher.chw.edu.hk/{代碼}/index.html
入口檔：    index.html（必須）
路徑規則：  用相對路徑，不要用 / 開頭
新 _web：   最多等 1 小時；急用聯絡 IT
```

---

## 下一步

→ 課後用 Agent 生成更多教學小工具，放入 `_web` 即可上線  
→ 技術細節（IT / 管理員）見 [`references/TEACHER-WEB-SERVER-SPEC.md`](../references/TEACHER-WEB-SERVER-SPEC.md)
