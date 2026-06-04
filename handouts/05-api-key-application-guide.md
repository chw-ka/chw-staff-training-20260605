# API Key 申請指南 — Gemini + DeepSeek（課後可選）

> **課堂唔使做。** 培訓當日 Agent 用 **Auto**（Demo Login 或 Cursor 訂閱）即可。  
> 本指南供**課後**離開 Demo 帳號、或想用自己 Key 慳用量時參考。  
> 本課程**不使用 OpenAI API**。

---

## 你需要準備什麼？

| 平台 | 用途 | 費用 | 香港申請 |
|------|------|------|----------|
| **Gemini API** | 活動一/三文字、活動三 AI 插圖（多模態） | 有免費額度 | ✅ 一般可直接申請 |
| **DeepSeek API** | 活動一/二 Agent 主力（文字、寫 code） | 按用量計，極平 | ✅ 一般可直接申請 |

> 兩個 Key 都申請到最順暢。若時間有限，**DeepSeek 優先**；Google Drive MCP 需額外 OAuth（見 [`06-google-drive-mcp-setup.md`](06-google-drive-mcp-setup.md)）。

---

## Part A：申請 Gemini API Key

### Step 1：前往 Google AI Studio

1. 開啟 https://aistudio.google.com/apikey
2. 用 **Google 帳號**登入（個人或學校 `@school.edu.hk` 均可，視乎校規）

### Step 2：建立 API Key

1. 按 **Create API Key**
2. 選擇 Google Cloud Project（可選 **Create project** 新建一個，例如 `chw-cursor-training`）
3. 複製產生的 Key（格式：`AIzaSy...`）
4. **立即貼至安全位置**（Keep、1Password、或等下填入 Cursor）— Key 之後可能不再完整顯示

### Step 3：確認免費額度

- Gemini 有每日免費 request 限額（足夠培訓與日常試用）
- 詳情：https://ai.google.dev/pricing

### 安全提醒

- ❌ 勿將 Key 貼至 WhatsApp 群組、GitHub、公開 document
- ❌ 勿用「分享螢幕」展示 Key
- ✅ 若 Key 外洩，去 AI Studio **刪除並重新建立**

---

## Part B：申請 DeepSeek API Key

### Step 1：前往 DeepSeek 开放平台

1. 開啟 https://platform.deepseek.com
2. 註冊 / 登入（支援電郵、手機、GitHub）

### Step 2：建立 API Key

1. 進入左側 **API Keys**
2. 按 **Create API Key**
3. 命名（例如 `cursor-chw-training`）
4. 複製 Key（格式：`sk-...`）— **只顯示一次**

### Step 3：充值（Top-up）

DeepSeek 是**按用量付費**，需預先充值少量金額：

1. 進入 **Top up** / 充值頁
2. 充值建議：**¥10–20 人民幣**已足夠數個月輕量使用
3. 支援 Alipay / 微信支付 / 部分信用卡（以平台當時選項為準）

> 培訓當日若 balance 為 0，Agent 會回覆 402 / insufficient balance。

### Step 4：記下 Model 名稱

在 Cursor 要用以下 model name（2026 年常用）：

| Model 名稱 | 適合 |
|------------|------|
| `deepseek-v4-flash` | 一般 Agent、寫 code、minutes |
| `deepseek-v4-pro`（或兼容：`deepseek-reasoner`） | 複雜推理（較慢、較貴） |

---

## Part C：安全存放 Key

建議用以下任一方式：

1. **課堂當日直接貼入 Cursor**（最簡單）
2. 存入 `config/.env`（本 project 已 gitignore，不會上傳）：

```bash
cp config/.env.example config/.env
# 用 Cursor 開啟 .env 填入 Key
```

3. 個人密碼管理器（1Password、Bitwarden）

---

## 常見問題

**Q：學校 Google 帳號無權限開 AI Studio？**  
A：用個人 Gmail 申請，或向 IT 申請開通；課堂可暫用 DeepSeek 做全部活動。

**Q：DeepSeek 要 VPN 嗎？**  
A：香港一般**不必 VPN**，但校園防火牆可能封鎖；課前在家測試一次。

**Q：我只申請到 Gemini，夠不夠？**  
A：夠完成三個活動。Google Drive 為課後自學（見 09）。

**Q：API Key 與 ChatGPT Plus 有什麼分別？**  
A：完全不同。本課程用 **Gemini / DeepSeek 開發者 API**，按用量計費或有免費額度；不需要 ChatGPT 訂閱。

**Q：課堂可不可以共用學校 Key？**  
A：可以作後備，但**強烈建議每人用自己 Key**，課後繼續練習。共用 Key 有 quota 與私隱風險。

---

## 課後自測 Checklist（可選）

離開 Demo 帳號後，如需自備 Key：

- [ ] 已取得 Gemini API Key（`AIzaSy...`）
- [ ] 已取得 DeepSeek API Key（`sk-...`）
- [ ] DeepSeek 帳戶已充值（如用 DeepSeek）
- [ ] 已跟 [`03-faq-hk-guide.md`](03-faq-hk-guide.md) 填入 Cursor Settings

**課堂必做：**

- [ ] 已跟 [`08-appendix-安裝清單.md`](08-appendix-安裝清單.md) 完成 Demo Login；Agent 用 **Auto**

---

## 下一步

→ 課堂：跟 [`08-appendix-安裝清單.md`](08-appendix-安裝清單.md) 開始  
→ 課後填 Key：見 [`03-faq-hk-guide.md`](03-faq-hk-guide.md)
