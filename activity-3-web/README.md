# 活動三：生成 HTML + CSS + JS（教學用靜態網站）

> 目標：用 Cursor Agent 由 0 生成一個可直接放上 webhost 的靜態網站（無需 build）。

## 教學目標

- 由自然語言需求 → 生成完整前端（HTML/CSS/JS）
- 示範 UI/UX 基本原則（排版、可讀性、互動回饋）
- **Wow 點：** 瀏覽器打開 `output/index.html` 即時預覽；課後可複製到 NAS 上線

## 本活動內容

- `starter/`：已備一個「功課命名器」示範（純靜態）
- `output/`：課堂由 Agent 生成的新版本放這裡（方便比較）

## 最快試用

1. 用瀏覽器打開 `starter/index.html`
2. 你會見到一個互動表單，輸入姓名/科目/原檔名 → 生成建議檔名

## 課堂 Demo 流程（60–85 min，約 20–25 min 實操）

1. 講者展示 `starter/` 效果（1 分鐘）
2. 叫 Agent 生成一個「老師用小工具」新版本，輸出到 `output/`
3. 要求 Agent：
   - 有 1 個表單 + 1 個結果區 + 1 個複製按鈕
   - 有現代 UI（卡片、grid、responsive）
   - JS 有基本 validation 與提示文字
4. 打開 `output/index.html` 即時預覽
5. （可選，1 分鐘）口述：`teacher.chw.edu.hk` 上線見 [`handouts/07-static-site-publish.md`](../handouts/07-static-site-publish.md)

## Hosting（teacher.chw.edu.hk）

學校教師網站 **teacher.chw.edu.hk** 會讀取 NAS 上各老師 `_web` folder 的靜態檔：

- NAS：`\\10.10.0.13\staff\{代碼}\_web\`
- 公開網址：`https://teacher.chw.edu.hk/{代碼}/`

**課堂以本機 preview 為主**；完整發佈步驟見 [`handouts/07-static-site-publish.md`](../handouts/07-static-site-publish.md)。

## 一句上線（課後）

1. 複製 `publish.config.example.json` → `publish.config.json`，填入你的 **教師代碼**（或 NAS 已 map 路徑）
2. 在 Agent 講：**「publish」** 或 **「上線」** — Agent 會跟 [`publish-web` SKILL](.cursor/skills/publish-web/SKILL.md) 執行
3. 或手動：
   ```powershell
   python scripts/publish_web.py --dry-run   # 先預覽會 copy 咩
   python scripts/publish_web.py --yes       # 確認後才 copy 去 _web
   ```

公開網址：`https://teacher.chw.edu.hk/{你的代碼}/`

## Cursor SKILL / RULE

| 檔案 | 用途 |
|------|------|
| `.cursor/skills/teaching-web/` | 生成 Simulation / Game / 互動練習 |
| `.cursor/skills/publish-web/` | 一句 **publish** → 複製去 NAS `_web` |
| `.cursor/rules/teaching-web.mdc` | 在 `output/` 工作時自動提醒規則 |
