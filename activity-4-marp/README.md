# 活動四（課後延伸）：Marp 簡報

> **唔喺 90 分鐘課堂內。** 若需要 Markdown → 簡報，課後自學。  
> 主線活動三已改為 **[`activity-3-web/`](../activity-3-web/)** 靜態網站。

## 檔案

| 檔案 | 說明 |
|------|------|
| [`template-tech-with-footer.md`](template-tech-with-footer.md) | tech 主題模板 |
| [`output/morning-briefing.md`](output/morning-briefing.md) | 視藝科早會簡報示例 |
| [`marp-syntax-reference.md`](marp-syntax-reference.md) | 語法速查 |

## 匯出 PPTX

```powershell
cd activity-4-marp
npx @marp-team/marp-cli output/morning-briefing.md --pptx --no-stdin --allow-local-files
```

Cursor Skill：`.cursor/skills/marp-slide/`
