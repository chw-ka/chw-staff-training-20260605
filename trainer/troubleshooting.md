# 即場 Troubleshooting 指南

## API / 連線問題

| 症狀 | 可能原因 | 解決方法 |
|------|----------|----------|
| DeepSeek 404 | Base URL 打錯 | 用 `https://api.deepseek.com`，**不要**加 `/v1` |
| DeepSeek 401 | Key 錯 | 重新複製 `sk-...`，確認用 DeepSeek 平台 Key |
| DeepSeek 402 | 餘額不足 | 去 platform.deepseek.com 充值 |
| Gemini Invalid Key | Key 錯或 project 未開 | 重新在 AI Studio 建立 Key |
| Gemini quota exceeded | 超免費額度 | 等重置或改用 DeepSeek |
| 一直 loading | 校園防火牆 | 試 hotspot；查 IT 是否封鎖 API domain |
| 回覆變普通話 | Model 問題 | Prompt 加「請用繁體中文書面語」 |

**備用方案：** 展示 `activity-1-minutes/expected-output-sample.md`，跳過 live API。

---

## Cursor 介面問題

| 症狀 | 解決方法 |
|------|----------|
| 找不到 Agent | `Cmd + I`（Mac）或 `Ctrl + I`（Windows） |
| 找不到 Gemini 欄位 | Settings → Models → 搜尋 Google / Gemini |
| DeepSeek 填哪裡？ | 課堂唔使；課後見 [`03-faq-hk-guide.md`](../handouts/03-faq-hk-guide.md) |
| 無 Verify 按鈕 | 更新 Cursor；手動在 Agent 試一句 |

---

## 活動一：Workflow — 錄音 → Minutes

| 症狀 | 解決方法 |
|------|----------|
| Whisper 下載慢 / 失敗 | 課前講者預跑 `pip install -r activity-1-minutes/scripts/requirements.txt`；失敗則跳 Phase 1 |
| `ffmpeg` not found | 安裝 ffmpeg；或跳 Phase 1 用 `sample-meeting-transcript.txt` |
| Phase 1 超過 10 min | 展示 `demo-short-clip-expected-transcript.txt`，直入 Phase 2 |
| 格式不對 | 確認 `@minutes-template.md` + `@議程_視藝科組會_20260528.docx` |
| 格式唔似上學年 | 第三步確認 `@會議紀錄_視藝科組_20250522_上學年.docx` 係格式參考；對照 `expected-output-sample.md` |
| Agent 讀唔到 .docx | 用 Word 開確認檔案存在；或 Prompt 加「請讀 docx 內容」 |
| 冇出 .docx | Prompt 加「請將 .md 轉成 Word，存為 output/會議紀錄_草稿.docx」；需 `python-docx` |
| 寫 code 用邊個 model？ | **Auto**（Agent） |
| 轉寫用邊個 model？ | **Whisper large-v3**（在 transcribe.py 內，非 Agent 下拉） |
| 1 小時錄音課堂做唔完 | 正常；課後本機跑 `samples/新錄音 2.m4a`，預留 1–2 小時 |

**備用方案：** 跳過第一步，展示 `expected-output-sample.md`。

---

## 活動二：本機文件整理

| 症狀 | 解決方法 |
|------|----------|
| 只按副檔名分類 | 提醒 Agent 讀內容；引用 `@file-organizer SKILL` |
| 未傾就搬檔 | 先做階段 A；SKILL 禁止未確認就 mass-move |
| 搵唔到 inbox | Open Folder 選 `activity-2-files` |
| sorted 類別錯 | 改 `my_organization_profile.md` 再跑階段 C |

---

## 活動二（課後）：Google Drive MCP 自學

| 症狀 | 解決方法 |
|------|----------|
| MCP google-drive 紅色 | 跑 `activity-5-gdrive/setup-auth.sh`；Reload Cursor |
| `redirect_uri_mismatch` | OAuth client 必須是 **Desktop app** |
| Access blocked | OAuth consent 加 Test user |
| listFolder 找不到 folder | folder 名：`CHW_Training_垃圾崗` |
| Agent 不用 MCP | Prompt 寫明「用 Google Drive MCP」 |
| 用哪個 model？ | **Auto** |
| **全場 OAuth 失敗** | 改演示 [`activity-2-files/`](../activity-2-files/) 本機整理，或預錄片段 |

---

## 活動二（本機 files）

---

## 活動三：靜態網站

| 症狀 | 解決方法 |
|------|----------|
| 用哪個 model？ | **Auto** |
| 打開白畫面 | 確認路徑係 `output/index.html`；叫 Agent 檢查 JS 錯誤 |
| 樣式錯亂 | 要求「相對路徑引用 CSS」；唔好用 `/styles.css` |
| 上線 404 | 見 `07-static-site-publish.md` — 要有 `index.html`、等 NAS 掃描 |

---

## 時間不足時的裁剪策略

| 剩餘時間 | 建議 |
|----------|------|
| 少 5 分鐘 | 活動三只展示 starter + 講者 output preview |
| 少 10 分鐘 | 活動二只整理 1 檔；或切 Watchdog 備用 |
| 少 15 分鐘 | 活動一展示 expected output |
| API 全場掛 | 三活動用預備 output + 講 workflow |

---

## 緊急聯絡

- DeepSeek 支援：https://platform.deepseek.com
- Google AI Studio：https://aistudio.google.com
- IT 同事：[填入]
