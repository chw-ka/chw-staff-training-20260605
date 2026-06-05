# CHW Staff Training 2026 — Cursor 進階培訓包

> **課程主題：** 2026年度 AI 驅動校園：從行政解放到高階自主開發  
> **時長：** 90 分鐘 | **對象：** Power Users 教職員  
> **培訓日期：** 2026-06-05（可按實際日期調整）

本 repository 包含講者與學員所需的**全部課堂素材**。老師只需 clone / 下載此 project，依照 handouts 逐步操作即可。

---

## 資料夾結構

```
chw-staff-training-20260605/
├── LessonPlan.md                 ← 90 分鐘課程編排表（總覽）
├── README.md                     ← 你正在看的這份文件
│
├── handouts/                     ← 學員講義（課堂派發 / 投影用）
│   ├── 01-cursor-setup-guide.md  ← Cursor 快速開始（Auto，唔使填 Key）
│   ├── 02-prompt-cheatsheet.md   ← 三個活動的 Prompt 懶人包
│   ├── 03-faq-hk-guide.md        ← 課後 FAQ
│   ├── 04-filesystem-mcp-guide.md ← Filesystem MCP 試玩
│   ├── 05-api-key-application-guide.md ← API Key 申請（課後可選）
│   ├── 06-google-drive-mcp-setup.md ← Drive MCP（課後自學）
│   ├── 09-google-drive-self-study.md ← 課後自學指引
│   ├── 07-static-site-publish.md ← 活動三發佈（teacher.chw.edu.hk）
│   └── 08-appendix-安裝清單.md   ← 附錄：Cursor / Demo Login / Python
│
├── .cursor/
│   ├── rules/                    ← Project AI 規則（non-dev 語氣等）
│   └── mcp.json                  ← Filesystem MCP 設定（project 級）
│
├── trainer/                      ← 講者專用（勿派發給學員）
│   ├── pre-class-checklist.md    ← 課前 48 小時 / 當日 checklist
│   ├── demo-script.md            ← 逐步 demo 腳本（含話術）
│   ├── talking-points.md         ← 各時段核心概念講解要點
│   ├── troubleshooting.md        ← 常見問題即場應對
│   ├── on-stage-checklist.md     ← 現場 Demo 不出錯
│   ├── rag-at-folder-metaphor.md ← @Folder「實習老師」比喻
│   ├── demo-vba-pptx/            ← VBA 10 張 PPT 一鍵生成
│   ├── demo-chaotic-transcript/  ← 混亂逐字稿 → Minutes
│   └── demo-student-compositions/← @Folder 評作文 demo
│
├── activity-1-minutes/           ← 活動一：Workflow 錄音 → Minutes
│   ├── README.md                 ← Workflow 說明 + 三 Phase
│   ├── sample-meeting-transcript.txt
│   ├── 議程_視藝科組會_20260528.docx  ← 議程（Word）
│   ├── 會議紀錄_視藝科組_20250522_上學年.docx ← 上學年紀錄（第三步格式參考）
│   ├── minutes-template.md
│   ├── expected-output-sample.md
│   ├── samples/demo-short-clip.m4a  ← Phase 1 短錄音 (~45s)
│   ├── scripts/transcribe.py     ← Whisper 轉寫
│   └── .cursor/skills/meeting-minutes/SKILL.md
│
├── activity-2-files/             ← 活動二：Open Folder 即用（inbox ~100 檔）
│   ├── inbox/
│   ├── sorted/（教學、行政、ICT…）
│   ├── handouts/（prompt-cheatsheet、cursor-setup-brief）
│   ├── .cursor/skills/file-organizer/
│   └── my_organization_profile.example.md
│
├── activity-5-gdrive/            ← Google Drive 整理（課後自學）
│   ├── README.md
│   ├── sample-prompts.md
│   └── samples/
│
├── activity-3-web/               ← 活動三：生成 HTML+CSS+JS（webhost）
│   ├── README.md
│   ├── sample-prompts.md
│   ├── starter/                 ← 直接打開 index.html
│   └── output/                  ← 課堂生成版本
│
├── activity-4-marp/              ← 課後延伸：MARP 簡報（唔喺 90 分鐘內）
│   ├── marp-syntax-reference.md
│   ├── template-tech-with-footer.md
│   ├── sample-minutes-for-slides.md
│   └── assets/README.md
│
└── config/
    ├── .env.example              ← API Key + Model 選項說明（同 .env.sample）
    ├── .env.sample               ← 同上
    ├── gcp-oauth.keys.example.json ← Google OAuth 範本（複製為 gcp-oauth.keys.json）
    └── cursor-models.example.json
```

---

## 講者快速開始

### 課前 48 小時

1. 閱讀 `trainer/pre-class-checklist.md`，逐項打勾。
2. 確認學員已完成 Cursor 安裝及 Demo Login（Google Drive OAuth **唔使**，課後見 09）
3. 自己申請 Gemini + DeepSeek Key，填入 `config/.env` 作 demo（**可選**；課堂學員用 Auto）。
4. 預跑 `activity-3-web/starter/index.html` 確認瀏覽器可開。
5. 在講者電腦預跑一次 `trainer/demo-script.md` 全流程（**含活動一 Whisper Phase 1**）。

### 課堂當日

1. 投影 `handouts/08-appendix-安裝清單.md`，學員跟附錄安裝 Cursor、Open Folder；Agent 用 **Auto**（10 分鐘）。
2. 按 `LessonPlan.md` 時間表，依序進行三個活動。
3. 派發 `handouts/02-prompt-cheatsheet.md` 與 `handouts/03-faq-hk-guide.md`。
4. 隨時參考 `trainer/troubleshooting.md`。

### 課後

1. 提醒學員妥善保管自己的 API Key，勿分享。
2. 將此 repo 連結發給老師，鼓勵課後自行練習。
3. 收集 feedback（可選：Google Form）。

---

## 學員快速開始

1. 安裝 [Cursor](https://cursor.com)（選 Download for your OS）。
2. 用 Cursor 開啟此 project folder。
3. 跟 [`handouts/08-appendix-安裝清單.md`](handouts/08-appendix-安裝清單.md) 完成 Demo Login；Agent Model 選 **Auto**。
4. 在 Agent 視窗（`Cmd/Ctrl + I`）貼上 `handouts/02-prompt-cheatsheet.md` 的 Prompt 開始實操。

> 課後如需自備 API Key，見 [`handouts/05-api-key-application-guide.md`](handouts/05-api-key-application-guide.md)。
---

## 所需軟件（學員電腦）

| 軟件 | 用途 | 安裝方式 |
|------|------|----------|
| Cursor | 主工具 | cursor.com |
| Google 帳號 | 課後 Drive 自學（可選） | 見 `09-google-drive-self-study.md` |
| Python 3.10+ | 活動一 Whisper 轉寫；備用 Watchdog | 課堂 Phase 1 需用；見 `activity-1-minutes/scripts/` |
| ffmpeg | 活動一讀取 .m4a | 與 Whisper 一併使用 |
| VS Code Marp 擴充（可選） | 課後 MARP 延伸 | Cursor 內裝 Marp for VS Code；見 `activity-4-marp/` |

---

## 私隱提醒

- 課堂用的錄音逐字稿、學生姓名均為**虛構示範資料**。
- 處理真實學生資料時，請使用校內核准工具；參考 `handouts/03-faq-hk-guide.md` 的 Ollama 本地方案。
