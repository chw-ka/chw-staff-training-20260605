#!/bin/bash
# Google Drive MCP 首次 OAuth — 課前執行一次
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
KEYS="$ROOT/config/gcp-oauth.keys.json"

if [ ! -f "$KEYS" ]; then
  echo "❌ 找不到 $KEYS"
  echo "   請先跟 handouts/06-google-drive-mcp-setup.md 下載 OAuth JSON"
  exit 1
fi

export GOOGLE_DRIVE_OAUTH_CREDENTIALS="$KEYS"
echo "🔐 開始 Google OAuth（瀏覽器會彈出）..."
npx -y @piotr-agier/google-drive-mcp auth
echo "✅ 完成。請 Reload Cursor，確認 MCP → google-drive Connected"
