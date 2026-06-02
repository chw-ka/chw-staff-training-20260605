# Prompt 懶人包 — 三個活動實操指令

> 直接複製貼上到 Agent 視窗（`Cmd/Ctrl + I`）。  
> 記得用 `@` 引用相關檔案，效果更準確。

### 用邊個 Model？

| 活動 | Agent 右上角選 |
|------|----------------|
| 活動一、二 | **deepseek-v4-flash** |
| 活動三 | **gemini-2.5-flash** |

---

## 活動一：錄音變 Minutes（20–40 min）

### 基本版 Prompt

```
你係迦密聖道中學（CHW）嘅行政助理。請讀取 @activity-1-minutes/sample-meeting-transcript.txt，
跟住 @activity-1-minutes/minutes-template.md 嘅格式，用香港廣東話書面語撰寫完整會議紀錄。

要求：
1. 列出所有出席者同缺席者
2. 每個議程項要有：討論摘要、決議、跟進負責人同截止日期
3. 用 Word 友好嘅 Markdown 格式輸出
4. 儲存為 activity-1-minutes/output/meeting-minutes-draft.md
```

### 進階版（引用 SKILL）

```
@.cursor/skills/meeting-minutes/SKILL.md

請按照 SKILL 嘅流程，處理 @activity-1-minutes/sample-meeting-transcript.txt，
輸出會議紀錄並儲存。
```

### 老師可自訂的變體

- 將 `sample-meeting-transcript.txt` 換成你自己嘅逐字稿
- 在 Prompt 加：「我哋科組叫 XXX，校長叫 YYY」

---

## 活動二：【雲端神蹟】Google Drive 整理（40–65 min）

> 並排開 **Cursor** + **drive.google.com**。Model 選 **deepseek-v4-flash**。  
> 課前完成 [`06-google-drive-mcp-setup.md`](06-google-drive-mcp-setup.md)。

### 主推 Prompt

```
我 Google Drive 有個 folder 叫「CHW_Training_垃圾崗」，入面係學生交嘅功課但檔名好亂。

請用 Google Drive MCP：
1. 讀取 @activity-2-gdrive/rename_rules.example.json 嘅規則
2. listFolder 列出「CHW_Training_垃圾崗」入面所有檔案
3. 建立「CHW_Training_已整理/視覺藝術/」folder（若未有）
4. 逐個檔案 renameItem 同 moveItem，改成【功課】_學生名_視覺藝術.副檔名
5. 每步等我 Approve — 我會喺 browser 睇 Google Drive
```

### 廣東話簡化版

```
幫我整理 Google Drive「CHW_Training_垃圾崗」嘅亂碼功課，
跟 @activity-2-gdrive/rename_rules.example.json 改名搬去「CHW_Training_已整理/視覺藝術/」。
用 Google Drive MCP，逐 step 等我 Approve。
```

### 課堂操作

1. 開 Google Drive → 確認 `CHW_Training_垃圾崗` 有 4 個亂碼檔
2. Agent 貼 Prompt → 逐次按 **Approve**
3. 睇 browser：folder 自己出現、檔名自己改、檔案自己移位

### OAuth 測試（設定後先做）

```
用 Google Drive MCP listFolder 列出「CHW_Training_垃圾崗」有咩檔案。
```

---

## 活動三：MARP 直出 PPT（65–85 min）

### 完整 Prompt

```
校長要求我針對今日科組會議嘅決議，準備明日早會簡報。

請：
1. 讀取 @activity-1-minutes/expected-output-sample.md（或你活動一嘅 output）
2. 參考 @activity-3-marp/template-with-footer.md 嘅 MARP 格式同校徽 footer
3. 參考 @activity-3-marp/marp-syntax-reference.md 嘅語法
4. 製作 6–8 頁簡報，包括：封面、會議概要、3 個決議重點、跟進時間表、總結
5. 每頁用 bg left 或 bg right 分欄排版（一邊文字、一邊圖片 placeholder）
6. 如有 Gemini API，為每個決議生成一張教育主題插圖，存入 activity-3-marp/assets/
7. 輸出為 activity-3-marp/output/morning-briefing.md
```

### 只學 MARP 語法（無 API 圖片）

```
請根據 @activity-3-marp/sample-minutes-for-slides.md 嘅內容，
用 @activity-3-marp/template-with-footer.md 嘅 footer 同 CSS，
寫一份 5 頁 MARP 簡報。圖片位置用 placeholder URL 即可。
```

### MARP 語法速記

```markdown
---
marp: true
theme: default
---

# 標題頁
副標題

---

<!-- _class: lead -->
# 第二頁

---

![bg left:40%](assets/school-logo.png)

# 分欄排版

右邊文字，左邊 40% 圖片
```

---

## 通用技巧

| 技巧 | 用法 |
|------|------|
| `@檔案` | 讓 Agent 讀取 project 內特定檔案 |
| 「請用廣東話」 | 控制輸出語言 |
| 「儲存為 xxx.md」 | 指定輸出位置 |
| 「解釋你點做」 | 教學時讓全班睇 Agent 思路 |
| Allow / Run | Agent 改檔或跑 terminal 前會問你批准 — 課堂請按 Allow |

---

## 課後練習建議

1. 用自己科組會議逐字稿跑活動一
2. 改 `rename_rules.example.json` 配合你嘅檔名規則
3. 用 MARP 做下週早會簡報

詳見 `handouts/03-faq-hk-guide.md`。


---

## 活動四：生成 HTML + CSS + JS（延伸活動）

> Model：建議 **deepseek-v4-flash**。
> 生成靜態檔（無需 build），方便之後放 Share Drive 由 webhost 發佈。

### 主推 Prompt

```
請幫我用純 HTML + CSS + Vanilla JS 寫一個教學用小網站，功能係「功課命名器」。

要求：
1. 輸出到 activity-4-web/output/，包含：index.html、styles.css、app.js
2. UI 要現代、清晰、mobile responsive（兩欄 → 手機一欄）
3. 表單欄位：學生姓名、科目、原檔名、前綴（預設【功課】）
4. 按「生成」後顯示建議檔名：{prefix}_{student}_{subject}.{ext}
5. 提供「複製到剪貼簿」按鈕（成功/失敗提示）
6. 所有文字用香港繁中
7. 最後請提供 5 條老師可以改嘅延伸功能點

提示：我哋之後會放呢個 folder 去 share drive，由 webhost 靜態發佈。
```

### 發佈提示

見 `handouts/07-static-site-publish.md`。
