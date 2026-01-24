import tkinter as tk
import json
import os
import warnings
warnings.filterwarnings("ignore")
import sys
from focus_assist import enable_focus_assist, disable_focus_assist
from win10toast import ToastNotifier

toaster = ToastNotifier()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

CONFIG_FILE = resource_path("config.json")

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_notification(title, message):
    toaster.show_toast(title, message, duration=4, threaded=True)

def start_gui():
    window = tk.Tk()
    window.title("Smart Notification Manager")
    window.geometry("320x220")
    window.resizable(False, False)

    data = load_config()

    status = tk.StringVar()
    status.set("Focus Mode: ON" if data["focus_mode"] else "Focus Mode: OFF")

    status_label = tk.Label(
        window,
        textvariable=status,
        font=("Arial", 14, "bold"),
        fg="green" if data["focus_mode"] else "red"
    )
    status_label.pack(pady=30)

    def toggle_focus():
    data = load_config()
    data["focus_mode"] = not data["focus_mode"]
    save_config(data)

    if data["focus_mode"]:
        enable_focus_assist()
        status.set("Focus Mode: ON")
        status_label.config(fg="green")
        show_notification("Focus Mode ON", "All notifications blocked")
    else:
        disable_focus_assist()
        status.set("Focus Mode: OFF")
        status_label.config(fg="red")
        show_notification("Focus Mode OFF", "Notifications restored")


    tk.Button(
        window,
        text="Toggle Focus Mode",
        width=20,
        height=2,
        command=toggle_focus
    ).pack()

    window.mainloop()
