---
name: teaching-web
description: >-
  生成中學教學用互動靜態網頁（Simulation、互動練習、簡單 Game）。
  輸出 HTML/CSS/JS 到 activity-3-web/output/，本機 preview。
  Use when building teaching simulations, interactive quizzes, classroom games,
  or static lesson pages for teacher.chw.edu.hk.
---

# 教學用互動網頁 SKILL

## 適用時機

- 老師要整 **Simulation**（例如 RGB 混色、pH、力分解）
- **互動練習**（選擇題 + 解釋、填空 check）
- **簡單 Game**（配對、限時計分、闖關）
- 輸出到 `activity-3-web/output/`，**純靜態**（唔使 build、唔使 Node）

## 核心原則

1. **一頁一核心互動** — 30 秒內學生明玩咩
2. **即時回饋** — 拖/按/輸入後馬上顯示結果、對錯、分數或解釋
3. **香港繁中書面語** — 術語可跟科目
4. **相對路徑** — `styles.css`、`./assets/x.png`；**禁止** `/styles.css` 開頭（上線會壞）
5. **唔放 API Key** — 靜態網頁係公開檔
6. **老師把關** — 試玩後修正內容同數值

## 標準輸出結構

```
activity-3-web/output/
├── index.html      ← 入口（必須）
├── styles.css
├── app.js
└── assets/         ← 可選
```

## Prompt 四要素（生成前確認）

| 要素 | 例子 |
|------|------|
| 科目 + 課題 | 中二科學 — 酸鹼度 |
| 學生做咩 | 拖 slider、選答案、配對卡片 |
| 回饋 | 對/錯提示、計分、下一題 |
| 技術 | Vanilla JS、responsive、output/ |

## 完成後必做

1. 話老師點 preview：**雙擊 `output/index.html`** 或拖入 Chrome
2. 提醒可 **publish 上線** — 見同資料夾 `publish-web` SKILL 或講 `publish` / `上線`

## 參考

- 講者話術：[`trainer/talking-points-activity3-web.md`](../../../trainer/talking-points-activity3-web.md)
- 上線：[`handouts/07-static-site-publish.md`](../../../handouts/07-static-site-publish.md)
- starter 示範互動邏輯：[`starter/`](../../starter/)
