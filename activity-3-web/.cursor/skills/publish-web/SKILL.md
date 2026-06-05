---
name: publish-web
description: >-
  將 activity-3-web/output/ 發佈到 NAS _web folder（teacher.chw.edu.hk）。
  Use when the user says publish、上線、發佈、deploy _web、放上教師網站.
---

# 發佈教學網頁 SKILL（teacher.chw.edu.hk）

## 觸發

用戶講：**publish**、**上線**、**發佈**、**copy 去 _web**、**放上教師網站** 等。

## 前置（缺一即停，教用戶設定）

1. **`activity-3-web/publish.config.json`** 存在（由 `publish.config.example.json` 複製）
   - `teacher_code`：教師代碼（例如 `KA`）
   - 或填 `publish_target_override`：已 map 的 NAS 路徑（例如 `P:\\KA\\_web`）
2. **`activity-3-web/output/index.html`** 存在且老師已 preview 滿意
3. NAS 已連線（檔案總管能開 `\\10.10.0.13\staff` 或 `P:\`）

## 執行步驟（Agent）

```
1. 確認 output/index.html 存在
2. 若無 publish.config.json → 引導複製 example 並填 teacher_code
3. 先 dry-run：
   python scripts/publish_web.py --dry-run
4. 將 dry-run 結果展示俾用戶，問：「確認複製去 _web？」
5. 用戶確認後：
   python scripts/publish_web.py --yes
6. 回報公開網址：https://teacher.chw.edu.hk/{teacher_code}/
```

## 安全規則

- **未 preview 唔好 publish**
- **未得用戶確認唔好加 `--yes`**
- **唔刪** `_web` 入面其他舊檔（腳本只覆寫同名檔／資料夾）
- 新開 `_web` 可能要等 **最多 1 小時** 先出網址 — 見 07 講義

## 用戶一句話範例

| 用戶講 | Agent 做 |
|--------|----------|
| 「publish」 | dry-run → 確認 → `--yes` |
| 「上線」 | 同上 |
| 「preview 完，可以發佈」 | 可跳過再問，直接 `--yes`（若剛才已 dry-run） |

## 參考

- 詳細步驟：[`handouts/07-static-site-publish.md`](../../../handouts/07-static-site-publish.md)
- IT 規格：[`references/TEACHER-WEB-SERVER-SPEC.md`](../../../references/TEACHER-WEB-SERVER-SPEC.md)
