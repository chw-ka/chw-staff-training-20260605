#!/usr/bin/env python3
"""Generate trainer infographics (Gemini or SiliconFlow), 16:9, optional no-text mode."""
from __future__ import annotations

import argparse
import base64
import json
import struct
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
OUT_DIR = ROOT / "trainer" / "infographics"

GEMINI_MODEL = "gemini-2.5-flash-image"
SILICONFLOW_BASE = "https://api.siliconflow.cn/v1"
SILICONFLOW_MODEL = "Qwen/Qwen-Image"
SILICONFLOW_SIZE = "1920x1080"
GEMINI_ASPECT = "16:9"

ASPECT_BLOCK = (
    "MANDATORY CANVAS: landscape 16:9 widescreen presentation slide, exact aspect "
    "ratio 16:9, resolution 1920x1080 pixels, horizontal layout only, NOT square, "
    "NOT 4:3, NOT portrait."
)

STYLE_LOCK = (
    "Style lock: flat vector infographic, white background, navy #1e3a5f primary, "
    "orange #f5a623 accent, generous whitespace, MANDATORY 16:9 landscape 1920x1080 "
    "widescreen slide, 4K quality, CHW school staff training. Minimal English labels "
    "only; avoid long Traditional Chinese inside the image."
)

STYLE_TECH = (
    "Style lock: dark GitHub-style tech palette background #0d1117, headings #58a6ff, "
    "accent #7ee787, MANDATORY 16:9 landscape 1920x1080 widescreen, flat vector "
    "infographic for school training."
)

NO_TEXT_BLOCK = (
    "NO TEXT VERSION: Do not render any letters, words, or Chinese characters inside "
    "the image. Use icons, arrows, numbered circles, and empty rounded rectangles as "
    "text placeholders only. I will add Traditional Chinese in PowerPoint. "
    "MANDATORY 16:9 landscape 1920x1080 widescreen."
)

