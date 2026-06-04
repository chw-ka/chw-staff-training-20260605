# 活動二 Prompt — 【雲端神蹟】Google Drive 整理

## 主推 Prompt（課堂投影用）

```
我 Google Drive 有個 folder 叫「CHW_Training_垃圾崗」，裡面是學生交的功課但檔名很亂。

請用 Google Drive MCP：
1. 讀取 @activity-5-gdrive/rename_rules.example.json 的規則
2. listFolder 列出「CHW_Training_垃圾崗」裡面所有檔案
3. 若未有「CHW_Training_已整理」folder，用 createFolder 建立
4. 在「CHW_Training_已整理」裡面建立「視覺藝術」子 folder
5. 逐個檔案：renameItem 改成【功課】_學生名_視覺藝術.副檔名，再用 moveItem 搬去「視覺藝術」folder
6. 每做一步告訴我做了什麼

我會在 browser 開著 Google Drive 看。請逐個 tool call 等我 Approve。
```

## 書面語簡化版

```
幫我整理 Google Drive「CHW_Training_垃圾崗」裡面的亂碼功課。
跟 @activity-5-gdrive/rename_rules.example.json 改名，搬去「CHW_Training_已整理/視覺藝術/」。
用 Google Drive MCP，逐 step 等我 Approve。
```

## 試探性第一步（OAuth 測試）

```
用 Google Drive MCP 的 listFolder 列出我 Drive root 裡面有哪些 folder，
確認看到「CHW_Training_垃圾崗」。
```

## Demo 話術（講者）

> 「大家現在 Cursor 與 Google Drive 並排開。
> 我不寫 code、不裝 Python — 只是跟 Agent 說：『幫我整理垃圾崗』。
> 每次 Agent 想動你的 Drive，都會彈 Approve — 你按完，回去 browser 看，檔案自己動了。
> 這就是 **雲端 MCP 自動化**。」

## 老師 Approve 時要看

| Tool | 做什麼 | 瀏覽器會見到 |
|------|------|--------------|
| `listFolder` | 列出垃圾崗檔案 | — |
| `createFolder` | 建新 folder | 左側出現新 folder |
| `renameItem` | 改名 | 檔名即時變 |
| `moveItem` | 搬去子 folder | 檔案消失於垃圾崗、出現於已整理 |

## 常見 Agent 行為

- 可能先 `search` 找 folder ID — 正常
- 可能一次過 propose 多個 tool — 可以逐個 Approve 看效果
- 若 folder 名打錯 — 改 Prompt 指定正確名稱
