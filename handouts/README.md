# 學員講義索引 — 閱讀與派發次序

> 檔名編號（00–09）方便管理；**實際使用請依下表時序**，無需由 01 順序讀至 09。  
> **Word 列印版：** [`docx/`](docx/) — **合訂本** [`docx/CHW-Cursor-Training-Handouts-Merged.docx`](docx/CHW-Cursor-Training-Handouts-Merged.docx)（封面+目錄+全章）；執行 `python scripts/build_handout_docx.py` 更新

---

## 課前（培訓日前 1–3 日）

| 次序 | 檔案 | 用途 | 必做？ |
|:---:|------|------|:------:|
| 1 | [`08-appendix-安裝清單.md`](08-appendix-安裝清單.md) | 安裝 Cursor、Demo Login、Open Folder | ✅ |
| 2 | [`05-api-key-application-guide.md`](05-api-key-application-guide.md) | 自備 Gemini／DeepSeek（離開 Demo 後用） | 可選 |
| — | [`06-google-drive-mcp-setup.md`](06-google-drive-mcp-setup.md) + [`09-google-drive-self-study.md`](09-google-drive-self-study.md) | 雲端 Drive 整理 | 課後自學 |

---

## 課堂當日（90 分鐘）

| 時段 | 次序 | 檔案 | 對應活動 |
|------|:---:|------|----------|
| 00–10 min 引入 | 0 | [`00-core-concepts-glossary.md`](00-core-concepts-glossary.md) | Workflow、SKILL、MCP、排版文字等 |
| 10–20 min 環境 | 1 | [`08-appendix-安裝清單.md`](08-appendix-安裝清單.md) | 投影跟做 |
| | 2 | [`01-cursor-setup-guide.md`](01-cursor-setup-guide.md) | Auto、快捷鍵 |
| 20–85 min 實操 | 3 | [`02-prompt-cheatsheet.md`](02-prompt-cheatsheet.md) | 活動一至三 + MARP 延伸 Prompt |
| 60–85 min（可選口述） | 4 | [`07-static-site-publish.md`](07-static-site-publish.md) | 活動三上線 `teacher.chw.edu.hk` |
| 85–90 min | 5 | [`03-faq-hk-guide.md`](03-faq-hk-guide.md) | 派發、課後填 Key 速查 |

**講者列印建議：** 00（或課堂投影）、08、02、03（見 [`trainer/pre-class-checklist.md`](../trainer/pre-class-checklist.md)）

---

## 課後自學

| 次序 | 檔案 | 用途 |
|:---:|------|------|
| 1 | [`03-faq-hk-guide.md`](03-faq-hk-guide.md) | API Key 填入、Ollama、常見錯誤 |
| 2 | [`05-api-key-application-guide.md`](05-api-key-application-guide.md) | 若課前未申請 Key |
| 3 | [`07-static-site-publish.md`](07-static-site-publish.md) | 將活動三 `output/` 放上 NAS `_web` |
| 4 | [`04-filesystem-mcp-guide.md`](04-filesystem-mcp-guide.md) | Filesystem MCP 試玩 |
| 5 | [`06-google-drive-mcp-setup.md`](06-google-drive-mcp-setup.md) | OAuth 設定 |
| 6 | [`09-google-drive-self-study.md`](09-google-drive-self-study.md) | 雲端整理（配合 [`activity-5-gdrive/`](../activity-5-gdrive/)） |
| — | [`02-prompt-cheatsheet.md`](02-prompt-cheatsheet.md) 末段 | MARP 簡報 → [`activity-4-marp/`](../activity-4-marp/) |

---

## 與活動資料夾對照

| 活動 | 課堂主講義 | 活動內精簡版 |
|------|------------|--------------|
| 活動一 Minutes | `02` Phase 1–3 | [`activity-1-minutes/handouts/`](../activity-1-minutes/handouts/) |
| 活動二本機整理 | `02` 活動二段 | [`activity-2-files/handouts/`](../activity-2-files/handouts/) |
| 活動三靜態網站 | `02` + `07` | [`activity-3-web/sample-prompts.md`](../activity-3-web/sample-prompts.md) |
| 課後 MARP | `02` 延伸段 | [`activity-4-marp/`](../activity-4-marp/) |
| 課後 Drive | `06` + `09` | [`activity-5-gdrive/`](../activity-5-gdrive/) |

---

## 講者專用（不派發學員）

| 檔案 | 用途 |
|------|------|
| [`10-google-forms-service-account-setup.md`](10-google-forms-service-account-setup.md) | 以 Service Account API 建立課後回饋問卷 |

---

## 即場問題

課堂若遇阻，講者請參考 [`trainer/troubleshooting.md`](../trainer/troubleshooting.md)（不派發學員）。
