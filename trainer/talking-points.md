# 講者 Talking Points — 各時段核心概念

---

## 00–10 min｜引入

### 0. 點解要學 Cursor？（開場必講，約 3–4 分鐘）

**背景（用口語講，書面重點如下）：**

| 要講 | 重點句 |
|------|--------|
| 定位轉變 | Cursor **原本係專業級** 開發工具；而家介面易用，**好多非 IT 同事都用緊** |
| 以前最好選擇 | 純聊天、寫文書，不少人覺得 **Claude Desktop** 最順手 |
| 香港現實 | Claude Desktop、Codex 等 **香港用唔到**（地區／帳戶限制） |
| 今日取捨 | 學校培訓選 **Cursor** — 能接 API、MCP、Skills，又可在本機操作檔案 |
| **今日真正目標** | 最重要係學 **概念**，帶返學校自己砌： |

**五個概念（可逐個舉今日 Activity 對應）：**

1. **Workflow（工作流）** — 唔係問一句就算，而係「輸入 → 步驟 → 輸出」；老師係設計師，AI 係實習文員
2. **MCP** — 連接外部服務（今日：Google Drive）；比喻「隨意門」
3. **Skills** — 可重複使用的專用規則（今日：會議紀錄 SKILL）
4. **Rules** — 長期約束 AI 語氣、格式（例如：繁體書面語、表格欄位）
5. **Model** — 課堂用 **Auto**；課後可自備 API Key（見 05 / 03 FAQ）

**收束一句（建議原句照講）：**

> 「我哋唔係培訓你變程式員，而係培訓你識得 **設計工作流** — Cursor 只係而家香港用得著嘅 **載體**。」

---

### 1. Cursor 介面速覽（約 2–3 分鐘，邊講邊指住螢幕）

> 好多同事未開過 — **唔使驚似寫程式個樣**，今日主要用右邊同設定，中間當「預覽 Word」。

**三個區域（由左至右）：**

| 位置 | 叫咩 | 今日用途 | 比喻 |
|------|------|----------|------|
| **左** | 檔案列表（Explorer） | 睇培訓資料夾入面有咩檔 | 櫃桶目錄 — 今日已幫大家 **Open Folder** 開好 |
| **中** | 編輯／預覽區 | 睇會議紀錄、排版文字、簡報預覽 | 好似 Word 工作區 |
| **右** | **Agent** 對話窗 | **本課主力** — 貼 prompt、批核操作 | 實習文員 + 秘書，坐喺你右手邊 |

**必記四個掣（可即場按一次俾全班睇）：**

| 操作 | 快捷鍵 | 講法 |
|------|--------|------|
| 開 **Agent** | `Ctrl + I`（Mac：`Cmd + I`） | 今日 90% 時間用呢個 |
| 開 **Chat** | `Ctrl + L` | 純問答、唔改檔 — 課堂較少用 |
| **設定** | `Ctrl + ,` | 課堂唔使填 Key；課後見 03 FAQ |
| 引用檔案 | 輸入 `@` | 話 Agent 讀邊份稿，唔使複製貼成段 |

**Agent 窗內再指三個位：**

1. **Model 下拉**（左上角）— 課堂揀 **Auto** 即可
2. **輸入框** — 貼 prompt；可以 `@sample-meeting-transcript.txt` 咁講
3. **Approve / Allow** — Agent 想改檔、連 Drive 前會問你；**一定要你批准先郁** — 安全閥

**可選一句（減低抗拒）：**

> 「中間嗰堆字唔使逐行睇；你係 **老闘**，Agent 係 **幫你執嘢** 嗰個。右邊講嘢，中間睇結果。」

**概念預告（指 `.cursor` 資料夾，唔深入）：**

- **Rules** — 長期叮囑（語氣、表格格式）
- **Skills** — 某類工作嘅專用指引（例如會議紀錄）
- 詳細設定下一節跟 **附錄** 做；呢度只係 **認路**

**節奏提示：** 講完介面 → 再講 AI 大趨勢 → 學員跟附錄 Open Folder 時就唔會搵唔到掣。

---

### 2. AI 2026 變革（約 3 分鐘）

1. **從 Chatbot 到 Agent** — 舊：一問一答；新：多步驟、自動執行
2. **Agentic Workflow** — 呼應上面：老師做「工作流設計師」
3. **今日三個 Activity** — Minutes（Workflow + Skill）→ 本機執檔 → **靜態網站**（瀏覽器 preview）

