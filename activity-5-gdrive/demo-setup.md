# 講者 Demo 設定 — Google Drive 垃圾崗

## 課前（講者 + 學員）

### 1. 建立測試 folder

在 [Google Drive](https://drive.google.com)：

1. 新建 folder：**CHW_Training_垃圾崗**
2. 上傳 `samples/` 內 4 個檔案（或任意亂碼檔名對照 `rename_rules.example.json`）

### 2. 確認 MCP 已連

```bash
# 首次 OAuth（每位老師課前做一次）
npx -y @piotr-agier/google-drive-mcp auth
```

Cursor → Settings → MCP → `google-drive` 綠色 Connected

### 3. 課堂座位

- 左：Cursor Agent
- 右：Chrome → drive.google.com → 開著 `CHW_Training_垃圾崗`

## 講者 wow 演示順序

1. 展示垃圾崗 4 個亂碼檔
2. 貼主推 Prompt
3. **慢動作** Approve 第一個 `listFolder` — 解釋 Agent 正在看雲端
4. Approve `createFolder` — 叫老師看 Drive 左欄
5. Approve `renameItem` + `moveItem` — 「隱形人出現了！」
6. 開 `CHW_Training_已整理/視覺藝術/` 展示成果

## 時間不夠

只 demo 整理 **一個** 檔（IMG_8742.jpg），其餘叫老師自己試。

## 全場 OAuth 失敗

切換備用：演示 [`activity-2-files/`](../activity-2-files/) 本機整理（見 trainer/troubleshooting.md）
