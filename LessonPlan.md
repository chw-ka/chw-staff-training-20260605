## 📋 課程基本資料

* **課程主題：** 2026年度 AI 驅動校園：從行政解放到高階自主開發
* **對象：** 有意願深入學習 AI 應用的學校教職員（Power Users）
* **時長：** 90 分鐘
* **主要工具：** Cursor (Agent / Composer 模式)、HTML/CSS/JS（靜態網站）
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

<br>生成靜態網站 | **Vibe Coding**<br>

<br>**Workflow** | **情境：** 老師想整一個**教學／行政小工具**（例如功課命名器），俾同事或學生用瀏覽器開。**做法：** 跟 [`activity-3-web/sample-prompts.md`](activity-3-web/sample-prompts.md) 叫 Agent 生成 **HTML + CSS + JS** 到 `output/` → **本機打開 `index.html` 預覽**。**Wow 點：** 唔使 PowerPoint、唔使 build；課後可複製到 NAS `_web` 上線（見 [`handouts/07-static-site-publish.md`](handouts/07-static-site-publish.md)）。 |
| 85-90 min<br>

<br>(05") | **總結與反思** | **數據私隱與未來** | **安全意識：** 提醒老師，處理涉及學生私隱或學校機密文件時，未來可結合今日學到的 MCP 工作流，在校內以 **Ollama 本地部署開源模型**安全處理。**結語：** 老師的價值不再是重複性行政，而是成為「工作流的總設計師」。 |

---

## 📌 講義筆記（Handout）必備三大核心板塊

以下素材已備妥，可直接派發或投影：

| 板塊 | 檔案 |
|------|------|
| **閱讀次序總覽** | [`handouts/README.md`](handouts/README.md) |
| **核心概念速查（Workflow / SKILL / MCP / .md）** | [`handouts/00-core-concepts-glossary.md`](handouts/00-core-concepts-glossary.md) |
| **附錄：安裝清單（課前＋課堂必做）** | [`handouts/08-appendix-安裝清單.md`](handouts/08-appendix-安裝清單.md) |
| 駁通水喉（Cursor 快速開始） | [`handouts/01-cursor-setup-guide.md`](handouts/01-cursor-setup-guide.md) |
| Prompt 懶人包（課堂核心） | [`handouts/02-prompt-cheatsheet.md`](handouts/02-prompt-cheatsheet.md) |
| 靜態網站發佈（活動三；可課堂口述） | [`handouts/07-static-site-publish.md`](handouts/07-static-site-publish.md) |
| 課後 FAQ 與香港自救 | [`handouts/03-faq-hk-guide.md`](handouts/03-faq-hk-guide.md) |
| API Key 申請（課後可選） | [`handouts/05-api-key-application-guide.md`](handouts/05-api-key-application-guide.md) |
| Filesystem MCP 試玩（課後） | [`handouts/04-filesystem-mcp-guide.md`](handouts/04-filesystem-mcp-guide.md) |
| Google Drive MCP 設定（課後自學） | [`handouts/06-google-drive-mcp-setup.md`](handouts/06-google-drive-mcp-setup.md) + [`09-google-drive-self-study.md`](handouts/09-google-drive-self-study.md) |

---

## 📦 完整培訓包索引

| 用途 | 位置 |
|------|------|
| 總覽與快速開始 | [`README.md`](README.md) |
| 課前 checklist | [`trainer/pre-class-checklist.md`](trainer/pre-class-checklist.md) |
| 逐步 demo 腳本 | [`trainer/demo-script.md`](trainer/demo-script.md) |
| 活動一詳細腳本 | [`trainer/activity-1-demo-script.md`](trainer/activity-1-demo-script.md) |
| 各時段講解要點 | [`trainer/talking-points.md`](trainer/talking-points.md) |
| 活動三詳細話術 | [`trainer/talking-points-activity3-web.md`](trainer/talking-points-activity3-web.md) |
| 即場 troubleshooting | [`trainer/troubleshooting.md`](trainer/troubleshooting.md) |
| 活動一：逐字稿 + 範本 + SKILL | [`activity-1-minutes/`](activity-1-minutes/) |
| 活動二：本機文件整理 | [`activity-2-files/`](activity-2-files/) |
| Google Drive 整理（課後自學） | [`activity-5-gdrive/`](activity-5-gdrive/) |
| 活動三：靜態網站（HTML/CSS/JS） | [`activity-3-web/`](activity-3-web/)（含 teaching-web / publish-web SKILL） |
| MARP 簡報（課後延伸） | [`activity-4-marp/`](activity-4-marp/) |
| API Key 範本（講者填寫） | [`config/.env.example`](config/.env.example) |

### 講者課前必做

1. 確認學員已完成 Cursor 安裝及 Demo Login（見 [`08-appendix-安裝清單.md`](handouts/08-appendix-安裝清單.md)；API Key 課後可選，見 05）
2. （可選）講者自己完成 Google Drive MCP，供課後 demo（[`06`](handouts/06-google-drive-mcp-setup.md) + [`09`](handouts/09-google-drive-self-study.md)）
3. 複製 `config/.env.example` → `config/.env`，填入講者自己的 Key 作 demo 用
4. 預跑 [`activity-3-web/starter/index.html`](activity-3-web/starter/index.html) 確認瀏覽器可開
5. 預跑 [`trainer/demo-script.md`](trainer/demo-script.md) 全流程
6. 派發課前電郵（見 checklist 範本）



---

## 🧩 延伸活動（課後或加堂）

**MARP 簡報（原活動三，改為課後）**

- **素材**：[`activity-4-marp/`](activity-4-marp/)（tech 模板 + sample）
- **Skill**：`.cursor/skills/marp-slide/`
- **注意**：AI 生圖簡報質素参差；課堂主線已改 **活動三 靜態網站**