**節奏提示：** 先講「點解 Cursor」→ **指認介面** → 再講「AI 點變」→ 最後預覽三個 Activity → 下一節跟 **附錄** 做環境準備。

---

## 10–20 min｜環境準備

> **唔使逐項教安裝。** 簡短帶做，詳細步驟叫學員 **返去睇附錄**。

**話術（約 1–2 分鐘）：**
> 「下一節大家跟 [`handouts/08-appendix-安裝清單.md`](../handouts/08-appendix-安裝清單.md) 做 — 我哋課前已講清楚要裝咩：**Cursor**、**Demo Login**（用到 **7月3日**）、同有需要先至裝 **Python**。
> Python 大部分唔使自己裝 — 跟活動一叫 Agent 幫你，搞掂就唔使理附錄 C。
> Agent Model 揀 **Auto**，唔使填 API Key。」

**講者動作：**
1. 投影附錄 A–C 目錄（30 秒）— 唔逐 step 讀
2. 派 Demo Login（紙／投影片）— **勿公開轉發**
3. 巡場：已完成者先開 02 預習
4. 落後者：指住附錄做，唔阻塞全班

**唔使喺呢度講：** Google Drive MCP 細節（06 handout）、API Key 填入方法 — 課後見 03 FAQ，問先答。

---

## 20–40 min｜活動一：Workflow — 錄音 → Minutes

> **本活動真正目標：學懂 Workflow**（以會議紀錄為例）。詳細腳本：[`activity-1-demo-script.md`](activity-1-demo-script.md)

### 開場（2 min）— 講清 Workflow

```
錄音 → 文字 → + Agenda + 格式範本 →（+ 上年纪錄）→ 會議紀錄
```

| 要講 | 重點句 |
|------|--------|
| 真實痛點 | 1 小時錄音 **upload 唔到** 網頁、**最準 model 要 1–2 小時** |
| Cursor 價值 | 叫 Agent **寫 code**，本機用 **Whisper large-v3** 慢慢轉 |
| 課堂取捨 | Phase 1 用 **~45 秒** clip；Phase 2–3 用備好嘅 **視藝科完整逐字稿** |
| Model 概念 | Agent 用 **Auto** 寫 code；轉文字最準用 **Whisper large-v3**（唔係同一個腦） |

---

### Phase 1（8 min）— 錄音 → 文字 · Vibe Coding

1. 播放 `demo-short-clip.m4a` 幾秒
2. Agent 貼 **Phase 1 Prompt**（02 handout）→ Allow 寫 script + 跑 terminal
3. 開 `output/transcript-from-audio.txt`

**必講收束：**
> 「左面檔案不斷生成 — **唔使驚、唔使識睇 code**。你係老闘，最重要 **Input / Output**。呢個就叫 **Vibe Coding**。」

---

### Phase 2（8 min）— Agenda + 範本 → 紀錄

- 展示 `議程_視藝科組會_20260528.docx`、`minutes-template.md`
- Phase 2 Prompt + `@meeting-minutes SKILL`
- 輸出 `meeting-minutes-draft.md`（改稿）+ `會議紀錄_草稿.docx`（Word 開）— **AI 起草，你覆核**

---

### 第三步（4 min）— 用上學年格式寫今年紀錄

- `@會議紀錄_視藝科組_20250522_上學年.docx` 做**格式參考**（唔係合併）
- 內容來自 `@sample-meeting-transcript.txt` + 議程
- 輸出 `meeting-minutes-final.md` + `會議紀錄_視藝科組_20260528.docx`

---

### 備用

| 情況 | 做法 |
|------|------|
| Whisper 太慢 / 下載失敗 | 跳過 Phase 1，直接用 `sample-meeting-transcript.txt` |
| 時間不足 | 第三步講者 demo only |
| 對照 output | `expected-output-sample.md` |

---

## 40–60 min｜活動二：本機文件整理

> 完整話術：[`talking-points-activity2-files.md`](talking-points-activity2-files.md)

**一句話：** 先傾 → 定規則 → 讀**內容**分類入 `sorted/`（教學、行政、ICT…）。Open Folder **`activity-2-files`**。

---

## 60–85 min｜活動三：靜態網站（HTML/CSS/JS）

> 完整話術：[`talking-points-activity3-web.md`](talking-points-activity3-web.md)

**一句話：** Agent 生成小工具 → 本機打開 `output/index.html` preview → 課後可複製 NAS `_web` 上線（07 講義）。

