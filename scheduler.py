from datetime import datetime
from focus_assist import enable_focus_assist, disable_focus_assist

def check_schedule(config):
    if not config.get("auto_focus", False):
        return config["focus_mode"]

    now = datetime.now().time()
    start = datetime.strptime(config["focus_schedule"]["start"], "%H:%M").time()
    end = datetime.strptime(config["focus_schedule"]["end"], "%H:%M").time()

    if start <= now <= end:
        enable_focus_assist()
        return True
    else:
        disable_focus_assist()
        return False
