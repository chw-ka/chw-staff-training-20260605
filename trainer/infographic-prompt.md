# Infographic Prompts — 配合講者 Talking Points 生圖

> **對照：** [`talking-points.md`](talking-points.md)（各時段話術）· [`talking-points-activity2-files.md`](talking-points-activity2-files.md)  
> **生圖腳本：** `scripts/generate_infographics.py`（支援 `--backend gemini|siliconflow`）  
> **已生成圖片：** [`infographics/`](infographics/)（fig-01 … fig-10）  
> **小提示：** AI 出繁中常糊／錯字 → **建議預設用「無字版」**（見下文），字喺 PowerPoint 加。

---

## 生圖 Model 選擇

| 優先 | Backend | Model | 適用 | 備註 |
|------|---------|-------|------|------|
| **★ 建議** | **SiliconFlow** | `Qwen/Qwen-Image` | 香港、要準 **16:9**、少文字 | API：`image_size: "1920x1080"`；`.env` 要 `SILICONFLOW_API_KEY` |
| 次選 | Gemini | `gemini-2.5-flash-image` | 已有 `GEMINI_API_KEY` | **必須**加 `imageConfig.aspectRatio: "16:9"`，否則易出 **1:1 方圖** |
| 唔建議 | Gemini | 同上 + 繁中長句 | 投影用 | 中文字常唔清；改 **無字版** 或 SiliconFlow |

```powershell
# 建議：SiliconFlow + 無字版 + 強制重生成
python scripts/generate_infographics.py --backend siliconflow --force

# Gemini（腳本會送 imageConfig aspectRatio 16:9）
python scripts/generate_infographics.py --backend gemini --force

# 若堅持圖內出字（唔建議繁中）
python scripts/generate_infographics.py --backend siliconflow --with-text --force
```

---

## 比例硬性要求（16:9 投影）

> **問題：** 只喺 prompt 寫「16:9」**唔夠** — Gemini 預設常出 **1024×1024（1:1）**。  
> **目標：** **1920×1080** 或同等 **16:9**（闊 : 高 = **1.778**），配合 PowerPoint 闊螢幕。

**每張 prompt 開頭必須有（英文，俾 model 跟）：**

```
MANDATORY CANVAS: landscape 16:9 widescreen presentation slide, exact aspect ratio 16:9, resolution 1920x1080 pixels, horizontal layout only, NOT square, NOT 4:3, NOT portrait.
```

**SiliconFlow API：** `image_size: "1920x1080"`（腳本已設）

**Gemini API：** `generationConfig.imageConfig.aspectRatio: "16:9"`（腳本已設）

**匯入 PPTX 後自查：** 右鍵圖片 → 大小 → 比例應約 **1.78**（例如 1920×1080、1344×768）。

---

## 風格統一（每張 prompt 末尾加）

**有字版**（僅短英文 label；繁中建議改 PowerPoint 加）：

```
Style lock: flat vector infographic, white background, navy #1e3a5f primary, orange #f5a623 accent, generous whitespace, MANDATORY 16:9 landscape 1920x1080 widescreen slide, 4K quality, CHW school staff training. Minimal English labels only; avoid long Traditional Chinese inside the image.
```

**無字版（★ 建議預設）** — 每張 prompt 末尾加：

```
NO TEXT VERSION: Do not render any letters, words, or Chinese characters inside the image. Use icons, arrows, numbered circles ①②③④⑤, and empty rounded rectangles as text placeholders only. I will add Traditional Chinese in PowerPoint. MANDATORY 16:9 landscape 1920x1080 widescreen.
```

**活動三 web 預覽圖**（可選）：改用 navy/orange web app palette — 呼應 `activity-3-web/starter/`。

---

## 圖 1｜Cursor 介面三區

**對照：** talking-points **§1 Cursor 介面速覽**（00–10 min）

**用途：** 邊講「左中右」邊投影

```
Create a clean educational infographic, 16:9 landscape, flat modern style, soft navy blue and warm orange accent, white background.

Show a simplified desktop app window labeled "Cursor" with THREE clearly separated vertical panels:

LEFT panel (25% width): file explorer tree icon, folder names, label in Traditional Chinese: 「檔案列表 — 櫃桶目錄」note 「Open Folder 已開好培訓資料夾」

CENTER panel (50% width): document preview like Word, meeting minutes text, label: 「編輯／預覽區 — 好似 Word，唔使逐行睇 code」

RIGHT panel (25% width): chat/agent panel with message bubbles, highlighted as the main focus with a glowing border, label: 「Agent — 今日主力 ✦」

At the bottom, four small badge icons with shortcuts:
「Ctrl+I Agent」「Ctrl+L Chat」「Ctrl+ , 設定」「@ 引用檔案」

Inside the Agent panel, annotate three spots with arrows:
1. 「Model 下拉 → Auto」top-left
2. 「貼 Prompt」input box
3. 「Approve 批准 — 安全閥」button

Friendly tone for school teachers, not scary developer aesthetic. No real code, no gibberish text. Professional training slide quality. Traditional Chinese labels only.
```

