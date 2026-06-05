#!/usr/bin/env python3
"""Copy activity-3-web/output/ to teacher NAS _web folder for teacher.chw.edu.hk."""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEB_ROOT = ROOT / "activity-3-web"
CONFIG_NAME = "publish.config.json"
EXAMPLE_CONFIG = WEB_ROOT / "publish.config.example.json"


def load_config() -> dict:
    path = WEB_ROOT / CONFIG_NAME
    if not path.exists():
        print(
            f"Missing {path}\n"
            f"  Copy: {EXAMPLE_CONFIG.name} → {CONFIG_NAME}\n"
            f"  Fill in teacher_code (and publish_target_override if you use P:\\ drive).",
            file=sys.stderr,
        )
        sys.exit(1)
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def resolve_paths(cfg: dict) -> tuple[Path, Path, str]:
    override = (cfg.get("publish_target_override") or "").strip()
    teacher = (cfg.get("teacher_code") or "").strip()
    if not teacher and not override:
        print("Set teacher_code or publish_target_override in publish.config.json", file=sys.stderr)
        sys.exit(1)

    source = WEB_ROOT / (cfg.get("source_dir") or "output")
    if override:
        dest = Path(override)
    else:
        nas = cfg.get("nas_root") or r"\\10.10.0.13\staff"
        web_folder = cfg.get("web_folder") or "_web"
        dest = Path(nas) / teacher / web_folder

    code = teacher or dest.parent.name
    public_url = f"https://teacher.chw.edu.hk/{code}/"
    return source, dest, public_url


def validate_source(source: Path) -> None:
    index = source / "index.html"
    if not source.is_dir():
        print(f"Source folder not found: {source}", file=sys.stderr)
        sys.exit(1)
    if not index.is_file():
        print(f"Missing {index} — generate or preview locally first.", file=sys.stderr)
        sys.exit(1)


def iter_files(source: Path) -> list[Path]:
    return [p for p in source.iterdir() if not p.name.startswith(".")]


def publish(source: Path, dest: Path, *, dry_run: bool) -> int:
    validate_source(source)
    files = iter_files(source)
    if not files:
        print(f"No files to publish in {source}", file=sys.stderr)
        return 1

    if dry_run:
        print(f"[dry-run] Would copy {len(files)} item(s) from:\n  {source}\nto:\n  {dest}\n")
        for p in sorted(files):
            print(f"  → {p.name}")
        return 0

    dest.mkdir(parents=True, exist_ok=True)
    copied = 0
    for item in files:
        target = dest / item.name
        if item.is_dir():
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)
        copied += 1
        print(f"  copied: {item.name}")

    print(f"\nPublished {copied} item(s) to {dest}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish activity-3-web output to NAS _web")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be copied")
    parser.add_argument("--yes", action="store_true", help="Copy without dry-run (use after preview)")
    args = parser.parse_args()

    cfg = load_config()
    source, dest, public_url = resolve_paths(cfg)
    dry_run = not args.yes

    rc = publish(source, dest, dry_run=dry_run)
    if rc == 0:
        print(f"\nPublic URL: {public_url}")
        if dry_run:
            print("Run again with --yes to publish.")
    return rc


if __name__ == "__main__":
    sys.exit(main())
