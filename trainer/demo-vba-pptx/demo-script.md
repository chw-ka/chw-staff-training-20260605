# 講者 Demo 腳本 — 1 秒生成 10 張 PPT（VBA）

> 主題：**中一中文科：文言文基本閱讀技巧（六書與虛詞）**  
> 檔案：[`GenerateWenYanWenSlides.bas`](GenerateWenYanWenSlides.bas)

---

## 開場話術（30 秒）

> 「各位同事，改 PPT 最花時間。今日不用 AI 出 slide — 用 PowerPoint 內置的『自動化』，
> 按一個掣，**10 張課堂簡報即刻出現**。
> 原理與 Cursor Agent 類似：你預先寫好規則，電腦幫你執行。」

---

## Step 1：顯示「開發人員」索引標籤

**Windows：**

1. 開啟 **PowerPoint**（空白簡報即可）
2. **檔案 → 選項 → 自訂功能區**
3. 右側勾選 **開發人員**
4. 按 **確定**

**Mac：**

1. **PowerPoint → 偏好設定 → 功能區與工具列**
2. 勾選 **開發人員**（Developer）

**話術：**
> 「『開發人員』聽起來很 technical — 其實只是 PowerPoint 的進階工具列，今日只用其中一個功能。」

---

## Step 2：開啟 VBA 編輯器

- **Windows：** 按 **`Alt + F11`**
- **Mac：** 按 **`Fn + Option + F11`**（或 **工具 → 巨集 → Visual Basic Editor**）

**話術：**
> 「會彈出一個新視窗 — 不必擔心，我們只是貼一段現成『食譜』，不必自己寫。」

---

## Step 3：插入 Module 並貼上程式碼

1. 左側 **Project** 視窗 → 右鍵 **VBAProject** → **插入 → 模組**
2. 開啟本 repo 的 [`GenerateWenYanWenSlides.bas`](GenerateWenYanWenSlides.bas)
3. **全選複製** → 貼入 Module 空白位置
4. **Ctrl + S** 儲存（若提示，可存成 `.pptm` 啟用巨集的簡報）

**話術：**
> 「這段 code 已經幫大家寫好 10 張 slide 的標題與內容 — 六書、虛詞、小測都有。」

---

## Step 4：執行 — 按 F5

1. 游標放在 `GenerateWenYanWenSlides` 程序內任意一行
2. 按 **`F5`**（或工具列 **執行 → 執行 Sub/UserForm**）
3. 若 Office 問巨集安全性 → 選 **啟用**（僅限你信任的檔案）

**話術（執行中）：**
> 「留意 — 不是 AI 即時想內容，而是**預先寫好的腳本一次過排版**。
> 教學上你可以改 topic、改字句，再按 F5 就出新版。」

**成功後：**
> 「10 張簡報，字體已統一微軟正黑體。你可以即刻改字、加校徽、加動畫 — 與平時改 PPT 一樣。」

---

## 常見問題

| 問題 | 解決 |
|------|------|
| 找不到開發人員 | 檔案 → 選項 → 自訂功能區 → 勾選 |
| Mac F11 無反應 | 用 Fn + Option + F11 |
| 巨集被停用 | 檔案 → 選項 → 信任中心 → 巨集設定 → 啟用 |
| 執行報錯 | 確認貼了完整 code；PowerPoint 要開著至少一個 instance |

---

## 與 Cursor 培訓的連結

> 「VBA 是**固定 workflow**；Cursor Agent 是**用自然語言改 workflow**。
> 兩者都是：老師做設計師，電腦做重複勞動。」

---

## 下一步

→ 若時間許可，示範叫 Agent「把這 10 張 slide 內容改成 Open Day 簡介版」對比 VBA 固定 vs AI 靈活
