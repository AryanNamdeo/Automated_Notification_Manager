import sys
import os
import time
import json
import threading
from tracker import get_running_apps
from notifier import notify
from tray import run_tray
import sys

if "--gui" in sys.argv:
    from gui import start_gui
    start_gui()
    sys.exit()
# =========================
# PyInstaller resource path
# =========================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS   # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# =========================
# Load config safely
# =========================
def load_config():
    config_path = resource_path("config.json")
    with open(config_path, "r") as f:
        return json.load(f)

# =========================
# Program starts here
# =========================
if __name__ == "__main__":

    print("🔔 Smart Notification Manager started...")

    # ▶ Start tray in background
    tray_thread = threading.Thread(target=run_tray, daemon=True)
    tray_thread.start()

    # ▶ Infinite monitoring loop
    while True:
        config = load_config()

        if config.get("focus_mode", False):
            running_apps = get_running_apps()

            for app in config.get("blocked_apps", []):
                for running in running_apps:
                    if app.lower() in running.lower():
                        notify(
                            "⚠ Focus Alert",
                            f"{app} is running. Stay focused!"
                        )
                        time.sleep(10)

        time.sleep(config.get("alert_time_minutes", 1) * 60)
