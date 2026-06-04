## 活動二 Demo（00:40–01:05）— 【雲端神蹟】

**[並排：Cursor + Chrome drive.google.com]**

**話術：**
> 「第二個痛點：Google Drive 垃圾崗。今日不寫 Python — 用 MCP 直接操作雲端。
> 大家 Drive 開著 `CHW_Training_垃圾崗`，Cursor 貼 Prompt，每次 Approve 就回去 browser 看。」

**動作：**
1. 展示垃圾崗 4 個亂碼檔（10 秒）
2. 貼 `activity-2-gdrive/sample-prompts.md` 主推 Prompt
3. **慢動作** Approve：`listFolder` → `createFolder` → `renameItem` → `moveItem`
4. 開 `CHW_Training_已整理/視覺藝術/` 展示成果

**話術（第一個 move 後）：**
> 「有沒有看到？你沒有動過 browser，檔案自己移了。這就是雲端自動化。」

**全班練習：** 跟著 Approve 完整整理（約 8 min）

**備用（OAuth 全掛）：**
```bash
cd activity-2-watchdog && bash setup.sh && source .venv/bin/activate && python3 homework_watcher.py
```
