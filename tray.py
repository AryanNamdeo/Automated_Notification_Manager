import pystray
from pystray import MenuItem as item
from PIL import Image
import subprocess
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def on_open_gui(icon, item):
    subprocess.Popen([sys.executable, "--gui"])

def on_exit(icon, item):
    icon.stop()
    sys.exit()

def run_tray():
    image = Image.open(resource_path("icon.ico"))

    menu = (
        item("Open Control Panel", on_open_gui),
        item("Exit", on_exit)
    )

    icon = pystray.Icon(
        "SmartNotifier",
        image,
        "Smart Notification Manager",
        menu
    )
    icon.run()