- Model：**Auto**
- 先展示 `starter/index.html`，再 live 生成 `output/`
- **唔喺課堂逐 step 教 07** — 總結可口述 30 秒；詳細課後跟講義

---

## 85–90 min｜總結

> 投影 [`fig-10-closing-summary.png`](infographics/fig-10-closing-summary.png)（可選）。  
> 派發／提醒：`03-faq-hk-guide.md` · **課後延伸**（見下）。

### 1. 私隱（必講，約 1 分鐘）

| 要講 | 重點句 |
|------|--------|
| 課堂範圍 | 今日只動 **project 內示範檔**，唔改你真正 Downloads／桌面 |
| 敏感資料 | 學生私隱、成績、評語 → **Ollama 本機** 或校內核准工具（見 `03-faq-hk-guide.md`） |
| 公開網站 | 放入 `_web` 的檔案 = **公開**；**唔好**把 API Key 寫入 HTML/JS |

**收束一句：**

> 「Agent 好勁，但**批核同邊份資料可以出街**，仍然係你嘅責任。」

---

### 2. 活動三上線提醒（約 1 分鐘）

**對照講義：** [`handouts/07-static-site-publish.md`](../handouts/07-static-site-publish.md) · 素材 [`activity-3-web/`](../activity-3-web/)

**話術（建議原句）：**

> 「剛才活動三已經 preview 咗小工具 — **上線**就係將 `output/` 複製去 NAS **`_web`**，同事打開 **`teacher.chw.edu.hk/{代碼}/`** 就睇到。」

**三句講清原理（唔使逐 step 讀講義）：**

| 概念 | 講法 |
|------|------|
| 唔係 Google Drive | Drive **唔會**當網站跑 HTML/JS；學校係 **NAS → 伺服器 → HTTPS 網址** |
| 你要做咩 | 喺 NAS 自己 folder 開 **`_web`**，放入 `index.html` 等靜態檔 |
| Wow 句 | 「**唔使申請 hosting** — 07 講義有路徑同常見問題」 |

**必記三點（可快速投影 07 參考卡）：**

1. 路徑：`\\10.10.0.13\staff\{代碼}\_web\`
2. 入口：**必須有** `index.html`；CSS/圖片用**相對路徑**
3. 新開 `_web` 可能要等 **最多 1 小時** 掃描

---

### 3. 課後延伸 — Google Drive 整理（約 1 分鐘）

**對照講義：** [`handouts/09-google-drive-self-study.md`](../handouts/09-google-drive-self-study.md) · 設定 [`06-google-drive-mcp-setup.md`](../handouts/06-google-drive-mcp-setup.md) · 素材 [`activity-5-gdrive/`](../activity-5-gdrive/)

**話術（建議原句）：**

> 「課堂活動二係 **本機 inbox 執檔** — 唔使 OAuth，全班跟得上。  
> 若你想整理 **Google Drive 垃圾崗**，呢個 **唔喺 90 分鐘內**；課後睇 **09 自學指引**。」

**與活動二對照（一表講清）：**

| | 課堂活動二 | 課後 09 自學 |
|--|-----------|--------------|
| 位置 | 本機 `activity-2-files` | **雲端** Drive |
| 技術 | Agent + `@inbox/` | **Google Drive MCP** |
| 課前 | 唔使 OAuth | 要跟 **06** 做 OAuth |
| 你已學識 | 先傾 → 定規則 → Approve | **同一套 Workflow**，只係「隨意門」改連 Drive |

**收束：**

> 「09 寫明：**做完 OAuth → 開 `activity-5-gdrive` → 貼 sample prompt → 逐 step Approve** — 同今日一樣，你係老闘。」

---

### 4. 結語（約 30 秒）

**建議原句照講：**

> 「老師嘅價值唔再係重複性行政，而係 **工作流總設計師**。  
> 課堂三個 Activity 係起點；**07 上線、09 整雲端、MARP 簡報（activity-4-marp）**，都係同一套 Agent + Approve，課後慢慢試。」

**派發提醒：**

| 講義 | 用途 |
|------|------|
| `02-prompt-cheatsheet.md` | 三個活動 Prompt 懶人包 |
| `03-faq-hk-guide.md` | API Key、Ollama、常見問題 |
| `07-static-site-publish.md` | 活動三：teacher.chw.edu.hk 上線 |
| `09-google-drive-self-study.md` | 課後：Drive MCP 整理 |
