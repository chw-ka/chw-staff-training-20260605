# API Key 申請指南 — Gemini + DeepSeek（課後可選）

> **課堂無需進行。** 培訓當日 Agent 使用 **Auto**（Demo Login 或 Cursor 訂閱）即可。  
> 本指南供**課後**離開 Demo 帳號、或欲使用自有 Key 以節省用量時參考。  
> 本課程**不使用 OpenAI API**。

---

## 您需要準備什麼？

| 平台 | 用途 | 費用 | 香港申請 |
|------|------|------|----------|
| **Gemini API** | 活動一文字（可選）、課後 MARP 插圖（可選） | 有免費額度 | ✅ 一般可直接申請 |
| **DeepSeek API** | 活動一／二 Agent 主力（文字、撰寫程式） | 按用量計費，費用低 | ✅ 一般可直接申請 |

> 兩個 Key 均申請最為順暢。若時間有限，**請優先申請 DeepSeek**；Google Drive MCP 需額外 OAuth（見 [`06-google-drive-mcp-setup.md`](06-google-drive-mcp-setup.md)）。

---

## Part A：申請 Gemini API Key

### Step 1：前往 Google AI Studio

1. 開啟 https://aistudio.google.com/apikey
2. 以 **Google 帳號**登入（個人或學校 `@school.edu.hk` 均可，視乎校規）

### Step 2：建立 API Key

1. 按 **Create API Key**
2. 選擇 Google Cloud Project（可選 **Create project** 新建，例如 `chw-cursor-training`）
3. 複製產生的 Key（格式：`AIzaSy...`）
4. **請立即貼至安全位置**（Keep、1Password 或稍後填入 Cursor）— Key 之後可能不再完整顯示

### Step 3：確認免費額度

- Gemini 有每日免費 request 限額（足夠培訓與日常試用）
- 詳情：https://ai.google.dev/pricing

### 安全提醒

- ❌ 勿將 Key 貼至 WhatsApp 群組、GitHub、公開文件
- ❌ 勿於「分享螢幕」時展示 Key
- ✅ 若 Key 外洩，請至 AI Studio **刪除並重新建立**

---

## Part B：申請 DeepSeek API Key

### Step 1：前往 DeepSeek 开放平台

1. 開啟 https://platform.deepseek.com
2. 註冊／登入（支援電郵、手機、GitHub）

### Step 2：建立 API Key

1. 進入左側 **API Keys**
2. 按 **Create API Key**
3. 命名（例如 `cursor-chw-training`）
4. 複製 Key（格式：`sk-...`）— **僅顯示一次**

### Step 3：充值（Top-up）

DeepSeek 為**按用量付費**，需預先充值少量金額：

1. 進入 **Top up**／充值頁
2. 充值建議：**¥10–20 人民幣**已足夠數月輕量使用
3. 支援 Alipay／微信支付／部分信用卡（以平台當時選項為準）

> 培訓當日若 balance 為 0，Agent 可能回覆 402／insufficient balance。

### Step 4：記下 Model 名稱

於 Cursor 使用以下 model name（2026 年常用）：

| Model 名稱 | 適合 |
|------------|------|
| `deepseek-v4-flash` | 一般 Agent、撰寫程式、會議紀錄 |
| `deepseek-v4-pro`（或兼容：`deepseek-reasoner`） | 複雜推理（較慢、較貴） |

---

## Part C：安全存放 Key

建議採用以下任一方式：

1. **課堂當日直接貼入 Cursor**（最簡單）
2. 存入 `config/.env`（本專案已 gitignore，不會上傳）：

```bash
cp config/.env.example config/.env
# 以 Cursor 開啟 .env 填入 Key
```

3. 個人密碼管理器（1Password、Bitwarden）

---

## 常見問題

**問：學校 Google 帳號無權限開啟 AI Studio？**  
答：可使用個人 Gmail 申請，或向資訊科技組申請開通；課堂可暫以 DeepSeek 完成全部活動。

**問：DeepSeek 是否需要 VPN？**  
答：香港一般**無需 VPN**，但校園防火牆可能封鎖；建議課前於家中測試一次。

**問：僅申請到 Gemini，是否足夠？**  
答：足以完成三個活動。Google Drive 為課後自學（見 09）。

**問：API Key 與 ChatGPT Plus 有何分別？**  
答：完全不同。本課程使用 **Gemini／DeepSeek 開發者 API**，按用量計費或有免費額度；無需 ChatGPT 訂閱。

**問：課堂可否共用學校 Key？**  
答：可作後備，但**強烈建議每人使用自有 Key**，以便課後繼續練習。共用 Key 有 quota 與私隱風險。

---

## 課後自測 Checklist（可選）

離開 Demo 帳號後，若需自備 Key：

- [ ] 已取得 Gemini API Key（`AIzaSy...`）
- [ ] 已取得 DeepSeek API Key（`sk-...`）
- [ ] DeepSeek 帳戶已充值（若使用 DeepSeek）
- [ ] 已依 [`03-faq-hk-guide.md`](03-faq-hk-guide.md) 填入 Cursor Settings

**課堂必做：**

- [ ] 已依 [`08-appendix-安裝清單.md`](08-appendix-安裝清單.md) 完成 Demo Login；Agent 使用 **Auto**

---

## 下一步

→ 課堂：依 [`08-appendix-安裝清單.md`](08-appendix-安裝清單.md) 開始  
→ 課後填寫 Key：見 [`03-faq-hk-guide.md`](03-faq-hk-guide.md)
