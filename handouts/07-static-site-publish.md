# 靜態網站發佈指南（HTML/CSS/JS）

> 配合「活動四：生成 HTML + CSS + JS」。  
> 你稍後會提供 webhost，我會再按實際 host 補上最精準步驟。

---

## 先講清楚：Google Drive 係儲存，不係 hosting

- Google Drive **本身唔會**當網站執行 HTML/JS（通常只會預覽/下載）
- 你提到的 webhost 應該係「讀某個 Share Drive folder，然後對外提供網址」
- 所以我哋要準備嘅輸出格式必須係：**一個 folder 入面只有靜態檔**

---

## 我哋嘅標準輸出格式（建議）

每個網站一個 folder，例如：

```
site-homework-namer/
├── index.html
├── styles.css
├── app.js
└── assets/
    ├── logo.png
    └── illustration.png
```

> 任何 webhost 基本都支援 `index.html` 做入口。

---

## 發佈前 Checklist

- [ ] 用瀏覽器打開 `index.html`，確認可運作
- [ ] 所有檔案路徑用相對路徑（例如 `./styles.css`、`assets/logo.png`）
- [ ] 無需 build、無需 Node server（純靜態）
- [ ] 無放入任何 API key（前端公開檔案不可放 secret）

---

## 上線流程（通用版）

> 等你提供 webhost 後，我會將以下步驟替換為「實際按鈕位置 + 截圖級指引」。

1. 在 shared drive 建立一個 folder（例如：`CHW_Websites/site-homework-namer/`）
2. 將 `index.html / styles.css / app.js / assets/` 上傳到該 folder
3. 等 webhost 同步（可能 10–60 秒）
4. 用 webhost 提供嘅網址打開

---

## 常見問題

**Q：點解唔可以直接將 Gemini/DeepSeek API key 寫入 JS？**  
A：因為靜態網站係公開檔案，任何人都可 view source。要用 API 必須加後端或用 server-side proxy。

**Q：我想加「Login」保護網頁？**  
A：要睇你個 webhost 有冇 password protection / SSO。你俾我 host 資料後我可以補上。

**Q：點解我改完檔案但網站未更新？**  
A：webhost 可能有 cache；可試 hard refresh（`Cmd/Ctrl + Shift + R`）或等同步。

---

## 下一步

你俾我以下資料，我就可以出一份「完全客製」版發佈指引：

- webhost 係咩（平台名 / 網址）
- 佢係咪讀 Google Shared Drive / OneDrive / SMB share
- 佢要求嘅 folder 結構（例如必須叫 `public/` / `www/`）
- 佢嘅 base path（例如 `https://host/sitename/` 或獨立 subdomain）
