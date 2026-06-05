# 附錄：課前安裝清單

> **閱讀次序：** 見 [`README.md`](README.md)。  
> **課堂第 10–20 分鐘：** 講者無需逐項講解安裝；請學員 **依本附錄操作**，已完成者可先行閱讀 [`02-prompt-cheatsheet.md`](02-prompt-cheatsheet.md)。  
> Agent Model 一律使用 **Auto**（詳見 [`01-cursor-setup-guide.md`](01-cursor-setup-guide.md)）。

---

## 須安裝／準備的項目

| 項目 | 何時需要 | 您須進行 |
|------|----------|----------|
| **Cursor** | 全課必須 | [附錄 A](#附錄-a安裝-cursor) |
| **Demo Login** | 全課必須 | [附錄 B](#附錄-bdemo-login)（有效期至 **2026年7月3日**） |
| **Python 3.10+** | 活動一（Whisper 轉寫） | [附錄 C](#附錄-cpython僅在需要時) — **優先請 Cursor Agent 協助安裝** |
| **Google Drive MCP** | 課後自學（可選） | [`09-google-drive-self-study.md`](09-google-drive-self-study.md) |
| **Gemini／DeepSeek Key** | 課後（可選） | 課堂使用 **Auto**，無需填寫 → [`05-api-key-application-guide.md`](05-api-key-application-guide.md) |

---

## 附錄 A：安裝 Cursor

1. 前往 [https://cursor.com](https://cursor.com) → **Download**
2. 執行安裝程式（Windows／Mac 依螢幕指示即可）
3. 首次開啟 → 使用 **附錄 B Demo Login** 登入（或您自己的 Cursor 帳號）
4. **File → Open Folder** → 選擇培訓資料夾 `chw-staff-training-20260605`

**完成指標：** 左側可見 `activity-1-minutes`、`handouts` 等資料夾。

---

## 附錄 B：Demo Login

> 課堂提供 **演示用 Cursor 登入**，方便尚未訂閱的同事即場使用。  
> **有效期至：2026年7月3日**（過後請改用自行註冊的 Cursor 帳號）

| 欄位 | 內容 |
|------|------|
| 登入方式 | Cursor → Sign in → Email |
| Demo 電郵 | `<!-- 講者課前填入，例：chw-training-demo@example.com -->` **（課堂由講者派發）** |
| Demo 密碼 | **（課堂由講者派發，請勿公開轉發）** |

**注意：**
- Demo 帳號僅供培訓，**請勿**存放真實學生資料
- 有效期後若仍須使用 Cursor，請自行至 cursor.com 註冊
- 課堂 Agent Model 使用 **Auto** 即可，無需額外填寫 API Key

---

## 附錄 C：Python（僅在需要時）

> **活動一** Phase 1 會以 Python 執行 Whisper 轉寫。  
> **大部分同事無需自行下載 Python** — 請先依活動進行，由 Cursor Agent 協助。

### 做法一（建議）：請 Cursor 自動處理

1. 依 [`02-prompt-cheatsheet.md`](02-prompt-cheatsheet.md) **Phase 1 Prompt**
2. Agent 可能於 terminal 執行 `pip install …` 或提示安裝 Python
3. 每次彈出 **Allow／Run** → 請按批准
4. 若順利執行完 `transcribe.py` → **無需再進行附錄 C 手動安裝**

### 做法二：僅於 Cursor 無法自動處理時手動安裝

以下情況才需要：

- Terminal 顯示 `python 不是內部或外部命令`（Windows）或 `command not found: python`
- Agent 明確表示無法自動安裝，請您手動處理

**Windows 手動安裝：**

1. 前往 [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. 下載 **Python 3.12**（或 3.10 以上）
3. 安裝時 **勾選「Add python.exe to PATH」**（重要）
4. 關閉後重新開啟 Cursor
5. 於 Agent 輸入：`python --version` → 應顯示 `Python 3.12.x`

**Mac 手動安裝：**

1. 前往 python.org 下載 macOS 安裝程式，或
2. 若學校容許：`brew install python@3.12`

**Whisper 尚需 ffmpeg（讀取 .m4a 錄音）：**

- Windows：若 Phase 1 報錯缺少 ffmpeg，請告知講者／資訊科技組；或搜尋「ffmpeg windows 安裝」依官方指引
- Mac：`brew install ffmpeg`（需 IT 批准時請講者協助）

---

## 安裝完成後

1. 按 `Ctrl + I` 開啟 Agent，Model 選 **Auto**
2. 開始 [`02-prompt-cheatsheet.md`](02-prompt-cheatsheet.md) **活動一**

---

## 常見問題

| 問題 | 處理 |
|------|------|
| Demo Login 無法登入 | 請確認未過 **7月3日**；向講者索取最新帳密 |
| 不確定 Python 是否已安裝 | 可於 Agent 詢問：`本機是否已安裝 Python？若有，是哪個版本？` |
| 已安裝 Python 但 Cursor 無法偵測 | 請重新開啟 Cursor；Windows 請確認安裝時已勾選 PATH |
| 不願安裝 Python | 活動一可跳過 Phase 1 轉寫，直接使用 `sample-meeting-transcript.txt` 進行 Phase 2–3 |

---

*講者專用：Demo 帳密請更新 [`trainer/pre-class-checklist.md`](../trainer/pre-class-checklist.md)，請勿將真實密碼 commit 至 git。*
