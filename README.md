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
│   ├── 01-cursor-setup-guide.md  ← Gemini + DeepSeek 填入 Cursor
│   ├── 02-prompt-cheatsheet.md   ← 三個活動的 Prompt 懶人包
│   ├── 03-faq-hk-guide.md        ← 課後 FAQ
│   ├── 04-filesystem-mcp-guide.md ← Filesystem MCP 試玩
│   ├── 05-api-key-application-guide.md ← API Key 申請（課前必做）
│   ├── 06-google-drive-mcp-setup.md ← 活動二 Google Drive MCP
│   └── 07-static-site-publish.md ← 活動四發佈（teacher.chw.edu.hk）
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
├── activity-1-minutes/           ← 活動一：錄音變 Minutes
│   ├── sample-meeting-transcript.txt
│   ├── minutes-template.md
│   ├── expected-output-sample.md
│   └── .cursor/skills/meeting-minutes/SKILL.md
│
├── activity-2-gdrive/            ← 活動二：【雲端神蹟】Google Drive 整理
│   ├── README.md
│   ├── sample-prompts.md
│   ├── rename_rules.example.json
│   ├── demo-setup.md
│   ├── setup-auth.sh
│   └── samples/                  ← 上傳到 Google Drive 垃圾崗
│
├── activity-2-watchdog/          ← 備用（OAuth 失敗時本地 demo）
│
├── activity-3-marp/              ← 活動三：MARP 直出 PPT
│   ├── marp-syntax-reference.md
│   ├── template-with-footer.md
│   ├── sample-minutes-for-slides.md
│   └── assets/README.md          ← 放置校徽 PNG
│
├── activity-4-web/               ← 活動四：生成 HTML+CSS+JS（webhost）
│   ├── README.md
│   ├── sample-prompts.md
│   ├── starter/                 ← 直接打開 index.html
│   └── output/                  ← 課堂生成版本
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
2. 確認學員已收到 [`handouts/05-api-key-application-guide.md`](handouts/05-api-key-application-guide.md)（課前 3–7 天）。
3. 自己申請 Gemini + DeepSeek Key，填入 `config/.env` 作 demo。
4. 將校徽 PNG 放入 `activity-3-marp/assets/school-logo.png`。
5. 在講者電腦預跑一次 `trainer/demo-script.md` 全流程。

### 課堂當日

1. 投影 `handouts/01-cursor-setup-guide.md`，帶全班完成 Gemini + DeepSeek 設定（10 分鐘）。
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
2. 跟 [`handouts/05-api-key-application-guide.md`](handouts/05-api-key-application-guide.md) 申請 **Gemini** + **DeepSeek** Key。
3. 用 Cursor 開啟此 project folder。
4. 跟 [`handouts/01-cursor-setup-guide.md`](handouts/01-cursor-setup-guide.md) 設定 API。
5. 在 Agent 視窗（`Cmd/Ctrl + I`）貼上 `handouts/02-prompt-cheatsheet.md` 的 Prompt 開始實操。

---

## 所需軟件（學員電腦）

| 軟件 | 用途 | 安裝方式 |
|------|------|----------|
| Cursor | 主工具 | cursor.com |
| Google 帳號 | 活動二 Drive MCP | 課前 OAuth 設定 |
| Python 3.10+（可選） | 備用 Watchdog demo | 見 activity-2-watchdog |
| VS Code Marp 擴充（可選） | 預覽 MARP 簡報 | Cursor 內裝 Marp for VS Code |

---

## 私隱提醒

- 課堂用的錄音逐字稿、學生姓名均為**虛構示範資料**。
- 處理真實學生資料時，請使用校內核准工具；參考 `handouts/03-faq-hk-guide.md` 的 Ollama 本地方案。
