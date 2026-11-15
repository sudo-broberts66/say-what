#!/usr/bin/env python3
"""Build the standalone site in docs/ from the two page sources.

The sources (inside-what.html, say-what.html) are page fragments: a <title>,
<meta>, <link> and <style> followed by the page body, with no <html> or <head>
of their own. This wraps each one in a complete HTML document and points the
links between the two pages at each other.

    python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "docs"

SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{description}">
<style>
:root {{ color-scheme: light; padding: env(safe-area-inset-top, 0px) 0 env(safe-area-inset-bottom, 0px); }}
body {{ margin: 0; font: 14px system-ui, sans-serif; }}
img {{ max-width: 100%; }}
[hidden] {{ display: none !important; }}
</style>
{head}
</head>
<body>
{body}
</body>
</html>
"""

TEXT_ARTIFACT = "https://claude.ai/artifact/KjvZS9prbv5et53TCUQZ39"
TEXT_INTRO = '<p class="prose">You can check each part of that on this page, starting with your own reflexes.</p>'

PAGES = [
    {
        "src": "inside-what.html",
        "out": "index.html",
        "description": "Why do we say “what?” when we already heard it? A six-scene interactive "
                       "experience, with sound, of the half-second where your mouth outruns your understanding.",
        "replace": [(TEXT_ARTIFACT, "text.html")],
    },
    {
        "src": "say-what.html",
        "out": "text.html",
        "description": "Why do we say “what?” when we already heard it? The answer as a single "
                       "interactive page: a reaction test, a slow-motion timeline, and the research behind it.",
        "replace": [(TEXT_INTRO, TEXT_INTRO.replace(
            "</p>", ' Or <a href="index.html">step inside the immersive version</a>, with sound.</p>'))],
    },
]


def build():
    OUT.mkdir(exist_ok=True)
    for page in PAGES:
        source = (ROOT / page["src"]).read_text(encoding="utf-8")
        for old, new in page["replace"]:
            if old not in source:
                raise SystemExit(f"{page['src']}: expected text not found: {old[:60]}")
            source = source.replace(old, new)
        cut = source.index("</style>") + len("</style>")
        html = SHELL.format(description=page["description"],
                            head=source[:cut].strip(), body=source[cut:].strip())
        (OUT / page["out"]).write_text(html, encoding="utf-8")
        print(f"docs/{page['out']}  ({len(html):,} bytes)")
    # Tell GitHub Pages to serve the files as they are.
    (OUT / ".nojekyll").write_text("", encoding="utf-8")


if __name__ == "__main__":
    build()
