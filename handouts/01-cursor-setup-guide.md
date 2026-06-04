# 駁通水喉 — Cursor + Gemini / DeepSeek 設定指南

> 課堂第 10–20 分鐘跟做。  
> 請先完成 [`05-api-key-application-guide.md`](05-api-key-application-guide.md) 申請 Key。  
> **本課程不使用 OpenAI API。**

---

## 本課程用哪個 Model？

| 活動 | 建議 Model | 原因 |
|------|------------|------|
| 活動一 Minutes | **DeepSeek** `deepseek-v4-flash` | 長文本穩定、便宜 |
| 活動二 Drive 整理 | **DeepSeek** `deepseek-v4-flash` | MCP tool calls |
| 活動三 MARP + 插圖 | **Gemini** `gemini-2.5-flash` | 多模態 |

Agent 視窗左上角可切換 Model。

---

## Step 1：安裝並開啟 Cursor

1. 前往 https://cursor.com 下載並安裝
2. 登入或建立 Cursor 帳號
3. **File → Open Folder** → 選 `chw-staff-training-20260605`

---

## Step 2：開啟 Settings

| 平台 | 方法 |
|------|------|
| Mac | `Cmd + ,` |
| Windows | `Ctrl + ,` |

或：左下角 ⚙️ → **Cursor Settings** → **Models**

---

## Step 3A：設定 Gemini API Key

1. 在 Models 頁面搜尋 **Google** 或 **Gemini**
2. 找到 **Google API Key** / **Gemini API Key** 欄位
3. 貼上你的 Gemini Key（`AIzaSy...`）
4. 在 Models 列表 **Add model**，輸入：
   ```
   gemini-2.5-flash
   ```
5. 啟用該 model，按 **Verify**（如有）確認連線

### 圖解

```
Cursor Settings → Models
  ├── Google API Key / Gemini API Key   ← 貼 AIzaSy...
  └── Models 列表
        └── gemini-2.5-flash  ☑         ← 啟用
```

---

## Step 3B：設定 DeepSeek API Key

DeepSeek 使用 **OpenAI 兼容格式** 接入 Cursor — 這裡填的是 **DeepSeek Key**，不是 OpenAI。

1. 仍在 **Models** 頁面
2. 找到 **OpenAI API Key** 欄位 → 貼上 **DeepSeek Key**（`sk-...`）
3. 開啟 **Override OpenAI Base URL**
4. Base URL 填：
   ```
   https://api.deepseek.com
   ```
   > ⚠️ **不要**加 `/v1`（Cursor 會自己處理路徑；加了可能 404）
5. **Add model**，輸入：
   ```
   deepseek-v4-flash
   ```
6. 啟用並 **Verify**

### 圖解

```
Cursor Settings → Models
  ├── OpenAI API Key              ← 貼 DeepSeek 的 sk-...（不是 OpenAI！）
  ├── Override Base URL  ☑
  ├── Base URL                    ← https://api.deepseek.com
  └── Models 列表
        └── deepseek-v4-flash  ☑      ← 啟用
```

> **重要：** 我們**沒有使用 OpenAI**，只是借用 Cursor 的「兼容接口」去連 DeepSeek。

---

## Step 4：測試連線

1. `Cmd/Ctrl + I` 開啟 **Agent**
2. 右上角選 **deepseek-v4-flash**
3. 輸入：

```
你好，請用繁體中文書面語回覆我：DeepSeek 連線正常嗎？
```

4. 再切換 **gemini-2.5-flash**，輸入：

```
你好，請用繁體中文書面語回覆我：Gemini 連線正常嗎？
```

兩個都有回覆 → ✅ 設定成功

---

## Step 5：認識 Agent 視窗

| 快捷鍵 | 功能 |
|--------|------|
| `Cmd/Ctrl + I` | Agent（本課程主要用） |
| `Cmd/Ctrl + L` | Chat 問答 |
| `@` | 引用 project 檔案 |
| Model 下拉 | 切換 DeepSeek / Gemini |

---

## 常見錯誤

| 錯誤 | 檢查 |
|------|------|
| Invalid API Key | Key 是否完整複製；Gemini 用 AI Studio 那把，DeepSeek 用 platform 那把 |
| 404 / Connection error | DeepSeek Base URL 是否 `https://api.deepseek.com`（無 `/v1`） |
| 402 / Insufficient balance | DeepSeek 要充值（見 05 申請指南） |
| Model not found | Model 名稱是否 `deepseek-v4-flash` / `gemini-2.5-flash` |
| 校園 Wi-Fi 連不到 | 試手機 hotspot；DeepSeek 可能被 IT 封鎖 |

---

## 下一步

→ 打開 [`02-prompt-cheatsheet.md`](02-prompt-cheatsheet.md) 開始**活動一**
