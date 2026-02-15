import pystray
from pystray import MenuItem as item
from PIL import Image
import subprocess
import sys
import os

def on_open_gui(icon, item):
    # SAME exe ko --gui flag ke sath run karo
    subprocess.Popen([sys.executable, "--gui"])

def on_exit(icon, item):
    icon.stop()
    os._exit(0)

def run_tray():
    image = Image.new("RGB", (64, 64), "green")

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
