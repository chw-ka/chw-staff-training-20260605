# 課後 FAQ — Gemini／DeepSeek 使用指南（課後可選）

> **課堂無需進行以下設定。** Agent 使用 **Auto** 即可。  
> 本 FAQ 供離開 Demo 帳號後、自備 API Key 時參考。

---

## 關於 API Key

**問：課堂使用的 Key 課後是否仍可使用？**  
答：若為**您自行申請**的 Key，當然可以。請勿將 Key 上傳至 GitHub 或分享予他人。

**問：不記得申請步驟？**  
答：請重閱 [`05-api-key-application-guide.md`](05-api-key-application-guide.md)。

**問：是否必須同時擁有兩個 Key？**  
答：不一定。**DeepSeek** 可完成活動一、二、三（靜態網站）；**Gemini** 可選用於課後 MARP 插圖。課堂 Agent 使用 **Auto** 即可。

---

## Gemini 與 DeepSeek 如何選擇？

| 方案 | 優點 | 缺點 | 適合 |
|------|------|------|------|
| **Gemini API** | 香港易申請、有免費額度、支援圖片生成 | 撰寫程式偶爾不如 DeepSeek | 簡報、插圖、一般文字 |
| **DeepSeek API** | 費用低、撰寫程式能力強、長文本穩定 | 需充值人民幣 | Agent、會議紀錄、Python |
| **Ollama 本地** | 資料不出校園 | 需較強電腦配置 | 學生私隱資料 |

**本課程建議組合：** DeepSeek 作日常 Agent；Gemini 作多模態用途。

---

## Gemini 設定速查

1. https://aistudio.google.com/apikey → Create API Key
2. Cursor Settings → Models → **Google API Key**
3. Add model：`gemini-2.5-flash`

---

## DeepSeek 設定速查

1. https://platform.deepseek.com → API Keys → Create
2. 充值少量 balance
3. Cursor Settings → Models：
   - **OpenAI API Key** 欄貼上 DeepSeek 的 `sk-...`
   - **Override Base URL**：`https://api.deepseek.com`
   - Add model：`deepseek-v4-flash`

> 此處「OpenAI API Key」欄僅為 Cursor 介面名稱，**不代表使用 OpenAI 服務**。

---

## 方案 C：Ollama 本地部署（私隱優先）

適合處理**學生個人資料、成績、評語**。

```bash
brew install ollama
ollama pull deepseek-r1:8b
ollama serve
```

Cursor Settings → Override Base URL：`http://localhost:11434/v1`  
API Key 填：`ollama`（任意字串）  
Add model：`deepseek-r1:8b`

---

## 常見問題

**問：Cursor 與 ChatGPT 有何分別？**  
答：Cursor 為整合開發環境（IDE），Agent 可讀寫專案檔案、執行 script。ChatGPT 主要為網頁對話。

**問：MCP、SKILL、Workflow、.md 是什麼？**  
答：見 [`00-core-concepts-glossary.md`](00-core-concepts-glossary.md)。MCP 試用見 [`04-filesystem-mcp-guide.md`](04-filesystem-mcp-guide.md)。

**問：MCP 是什麼？（一句）**  
答：連線服務的共通標準；課堂活動二無需啟用 MCP 即可完成本機整理。

**問：DeepSeek 402／balance 不足？**  
答：請至 platform.deepseek.com 充值。

**問：Gemini quota exceeded？**  
答：等候翌日 free tier 重置，或改用 DeepSeek。

**問：校園 Wi-Fi 無法連接 API？**  
答：可嘗試 hotspot；向資訊科技組查詢是否封鎖 `api.deepseek.com`／Google API；敏感工作請改用 Ollama。

**問：MARP 如何匯出 PPT？（課後延伸）**  
答：見 `activity-4-marp/` — 安裝 Marp for VS Code → Export；或 `npx @marp-team/marp-cli file.md --pptx`

---

## 延伸資源

| 資源 | 連結 |
|------|------|
| Gemini AI Studio | https://aistudio.google.com |
| DeepSeek Platform | https://platform.deepseek.com |
| Cursor 文檔 | https://docs.cursor.com |
| MARP | https://marp.app |
| Ollama | https://ollama.com |

---

## 即場／常見錯誤

課堂若遇阻（Allow 未彈出、Whisper 較慢、MCP 顯示紅色等）→ 講者將依 [`trainer/troubleshooting.md`](../trainer/troubleshooting.md) 處理；學員可先查閱本 FAQ 上表。

---

## 聯絡

課程問題：[填入講者 email]  
資訊科技支援：[填入校內 IT]