# Content prompts — aspect ratio enforced via ASPECT_BLOCK in script, not only here.
FIGURES: list[tuple[str, str, str, str | None]] = [
    (
        "fig-01-cursor-interface.png",
        "圖1 Cursor 介面三區",
        """Create a clean educational infographic, flat modern style, soft navy blue and warm orange accent, white background.

Show a simplified desktop app window labeled "Cursor" with THREE clearly separated vertical panels:

LEFT panel (25% width): file explorer tree icon, folder names.

CENTER panel (50% width): document preview like Word, meeting minutes text.

RIGHT panel (25% width): chat/agent panel with message bubbles, highlighted with a glowing border.

At the bottom, four small badge icons for keyboard shortcuts.

Inside the Agent panel, annotate three spots with arrows (model dropdown, prompt input, approve button).

Friendly tone for school teachers, not scary developer aesthetic. No real code.""",
        None,
    ),
    (
        "fig-02-why-cursor-hk.png",
        "圖2 點解學 Cursor",
        """Educational comparison infographic, minimalist flowchart style, school training workshop look.

Three-column flow left to right:

Column 1 — past best chat app icon.

Column 2 — Hong Kong map silhouette with gentle barrier icon.

Column 3 — generic IDE window icon for Cursor-style tool.

Bottom banner area for key message.

Clean icons, flat design, navy/teal/white palette, suitable for projector.""",
        None,
    ),
    (
        "fig-03-five-concepts.png",
        "圖3 五個核心概念",
        """Infographic poster, five equal cards in a row, modern flat illustration for non-technical school staff.

Card 1 — Workflow: arrow flow input to output.

Card 2 — MCP: magical door portal to folder and cloud.

Card 3 — Skills: reusable recipe card icon.

Card 4 — Rules: checklist document.

Card 5 — Model: dropdown and key icon.

Soft colors, professional, white background, subtle shadows.""",
        None,
    ),
    (
        "fig-04-boss-vs-intern.png",
        "圖4 老闘 vs 實習文員",
        """Friendly workplace metaphor illustration, warm cartoon-flat style (not childish), for adult teachers.

A confident teacher at desk pointing right; helpful assistant agent at computer; center screen shows formatted meeting minutes (not code).

School admin office setting. Avoid scary tech imagery.""",
        None,
    ),
    (
        "fig-05-90min-timeline.png",
        "圖5 90分鐘時間軸",
        """Horizontal timeline infographic, six milestones on one line, clean corporate-training style.

Six milestones for a 90-minute training session: intro, setup, activity 1 minutes, activity 2 files, activity 3 static web preview, closing summary.

Connecting arrow labeled workflow. Color-coded milestones. Large icons for classroom visibility.""",
        None,
    ),
    (
        "fig-06-chatbot-to-agent.png",
        "圖6 Chatbot→Agent",
        """Before-and-after infographic, split screen.

LEFT gray — old chatbot: single Q and single A.

RIGHT bright — new agent: goal plus 3-4 connected steps ending in approval.

Center arrow for transformation. Flat icons, training slide aesthetic.""",
        None,
    ),
    (
        "fig-07-activity1-workflow.png",
        "圖7 活動一 Workflow",
        """Horizontal workflow infographic, four connected steps with arrows, school training style.

Step 1 microphone — audio file.
Step 2 document — transcript.
Step 3 checklist — agenda and template.
Step 4 formal document — meeting minutes.

Side note box for timing. Navy/orange palette, flat icons.""",
        None,
    ),
    (
        "fig-08-activity2-files.png",
        "圖8 活動二 執檔",
        """Three-phase horizontal infographic, school admin training style.

Phase A talk, Phase B rules document, Phase C folder sort magic.

Center inbox pile of messy files. Output folders for sorted categories.

Navy/orange, flat vector.""",
        None,
    ),
    (
        "fig-09-activity3-marp.png",
        "圖9 活動三 靜態網站",
        """Web app workflow infographic, modern clean UI style, navy and orange accents.

Flow left to right: prompt to agent, HTML CSS JS files in output folder, browser preview index.html, optional copy to NAS _web folder for teacher.chw.edu.hk.

Homework naming tool or small admin utility context. Not cluttered.""",
        None,
    ),
    (
        "fig-10-closing-summary.png",
        "圖10 總結",
        """Closing infographic, calm professional style, white background navy text.

Three cards: privacy lock, demo folder only, after-class self study cloud.

Bottom quote banner area. Minimal text, large icons.""",
        None,
    ),
]


def load_env(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def image_dimensions(data: bytes) -> tuple[int, int]:
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        w, h = struct.unpack(">II", data[16:24])
        return w, h
    return 0, 0


def build_prompt(content: str, style: str, no_text: bool) -> str:
    parts = [ASPECT_BLOCK, content.strip()]
    parts.append(NO_TEXT_BLOCK if no_text else style)
    return "\n\n".join(parts)


def generate_gemini(api_key: str, prompt: str) -> bytes:
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent?key={api_key}"
    )
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": GEMINI_ASPECT},
        },
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read().decode())

    for part in data.get("candidates", [{}])[0].get("content", {}).get("parts", []):
        inline = part.get("inlineData") or part.get("inline_data")
        if inline and inline.get("data"):
            return base64.b64decode(inline["data"])

    raise RuntimeError(f"No image in Gemini response: {json.dumps(data)[:500]}")


