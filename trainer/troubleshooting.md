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
| DeepSeek 填哪裡？ | OpenAI API Key 欄 + Override URL（見 01 設定指南） |
| 無 Verify 按鈕 | 更新 Cursor；手動在 Agent 試一句 |

---

## 活動一：Minutes

| 症狀 | 解決方法 |
|------|----------|
| 逐字稿太長 | `@sample-meeting-transcript.txt` 讓 Agent 讀檔 |
| 格式不對 | 貼 `minutes-template.md` 全文 |
| 用哪個 model？ | **deepseek-v4-flash** |

---

## 活動二：Google Drive MCP【雲端神蹟】

| 症狀 | 解決方法 |
|------|----------|
| MCP google-drive 紅色 | 跑 `activity-2-gdrive/setup-auth.sh`；Reload Cursor |
| `redirect_uri_mismatch` | OAuth client 必須是 **Desktop app** |
| Access blocked | OAuth consent 加 Test user |
| listFolder 找不到 folder | folder 名：`CHW_Training_垃圾崗` |
| Agent 不用 MCP | Prompt 寫明「用 Google Drive MCP」 |
| 用哪個 model？ | **deepseek-v4-flash** |
| **全場 OAuth 失敗** | 改用下方 Watchdog 備用 |

### 備用：本地 Watchdog

```bash
cd activity-2-watchdog && bash setup.sh && source .venv/bin/activate
python3 homework_watcher.py
```

---

## 活動二備用：Watchdog

| 症狀 | 解決方法 |
|------|----------|
| `ModuleNotFoundError: watchdog` | `bash setup.sh` |
| 腳本不觸發 | inbox 要新檔 |

---

## 活動三：MARP

| 症狀 | 解決方法 |
|------|----------|
| 用哪個 model？ | **gemini-2.5-flash**（插圖） |
| 圖片生成失敗 | 用 placeholder；重點教 MARP 語法 |
| 校徽不顯示 | 確認 `assets/school-logo.png` 存在 |

---

## 時間不足時的裁剪策略

| 剩餘時間 | 建議 |
|----------|------|
| 少 5 分鐘 | 活動三展示 template，不 live 生圖 |
| 少 10 分鐘 | 活動二只整理 1 檔；或切 Watchdog 備用 |
| 少 15 分鐘 | 活動一展示 expected output |
| API 全場掛 | 三活動用預備 output + 講 workflow |

---

## 緊急聯絡

- DeepSeek 支援：https://platform.deepseek.com
- Google AI Studio：https://aistudio.google.com
- IT 同事：[填入]
