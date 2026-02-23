import os
import json
from datetime import datetime

# Configuration
FINAL_SITE_FILE = "final_design.html"
TARGET_FILE = "index.html"
STATE_FILE = "state.json"
END_DATE = datetime(2026, 12, 31)

def get_days_remaining():
    today = datetime.now()
    delta = END_DATE - today
    return max(1, delta.days)

def build():
    if not os.path.exists(FINAL_SITE_FILE):
        print("Final design file missing.")
        return

    with open(FINAL_SITE_FILE, "r") as f:
        full_code = f.readlines()

    # Load state
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            state = json.load(f)
    else:
        state = {"current_line": 0}

    current_line = state["current_line"]
    total_lines = len(full_code)
    days_left = get_days_remaining()
    
    # Calculate how many lines to add today
    lines_remaining = total_lines - current_line
    lines_per_day = max(1, lines_remaining // days_left)
    
    # If it's the last day, take everything
    if days_left <= 1:
        lines_per_day = lines_remaining

    new_end_line = min(total_lines, current_line + lines_per_day)
    
    # Write the current progress
    with open(TARGET_FILE, "w") as f:
        f.writelines(full_code[:new_end_line])

    # Update state
    state["current_line"] = new_end_line
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

    print(f"Added {new_end_line - current_line} lines. Total progress: {new_end_line}/{total_lines}")

if __name__ == "__main__":
    build()
