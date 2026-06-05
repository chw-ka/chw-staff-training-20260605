# 學員講義 — Word 列印版

本資料夾由 [`scripts/build_handout_docx.py`](../../scripts/build_handout_docx.py) 自動產生，供**列印／PDF**派發同事。全文已改為**繁體中文書面語**。

## 一次過列印（推薦）

| 檔案 | 說明 |
|------|------|
| **`CHW-Cursor-Training-Handouts-Merged.docx`** | 封面 + **目錄** + 全部 10 章合併；開啟 Word 後對目錄**右鍵 → 更新功能變數** |

```bash
python scripts/build_handout_docx.py
```

（需已安裝 `python-docx`、`docxcompose`）

## 建議列印次序

| 次序 | 檔案 | 備註 |
|:---:|------|------|
| 1 | `00-core-concepts-glossary.docx` | 概念速查（可課前派發） |
| 2 | `08-appendix-install-checklist.docx` | 課堂跟做（附錄：安裝清單） |
| 3 | `02-prompt-cheatsheet.docx` | **核心** — 三活動 Prompt |
| 4 | `03-faq-hk-guide.docx` | 課末派發 |
| 5 | 其餘 | 課後自學按需列印 |

完整閱讀次序見 [`../README.md`](../README.md)。

## 版面說明

- 字型：**微軟正黑體** 11pt；程式碼用 Consolas
- 標題：深藍／學院藍
- 表格：淺藍表頭
- 頁尾：校名 · 培訓名稱 · 檔名

修改 `handouts/*.md` 後請重新執行上述指令以更新 `.docx`。
