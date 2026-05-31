# 活動二 Prompt — 【雲端神蹟】Google Drive 整理

## 主推 Prompt（課堂投影用）

```
我 Google Drive 有個 folder 叫「CHW_Training_垃圾崗」，入面係學生交嘅功課但檔名好亂。

請用 Google Drive MCP：
1. 讀取 @activity-2-gdrive/rename_rules.example.json 嘅規則
2. listFolder 列出「CHW_Training_垃圾崗」入面所有檔案
3. 若未有「CHW_Training_已整理」folder，用 createFolder 建立
4. 喺「CHW_Training_已整理」入面建立「視覺藝術」子 folder
5. 逐個檔案：renameItem 改成【功課】_學生名_視覺藝術.副檔名，再用 moveItem 搬去「視覺藝術」folder
6. 每做一步話我知做咗咩

我會喺 browser 開住 Google Drive 睇。請逐個 tool call 等我 Approve。
```

## 廣東話 Vibe Coding 簡化版

```
幫我整理 Google Drive「CHW_Training_垃圾崗」入面嘅亂碼功課。
跟 @activity-2-gdrive/rename_rules.example.json 改名，搬去「CHW_Training_已整理/視覺藝術/」。
用 Google Drive MCP，逐 step 等我 Approve。
```

## 試探性第一步（OAuth 測試）

```
用 Google Drive MCP 嘅 listFolder 列出我 Drive root 入面有咩 folder，
確認睇到「CHW_Training_垃圾崗」。
```

## Demo 話術（講者）

> 「大家而家 Cursor 同 Google Drive 並排開。
> 我唔寫 code、唔裝 Python — 淨係同 Agent 講：『幫我整理垃圾崗』。
> 每次 Agent 想郁你個 Drive，都會彈 Approve — 你撳完，返去 browser 睇，檔案自己郁咗。
> 呢個就係 **雲端 MCP 自動化**。」

## 老師 Approve 時要睇

| Tool | 做咩 | 瀏覽器會見到 |
|------|------|--------------|
| `listFolder` | 列出垃圾崗檔案 | — |
| `createFolder` | 建新 folder | 左側出現新 folder |
| `renameItem` | 改名 | 檔名即時變 |
| `moveItem` | 搬去子 folder | 檔案消失於垃圾崗、出現於已整理 |

## 常見 Agent 行為

- 可能先 `search` 搵 folder ID — 正常
- 可能一次過 propose 多個 tool — 可以逐個 Approve 睇效果
- 若 folder 名打錯 — 改 Prompt 指定正確名稱
