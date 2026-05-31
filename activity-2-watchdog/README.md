# ⚠️ 備用方案 — 本地 Watchdog（已取代）

> **主活動**已改為 [`../activity-2-gdrive/`](../activity-2-gdrive/) — Google Drive MCP【雲端神蹟】。  
> 本 folder 只作 **OAuth 失敗 / 校園封鎖** 時的講者備用 demo。

## 何時用

- Google Drive MCP 全場連唔到
- 來不及完成 OAuth 設定

## 快速啟動

```bash
cd activity-2-watchdog
bash setup.sh && source .venv/bin/activate
python3 homework_watcher.py
# 複製 downloads/ 檔案到 inbox/
```

詳見原 README 內容。
