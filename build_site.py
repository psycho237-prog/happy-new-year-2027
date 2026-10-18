import json
from pathlib import Path
from html import escape

STATE_FILE = Path("state.json")
HTML_FILE = Path("index.html")


def read_count():
    if not STATE_FILE.exists():
        return 0

    try:
        state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        return int(state.get("count", 0))
    except (json.JSONDecodeError, TypeError, ValueError):
        return 0


count = read_count() + 1
STATE_FILE.write_text(
    json.dumps({"count": count}, indent=2) + "\n",
    encoding="utf-8",
)

new_div = f'    <div class="build-item" hidden>Build {count}</div>\n'

if HTML_FILE.exists():
    html = HTML_FILE.read_text(encoding="utf-8")
else:
    html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Happy New Year 2027</title>
</head>
<body>
  <main>
    <h1>Happy New Year 2027</h1>
  </main>
</body>
</html>
"""

if "</body>" in html:
    html = html.replace("</body>", f"{new_div}</body>", 1)
else:
    html += f"\n{new_div}"

HTML_FILE.write_text(html, encoding="utf-8")
print(f"Build complete. Total build items: {count}")
