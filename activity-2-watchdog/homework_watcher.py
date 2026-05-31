#!/usr/bin/env python3
"""
Homework folder watcher — 監聽 inbox/，按 rename_rules.example.json 自動改名及分類。
培訓示範用。執行：python3 homework_watcher.py
"""

import json
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

BASE_DIR = Path(__file__).parent
INBOX = BASE_DIR / "inbox"
SORTED = BASE_DIR / "sorted"
RULES_FILE = BASE_DIR / "rename_rules.example.json"


def load_rules() -> dict:
    with open(RULES_FILE, encoding="utf-8") as f:
        return json.load(f)


def build_name(rules: dict, source: str, ext: str) -> tuple[str, str]:
    """Return (new_filename, subject_folder)."""
    prefix = rules.get("prefix", "【功課】")
    pattern = rules.get("naming_pattern", "{prefix}_{student_name}_{subject}{extension}")

    for item in rules.get("mappings", []):
        if item["source"] == source:
            new_name = pattern.format(
                prefix=prefix,
                student_name=item["student_name"],
                subject=item["subject"],
                extension=ext,
            )
            return new_name, item["subject"]

    default = rules.get("default_subject", "未分類")
    new_name = f"{prefix}_未知_{default}{ext}"
    return new_name, default


class HomeworkHandler(FileSystemEventHandler):
    def __init__(self, rules: dict):
        self.rules = rules
        self._processing: set[str] = set()

    def on_created(self, event):
        if event.is_directory:
            return
        self._handle(event.src_path)

    def on_moved(self, event):
        if event.is_directory:
            return
        self._handle(event.dest_path)

    def _handle(self, src_path: str):
        path = Path(src_path)
        if path.name.startswith(".") or str(path) in self._processing:
            return

        self._processing.add(str(path))
        time.sleep(2)  # 等待下載完成

        if not path.exists():
            self._processing.discard(str(path))
            return

        new_name, subject = build_name(self.rules, path.name, path.suffix)
        dest_dir = SORTED / subject
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / new_name

        counter = 1
        while dest.exists():
            dest = dest_dir / f"{path.stem}_{counter}{path.suffix}"
            counter += 1

        path.rename(dest)
        print(f"✅ 已處理：{path.name} → {dest.relative_to(BASE_DIR)}")
        self._processing.discard(str(path))


def main():
    rules = load_rules()
    INBOX.mkdir(exist_ok=True)
    SORTED.mkdir(exist_ok=True)

    handler = HomeworkHandler(rules)
    observer = Observer()
    observer.schedule(handler, str(INBOX), recursive=False)
    observer.start()

    print(f"👀 監聽中：{INBOX}")
    print("   將 downloads/ 內的檔案複製到 inbox/ 測試。按 Ctrl+C 停止。")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n⏹ 已停止監聽。")

    observer.join()


if __name__ == "__main__":
    main()
