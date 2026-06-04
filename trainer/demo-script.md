# 講者 Demo Script — 逐步操作腳本

> 講者請課前完整預跑一遍，記錄實際所需時間。

---

## 開場（00:00–00:10）

**[投影 LessonPlan.md 或簡短 intro slide]**

**話術：**
> 「各位同事午安/早安。今日 90 分鐘，我們不是學 ChatGPT 問答，而是學如何用 Cursor Agent 自動做 meeting minutes、整理檔案、出簡報。
> 完堂時你會有一條完整 workflow，可以直接帶回科組使用。」

**動作：** 無需操作電腦。

---

## 環境設定（00:10–00:20）

**[投影 handouts/08-appendix-安裝清單.md]**

**話術：**
> 「安裝 Cursor、Demo Login、Python 跟 **附錄** 做 — 我唔逐 step 讀。Demo 登入用到 **7月3日**，帳密我而家派。
> Python 大部分唔使自己裝：跟活動一叫 Agent 幫你，得就唔使理附錄 C。
> Agent Model 揀 **Auto** 就得，唔使填 API Key。」

**動作：**
1. 派 Demo Login（紙／投影片）
2. 學員跟附錄 A–B 自做；Open Folder
3. 講者巡場；已完成者預習 02 handout
4. 快速測試：Agent 問一句「請用繁體中文書面語回覆：連線正常嗎？」

**成功指標：** 大部分學員 Agent 收到繁體中文書面語回覆。

**若有人 lag：** 已完成者先閱讀 `handouts/02-prompt-cheatsheet.md`。

---

## 活動一 Demo（00:20–00:40）— Workflow 三階段

**[開啟 activity-1-minutes/，投影 README workflow 圖]**

**話術：**
> 「活動一學 **Workflow**，唔係淨係出 minutes。
> 真實流程：錄音 → 文字 → Agenda + 範本 → 紀錄；可加埋上年纪錄。
> 一個鐘錄音用最準 model 轉文字要 **一兩個鐘**，網頁又 upload 唔到 — 所以 Cursor 幫你 **寫 code** 本機跑。
> 今日 Phase 1 用 **45 秒** clip 示範；Phase 2–3 用視藝科完整稿。」

**Phase 1（~8 min）：**
1. 播放 `samples/demo-short-clip.m4a`
2. Agent 貼 `02-prompt-cheatsheet.md` **Phase 1 Prompt**（Model：**Auto**）
3. Allow 生成 script + 跑 Whisper → `output/transcript-from-audio.txt`
4. **Vibe Coding 話術：** 左面檔案自己郁，唔使睇 code，重 Input/Output

**Phase 2（~8 min）：**
1. 展示 `議程_視藝科組會_20260528.docx`、`minutes-template.md`
2. 貼 **Phase 2 Prompt** + SKILL
3. 對照 `expected-output-sample.md`

**Phase 3（~4 min）：**
1. 貼 **第三步 Prompt**，用 `@會議紀錄_視藝科組_20250522_上學年.docx` 做格式參考
2. 對照 `expected-output-sample.md`

**全班練習：** Phase 1 + 2 必做；Phase 3 時間許可再做。

**詳細腳本：** [`trainer/activity-1-demo-script.md`](activity-1-demo-script.md)

**Whisper 備用：** 跳過 live 轉寫，見 `troubleshooting.md`。

---

## 活動二 Demo（00:40–01:00）— 先傾清楚，再執行

**[Open Folder `activity-2-files/`]**

**話術：** 見 [`talking-points-activity2-files.md`](talking-points-activity2-files.md) 開場。

**動作：**
1. 展示 `inbox/` ~100 亂檔 + `sorted/` 目標結構（教學、行政、ICT…）
2. 階段 A：傾談 Prompt（唔搬檔）— 全班 3 min
3. 階段 B：定 `my_organization_profile.md` — 5 min
4. 階段 C：一句執行 → 逐步 Approve → 睇 `sorted/` 入檔

**全班練習：** 時間唔夠可跳 A，用 `.example` 直做 C。

**課後：** Google Drive 見 `09-google-drive-self-study.md`

---

## 活動三 Demo（01:00–01:25）

**[開啟 activity-3-marp/]**

**話術：**
> 「校長說：明天早會你要匯報。傳統開 PowerPoint 起碼一個鐘。
> MARP 用 Markdown 寫 slide；Agent 讀剛才的 minutes，直接出簡報。」

**動作：**
1. 快速展示 `marp-syntax-reference.md` 的 `bg left` 語法（2 min）
2. 展示 `template-with-footer.md` footer 效果（1 min）
3. Agent 貼活動三 Prompt
4. Allow 生成 `activity-3-marp/output/morning-briefing.md`
5. 開 Marp Preview 或 export PDF

**若 Gemini 圖片失敗：**
> 「圖片生成需要額外 API；今日重點是 MARP workflow，placeholder 也可以。」

**全班練習：** 生成簡報或改 template（約 8 min）。

---

## 總結（01:25–01:30）

**話術：**
> 「今日三個 activity：會議 → 紀錄 → 簡報；Google Drive 垃圾崗 → 雲端自動整理。
> 處理學生私隱時，請考慮用 Ollama 本地模型 — FAQ 有教。
> **課後**如用自己 Key，詳見 handouts/03-faq-hk-guide.md 及 05 申請指南。
> 多謝大家，祝各位成為工作流總設計師！」

**動作：** 派發/分享 handouts 連結，Q&A（可 overrun 1–2 min）。

---

## 講者備忘

| 項目 | 位置 |
|------|------|
| 講者 demo 用 Key | `config/.env`（勿 commit；課堂學員用 Auto） |
| Google OAuth | `config/gcp-oauth.keys.json` |
| 活動二 Drive | `CHW_Training_垃圾崗` + samples/ |
| Agent Model | **Auto**（全課） |
| 活動一 Whisper | `large-v3`（`scripts/transcribe.py`） |
| 活動一短 clip | `activity-1-minutes/samples/demo-short-clip.m4a` |
| 活動一詳細腳本 | `trainer/activity-1-demo-script.md` |
| 校徽 | activity-3-marp/assets/school-logo.png |
| 備用 output | activity-1-minutes/expected-output-sample.md |
| 活動二示範檔 | `activity-2-files/inbox/` |
| 課後 Drive 自學 | `09-google-drive-self-study.md` |
