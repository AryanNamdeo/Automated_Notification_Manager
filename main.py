import sys
import os
import time
import json
import threading
from tray import run_tray
from scheduler import check_schedule
from tracker import kill_blocked_apps   # ✅ NEW IMPORT

# =========================
# GUI Mode
# =========================
if "--gui" in sys.argv:
    from gui import start_gui
    start_gui()
    sys.exit()

# =========================
# PyInstaller resource path
# =========================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
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
        try:
            config = load_config()

            # Apply schedule if enabled
            config["focus_mode"] = check_schedule(config)

            # If focus mode is ON → kill blocked apps
            if config.get("focus_mode", False):
                kill_blocked_apps(config.get("blocked_apps", []))

            # Check every 5 seconds (fast & stable)
            time.sleep(5)

        except Exception as e:
            print("Error:", e)
            time.sleep(5)