---

## 圖 2｜點解學 Cursor（香港情境）

**對照：** talking-points **§0 點解要學 Cursor？**（00–10 min，開場必講）

**用途：** 開場「點解唔用 Claude Desktop」

```
Educational comparison infographic, 16:9, minimalist flowchart style, school training workshop look.

Title at top in Traditional Chinese: 「點解今日學 Cursor？」

Subtitle banner: 「原本係專業級開發工具 — 而家非 IT 同事都用緊」

Three-column flow left to right:

Column 1 — 「以前最好」: icon of Claude Desktop chat app, caption 「Claude Desktop — 寫文書最順手」

Column 2 — 「香港現實」: red gentle X or barrier icon over Hong Kong map silhouette, captions 「Claude Desktop 用唔到」「Codex 用唔到」

Column 3 — 「今日選擇」: Cursor logo-style abstract window icon (generic, not exact trademark), caption 「Cursor — API + MCP + 本機檔案」

Bottom banner in Traditional Chinese: 「重點唔係變程式員，係學 **工作流設計** — Cursor 只係香港用得著嘅載體」

Clean icons, flat design, navy/teal/white palette, no cluttered text, suitable for projector.
```

---

## 圖 3｜五個核心概念

**對照：** talking-points **§0 五個概念** + **§1 概念預告**（Rules / Skills）

**用途：** 呼應 Workflow / MCP / Skills / Rules / Model

```
Infographic poster, 16:9 landscape, five equal cards in a row, modern flat illustration for non-technical school staff.

Title: 「Cursor 五個概念 — 帶返學校自己砌」

Card 1 — Workflow: arrow flow 「輸入 → 步驟 → 輸出」, subtitle 「老師 = 設計師，AI = 實習文員」

Card 2 — MCP: magical door portal connecting to folder icon and optional cloud, subtitle 「隨意門 — 本機檔案；課後可連 Drive」

Card 3 — Skills: reusable recipe card icon, subtitle 「會議紀錄 SKILL · 執檔 SKILL」

Card 4 — Rules: checklist document, subtitle 「繁體書面語、表格格式」

Card 5 — Model: dropdown labeled 「Auto」, small key icon for after-class, subtitle 「課堂 Auto；課後 API Key 可選」

Each card has a simple icon + Traditional Chinese label. Soft colors, professional, not cyberpunk. White background, subtle shadows.
```

---

## 圖 4｜老闘 vs 實習文員

**對照：** talking-points **§1 可選一句** + 活動一 **Phase 1 Vibe Coding 收束**

**用途：** 講「中間唔使逐行睇 code」

```
Friendly workplace metaphor illustration, 16:9, warm cartoon-flat style (not childish), for adult teachers.

Scene: A confident teacher labeled 「你 — 工作流老闘」 sits at desk pointing right.

On the right, a helpful assistant robot/human intern labeled 「Agent — 實習文員」 works on a computer screen.

Center screen shows formatted meeting minutes (not code).

Speech bubble from teacher: 「右邊講嘢，中間睇結果」

Small note: 「Approve 先至郁 — 安全閥」

Secondary tag: 「Vibe Coding — 重 Input / Output」

Traditional Chinese text. Clean, encouraging, school admin office setting. Avoid scary tech imagery.
```

---

## 圖 5｜90 分鐘課程時間軸

**對照：** talking-points **§2 今日三個 Activity** + LessonPlan 編排表

**用途：** 預覽整堂課（00–90 min）

