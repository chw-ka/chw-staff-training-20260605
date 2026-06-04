# Infographic Prompts — Gemini 生圖用

> 配合 [`talking-points.md`](talking-points.md) 開場及概念段。  
> 建議比例：**16:9**（投影）或 **3:4**（WhatsApp／簡報單頁）。  
> **小提示：** AI 出繁中文字有時會錯字；若標籤唔準，用文末「無字版」prompt 出圖，再喺 PowerPoint 加字。

---

## 風格統一（每張 prompt 末尾可加）

```
Style lock: flat vector infographic, white background, navy #1e3a5f primary, orange #f5a623 accent, generous whitespace, 4K, suitable for school staff training slides.
```

---

## 圖 1｜Cursor 介面三區（開場用）

**用途：** 邊講「左中右」邊投影

```
Create a clean educational infographic, 16:9 landscape, flat modern style, soft navy blue and warm orange accent, white background.

Show a simplified desktop app window labeled "Cursor" with THREE clearly separated vertical panels:

LEFT panel (25% width): file explorer tree icon, folder names, label in Traditional Chinese: 「檔案列表 — 櫃桶目錄」

CENTER panel (50% width): document preview like Word, meeting minutes text, label: 「編輯／預覽區 — 好似 Word」

RIGHT panel (25% width): chat/agent panel with message bubbles, highlighted as the main focus with a glowing border, label: 「Agent — 今日主力 ✦」

At the bottom, four small badge icons with shortcuts:
「Ctrl+I Agent」「Ctrl+L Chat」「Ctrl+ , 設定」「@ 引用檔案」

Inside the Agent panel, annotate three spots with arrows:
1. 「Model 下拉」top-left
2. 「貼 Prompt」input box
3. 「Approve 批准」button

Friendly tone for school teachers, not scary developer aesthetic. No real code, no gibberish text. Professional training slide quality. Traditional Chinese labels only.
```

---

## 圖 2｜點解學 Cursor（香港情境）

**用途：** 開場「點解唔用 Claude Desktop」

```
Educational comparison infographic, 16:9, minimalist flowchart style, school training workshop look.

Title at top in Traditional Chinese: 「點解今日學 Cursor？」

Three-column flow left to right:

Column 1 — 「以前」: icon of Claude Desktop chat app, caption 「Claude Desktop — 寫文書最順手」

Column 2 — 「香港現實」: red gentle X or barrier icon over Hong Kong map silhouette, captions 「Claude Desktop 用唔到」「Codex 用唔到」

Column 3 — 「今日選擇」: Cursor logo-style abstract window icon (generic, not exact trademark), caption 「Cursor — API + MCP + 本機檔案」

Bottom banner in Traditional Chinese: 「重點唔係變程式員，係學工作流設計」

Clean icons, flat design, navy/teal/white palette, no cluttered text, suitable for projector.
```

---

## 圖 3｜五個核心概念（概念總覽）

**用途：** 呼應 Workflow / MCP / Skills / Rules / Model

```
Infographic poster, 16:9 landscape, five equal cards in a row, modern flat illustration for non-technical school staff.

Title: 「Cursor 五個概念 — 帶返學校自己砌」

Card 1 — Workflow: arrow flow 「輸入 → 步驟 → 輸出」, subtitle 「老師 = 設計師，AI = 實習文員」

Card 2 — MCP: magical door portal connecting to cloud, subtitle 「隨意門 — 連 Google Drive」

Card 3 — Skills: reusable recipe card icon, subtitle 「會議紀錄專用規則」

Card 4 — Rules: checklist document, subtitle 「繁體書面語、表格格式」

Card 5 — Model / API: brain chip + key icon, subtitle 「DeepSeek / Gemini」

Each card has a simple icon + Traditional Chinese label. Soft colors, professional, not cyberpunk. White background, subtle shadows.
```

---

## 圖 4｜老闘 vs 實習文員（減抗拒）

**用途：** 講「中間唔使逐行睇 code」

```
Friendly workplace metaphor illustration, 16:9, warm cartoon-flat style (not childish), for adult teachers.

Scene: A confident teacher labeled 「你 — 工作流老闘」 sits at desk pointing right.

On the right, a helpful assistant robot/human intern labeled 「Agent — 實習文員」 works on a computer screen.

Center screen shows formatted meeting minutes (not code).

Speech bubble from teacher: 「右邊講嘢，中間睇結果」

Small note: 「Approve 先至郁 — 安全閥」

Traditional Chinese text. Clean, encouraging, school admin office setting. Avoid scary tech imagery.
```

