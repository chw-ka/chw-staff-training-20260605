# HKDSE PDF 擷取程式總結（供下個 chat 續用）

## 程式位置
- **主程式**：`scripts/pdf_to_md_langgraph.py`
- **共用模組**：`scripts/pdf_to_md_direct.py`（SYSTEM_PROMPT、QUESTION_SPLIT、split_questions 等）

## 必須用虛擬環境執行
```bash
source .venv/bin/activate
python scripts/pdf_to_md_langgraph.py --no-pre-filter --thread-id hkdse-2013 --paper 13_DSE_PHY --verbose
```
否則會出現 `ModuleNotFoundError: No module named 'yaml'`（系統 python 未裝 PyYAML）。

---

## 架構概覽
- **LangGraph** 工作流，使用 `SqliteSaver` checkpoint（`--sqlite-checkpoint` / `--thread-id`）
- **分卷抽取**：依序 `試卷一甲部 → 試卷一乙部 → 試卷二甲/乙/丙/丁`，每卷達標才進下一卷
- **Staging 落盤**：先寫到 `question_bank/.staging/{year}`，通過全卷 sanity 後才提交到 `question_bank/{year}`
- **完成後移檔**：成功擷取的 PDF 會從 `raw_pdfs` 移到 `raw_pdfs_extracted`

---

## 題數規則（硬編碼）
| 卷別 | 題型 | 規則 |
|------|------|------|
| 試卷一甲部 | 選擇題 | 33–36 題 |
| 試卷一乙部 | 結構題 | 8–15 題 |
| 試卷二甲/乙/丙/丁 | 選擇題 | 各 8 題 |
| 試卷二甲/乙/丙/丁 | 結構題 | 各 1 題 |

---

## 關鍵常數
- `MAX_API_CALLS_PER_DAY = 20`：每日 API 配額保險絲
- `MAX_QUALITY_RETRIES_PER_PDF = 4`：每卷未達標時自動補抽次數
- `SECTION_PLAN`：分卷順序

---

## Graph 節點
1. `node_quota_guard`：配額檢查
2. `node_pre_filter`：PyMuPDF 頁面預篩（`--no-pre-filter` 可略過）
3. `node_uploader`：上傳 PDF 至 Gemini（非 ASCII 檔名會先複製到暫存）
4. `node_extractor`：依當前卷別向 Gemini 抽取
5. `node_processor`：split → Pydantic 驗證 → 寫檔、去重、完成閘門、切下一卷
6. `node_uniqueness_report`：產出分卷唯一性報表
7. `node_finish_and_save`：配額熔斷時暫停並持久化

---

## 輸出結構
```
question_bank/
  .staging/          # 暫存（通過後提交到正式）
  _reports/          # 分卷唯一性報表 {year}_{paper}.md
  2012/試卷一甲部/選擇題/Q1.md ...
  2012/試卷一乙部/結構題/Q1.md ...
  2012/試卷二甲部/選擇題/Q1.md ...
```

---

## CLI 參數
- `--raw-dir`：輸入 PDF 目錄（預設 `raw_pdfs`）
- `--output-dir`：題庫輸出根目錄（預設 `question_bank`）
- `--paper`：只處理指定檔名 stem（如 `13_DSE_PHY`）
- `--thread-id`：checkpoint 線程 ID，續跑需相同
- `--no-pre-filter`：停用頁面預篩，建議使用
- `--verbose`：DEBUG 日誌

---

## 目前狀態
- **2012**：已完成，題數符合規則，`12_DSE_PHY.pdf` 已移至 `raw_pdfs_extracted`
- **2013**：可能正在執行中（用戶 terminal 顯示 `hkdse-2013 --paper 13_DSE_PHY`）
- **2014–2025**：尚待處理

---

## 已知注意點
1. 檔名含中文時，上傳前會自動複製到 ASCII 檔名暫存檔
2. checkpoint 與 thread-id 綁定，換年份建議用新 thread-id 或清 checkpoint
3. 每年首次處理會清空 `question_bank/{year}` 與 `.staging` 同年度目錄