```
Horizontal timeline infographic, 16:9, six milestones on one line, clean corporate-training style.

Title: 「CHW 教職員培訓 — 90 分鐘路線圖」

Milestone 1 (00–10 min): lightbulb icon, 「引入 — AI 2026」, tags 「Workflow」「Agent」

Milestone 2 (10–20 min): wrench icon, 「環境準備」, tags 「Cursor」「Auto」「附錄 08」

Milestone 3 (20–40 min): microphone + document, 「活動一 錄音→Minutes」, tags 「Whisper」「SKILL」「Vibe Coding」

Milestone 4 (40–60 min): folder inbox icon, 「活動二 本機執檔」, tags 「先傾後做」「讀內容」「Approve」

Milestone 5 (60–85 min): static web browser preview style, 「活動三 靜態小工具」, tags 「HTML/CSS/JS」「本機 preview」

Milestone 6 (85–90 min): shield icon, 「總結」, tags 「私隱」「Ollama」「工作流設計師」

Connecting arrow labeled 「Agentic Workflow」

Note at bottom: 「Google Drive 整理 — 課後自學 09，唔喺 90 分鐘內」

Color code each milestone differently but harmoniously. Traditional Chinese. Minimal text, large icons for classroom visibility.
```

---

## 圖 6｜Chatbot → Agent 演進

**對照：** talking-points **§2 AI 2026 變革**

**用途：** 「一問一答 vs 多步驟」

```
Before-and-after infographic, 16:9, split screen.

LEFT side gray tone — 「舊：Chatbot」: single question bubble → single answer bubble. Caption 「一問一答」

RIGHT side bright tone — 「新：Agent」: user goal at top, then 3–4 connected steps (read file → process → write output → ask approval), caption 「多步驟、自動執行、你批核」

Center arrow: 「2026 變革 — Agentic Workflow」

Bottom three small icons in a row: 「活動一 Minutes」「活動二 執檔」「活動三 靜態網站」

Bottom line: 「老師做工作流設計師」

Flat icons, Traditional Chinese, training slide aesthetic.
```

---

## 圖 7｜活動一 Workflow — 錄音 → Minutes

**對照：** talking-points **20–40 min 活動一** + [`activity-1-demo-script.md`](activity-1-demo-script.md)

**用途：** 活動一開場（20–40 min）

```
Horizontal workflow infographic, 16:9, four connected steps with arrows, school training style.

Title: 「活動一 — 學懂 Workflow（以會議紀錄為例）」

Step 1 — microphone icon: 「錄音 .m4a」subtitle 「Phase 1：Whisper large-v3」note 「課堂：~45 秒 demo clip」

Step 2 — document icon: 「文字 transcript」subtitle 「Agent 寫 code 本機轉 — Vibe Coding」

Step 3 — checklist + template: 「Agenda + 格式範本」subtitle 「Phase 2：Auto + meeting-minutes SKILL」

Step 4 — formal Word doc: 「會議紀錄 .docx」subtitle 「第三步（可選）：上學年格式 + 今年內容 — 唔係合併」

Bottom banner: 「Vibe Coding — 唔使識睇 code，重 Input / Output」

Side note box: 「1 小時錄音 ≈ 1–2 小時轉寫 → 課後自己機慢慢做」

Traditional Chinese, navy/orange palette, flat icons.
```

---

## 圖 8｜活動二 — 先傾後做 · 本機執檔

**對照：** [`talking-points-activity2-files.md`](talking-points-activity2-files.md)

**用途：** 活動二開場（40–60 min）

```
Three-phase horizontal infographic, 16:9, school admin training style.

Title: 「活動二 — inbox 約 100 檔 · 讀內容分類」

Phase A — speech bubbles icon: 「A 傾談 3–5 min」bullet 「唔搬檔，只傾分類規則」

Phase B — profile document icon: 「B 定規則 3–5 min」bullet 「my_organization_profile.md + folder_structure」

Phase C — magic folder sort icon: 「C 一句執行 10–12 min」bullet 「讀 @inbox/ 內容 → sorted/教學、行政、ICT…」

Center inbox pile labeled 「亂檔名 (1)(2) — 唔按副檔名分類」

Output folders shown: 「sorted/教學/2025-2026/」「sorted/行政/跨學年/」「sorted/trash/」

Bottom: 「Open Folder → activity-2-files · 逐步 Approve · 只動 project 內檔案」

Traditional Chinese, navy/orange, flat vector.
```

---

## 圖 9｜活動三 — 靜態網站小工具

**對照：** talking-points **60–85 min 活動三** + `activity-3-web/starter/`

**用途：** 活動三開場（60–85 min）

