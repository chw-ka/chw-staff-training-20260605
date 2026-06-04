## 📋 課程基本資料

* **課程主題：** 2026年度 AI 驅動校園：從行政解放到高階自主開發
* **對象：** 有意願深入學習 AI 應用的學校教職員（Power Users）
* **時長：** 90 分鐘
* **主要工具：** Cursor (Agent / Composer 模式)、MARP
* **環境配置策略：** 課堂 10 分鐘跟 [`handouts/08-appendix-安裝清單.md`](handouts/08-appendix-安裝清單.md) 安裝 Cursor、Demo Login；Agent **Model 用 Auto**，唔使手動填 API Key。課後可選申請 Gemini / DeepSeek（見 [`05-api-key-application-guide.md`](handouts/05-api-key-application-guide.md)）。

---

## 📅 90分鐘進階 Staff Training 課程編排表

| 時間 | 教學活動 (Activity) | 核心概念 (Concepts) | 實操內容與教學細節 (Details & Implementation) |
| --- | --- | --- | --- |
| 00-10 min<br>

<br>(10") | **引入：AI 2026 變革** | **Workflow 概念** | **觀念重塑：** 告別舊時代「一問一答」的對話框。**核心：** 介紹什麼是 **Agentic Workflow**（智能體工作流）—— AI 開始具備多步驟思考、自動執行任務的能力。 |
| 10-20 min<br>

<br>(10") | 環境準備：<br>

<br>駁通私家水喉 | **環境配置** | **講者：** 簡短帶做，詳見 [`handouts/08-appendix-安裝清單.md`](handouts/08-appendix-安裝清單.md)（Cursor、Demo Login 至 **7/3**、Python 優先由 Agent 自動裝）。**學員：** 跟附錄 Open Folder；Agent Model 選 **Auto**，即可開始活動一。 |
| 20-40 min<br>

<br>(20") | 活動 1：<br>

<br>Workflow — 錄音 → Minutes | **Workflow**<br>

<br>**Vibe Coding**<br>

<br>**SKILL** | **目標：** 學懂 **Agentic Workflow**，唔係淨係出一份紀錄。**完整流程：** 錄音 → 文字 → + 議程 + 格式 → 會議紀錄。**格式：** 第二步用通用範本；第三步（可選）用**上學年紀錄做格式參考**，配合今年議程同逐字稿寫**全新**紀錄（唔係合併）。**課堂：** 第一步用 ~45 秒 clip 示範；第二、三步用視藝科完整稿。**Wow 點：** 老師只需掌握 Input/Output。 |
| 40-60 min<br>

<br>(20") | 活動 2：<br>

<br>本機文件整理 | **Workflow**<br>

<br>**先傾後做** | **痛點：** 每日執檔、桌面亂。**做法：** 開 `activity-2-files`（含 SKILL、RULES）→ 先傾分類 → 定 profile → **讀檔內容**整理 inbox（唔按副檔名）→ `sorted/教學`、ICT 等。**Wow：** 一句執行，逐步 Approve。 |
| 60-85 min<br>

<br>(25") | 活動 3：<br>

<br>MARP 直出 PPT | **API (多模態)**<br>

<br>**SKILL (Marp 語法)** | **情境：** 校長要求針對剛才活動一的決議事項，明天早會向全校簡報。**SKILL 落地：** 學習 **MARP**（純文字排版簡報）語法。命令 Cursor Agent 讀取活動一的 Minutes 文本，一邊編寫簡報，一邊調用 **Gemini API** 生成符合主題的 AI 插圖。**Wow 點：** 透過 MCP 權限，Agent 自動把 AI 插圖下載到本地、精準排版，並套用含有學校校徽的 Global Footer。老師從頭到尾沒開過 PowerPoint，一份完全客製化的學校簡報已經憑空誕生。 |
| 85-90 min<br>

<br>(05") | **總結與反思** | **數據私隱與未來** | **安全意識：** 提醒老師，處理涉及學生私隱或學校機密文件時，未來可結合今日學到的 MCP 工作流，在校內以 **Ollama 本地部署開源模型**安全處理。**結語：** 老師的價值不再是重複性行政，而是成為「工作流的總設計師」。 |

---

## 📌 講義筆記（Handout）必備三大核心板塊

以下素材已備妥，可直接派發或投影：

| 板塊 | 檔案 |
|------|------|
| **API Key 申請（課前必做）** | [`handouts/05-api-key-application-guide.md`](handouts/05-api-key-application-guide.md) |
| 駁通水喉（Cursor 快速開始） | [`handouts/01-cursor-setup-guide.md`](handouts/01-cursor-setup-guide.md) + [`08-appendix-安裝清單.md`](handouts/08-appendix-安裝清單.md) |
| Prompt 懶人包 | [`handouts/02-prompt-cheatsheet.md`](handouts/02-prompt-cheatsheet.md) |
| 課後 FAQ 與香港自救 | [`handouts/03-faq-hk-guide.md`](handouts/03-faq-hk-guide.md) |
| Filesystem MCP 試玩 | [`handouts/04-filesystem-mcp-guide.md`](handouts/04-filesystem-mcp-guide.md) |
| Google Drive MCP 設定（課後自學） | [`handouts/06-google-drive-mcp-setup.md`](handouts/06-google-drive-mcp-setup.md) + [`09-google-drive-self-study.md`](handouts/09-google-drive-self-study.md) |
| 靜態網站發佈（teacher.chw.edu.hk） | [`handouts/07-static-site-publish.md`](handouts/07-static-site-publish.md) |
| **附錄：安裝清單（Cursor / Demo Login / Python）** | [`handouts/08-appendix-安裝清單.md`](handouts/08-appendix-安裝清單.md) |

---

## 📦 完整培訓包索引

| 用途 | 位置 |
|------|------|
| 總覽與快速開始 | [`README.md`](README.md) |
| 課前 checklist | [`trainer/pre-class-checklist.md`](trainer/pre-class-checklist.md) |
| 逐步 demo 腳本 | [`trainer/demo-script.md`](trainer/demo-script.md) |
| 活動一詳細腳本 | [`trainer/activity-1-demo-script.md`](trainer/activity-1-demo-script.md) |
| 各時段講解要點 | [`trainer/talking-points.md`](trainer/talking-points.md) |
| 即場 troubleshooting | [`trainer/troubleshooting.md`](trainer/troubleshooting.md) |
| 活動一：逐字稿 + 範本 + SKILL | [`activity-1-minutes/`](activity-1-minutes/) |
| 活動二：本機文件整理 | [`activity-2-files/`](activity-2-files/) |
| Google Drive 整理（課後自學） | [`activity-2-gdrive/`](activity-2-gdrive/) |
| 活動三：MARP 簡報模板 | [`activity-3-marp/`](activity-3-marp/) |
| 活動四：靜態網站（HTML/CSS/JS） | [`activity-4-web/`](activity-4-web/) |
| API Key 範本（講者填寫） | [`config/.env.example`](config/.env.example) |

### 講者課前必做

1. 確認學員已完成 Google Drive MCP 設定（[`handouts/06-google-drive-mcp-setup.md`](handouts/06-google-drive-mcp-setup.md)）
2. 確認學員已完成 Cursor 安裝及 Demo Login（API Key 課後可選，見 05 指南）
2. 複製 `config/.env.example` → `config/.env`，填入講者自己的 Key 作 demo 用
2. 放入校徽：`activity-3-marp/assets/school-logo.png`
3. 預跑 [`trainer/demo-script.md`](trainer/demo-script.md) 全流程
4. 派發課前電郵（見 checklist 範本）



---

## 🧩 延伸活動（課後或加堂）

**活動四：生成 HTML+CSS+JS（教學用靜態網站）**

- **目標**：用 Cursor Agent 生成一個可直接上線的靜態小工具（無需 build）
- **素材**：`activity-4-web/`（starter + prompts）
- **發佈**：跟 [`handouts/07-static-site-publish.md`](handouts/07-static-site-publish.md) 將靜態檔放入 NAS `_web` folder，經 `teacher.chw.edu.hk` 對外發佈