def generate_siliconflow(api_key: str, prompt: str, model: str, size: str) -> bytes:
    url = f"{SILICONFLOW_BASE}/images/generations"
    payload = {
        "model": model,
        "prompt": prompt,
        "image_size": size,
        "batch_size": 1,
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read().decode())

    items = data.get("data") or []
    if not items:
        raise RuntimeError(f"No image in SiliconFlow response: {json.dumps(data)[:300]}")

    item = items[0]
    b64 = item.get("b64_json")
    if b64:
        return base64.b64decode(b64)

    img_url = item.get("url")
    if not img_url:
        raise RuntimeError("SiliconFlow response missing url and b64_json")

    with urllib.request.urlopen(img_url, timeout=120) as img_resp:
        return img_resp.read()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate trainer infographic PNGs")
    p.add_argument(
        "--backend",
        choices=("siliconflow", "gemini"),
        default="siliconflow",
        help="Image API backend (default: siliconflow — better 16:9 in HK)",
    )
    p.add_argument(
        "--with-text",
        action="store_true",
        help="Allow text in image (default: no-text placeholders only)",
    )
    p.add_argument("--force", action="store_true", help="Regenerate even if file exists")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    no_text = not args.with_text
    env = load_env(ENV_PATH)

    if args.backend == "gemini":
        api_key = env.get("GEMINI_API_KEY", "")
        if not api_key:
            print("ERROR: GEMINI_API_KEY not found in .env", file=sys.stderr)
            return 1
        model_label = GEMINI_MODEL
        gen_fn = lambda prompt: generate_gemini(api_key, prompt)
    else:
        api_key = env.get("SILICONFLOW_API_KEY", "")
        if not api_key:
            print("ERROR: SILICONFLOW_API_KEY not found in .env", file=sys.stderr)
            return 1
        sf_model = env.get("SILICONFLOW_MODEL_IMAGE", SILICONFLOW_MODEL)
        sf_size = env.get("SILICONFLOW_IMAGE_SIZE", SILICONFLOW_SIZE)
        model_label = f"{sf_model} @ {sf_size}"
        gen_fn = lambda prompt: generate_siliconflow(api_key, prompt, sf_model, sf_size)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest: list[dict] = []
    failed: list[str] = []

    print(f"Backend: {args.backend}")
    print(f"Model:   {model_label}")
    print(f"Mode:    {'no-text (placeholders)' if no_text else 'with-text'}")
    print(f"Output:  {OUT_DIR}\n")

    for i, (filename, title, content, extra_style) in enumerate(FIGURES, start=1):
        style = extra_style or STYLE_LOCK
        full_prompt = build_prompt(content, style, no_text)
        out_path = OUT_DIR / filename

        if (
            not args.force
            and out_path.exists()
            and out_path.stat().st_size > 10_000
        ):
            w, h = image_dimensions(out_path.read_bytes())
            print(f"[{i}/10] SKIP (exists): {filename} ({w}x{h})")
            manifest.append(
                {
                    "file": filename,
                    "title": title,
                    "status": "skipped",
                    "width": w,
                    "height": h,
                }
            )
            continue

        print(f"[{i}/10] Generating {filename} …", flush=True)
        try:
            img_bytes = gen_fn(full_prompt)
            out_path.write_bytes(img_bytes)
            w, h = image_dimensions(img_bytes)
            ratio = round(w / h, 3) if h else 0
            size_kb = len(img_bytes) // 1024
            ok_ratio = "OK 16:9" if 1.74 <= ratio <= 1.79 else f"WARN ratio={ratio}"
            print(f"         → {out_path.name} ({size_kb} KB, {w}x{h}, {ok_ratio})")
            manifest.append(
                {
                    "file": filename,
                    "title": title,
                    "status": "ok",
                    "size_kb": size_kb,
                    "width": w,
                    "height": h,
                    "aspect_ratio": ratio,
                }
            )
        except urllib.error.HTTPError as e:
            err = e.read().decode(errors="replace")[:300]
            print(f"         FAIL HTTP {e.code}: {err}", file=sys.stderr)
            failed.append(filename)
            manifest.append({"file": filename, "title": title, "status": "fail", "error": err})
        except Exception as e:
            print(f"         FAIL: {e}", file=sys.stderr)
            failed.append(filename)
            manifest.append({"file": filename, "title": title, "status": "fail", "error": str(e)})

        if i < len(FIGURES):
            time.sleep(3)

    manifest_path = OUT_DIR / "manifest.json"
    manifest_path.write_text(
        json.dumps(
            {
                "backend": args.backend,
                "model": model_label,
                "no_text": no_text,
                "aspect_target": "16:9 (1920x1080)",
                "figures": manifest,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"\nManifest: {manifest_path}")
    if failed:
        print(f"Failed ({len(failed)}): {', '.join(failed)}", file=sys.stderr)
        return 1
    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
