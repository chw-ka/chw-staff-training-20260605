# 課後 FAQ — Gemini / DeepSeek 使用指南

---

## 關於 API Key

**Q：課堂用嘅 Key 課後仲用得？**  
A：如果你用**自己申請**嘅 Key，當然可以。請勿將 Key 上傳 GitHub 或分享俾他人。

**Q：我唔記得申請步驟？**  
A：重睇 [`05-api-key-application-guide.md`](05-api-key-application-guide.md)。

**Q：一定要兩個 Key 都有？**  
A：唔一定。**DeepSeek** 可完成活動一、二；**Gemini** 擅長活動三插圖。建議兩個都申請。

---

## Gemini vs DeepSeek 點揀？

| 方案 | 優點 | 缺點 | 適合 |
|------|------|------|------|
| **Gemini API** | 香港易申請、有免費額度、支援圖片生成 | 寫 code 偶爾不如 DeepSeek | 簡報、插圖、一般文字 |
| **DeepSeek API** | 極平、寫 code 強、長文本穩 | 需充值人民幣 | Agent、Minutes、Python |
| **Ollama 本地** | 數據不出校 | 需較強電腦 | 學生私隱資料 |

**本課程建議組合：** DeepSeek 做日常 Agent + Gemini 做多模態。

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
   - **OpenAI API Key** 欄貼 DeepSeek 的 `sk-...`
   - **Override Base URL**：`https://api.deepseek.com`
   - Add model：`deepseek-v4-flash`

> 呢度嘅「OpenAI API Key」欄只係 Cursor 接口名稱，**唔代表用 OpenAI**。

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

**Q：Cursor 同 ChatGPT 有咩分別？**  
A：Cursor 係 IDE，Agent 可讀寫 project 檔案、跑 script。ChatGPT 主要係網頁對話。

**Q：MCP 係咩？**  
A：Model Context Protocol — 俾 AI 標準化連接本機檔案、資料庫等。見 [`04-filesystem-mcp-guide.md`](04-filesystem-mcp-guide.md)。

**Q：DeepSeek 402 / balance 不足？**  
A：去 platform.deepseek.com 充值。

**Q：Gemini quota exceeded？**  
A：等翌日 free tier 重置，或改用 DeepSeek。

**Q：校園 Wi-Fi 連唔到 API？**  
A：試 hotspot；向 IT 查是否封鎖 `api.deepseek.com` / Google API；敏感工作改用 Ollama。

**Q：MARP 點 export PPT？**  
A：裝 Marp for VS Code → Export；或 `npx @marp-team/marp-cli file.md --pptx`

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

## 聯絡

課程問題：[填入講者 email]  
IT 支援：[填入校內 IT]
