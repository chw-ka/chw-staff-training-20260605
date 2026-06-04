#!/usr/bin/env python3
"""Test API keys in project root .env (DeepSeek, Gemini, OpenRouter, SiliconFlow)."""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
SILICONFLOW_BASE = "https://api.siliconflow.cn/v1"
OPENROUTER_BASE = "https://openrouter.ai/api/v1"


def load_env(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def mask(s: str, show: int = 8) -> str:
    if len(s) <= show:
        return "***"
    return s[:show] + "…"


def post_json(
    url: str,
    payload: dict,
    headers: dict[str, str],
    timeout: int = 60,
) -> tuple[int, dict]:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={**headers, "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.status, json.loads(resp.read().decode())


def run_test(name: str, fn) -> bool:
    print(f"[{name}] …")
    try:
        ok, msg = fn()
        print(f"  {'PASS' if ok else 'FAIL'}: {msg}")
        return ok
    except urllib.error.HTTPError as e:
        err = e.read().decode(errors="replace")[:500]
        print(f"  FAIL: HTTP {e.code}: {err}")
        return False
    except Exception as e:
        print(f"  FAIL: {e}")
        return False


def test_deepseek(key: str) -> tuple[bool, str]:
    status, data = post_json(
        "https://api.deepseek.com/chat/completions",
        {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": "Reply with exactly: OK"}],
            "max_tokens": 10,
        },
        {"Authorization": f"Bearer {key}"},
    )
    text = (
        data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    )
    return True, f"HTTP {status}; reply: {text[:80]}"


def test_gemini(key: str, model: str) -> tuple[bool, str]:
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={key}"
    )
    status, data = post_json(
        url,
        {
            "contents": [{"parts": [{"text": "Reply with exactly one word: OK"}]}],
            "generationConfig": {"maxOutputTokens": 16},
        },
        {},
    )
    parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
    text = " ".join(p.get("text", "") for p in parts).strip()
    return True, f"HTTP {status}; reply: {text[:80]}"


def test_openrouter_chat(key: str, model: str) -> tuple[bool, str]:
    status, data = post_json(
        f"{OPENROUTER_BASE}/chat/completions",
        {
            "model": model,
            "messages": [{"role": "user", "content": "Reply with exactly: OK"}],
            "max_tokens": 10,
        },
        {
            "Authorization": f"Bearer {key}",
            "HTTP-Referer": "https://chw-staff-training.local",
            "X-Title": "CHW Staff Training Test",
        },
    )
    text = (
        data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    )
    return True, f"HTTP {status}; model={model}; reply: {text[:80]}"


def test_siliconflow_chat(key: str, model: str) -> tuple[bool, str]:
    status, data = post_json(
        f"{SILICONFLOW_BASE}/chat/completions",
        {
            "model": model,
            "messages": [{"role": "user", "content": "Reply with exactly: OK"}],
            "max_tokens": 10,
        },
        {"Authorization": f"Bearer {key}"},
    )
    text = (
        data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    )
    return True, f"HTTP {status}; model={model}; reply: {text[:80]}"


def test_siliconflow_image(key: str, model: str, out_dir: Path) -> tuple[bool, str]:
    status, data = post_json(
        f"{SILICONFLOW_BASE}/images/generations",
        {
            "model": model,
            "prompt": "simple flat illustration of a school art exhibition, warm colors, no text",
            "image_size": "512x512",
            "batch_size": 1,
            "num_inference_steps": 8,
        },
        {"Authorization": f"Bearer {key}"},
        timeout=120,
    )
    items = data.get("data") or data.get("images") or []
    if not items:
        return False, f"HTTP {status}; no image in response: {str(data)[:200]}"

    item = items[0]
    url = item.get("url", "")
    b64 = item.get("b64_json", "")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "test-siliconflow.png"

    if b64:
        import base64

        out_path.write_bytes(base64.b64decode(b64))
        return True, f"HTTP {status}; saved b64 → {out_path} ({out_path.stat().st_size} bytes)"

    if url:
        with urllib.request.urlopen(url, timeout=60) as img_resp:
            out_path.write_bytes(img_resp.read())
        return True, f"HTTP {status}; downloaded → {out_path} ({out_path.stat().st_size} bytes)"

    return False, f"HTTP {status}; no url or b64_json in response"


def main() -> int:
    env = load_env(ENV_PATH)
    print(f"Reading: {ENV_PATH}\n")

    results: dict[str, bool] = {}

    if env.get("DEEPSEEK_API_KEY"):
        print(f"[DeepSeek direct] key {mask(env['DEEPSEEK_API_KEY'])}")
        results["deepseek"] = run_test(
            "DeepSeek chat", lambda: test_deepseek(env["DEEPSEEK_API_KEY"])
        )
        print()
    else:
        print("[DeepSeek direct] SKIP\n")

    if env.get("GEMINI_API_KEY"):
        model = env.get("GEMINI_MODEL", "gemini-2.5-flash")
        print(f"[Gemini direct] key {mask(env['GEMINI_API_KEY'])} model={model}")
        results["gemini"] = run_test(
            "Gemini", lambda: test_gemini(env["GEMINI_API_KEY"], model)
        )
        print()
    else:
        print("[Gemini direct] SKIP\n")

    if env.get("OPENROUTER_API_KEY"):
        or_model = env.get(
            "OPENROUTER_MODEL_GEMINI", "google/gemini-2.5-flash"
        )
        print(f"[OpenRouter] key {mask(env['OPENROUTER_API_KEY'])}")
        results["openrouter_gemini"] = run_test(
            f"OpenRouter chat ({or_model})",
            lambda: test_openrouter_chat(env["OPENROUTER_API_KEY"], or_model),
        )
        print()
    else:
        print("[OpenRouter] SKIP\n")

    sf_key = env.get("SILICONFLOW_API_KEY", "")
    if sf_key:
        sf_chat = env.get(
            "SILICONFLOW_MODEL_CHAT", "deepseek-ai/DeepSeek-V3.2"
        )
        sf_image = env.get("SILICONFLOW_MODEL_IMAGE", "Qwen/Qwen-Image")
        sf_image_fallbacks = [
            sf_image,
            "Qwen/Qwen-Image",
            "Tongyi-MAI/Z-Image-Turbo",
            "Kwai-Kolors/Kolors",
        ]
        # dedupe while preserving order
        seen: set[str] = set()
        sf_image_models = []
        for m in sf_image_fallbacks:
            if m not in seen:
                seen.add(m)
                sf_image_models.append(m)
        print(f"[SiliconFlow] key {mask(sf_key)}")
        results["siliconflow_chat"] = run_test(
            f"SiliconFlow chat ({sf_chat})",
            lambda: test_siliconflow_chat(sf_key, sf_chat),
        )
        out_dir = ROOT / "activity-3-marp" / "assets"
        def _sf_image_test() -> tuple[bool, str]:
            last_err = "no models tried"
            for m in sf_image_models:
                ok, msg = test_siliconflow_image(sf_key, m, out_dir)
                if ok:
                    return True, msg
                last_err = f"{m}: {msg}"
            return False, last_err

        results["siliconflow_image"] = run_test(
            "SiliconFlow image (Qwen-Image / fallbacks)",
            _sf_image_test,
        )
        print()
    else:
        print("[SiliconFlow] SKIP\n")

    print("--- Summary ---")
    for name, ok in results.items():
        print(f"  {name}: {'PASS' if ok else 'FAIL'}")

    failed = [k for k, v in results.items() if not v]
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
