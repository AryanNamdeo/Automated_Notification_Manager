import os
from datetime import datetime

LOG_FILE = "logs.txt"

def get_stats():
    stats = {
        "focus_on": 0,
        "focus_off": 0,
        "alerts": 0,
        "focus_minutes": 0
    }

    if not os.path.exists(LOG_FILE):
        return stats

    last_on_time = None

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if "Focus Mode ENABLED" in line:
                stats["focus_on"] += 1
                time_str = line.split("]")[0][1:]
                last_on_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

            elif "Focus Mode DISABLED" in line:
                stats["focus_off"] += 1
                if last_on_time:
                    time_str = line.split("]")[0][1:]
                    off_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
                    diff = (off_time - last_on_time).total_seconds() / 60
                    stats["focus_minutes"] += int(diff)
                    last_on_time = None

            elif "Focus Alert" in line:
                stats["alerts"] += 1

    return stats
