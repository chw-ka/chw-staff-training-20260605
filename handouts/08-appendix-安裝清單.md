# 附錄：課前安裝清單

> **課堂第 10–20 分鐘：** 講者唔使逐項教安裝；叫學員 **跟本附錄做**，已完成者可先行閱讀 [`02-prompt-cheatsheet.md`](02-prompt-cheatsheet.md)。  
> Agent Model 一律用 **Auto**（詳見 [`01-cursor-setup-guide.md`](01-cursor-setup-guide.md)）。

---

## 我們需要安裝／準備的項目

| 項目 | 何時需要 | 你要做咩 |
|------|----------|----------|
| **Cursor** | 全課必須 | [附錄 A](#附錄-a安裝-cursor) |
| **Demo Login** | 全課必須 | [附錄 B](#附錄-bdemo-login)（有效期至 **2026年7月3日**） |
| **Python 3.10+** | 活動一（Whisper 轉寫） | [附錄 C](#附錄-cpython僅在需要時) — **優先叫 Cursor 幫你裝** |
| **Google Drive MCP** | 課後自學（可選） | [`09-google-drive-self-study.md`](09-google-drive-self-study.md) |
| **Gemini / DeepSeek Key** | 課後（可選） | 課堂用 **Auto** 唔使填 → [`05-api-key-application-guide.md`](05-api-key-application-guide.md) |

---

## 附錄 A：安裝 Cursor

1. 前往 [https://cursor.com](https://cursor.com) → **Download**
2. 執行安裝程式（Windows / Mac 跟螢幕指示即可）
3. 首次開啟 → 用 **附錄 B Demo Login** 登入（或你自己的 Cursor 帳號）
4. **File → Open Folder** → 選培訓資料夾 `chw-staff-training-20260605`

**完成指標：** 左面見到 `activity-1-minutes`、`handouts` 等資料夾。

---

## 附錄 B：Demo Login

> 課堂提供 **演示用 Cursor 登入**，方便未有自己訂閱的同事即場使用。  
> **有效期至：2026年7月3日**（過後請改用自行註冊的 Cursor 帳號）

| 欄位 | 內容 |
|------|------|
| 登入方式 | Cursor → Sign in → Email |
| Demo 電郵 | `<!-- 講者課前填入，例：chw-training-demo@example.com -->` **（課堂由講者派發）** |
| Demo 密碼 | **（課堂由講者派發，勿公開轉發）** |

**注意：**
- Demo 帳號僅供培訓，**請勿**存放真實學生資料
- 有效期後如仍要使用 Cursor，請自行到 cursor.com 註冊
- 課堂 Agent Model 用 **Auto** 即可，唔使額外填 API Key

---

## 附錄 C：Python（僅在需要時）

> **活動一** Phase 1 會用 Python 跑 Whisper 轉寫。  
> **大部分同事唔使自己下載 Python** — 先跟活動做，叫 Cursor Agent 幫手。

### 做法一（建議）：叫 Cursor 自動處理

1. 跟 [`02-prompt-cheatsheet.md`](02-prompt-cheatsheet.md) **Phase 1 Prompt**
2. Agent 可能會在 terminal 執行 `pip install …` 或提示安裝 Python
3. 每次彈出 **Allow / Run** → 按批准
4. 若順利跑完 `transcribe.py` → **唔使再做附錄 C 手動安裝**

### 做法二：只有 Cursor 搞唔掂時先用手動安裝

以下情況才需要：

- Terminal 顯示 `python 不是內部或外部命令`（Windows）或 `command not found: python`
- Agent 明確話無法自動安裝，請你手動處理

**Windows 手動安裝：**

1. 前往 [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. 下載 **Python 3.12**（或 3.10 以上）
3. 安裝時 **勾選「Add python.exe to PATH」**（重要）
4. 關閉再開 Cursor
5. 在 Agent 輸入：`python --version` → 應見 `Python 3.12.x`

**Mac 手動安裝：**

1. 前往 python.org 下載 macOS 安裝程式，或
2. 若學校容許：`brew install python@3.12`

**Whisper 還需要 ffmpeg（讀 .m4a 錄音）：**

- Windows：若 Phase 1 報錯缺少 ffmpeg，請告知講者／IT；或搜尋「ffmpeg windows 安裝」跟官方指引
- Mac：`brew install ffmpeg`（需 IT 批准時請講者協助）

---

## 安裝完成後

1. `Ctrl + I` 開 Agent，Model 選 **Auto**
2. 開始 [`02-prompt-cheatsheet.md`](02-prompt-cheatsheet.md) **活動一**

---

## 常見問題

| 問題 | 處理 |
|------|------|
| Demo Login 登入唔到 | 確認未過 **7月3日**；向講者索取最新帳密 |
| 唔知 Python 裝未 | Agent 問：`我部機有冇 Python？有嘅話係邊個版本？` |
| 已裝 Python 但 Cursor 搵唔到 | 重開 Cursor；Windows 確認安裝時有勾 PATH |
| 唔想裝 Python | 活動一可跳過 Phase 1 轉寫，直接用 `sample-meeting-transcript.txt` 做 Phase 2–3 |

---

*講者專用：Demo 帳密請更新 [`trainer/pre-class-checklist.md`](../trainer/pre-class-checklist.md)，勿 commit 真實密碼入 git。*
