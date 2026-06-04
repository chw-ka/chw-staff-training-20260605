#!/usr/bin/env python3
"""
活動一示範：錄音 → 文字（Whisper）

課堂示範用 short clip；課後可改路徑轉 1 小時錄音（需時約 1–2 小時，建議本機慢慢跑）。

用法：
  pip install -r requirements.txt
  python transcribe.py
  python transcribe.py path/to/your.m4a path/to/output.txt
"""

from __future__ import annotations

import sys
from pathlib import Path

DEFAULT_AUDIO = Path(__file__).resolve().parent.parent / "samples" / "demo-short-clip.m4a"
DEFAULT_OUTPUT = Path(__file__).resolve().parent.parent / "output" / "transcript-from-audio.txt"

# large-v3 = 最準確；課後 1 小時錄音用此 model。課堂 demo 約 45 秒可接受。
MODEL_SIZE = "large-v3"


def transcribe(audio_path: Path, output_path: Path) -> None:
    try:
        from faster_whisper import WhisperModel
    except ImportError as e:
        raise SystemExit(
            "請先安裝：pip install -r scripts/requirements.txt"
        ) from e

    if not audio_path.exists():
        raise SystemExit(f"找不到錄音：{audio_path}")

    print(f"載入 Whisper {MODEL_SIZE}（首次會下載 model，需數分鐘）…")
    model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")

    print(f"轉寫：{audio_path.name} …")
    segments, info = model.transcribe(
        str(audio_path),
        language="zh",
        beam_size=5,
        vad_filter=True,
    )

    lines = [
        f"【語音轉文字】來源：{audio_path.name}",
        f"Model：Whisper {MODEL_SIZE}",
        f"偵測語言：{info.language}（信心 {info.language_probability:.0%}）",
        "",
    ]
    for seg in segments:
        lines.append(seg.text.strip())

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"完成 → {output_path}")


def main() -> None:
    audio = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_AUDIO
    output = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT
    transcribe(audio, output)


if __name__ == "__main__":
    main()
