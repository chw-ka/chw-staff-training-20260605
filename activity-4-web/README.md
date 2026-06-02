# 活動四：生成 HTML + CSS + JS（教學用靜態網站）

> 目標：用 Cursor Agent 由 0 生成一個可直接放上 webhost 的靜態網站（無需 build）。

## 教學目標

- 由自然語言需求 → 生成完整前端（HTML/CSS/JS）
- 示範 UI/UX 基本原則（排版、可讀性、互動回饋）
- 為日後「放 Share Drive → webhost 自動發佈」鋪路

## 本活動內容

- `starter/`：已備一個「功課命名器」示範（純靜態）
- `output/`：課堂由 Agent 生成的新版本放這裡（方便比較）

## 最快試用

1. 用瀏覽器打開 `starter/index.html`
2. 你會見到一個互動表單，輸入姓名/科目/原檔名 → 生成建議檔名

## 課堂 Demo 流程（15–25 分鐘）

1. 講者展示 `starter/` 效果（1 分鐘）
2. 叫 Agent 生成一個「老師用小工具」新版本，輸出到 `output/`
3. 要求 Agent：
   - 有 1 個表單 + 1 個結果區 + 1 個複製按鈕
   - 有現代 UI（卡片、grid、responsive）
   - JS 有基本 validation 同提示文字
4. 打開 `output/index.html` 即時預覽

## Hosting（你稍後提供 webhost 後接）

你提到「放係某個 Share Drive 就可以網上 access」——

- **Google Drive 本身唔係靜態網站 hosting**（通常需要第三方 webhost 去讀 Drive folder）
- 所以本活動輸出固定為：**一個 folder 入面幾個靜態檔**（index.html / styles.css / app.js / assets）

到你提供 webhost 後，我可以再：
- 寫一份 `handouts/07-webhost-publish.md`（針對你個 host）
- 幫你加「一鍵 export / publish」嘅流程（例如打包 zip、或生成特定 folder 結構）

