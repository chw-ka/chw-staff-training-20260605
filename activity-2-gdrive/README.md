# 活動二：【雲端神蹟】Google Drive 全自動整理

> 取代本地 Watchdog。老師在 Cursor 按 **Approve**，打開 Google Drive 睇檔案自己改名、開 folder、移位。

## 教學目標

- 理解 **MCP** 可以連接**雲端**服務（唔止本機 folder）
- 體驗「雲端自動化」：Agent 透過 Google Drive MCP 直接操作你的 Drive
- **Wow moment**：瀏覽器入面好似有隱形人幫手整理垃圾崗

## 技術 stack

| 組件 | 用途 |
|------|------|
| `@piotr-agier/google-drive-mcp` | Google Drive MCP server |
| Cursor Agent | 下達廣東話指令、Approve tool calls |
| Google OAuth | 授權 Agent 讀寫**你指定**嘅 Drive |

## 課前準備（每位老師）

1. 跟 [`handouts/06-google-drive-mcp-setup.md`](../handouts/06-google-drive-mcp-setup.md) 完成 OAuth + MCP 設定
2. 喺 Google Drive 建立 demo folder **「CHW_Training_垃圾崗」**
3. 將 `samples/` 入面 4 個亂碼檔**上傳**到該 folder
4. Cursor Settings → MCP → 確認 `google-drive` 為 **Connected**

## Demo folder 結構（課前建立）

```
My Drive/
└── CHW_Training_垃圾崗/          ← 亂碼功課（inbox）
    ├── IMG_8742.jpg
    ├── DSC_00341.jpg
    ├── homework_final_v3.pdf
    └── photo_20260528.png

（Agent 執行後會自動建立）
└── CHW_Training_已整理/
    └── 視覺藝術/
        ├── 【功課】_張小明_視覺藝術.jpg
        └── ...
```

## 課堂流程（25 min）

1. **（5 min）** 講解 MCP「隨意門」→ 今次連 Google Drive
2. **（2 min）** 老師並排開 Cursor + Google Drive 網頁（drive.google.com）
3. **（3 min）** 投影 `sample-prompts.md` 主推 Prompt
4. **（10 min）** 全班貼 Prompt → 逐次 **Approve** MCP tool calls → 睇 Drive 變化
5. **（5 min）** 討論：同本地執 file 有咩分別？校內 Shared Drive 點用？

## 安全提醒

- OAuth 只授權**你個人** Google 帳號
- 建議只用 **CHW_Training_*** 測試 folder，唔好叫 Agent 整理成個 My Drive
- 所有 move/rename 都會喺 Approve 前顯示 — 看清楚再按

## 備用方案

若 OAuth / MCP 連唔到：改用 [`../activity-2-watchdog/`](../activity-2-watchdog/) 本地 Watchdog demo（講者預跑 `setup.sh`）。
