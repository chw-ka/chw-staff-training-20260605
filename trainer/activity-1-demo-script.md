# 活動一 Demo 腳本 — Workflow：錄音 → Minutes

> 配合 [`talking-points.md`](talking-points.md) §20–40 min。  
> 預計 **20 分鐘**；講者課前必預跑 Phase 1（Whisper 下載 + 短 clip 轉寫）。

---

## 開場（2 min）— 講清 Workflow

**[投影 workflow 圖 — 見 `activity-1-minutes/README.md` 或 infographic]**

**話術：**
> 「活動一唔係淨係學出 minutes，係學 **Workflow**。
> 真實流程：錄音 → 文字 → 加 Agenda 同格式範本 → 先至出到會議紀錄。
> 如果有上年纪錄，可以跟足舊格式，用今年議程同逐字稿寫全新紀錄。」

**話術（現實限制）：**
> 「一個鐘科組會，要用 **最準** 嘅 model 轉文字，隨時 **一兩個鐘**，又冇邊個網站俾你 upload 咁大檔。
> 所以 Cursor 幫到你：叫佢 **寫 code**，喺 **自己部機** 慢慢轉。
> 今日時間有限，Phase 1 用 **45 秒** short clip；Phase 2–3 用準備好嘅 **視藝科完整逐字稿**。」

---

## Phase 1：錄音 → 文字（8 min）

**[開 `activity-1-minutes/samples/demo-short-clip.m4a` 播放幾秒 — 讓學員聽到係真錄音]**

**話術：**
> 「你要識嘅係 **Model** — 轉文字最準係 **Whisper large-v3**。
> 你唔使識 Python；**右邊 Agent** 幫你寫。Agent Model 揀 **Auto** 就得。」

**動作：**
1. `Ctrl+I` 開 Agent，Model：**Auto**
2. 貼 [`handouts/02-prompt-cheatsheet.md`](../handouts/02-prompt-cheatsheet.md) **Phase 1 Prompt**
3. 逐次 **Allow** — 學員會見到左面生成 `scripts/transcribe.py` 等檔
4. Allow 跑 terminal：`pip install -r ...` 及 `python transcribe.py`
5. 開 `output/transcript-from-audio.txt`，對照 `samples/demo-short-clip-expected-transcript.txt`

**話術（Vibe Coding）：**
> 「留意左面檔案 **自己郁** — 你唔使睇 code。
> 最重要：**Input = 錄音，Output = 文字**。呢個就叫 **Vibe Coding**。」

**若 Whisper 太慢 / 下載失敗：**
> 跳過 live 轉寫，直接展示 `demo-short-clip-expected-transcript.txt`，進 Phase 2。  
> 見 [`troubleshooting.md`](troubleshooting.md)。

**全班跟做（3 min）：** 同一 Phase 1 Prompt。

---

## Phase 2：Agenda + 範本 → 會議紀錄（8 min）

**話術：**
> 「有逐字稿未夠 — 要有 **Agenda** 同 **格式範本**，AI 先至知點排版、有咩決議。」

**動作：**
1. 簡介 `議程_視藝科組會_20260528.docx`、`minutes-template.md`（1 min）
2. Agent Model：**Auto**
3. 貼 **Phase 2 Prompt**（`@sample-meeting-transcript.txt` + `@議程_視藝科組會_20260528.docx` + `@minutes-template.md` + SKILL）
4. Allow 寫入 `output/meeting-minutes-draft.md` 同 `output/會議紀錄_草稿.docx`
5. 對照 `expected-output-sample.md` — 強調 **AI 起草，你覆核**

**全班跟做（4 min）。**

---

## 第三步：用上學年格式寫今年紀錄（4 min，可選）

**話術：**
> 「如果有上學年紀錄，可以俾 Agent **跟足舊紀錄嘅版面同欄位**，用**今年議程**同**今年逐字稿**寫一份**全新**紀錄 — 唔係把兩份合併。」

**動作：**
1. 貼 **第三步 Prompt**
2. 輸出 `output/meeting-minutes-final.md` 同 `output/會議紀錄_視藝科組_20260528.docx`
3. 對照 `expected-output-sample.md`

**全班跟做（可選，時間不足則講者 demo only）。**

---

## 收束（1 min）

**話術：**
> 「今日你已經做咗成條 **Workflow**，亦都做咗 **Vibe Coding**。
> 課後用你自己一個鐘錄音，喺屋企開 Cursor，叫佢寫 code，揀 **large-v3**，泡杯茶等佢跑完就得。」

---

## 講者備忘

| 項目 | 值 |
|------|-----|
| Phase 1 寫 code | Auto（Agent） |
| Phase 1 轉寫 model | Whisper **large-v3** |
| Phase 2–3 寫 minutes | Auto（Agent） |
| 短 clip | `samples/demo-short-clip.m4a` (~45s) |
| 完整逐字稿 | `sample-meeting-transcript.txt` |
| 備用（skip Phase 1） | 直接用 `sample-meeting-transcript.txt` 做 Phase 2 |
