# 活動二 Prompt 範例（講者投影用）

## 主推 Prompt

```
我個 Downloads 資料夾成日收到學生交的功課，但檔名很亂（例如 IMG_8742.jpg）。
請幫我寫一個 Python 腳本，用 watchdog 監聽 activity-2-watchdog/inbox/ 資料夾：

1. 一有新檔案進來，等 2 秒確保下載完成
2. 根據 @activity-2-watchdog/rename_rules.example.json 的規則重新命名
3. 將檔案搬去 activity-2-watchdog/sorted/ 對應科目子資料夾
4. 在 terminal 顯示「已處理：舊名 → 新名」
5. 幫我執行 pip install watchdog，然後 run 個腳本
```

## 備用 Prompt（時間不足）

```
請解釋 @activity-2-watchdog/homework_watcher.py 如何運作，然後幫我在 terminal 執行它。
```

## Demo 話術

> 「大家看，我現在不寫一行 code。我跟 Agent 說：『幫我監聽那個 folder，有新檔就改名』。
> Agent 會自己寫 script、裝 library、跑 terminal — 這就是 MCP 的威力：AI 不再只是聊天，它可以動你的電腦。」

## 測試動作

```bash
# Terminal 1：跑 watcher
cd activity-2-watchdog && python3 homework_watcher.py

# Terminal 2 或 Finder：複製測試檔
cp downloads/IMG_8742.jpg inbox/
```
