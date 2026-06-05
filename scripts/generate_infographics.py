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
    "widescreen slide, 4K quality, CHW school staff training."
)

STYLE_WITH_TEXT = (
    "TEXT VERSION: Render all labels, titles, and captions in clear readable ENGLISH "
    "only. Use short phrases (not paragraphs). Large sans-serif font, high contrast, "
    "legible on projector. Spell correctly. No Chinese characters. "
    "MANDATORY 16:9 landscape 1920x1080 widescreen."
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

# Content prompts — English text labels when --with-text; see trainer/infographic-prompt.md
FIGURES: list[tuple[str, str, str, str | None]] = [
    (
        "fig-01-cursor-interface.png",
        "Fig 1 Cursor Interface",
        """Create a clean educational infographic, flat modern style, navy blue and orange accent, white background.

Show a simplified desktop app window titled "Cursor" with THREE vertical panels:

LEFT (25%): file explorer tree, label "Files — Project folders", note "Open Folder ready"

CENTER (50%): document preview like Word with meeting minutes, label "Editor — Preview results (not code)"

RIGHT (25%): Agent chat panel with glowing border, label "Agent — Today's focus"

Bottom badges: "Ctrl+I Agent" | "Ctrl+L Chat" | "Ctrl+, Settings" | "@ Reference files"

Annotate Agent panel with arrows:
1. "Model → Auto" (dropdown)
2. "Paste Prompt" (input)
3. "Approve — Safety gate" (button)

Friendly for school teachers. No real code. All text in English.""",
        None,
    ),
    (
        "fig-02-why-cursor-hk.png",
        "Fig 2 Why Cursor (HK)",
        """Educational comparison infographic, minimalist flowchart, school training workshop.

Title: "Why learn Cursor today?"
Subtitle: "A pro developer tool — now used by non-IT staff"

Three columns left to right:
Col 1 "Previously best": Claude Desktop icon, caption "Best for writing"
Col 2 "Hong Kong reality": HK map + barrier, captions "Claude Desktop blocked" "Codex blocked"
Col 3 "Today's choice": generic IDE window, caption "Cursor — API + MCP + local files"

Bottom banner: "Goal: workflow design — Cursor is the tool that works in HK"

Navy/teal/white, clean icons, all English text.""",
        None,
    ),
    (
        "fig-03-five-concepts.png",
        "Fig 3 Five Concepts",
        """Infographic poster, five equal cards in a row, flat illustration for school staff.

Title: "Five Cursor concepts — take back to school"

Card 1 Workflow: arrows "Input → Steps → Output", subtitle "You = designer, AI = intern"
Card 2 MCP: portal door to folder + cloud, subtitle "Magic door — local files; Drive after class"
Card 3 Skills: recipe card, subtitle "Meeting minutes SKILL · File organizer SKILL"
Card 4 Rules: checklist doc, subtitle "Formal tone, table formats"
Card 5 Model: dropdown "Auto" + key icon, subtitle "Class: Auto; API Key optional after class"

White background, soft shadows, all English labels.""",
        None,
    ),
    (
        "fig-04-boss-vs-intern.png",
        "Fig 4 Boss vs Intern",
        """Friendly workplace metaphor, warm cartoon-flat style for adult teachers.

Teacher at desk labeled "You — Workflow boss" pointing right.
Assistant at computer labeled "Agent — Intern".
Screen shows formatted meeting minutes (NOT code).

Speech bubble: "Talk on the right, watch results in the middle"
Note: "Approve before changes — safety gate"
Tag: "Vibe Coding — Focus on Input / Output"

School office setting, encouraging tone, English text only.""",
        None,
    ),
    (
        "fig-05-90min-timeline.png",
        "Fig 5 90-min Timeline",
        """Horizontal timeline, six milestones, corporate training style.

Title: "CHW Staff Training — 90-minute roadmap"

M1 (00-10): "Intro — AI 2026" tags: Workflow, Agent
M2 (10-20): "Setup" tags: Cursor, Auto, Appendix 08
M3 (20-40): "Activity 1 Audio→Minutes" tags: Whisper, SKILL, Vibe Coding
M4 (40-60): "Activity 2 File sort" tags: Talk first, Read content, Approve
M5 (60-85): "Activity 3 Teaching web" tags: HTML/CSS/JS, Browser preview
M6 (85-90): "Closing" tags: Privacy, Ollama, Workflow designer

Arrow label: "Agentic Workflow"
Bottom note: "Google Drive — after-class self-study (not in 90 min)"

Color-coded milestones, large icons, English text.""",
        None,
    ),
    (
        "fig-06-chatbot-to-agent.png",
        "Fig 6 Chatbot to Agent",
        """Before-and-after split screen infographic.

LEFT gray "Old: Chatbot": one Q bubble → one A bubble, caption "Ask and answer"

RIGHT bright "New: Agent": goal at top, 4 steps (read → process → write → approval), caption "Multi-step, you approve"

Center arrow: "2026 shift — Agentic Workflow"

Bottom icons: "Activity 1 Minutes" | "Activity 2 Files" | "Activity 3 Web"
Bottom line: "Teachers as workflow designers"

Flat icons, English text, training slide style.""",
        None,
    ),
    (
        "fig-07-activity1-workflow.png",
        "Fig 7 Activity 1 Workflow",
        """Horizontal workflow, four steps with arrows, school training style.

Title: "Activity 1 — Learn Workflow (meeting minutes example)"

Step 1 mic: "Audio .m4a" subtitle "Phase 1: Whisper large-v3" note "Class: ~45s demo clip"
Step 2 doc: "Transcript text" subtitle "Agent writes code locally — Vibe Coding"
Step 3 checklist: "Agenda + template" subtitle "Phase 2: Auto + meeting-minutes SKILL"
Step 4 Word doc: "Minutes .docx" subtitle "Step 3 (optional): last year format + this year content"

Banner: "Vibe Coding — No need to read code; focus Input / Output"
Side note: "1-hour audio ≈ 1-2 hours to transcribe — run locally after class"

Navy/orange, English text.""",
        None,
    ),
    (
        "fig-08-activity2-files.png",
        "Fig 8 Activity 2 Files",
        """Three-phase horizontal infographic, school admin training.

Title: "Activity 2 — ~100 inbox files · sort by content"

Phase A speech bubbles: "A Talk 3-5 min" bullet "No moving files — agree rules"
Phase B profile doc: "B Set rules 3-5 min" bullet "my_organization_profile.md"
Phase C magic sort: "C Execute 10-12 min" bullet "Read @inbox/ → sorted/Teaching, Admin, ICT…"

Center messy pile: "Messy names (1)(2) — not by file extension"

Output folders: "sorted/Teaching/2025-2026/" "sorted/Admin/cross-year/" "sorted/trash/"

Bottom: "Open Folder → activity-2-files · Approve each step · Demo files only"

Navy/orange flat vector, English text.""",
        None,
    ),
    (
        "fig-09-activity3-marp.png",
        "Fig 9 Activity 3 Teaching Web",
        """Web app workflow infographic, modern clean UI, navy/orange school training style.

Title: "Activity 3 — Agent builds teaching web page"

Flow left to right:
1. "Teaching prompt" — simulation, quiz, or simple game
2. "Agent outputs" — index.html, styles.css, app.js → output/
3. "Browser preview" — open index.html locally
4. "Optional publish" — copy to NAS _web → teacher.chw.edu.hk

Caption: "No PowerPoint, no build step — instant browser Wow"
Tags: "HTML/CSS/JS" "Local preview" "Publish guide 07"
Bottom: "Class model: Auto"

English labels, professional school context, not cluttered.""",
        None,
    ),
    (
        "fig-10-closing-summary.png",
        "Fig 10 Closing Summary",
        """Closing infographic, calm professional, white background navy text.

Title: "Take back to school — Workflow designer"

Card 1 lock: "Sensitive data" subtitle "Student privacy → Ollama local / approved tools"
Card 2 folder: "Demo files only" subtitle "Don't touch real Downloads / Desktop"
Card 3 cloud: "After class" subtitle "Google Drive tidy-up → handout 09"

Bottom quote: "Your value is designing workflows, not repetitive admin"

Minimal text, large icons, English only.""",
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
    if no_text:
        parts.append(NO_TEXT_BLOCK)
    else:
        parts.extend([style, STYLE_WITH_TEXT])
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
