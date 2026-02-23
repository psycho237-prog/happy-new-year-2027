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
        state = {"current_line_float": 0.0}

    total_lines = len(full_code)
    days_left = get_days_remaining()
    
    # Calculate fractional lines per day to finish exactly on time
    lines_remaining = total_lines - state["current_line_float"]
    increment = lines_remaining / days_left
    
    new_line_float = state["current_line_float"] + increment
    new_line_int = int(new_line_float)
    
    # Write the code up to the integer index
    with open(TARGET_FILE, "w") as f:
        f.writelines(full_code[:new_line_int])
        f.write(f"\n<!-- Daily Build Progress: {datetime.now().strftime('%Y-%m-%d')} -->\n")

    # Update state
    state["current_line_float"] = new_line_float
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

    print(f"Progress: {new_line_int}/{total_lines} lines. {days_left} days remaining.")

if __name__ == "__main__":
    build()