```
Web app workflow infographic, 16:9, modern clean UI, navy/orange school training style.

Title: 「活動三 — Agent 生成靜態小工具」

Flow left to right:

1. Prompt: homework naming tool or admin utility
2. Agent outputs index.html, styles.css, app.js to activity-3-web/output/
3. Browser preview: open index.html locally
4. Optional: copy folder to NAS _web → teacher.chw.edu.hk

Caption: 「唔使 PowerPoint、唔使 build — 瀏覽器 preview 即時 Wow」

Tags: 「HTML/CSS/JS」「本機 preview」「07 上線講義」

Bottom note: 「課堂 Model：Auto」

Traditional Chinese labels, professional school context, not cluttered.
```

---

## 圖 10｜總結 — 私隱與課後

**對照：** talking-points **85–90 min 總結**

**用途：** 收束全堂

```
Closing infographic, 16:9, calm professional style, white background navy text.

Title: 「帶返學校 — 工作流總設計師」

Three cards:

Card 1 — lock icon: 「敏感資料」subtitle 「學生私隱 → Ollama 本機 / 校內核准工具」

Card 2 — folder icon: 「課堂只動示範檔」subtitle 「唔改真正 Downloads / 桌面」

Card 3 — cloud homework icon: 「課後自學」subtitle 「Google Drive 整理 → handouts/09」

Bottom quote banner: 「老師嘅價值唔再係重複行政，而係設計工作流」

Traditional Chinese, minimal text, large icons.
```

---

## 備用：無字版（★ 建議預設 — 字唔清時必用）

**Gemini / SiliconFlow 出繁中標籤常糊、錯字、亂碼。** 培訓投影建議 **全部用無字版** 生成，再跟下表喺 PowerPoint 加字。

若已用有字版 prompt，regenerate 時加：

```
Regenerate with NO text inside the image. Use numbered labels ①②③ and blank rounded rectangles for text placeholders only. I will add Traditional Chinese in PowerPoint later.
```

### 圖 1 無字版 placeholder 對照

| 編號 | PowerPoint 加字 |
|------|-----------------|
| 左欄 | 檔案列表 — 櫃桶目錄 |
| 中欄 | 編輯／預覽區 — 好似 Word |
| 右欄 | Agent — 今日主力 |
| ① | Model → Auto |
| ② | 貼 Prompt |
| ③ | Approve 批准 |
| 底欄 | Ctrl+I Agent · Ctrl+L Chat · Ctrl+, 設定 · @ 引用檔案 |

---

## 建議使用順序 — 總表

| 時段 | talking-points | 建議用圖 |
|------|----------------|----------|
| **00–10 min** 引入 | §0 點解 Cursor | 圖 2 |
| | §1 介面速覽 | 圖 1（可穿插圖 4） |
| | §2 AI 2026 | 圖 6 或 圖 3 |
| | 預覽全堂 | 圖 5（可選） |
| **10–20 min** 環境 | 投影附錄 08 | 圖 5 里程碑 2 特寫（可選） |
| **20–40 min** 活動一 | Workflow 開場 | 圖 7 |
| | Phase 1 收束 | 圖 4 |
| **40–60 min** 活動二 | 先傾後做 | 圖 8 |
| **60–85 min** 活動三 | 靜態網站 | 圖 9 |
| **85–90 min** 總結 | 私隱 + 課後 | 圖 10 |

---

## 建議使用順序 — 開場 10 分鐘（精簡）

| 順序 | 圖 | talking-points |
|------|-----|----------------|
| 1 | 圖 2 | §0 點解要學 Cursor |
| 2 | 圖 1 | §1 Cursor 介面速覽 |
| 3 | 圖 6 或 圖 3 | §2 AI 2026 變革 |
| 4 | 圖 5 | 預覽 90 分鐘（可選） |

圖 4 可穿插 §1 講「老闘 vs 實習文員」時用。

---

## 建議使用順序 — 活動一（20–40 min）

| 順序 | 圖 | 段落 |
|------|-----|------|
| 1 | 圖 7 | Workflow 開場 |
| 2 | 圖 4 | Phase 1 Vibe Coding 收束 |

---

## 建議使用順序 — 活動二（40–60 min）

| 順序 | 圖 | 段落 |
|------|-----|------|
| 1 | 圖 8 | 三階段 A→B→C + inbox 痛點 |

---

## 建議使用順序 — 活動三（60–85 min）

| 順序 | 圖 | 段落 |
|------|-----|------|
| 1 | 圖 9 | Prompt → HTML/CSS/JS → 瀏覽器 preview |

---

## 建議使用順序 — 總結（85–90 min）

| 順序 | 圖 | 段落 |
|------|-----|------|
| 1 | 圖 10 | 私隱 · Ollama · 課後 09 · 工作流設計師 |
