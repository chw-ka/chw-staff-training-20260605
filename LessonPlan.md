## 📋 課程基本資料

* **課程主題：** 2026年度 AI 驅動校園：從行政解放到高階自主開發
* **對象：** 有意願深入學習 AI 應用的學校教職員（Power Users）
* **時長：** 90 分鐘
* **主要工具：** Cursor (Agent / Composer 模式)、MARP、**Gemini API**、**DeepSeek API**
* **環境配置策略：** 學員課前按 [`handouts/05-api-key-application-guide.md`](handouts/05-api-key-application-guide.md) 自行申請 Gemini + DeepSeek Key；課堂 10 分鐘跟 [`handouts/01-cursor-setup-guide.md`](handouts/01-cursor-setup-guide.md) 填入 Cursor。**不使用 OpenAI API。**

---

## 📅 90分鐘進階 Staff Training 課程編排表

| 時間 | 教學活動 (Activity) | 核心概念 (Concepts) | 實操內容與教學細節 (Details & Implementation) |
| --- | --- | --- | --- |
| 00-10 min<br>

<br>(10") | **引入：AI 2026 變革** | **Workflow 概念** | **觀念重塑：** 告別舊時代「一問一答」的對話框。**核心：** 介紹什麼是 **Agentic Workflow**（智能體工作流）—— AI 開始具備多步驟思考、自動執行任務的能力。 |
| 10-20 min<br>

<br>(10") | 環境準備：<br>

<br>駁通私家水喉 | **環境配置** | **對照筆記：** 開 [`handouts/05-api-key-application-guide.md`](handouts/05-api-key-application-guide.md)（課前已申請）及 [`handouts/01-cursor-setup-guide.md`](handouts/01-cursor-setup-guide.md)。**實操：** 填入 **Gemini API Key** 同 **DeepSeek API Key**（DeepSeek 經 OpenAI 兼容接口，Base URL = `https://api.deepseek.com`）。**測試：** Agent 分別用 `deepseek-v4-flash` 同 `gemini-2.5-flash` 打廣東話測試句。 |
| 20-40 min<br>

<br>(20") | 活動 1：<br>

<br>錄音變 Minutes | **API**<br>

<br>**SKILL (提示詞)** | **痛點：** 1 小時科組會錄音，檔案大、網頁版易斷。**技術：** 解釋什麼是 **API**（大腦與服務的連接線），明白 API 能打破網頁版的字數與檔案限制。**SKILL 落地：** 利用「角色 + 學校背景 + 固定 Minutes 範本」的進階 Prompt，調用大模型 API 進行多步驟 Workflow 提煉。**Wow 點：** 丟入真實廣東話錄音，直接秒出結構完美的 Word 格式會議紀錄草稿。 |
| 40-65 min<br>

<br>(25") | 活動 2：<br>

<br>【雲端神蹟】<br>

<br>Google Drive 整理 | **MCP 概念**<br>

<br>**雲端 AUTOMATION**<br>

<br>**SKILL (Vibe Coding)** | **痛點：** 學校 Shared Drive / 個人 Drive 長期係垃圾崗，檔名亂、folder 冇規律。**技術 (MCP)：** 用「隨意門」比喻 — MCP 連接 **Google Drive**，Agent 可直接 list / rename / move 雲端檔案。**AUTOMATION 實踐：** Cursor Agent Window (`Cmd/Ctrl + I`) 用廣東話下令整理 `CHW_Training_垃圾崗`。**Wow 點：** 老師並排開 Cursor 同 browser，每按一次 **Approve**，睇住 Drive 入面檔案自己改名、開 folder、移位 — 好似隱形人幫手。 |
| 65-85 min<br>

<br>(20") | 活動 3：<br>

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
| 駁通水喉（Cursor 設定） | [`handouts/01-cursor-setup-guide.md`](handouts/01-cursor-setup-guide.md) |
| Prompt 懶人包 | [`handouts/02-prompt-cheatsheet.md`](handouts/02-prompt-cheatsheet.md) |
| 課後 FAQ 與香港自救 | [`handouts/03-faq-hk-guide.md`](handouts/03-faq-hk-guide.md) |
| Filesystem MCP 試玩 | [`handouts/04-filesystem-mcp-guide.md`](handouts/04-filesystem-mcp-guide.md) |
| Google Drive MCP 設定 | [`handouts/06-google-drive-mcp-setup.md`](handouts/06-google-drive-mcp-setup.md) |
| 靜態網站發佈（通用版） | [`handouts/07-static-site-publish.md`](handouts/07-static-site-publish.md) |

---

## 📦 完整培訓包索引

| 用途 | 位置 |
|------|------|
| 總覽與快速開始 | [`README.md`](README.md) |
| 課前 checklist | [`trainer/pre-class-checklist.md`](trainer/pre-class-checklist.md) |
| 逐步 demo 腳本 | [`trainer/demo-script.md`](trainer/demo-script.md) |
| 各時段講解要點 | [`trainer/talking-points.md`](trainer/talking-points.md) |
| 即場 troubleshooting | [`trainer/troubleshooting.md`](trainer/troubleshooting.md) |
| 活動一：逐字稿 + 範本 + SKILL | [`activity-1-minutes/`](activity-1-minutes/) |
| 活動二：Google Drive 雲端整理 | [`activity-2-gdrive/`](activity-2-gdrive/) |
| 活動三：MARP 簡報模板 | [`activity-3-marp/`](activity-3-marp/) |
| 活動四：靜態網站（HTML/CSS/JS） | [`activity-4-web/`](activity-4-web/) |
| API Key 範本（講者填寫） | [`config/.env.example`](config/.env.example) |

### 講者課前必做

1. 確認學員已完成 Google Drive MCP 設定（[`handouts/06-google-drive-mcp-setup.md`](handouts/06-google-drive-mcp-setup.md)）
2. 確認學員已按 [`handouts/05-api-key-application-guide.md`](handouts/05-api-key-application-guide.md) 申請 Gemini + DeepSeek Key
2. 複製 `config/.env.example` → `config/.env`，填入講者自己嘅 Key 作 demo 用
2. 放入校徽：`activity-3-marp/assets/school-logo.png`
3. 預跑 [`trainer/demo-script.md`](trainer/demo-script.md) 全流程
4. 派發課前電郵（見 checklist 範本）



---

## 🧩 延伸活動（課後或加堂）

**活動四：生成 HTML+CSS+JS（教學用靜態網站）**

- **目標**：用 Cursor Agent 生成一個可直接上線嘅靜態小工具（無需 build）
- **素材**：`activity-4-web/`（starter + prompts）
- **發佈**：先跟通用版 `handouts/07-static-site-publish.md`；待你提供 webhost，我再客製成「逐步截圖版」