---

## 圖 5｜今日三個 Activity 時間軸

**用途：** 預覽整堂課

```
Horizontal timeline infographic, 16:9, three milestones, clean corporate-training style.

Title: 「CHW 教職員培訓 — 今日路線圖」

Milestone 1 (20–40 min): document icon, 「活動一 會議紀錄」, tags 「DeepSeek」「Skill」「API」

Milestone 2 (40–65 min): Google Drive cloud icon with magic sparkle, 「活動二 雲端整理」, tags 「MCP」「Approve」

Milestone 3 (65–85 min): presentation slides icon, 「活動三 MARP 簡報」, tags 「Gemini」「多模態」

Connecting arrow labeled 「Agentic Workflow」

Color code each activity differently but harmoniously. Traditional Chinese. Minimal text, large icons for classroom visibility.
```

---

## 圖 6｜Chatbot → Agent 演進（AI 2026 段）

**用途：** 「一問一答 vs 多步驟」

```
Before-and-after infographic, 16:9, split screen.

LEFT side gray tone — 「舊：Chatbot」: single question bubble → single answer bubble. Caption 「一問一答」

RIGHT side bright tone — 「新：Agent」: user goal at top, then 3–4 connected steps (read file → process → write output → ask approval), caption 「多步驟、自動執行、你批核」

Center arrow: 「2026 變革」

Bottom: 「老師做工作流設計師」

Flat icons, Traditional Chinese, training slide aesthetic.
```

---

## 備用：無字版（中文字出錯時用）

若出圖後繁中標籤糊／錯，用原 prompt 再加以下句子 regenerate：

```
Regenerate with NO text inside the image. Use numbered labels ①②③ and blank rounded rectangles for text placeholders only. I will add Traditional Chinese in PowerPoint later.
```

### 圖 1 無字版 placeholder 對照

| 編號 | PowerPoint 加字 |
|------|-----------------|
| 左欄 | 檔案列表 — 櫃桶目錄 |
| 中欄 | 編輯／預覽區 — 好似 Word |
| 右欄 | Agent — 今日主力 |
| ① | Model 下拉 |
| ② | 貼 Prompt |
| ③ | Approve 批准 |
| 底欄 | Ctrl+I Agent · Ctrl+L Chat · Ctrl+, 設定 · @ 引用檔案 |

---

## 建議使用順序（開場 10 分鐘）

| 順序 | 圖 | talking-points 段落 |
|------|-----|---------------------|
| 1 | 圖 2 | §0 點解要學 Cursor |
| 2 | 圖 1 | §1 Cursor 介面速覽 |
| 3 | 圖 3 或 圖 6 | §2 AI 2026 變革 |
| 4 | 圖 5 | 預覽三個 Activity（可選） |

圖 4 可穿插 §1 講「老闘 vs 實習文員」時用。

---

## 圖 7｜活動一 Workflow — 錄音 → Minutes

**用途：** 活動一開場（20–40 min）

```
Horizontal workflow infographic, 16:9, four connected steps with arrows, school training style.

Title: 「活動一 — 學懂 Workflow（以會議紀錄為例）」

Step 1 — microphone icon: 「錄音 .m4a」subtitle 「Phase 1：Whisper large-v3」note 「課堂：45秒 demo」

Step 2 — document icon: 「文字 transcript」subtitle 「Cursor 寫 code 本機轉」

Step 3 — checklist + template: 「Agenda + 格式範本」subtitle 「Phase 2：DeepSeek + SKILL」

Step 4 — formal minutes: 「會議紀錄」subtitle 「第三步：上學年格式 + 今年內容（可選）」

Bottom banner: 「Vibe Coding — 唔使識睇 code，重 Input / Output」

Side note box: 「1小時錄音 ≈ 1–2小時轉寫 → 課後自己機慢慢做」

Traditional Chinese, navy/orange palette, flat icons.
```

---

## 建議使用順序（活動一）

| 順序 | 圖 | 段落 |
|------|-----|------|
| 1 | 圖 7 | 活動一 Workflow 開場 |
| 2 | 圖 4 | Phase 1 Vibe Coding 收束 |
