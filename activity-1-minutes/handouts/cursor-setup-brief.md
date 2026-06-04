# 開啟本活動 — Cursor 設定簡要

> 本資料夾可**獨立**用 Cursor 開啟，唔使開成個培訓包。

---

## Step 1：開啟資料夾

1. 安裝 [Cursor](https://cursor.com)
2. **File → Open Folder**
3. 選 **`activity-1-minutes`** 呢個資料夾（即本資料夾）

開啟後，左邊檔案列表應見到 `samples/`、`scripts/`、`handouts/` 等。

---

## Step 2：開 Agent，直接開始

1. `Ctrl + I`（Mac：`Cmd + I`）開 **Agent**
2. Model 用 **Auto** 或 Cursor 預設即可 — **唔使手動揀 DeepSeek**
3. 打開 [`handouts/prompt-cheatsheet.md`](prompt-cheatsheet.md)，由 Phase 1 開始貼 Prompt

### 點解唔使特別 set model？

| 階段 | 實際做咩 | 用咩 |
|------|----------|------|
| **Phase 1** | Agent **寫 Python code**，再喺本機跑 | **Whisper**（script 內，唔經 AI 連線） |
| **Phase 2–3** | Agent 讀檔、跟 SKILL 寫紀錄 | Cursor Agent（Auto 已夠） |

> ⚠️ **請勿**將 API Key 貼入 Agent 對話 — 如有需要，應在 Cursor Settings 設定；但本活動 Phase 1 轉寫**唔需要** DeepSeek Key。

---

## Step 3：Phase 1 本機準備（Whisper 轉寫）

| 軟件 | 用途 |
|------|------|
| Python 3.10+ | 跑轉寫 script |
| ffmpeg | 讀取 .m4a 錄音 |

**課前預跑（講者 / IT）：**

```powershell
pip install -r scripts/requirements.txt
python scripts/transcribe.py
```

首次跑 Whisper 會下載 large-v3（約 3 GB），請課前完成。

課堂上 Agent 會幫你執行上述指令；缺 Python 或 ffmpeg 時，跟 Agent 提示處理即可。

---

## 常見問題

| 問題 | 做法 |
|------|------|
| Whisper 下載太慢 | 課堂可跳過 live 轉寫，直接用 `samples/demo-short-clip-expected-transcript.txt` 進 Phase 2 |
| 找不到 ffmpeg | 安裝 ffmpeg 並加入 PATH；或請 Agent 協助檢查 |
| Agent 唔識寫紀錄格式 | 確認有 `@.cursor/skills/meeting-minutes/SKILL.md` |
| 要唔要 API Key？ | Phase 1 轉寫唔使；Phase 2–3 用 Cursor 內建 Agent 即可（Auto） |
