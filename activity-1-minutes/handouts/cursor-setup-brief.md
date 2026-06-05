# 開啟本活動 — Cursor 設定簡要

> 本資料夾可**獨立**以 Cursor 開啟，無需開啟整個培訓包。

---

## Step 1：開啟資料夾

1. 安裝 [Cursor](https://cursor.com)
2. **File → Open Folder**
3. 選擇 **`activity-1-minutes`** 本資料夾

開啟後，左側檔案列表應可見 `samples/`、`scripts/`、`handouts/` 等。

---

## Step 2：開啟 Agent，直接開始

1. 按 `Ctrl + I`（Mac：`Cmd + I`）開啟 **Agent**
2. Model 使用 **Auto** 或 Cursor 預設即可 — **無需手動選擇 DeepSeek**
3. 開啟 [`handouts/prompt-cheatsheet.md`](prompt-cheatsheet.md)，由 Phase 1 開始貼上 Prompt

### 為何無需特別設定 model？

| 階段 | 實際作業 | 使用 |
|------|----------|------|
| **Phase 1** | Agent **撰寫 Python 程式**，再於本機執行 | **Whisper**（script 內，不經 AI 連線） |
| **Phase 2–3** | Agent 讀檔、依 SKILL 撰寫紀錄 | Cursor Agent（Auto 已足夠） |

> ⚠️ **請勿**將 API Key 貼入 Agent 對話 — 如有需要，應於 Cursor Settings 設定；但本活動 Phase 1 轉寫**不需要** DeepSeek Key。

---

## Step 3：Phase 1 本機準備（Whisper 轉寫）

| 軟件 | 用途 |
|------|------|
| Python 3.10+ | 執行轉寫 script |
| ffmpeg | 讀取 .m4a 錄音 |

**課前預跑（講者／資訊科技組）：**

```powershell
pip install -r scripts/requirements.txt
python scripts/transcribe.py
```

首次執行 Whisper 會下載 large-v3（約 3 GB），請於課前完成。

課堂上 Agent 會協助執行上述指令；若缺少 Python 或 ffmpeg，請依 Agent 提示處理。

---

## 常見問題

| 問題 | 做法 |
|------|------|
| Whisper 下載太慢 | 課堂可跳過即場轉寫，直接使用 `samples/demo-short-clip-expected-transcript.txt` 進入 Phase 2 |
| 找不到 ffmpeg | 請安裝 ffmpeg 並加入 PATH；或請 Agent 協助檢查 |
| Agent 不熟悉紀錄格式 | 請確認已引用 `@.cursor/skills/meeting-minutes/SKILL.md` |
| 是否需要 API Key？ | Phase 1 轉寫不需要；Phase 2–3 使用 Cursor 內建 Agent 即可（Auto） |
