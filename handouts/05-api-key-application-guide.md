# API Key 申請指南 — Gemini + DeepSeek

> **課前必做**（建議培訓前 3–7 天完成）  
> 本課程**不使用 OpenAI API**。我哋只用 **Google Gemini** 同 **DeepSeek** 兩個平台。

---

## 你需要準備咩？

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
2. 選擇 Google Cloud Project（可揀 **Create project** 新建一個，例如 `chw-cursor-training`）
3. 複製產生嘅 Key（格式：`AIzaSy...`）
4. **立即貼去安全位置**（Keep、1Password、或等下填入 Cursor）— Key 之後可能唔再完整顯示

### Step 3：確認免費額度

- Gemini 有每日免費 request 限額（足夠培訓同日常試用）
- 詳情：https://ai.google.dev/pricing

### 安全提醒

- ❌ 勿將 Key 貼去 WhatsApp 群組、GitHub、公開 document
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

DeepSeek 係**按用量付費**，需預先充值少量金額：

1. 進入 **Top up** / 充值頁
2. 充值建議：**¥10–20 人民幣**已足夠數個月輕量使用
3. 支援 Alipay / 微信支付 / 部分信用卡（以平台當時選項為準）

> 培訓當日若 balance 為 0，Agent 會回覆 402 / insufficient balance。

### Step 4：記低 Model 名稱

在 Cursor 要用以下 model name（2026 年常用）：

| Model 名稱 | 適合 |
|------------|------|
| `deepseek-chat` | 一般 Agent、寫 code、minutes |
| `deepseek-reasoner` | 複雜推理（較慢、較貴） |

---

## Part C：安全存放 Key

建議用以下任一方式：

1. **課堂當日直接貼入 Cursor**（最簡單）
2. 存入 `config/.env`（本 project 已 gitignore，唔会上傳）：

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
A：香港一般**唔使 VPN**，但校園防火牆可能封鎖；課前在家測試一次。

**Q：我淨係申請到 Gemini，夠唔夠？**  
A：夠完成三個活動。活動二若 Drive MCP 未設定，講者會用備用方案或協助 OAuth。

**Q：API Key 同 ChatGPT Plus 有咩分別？**  
A：完全唔同。本課程用 **Gemini / DeepSeek 開發者 API**，按用量計費或有免費額度；唔需要 ChatGPT 訂閱。

**Q：課堂可唔可以共用學校 Key？**  
A：可以作後備，但**強烈建議每人用自己 Key**，課後繼續練習。共用 Key 有 quota 同私隱風險。

---

## 課前自測 Checklist

完成申請後，打勾：

- [ ] 已取得 Gemini API Key（`AIzaSy...`）
- [ ] 已取得 DeepSeek API Key（`sk-...`）
- [ ] DeepSeek 帳戶已充值
- [ ] 已跟 [`06-google-drive-mcp-setup.md`](06-google-drive-mcp-setup.md) 完成 OAuth + 上傳 samples 到 `CHW_Training_垃圾崗`
- [ ] 已安裝 Cursor：https://cursor.com
- [ ] 已下載培訓 project
- [ ] 跟 [`01-cursor-setup-guide.md`](01-cursor-setup-guide.md) 完成設定
- [ ] Agent 測試句收到廣東話回覆

---

## 下一步

→ 跟 [`01-cursor-setup-guide.md`](01-cursor-setup-guide.md) 將 Key 填入 Cursor
