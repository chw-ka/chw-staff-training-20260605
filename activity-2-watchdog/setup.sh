#!/bin/bash
# 活動二環境設定 — 課前或課堂執行一次
set -e
cd "$(dirname "$0")"

python3 -m venv .venv
source .venv/bin/activate
pip install -q -r requirements.txt
mkdir -p inbox sorted/視覺藝術

echo "✅ 環境就緒。執行監聽："
echo "   source activity-2-watchdog/.venv/bin/activate"
echo "   python3 activity-2-watchdog/homework_watcher.py"
