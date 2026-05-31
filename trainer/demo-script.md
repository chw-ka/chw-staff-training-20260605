# 講者 Demo Script — 逐步操作腳本

> 講者請課前完整預跑一遍，記錄實際所需時間。

---

## 開場（00:00–00:10）

**[投影 LessonPlan.md 或簡短 intro slide]**

**話術：**
> 「各位同事午安/早安。今日 90 分鐘，我哋唔係學 ChatGPT 問答，而係學點樣用 Cursor Agent 幫你自動做 meeting minutes、執 file、出簡報。
> 完堂時你會有一條完整 workflow，可以直接帶返去科組用。」

**動作：** 無需操作電腦。

---

## 環境設定（00:10–00:20）

**[投影 handouts/01-cursor-setup-guide.md]**

**話術：**
> 「首先『駁通水喉』。我哋唔用 OpenAI，只用 **Gemini** 同 **DeepSeek** 兩個 API。
> 請大家開 Cursor，Open Folder 揀今日個 project，跟住 01 設定指南填入你課前申請嘅 Key。」

**動作：**
1. 示範 Gemini Key → `gemini-2.0-flash`
2. 示範 DeepSeek Key → Override URL `https://api.deepseek.com` → `deepseek-chat`
3. 全班跟做，講者巡場
4. `Cmd+I` → 選 deepseek-chat →「你好，請用香港廣東話回覆我：連線正常嗎？」

**成功指標：** 全班收到廣東話回覆。

**若有人 lag：** 已完成的同事先閱讀 `handouts/02-prompt-cheatsheet.md`。

---

## 活動一 Demo（00:20–00:40）

**[開啟 activity-1-minutes/]**

**話術：**
> 「大家有冇試過一個鐘科組會，錄音轉文字好長，网页 paste 唔晒？
> API 就係打破呢個限制。我哋仲會用 SKILL — 把寫 minutes 嘅規則預先寫好，次次都用同一標準。」

**動作：**
1. 簡介 `sample-meeting-transcript.txt`（1 min）
2. 打開 Agent，貼上 `handouts/02-prompt-cheatsheet.md` 活動一 Prompt
3. 或加 `@.cursor/skills/meeting-minutes/SKILL.md`
4. Allow Agent 讀檔、寫檔
5. 開啟 output，對照 `expected-output-sample.md`

**話術（生成後）：**
> 「留意決議有冇漏、日期啱唔啱。AI 係草稿，你係 editor。」

**全班練習：** 用同一 Prompt 自己跑一遍（約 8 min）。

---

## 活動二 Demo（00:40–01:05）— 【雲端神蹟】

**[並排：Cursor + Chrome drive.google.com]**

**話術：**
> 「第二個痛點：Google Drive 垃圾崗。今日唔寫 Python — 用 MCP 直接郁雲端。
> 大家 Drive 開住 `CHW_Training_垃圾崗`，Cursor 貼 Prompt，每次 Approve 就返去 browser 睇。」

**動作：**
1. 展示垃圾崗 4 個亂碼檔
2. 貼 `activity-2-gdrive/sample-prompts.md` 主推 Prompt
3. 慢動作 Approve：`listFolder` → `createFolder` → `renameItem` → `moveItem`
4. 開 `CHW_Training_已整理/視覺藝術/` 展示成果

**全班練習：** 跟住 Approve 完整整理（約 8 min）

**備用（OAuth 全掛）：** 見 `activity-2-watchdog/` + `trainer/troubleshooting.md`

---

## 活動三 Demo（01:05–01:25）

**[開啟 activity-3-marp/]**

**話術：**
> 「校長話：聽日早會你要匯報。傳統開 PowerPoint 起碼一個鐘。
> MARP 用 Markdown 寫 slide；Agent 讀頭先 minutes，直接出簡報。」

**動作：**
1. 快速展示 `marp-syntax-reference.md` 的 `bg left` 語法（2 min）
2. 展示 `template-with-footer.md` footer 效果（1 min）
3. Agent 貼活動三 Prompt
4. Allow 生成 `activity-3-marp/output/morning-briefing.md`
5. 開 Marp Preview 或 export PDF

**若 Gemini 圖片失敗：**
> 「圖片生成需要額外 API；今日重點係 MARP workflow，placeholder 都得。」

**全班練習：** 生成簡報或改 template（約 8 min）。

---

## 總結（01:25–01:30）

**話術：**
> 「今日三個 activity：會議 → 紀錄 → 簡報；Google Drive 垃圾崗 → 雲端自動整理。
> 處理學生私隱時，請考虑用 Ollama 本地模型 — FAQ 有教。
> **重要：API Key 係你自己嘅，課後繼續用。** DeepSeek 記得 check 餘額。詳見 handouts/03-faq-hk-guide.md。
> 多謝大家，祝各位成為工作流總設計師！」

**動作：** 派發/分享 handouts 連結，Q&A（可 overrun 1–2 min）。

---

## 講者備忘

| 項目 | 位置 |
|------|------|
| 講者 demo 用 Key | `config/.env`（勿 commit） |
| Google OAuth | `config/gcp-oauth.keys.json` |
| 活動二 Drive | `CHW_Training_垃圾崗` + samples/ |
| DeepSeek Base URL | `https://api.deepseek.com` |
| 活動一/二 Model | `deepseek-v4-flash` |
| 活動三 Model | `gemini-2.5-flash` |
| 校徽 | activity-3-marp/assets/school-logo.png |
| 備用 output | activity-1-minutes/expected-output-sample.md |
| 備用本地 demo | activity-2-watchdog/homework_watcher.py |
