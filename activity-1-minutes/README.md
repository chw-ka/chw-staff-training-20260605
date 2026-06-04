# 活動一：錄音 → 會議紀錄（Workflow 實操）

> **本資料夾可獨立使用：** Cursor → **File → Open Folder** → 選本資料夾即可。  
> **本活動真正目標：** 學懂 **Workflow（工作流）** — 唔係淨係「問 AI 一句」。  
> **例子：** 錄音 → 文字 → 議程 + 格式 → 輸出會議紀錄（格式可跟通用範本或上學年紀錄）。

---

## 快速開始（3 步）

1. **開啟資料夾** — Cursor → Open Folder → 選 **`activity-1-minutes`**
2. **開 Agent** — `Ctrl + I`，Model 用 **Auto** 即可（詳見 [`handouts/cursor-setup-brief.md`](handouts/cursor-setup-brief.md)）
3. **貼 Prompt 實操** — 打開 [`handouts/prompt-cheatsheet.md`](handouts/prompt-cheatsheet.md)，由 Phase 1 開始

---

## 完整 Workflow 一覽

```
┌─────────┐    ┌─────────┐    ┌────────────────────────────┐    ┌─────────────┐
│  錄音    │ →  │  文字    │ →  │ 議程 + 格式（範本或上學年）  │ →  │  會議紀錄    │
│  .m4a   │    │ 逐字稿   │    │                            │    │             │
└─────────┘    └─────────┘    └────────────────────────────┘    └─────────────┘
   第一步          第一步            第二步 / 第三步（可選）
   Agent 寫 code   本機轉寫          Agent + SKILL
```

| 階段 | 課堂做咩 | 用咩 Model / 工具 | 時間（課堂） |
|------|----------|-------------------|--------------|
| **Phase 1** | 短錄音 → 逐字稿 | Cursor Agent 寫 Python + **Whisper large-v3** | ~8 min |
| **第二步** | 逐字稿 + 議程 + 通用範本 → `.md` + **`.docx` 草稿** | Cursor Agent + SKILL | ~8 min |
| **第三步** | 逐字稿 + 議程 + 上學年格式 → `.md` + **`.docx` 正式紀錄** | Cursor Agent + SKILL | ~4 min |

---

## 點解唔喺課堂轉 1 小時錄音？

| 現實 | 說明 |
|------|------|
| 網頁版限制 | 大多數平台 **唔俾 upload 咁大檔**，或有字數上限 |
| 最準 model 好慢 | **Whisper large-v3** 轉 1 小時錄音，求最準可以 **1–2 小時** |
| Cursor 嘅價值 | 叫 Agent **幫你寫 code**，本機慢慢跑 — 你唔使識寫程式 |
| 課堂策略 | 用 **~45 秒** short clip 示範 Phase 1；Phase 2–3 用已備好嘅 **完整視藝科逐字稿** |

---

## 資料夾說明

| 檔案 / 資料夾 | 用途 |
|---------------|------|
| `handouts/prompt-cheatsheet.md` | **Phase 1–3 Prompt**（課堂直接貼） |
| `handouts/cursor-setup-brief.md` | 開啟資料夾 + Agent 設定 |
| `.cursor/skills/meeting-minutes/SKILL.md` | 寫紀錄專用 SKILL |
| `.cursor/rules/` | AI 回應語氣規則（行政文書風格） |
| `samples/demo-short-clip.m4a` | **Phase 1** 示範用短錄音（~45 秒） |
| `samples/demo-short-clip-expected-transcript.txt` | 預期轉寫結果（對照用） |
| `samples/新錄音 2.m4a` | 完整長錄音（**課後**自行轉寫練習；~73 分鐘） |
| `sample-meeting-transcript.txt` | **Phase 2–3** 視藝科組完整逐字稿 |
| `議程_視藝科組會_20260528.docx` | 議程（Word，Phase 2） |
| `minutes-template.md` | 通用格式範本（第二步） |
| `會議紀錄_視藝科組_20250522_上學年.docx` | 上學年紀錄（第三步：**格式參考**，唔係合併內容） |
| `expected-output-sample.md` | 預期輸出（對照用） |
| `scripts/transcribe.py` | Whisper 轉寫 script（Agent 可改寫） |
| `scripts/build_sample_docs.py` | 重新產生 .docx 範本（需 `python-docx`） |
| `output/` | 你的輸出（逐字稿 `.txt`、紀錄 `.md` 草稿、正式 `.docx`） |

---

## 點解有兩種檔？

| 格式 | 用途 |
|------|------|
| **排版文字（.md）** | 喺 Cursor 內預覽、改稿；課堂順便接觸新格式 |
| **Word（.docx）** | 老師日常開檔、列印、傳同事 — **正式交付用呢個** |

---

## 課堂逐步操作

詳見 [`handouts/prompt-cheatsheet.md`](handouts/prompt-cheatsheet.md) 三個 Phase。

**Vibe Coding 收束（第一步尾聲必講）：**

> 你會見到 **左面檔案列表不斷有新檔** — 唔使驚，**唔使識睇 code**。  
> 老師嘅角色：清楚 **Input（錄音、議程、範本）** 同 **Output（逐字稿、Word 紀錄）**；中間點行，交俾 Agent。

**第二步、三步收束：**

> 「Cursor 會先出 **排版文字（.md）** 方便改；最後會幫你轉 **Word（.docx）** — 你平時開嘅就係呢份。」

---

## Phase 1 課前準備（講者 / IT）

1. 本機已安裝 **Python 3.10+** 及 **ffmpeg**（Whisper 需要）
2. 預跑：`pip install -r scripts/requirements.txt`
3. 首次跑 Whisper 會下載 large-v3（約 3 GB）— **請課前完成**
4. 測試：`python scripts/transcribe.py`

---

## 課後延伸

1. 用 `samples/新錄音 2.m4a` 在本機跑完整轉寫（預留 1–2 小時）
2. 換你自己科組錄音 + Agenda + 範本
3. 把 `.cursor/skills/meeting-minutes/` 複製到你日常 project 的 `.cursor/skills/`
