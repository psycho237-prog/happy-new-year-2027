from datetime import date
from pathlib import Path
import shutil

START_DATE = date(2026, 10, 18)
FINISH_DATE = date(2026, 12, 31)

final_design = Path("final_design.html")
index = Path("index.html")
today = date.today()

if not final_design.exists():
    raise FileNotFoundError("final_design.html is missing from the repository root.")

if today >= FINISH_DATE:
    shutil.copyfile(final_design, index)
    print("Final design published.")
else:
    total_days = (FINISH_DATE - START_DATE).days
    elapsed_days = max(0, (today - START_DATE).days)
    progress = min(99, int(elapsed_days / total_days * 100))

    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Happy New Year 2027 — Coming Soon</title>
  <style>
    body {{
      margin: 0; min-height: 100vh; display: grid; place-items: center;
      background: #0a0a0a; color: #f4f4f4;
      font-family: Arial, sans-serif; text-align: center;
    }}
    main {{ width: min(90%, 600px); }}
    h1 {{ color: #d4af37; }}
    progress {{ width: 100%; height: 24px; accent-color: #d4af37; }}
    p {{ color: #d4af37; }}
  </style>
</head>
<body>
  <main>
    <h1>Happy New Year 2027</h1>
    <p>The celebration is being built. The finished design arrives December 31, 2026.</p>
    <progress value="{progress}" max="100"></progress>
    <p>{progress}% complete</p>
  </main>
</body>
</html>
"""

    index.write_text(page, encoding="utf-8")
    print(f"Progress page updated: {progress}% complete.")
