import tkinter as tk
import json
import os
import sys
import warnings
warnings.filterwarnings("ignore")

from stats import get_stats
from logger import log_event
from focus_assist import enable_focus_assist, disable_focus_assist
from win10toast import ToastNotifier

toaster = ToastNotifier()

# -------------------------
# PyInstaller safe path
# -------------------------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

CONFIG_FILE = resource_path("config.json")

# -------------------------
# Config
# -------------------------
def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

# -------------------------
# Notification
# -------------------------
def show_notification(title, message):
    toaster.show_toast(title, message, duration=4, threaded=True)

# -------------------------
# GUI
# -------------------------
def start_gui():

    window = tk.Tk()
    window.title("Smart Notification Manager")
    window.geometry("380x340")
    window.resizable(False, False)
    window.configure(bg="#1e1e2f")

    data = load_config()
    focus_on = data.get("focus_mode", False)

    # ---------- Stats Window ----------
    def open_stats():
        stats = get_stats()

        stats_win = tk.Toplevel(window)
        stats_win.title("Focus Stats")
        stats_win.geometry("300x260")
        stats_win.resizable(False, False)

        tk.Label(stats_win, text="📊 Focus Statistics", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(stats_win, text=f"Focus Mode ON: {stats['focus_on']} times").pack(pady=5)
        tk.Label(stats_win, text=f"Focus Mode OFF: {stats['focus_off']} times").pack(pady=5)
        tk.Label(stats_win, text=f"Total Focus Time: {stats['focus_minutes']} minutes").pack(pady=5)
        tk.Label(stats_win, text=f"Blocked Alerts: {stats['alerts']}").pack(pady=5)

        tk.Button(stats_win, text="Close", command=stats_win.destroy).pack(pady=15)

    # ---------- Title ----------
    tk.Label(
        window,
        text="Smart Notification Manager",
        bg="#1e1e2f",
        fg="white",
        font=("Segoe UI", 14, "bold")
    ).pack(pady=15)

    # ---------- Card ----------
    card = tk.Frame(window, bg="#2a2a40")
    card.pack(padx=20, pady=10, fill="both", expand=True)

    status_var = tk.StringVar()

    def update_ui(state):
        if state:
            status_var.set("FOCUS MODE: ON")
            status_label.config(fg="#00ff99")
            info_label.config(text="All notifications are blocked")
            toggle_btn.config(text="Disable Focus Mode", bg="#ff4d4d")
        else:
            status_var.set("FOCUS MODE: OFF")
            status_label.config(fg="#ff6666")
            info_label.config(text="Notifications are allowed")
            toggle_btn.config(text="Enable Focus Mode", bg="#00cc99")

    status_label = tk.Label(
        card,
        textvariable=status_var,
        bg="#2a2a40",
        font=("Segoe UI", 16, "bold")
    )
    status_label.pack(pady=20)

    info_label = tk.Label(
        card,
        bg="#2a2a40",
        fg="#cccccc",
        font=("Segoe UI", 10)
    )
    info_label.pack(pady=5)

    def toggle_focus():
        data = load_config()
        data["focus_mode"] = not data.get("focus_mode", False)
        save_config(data)

        if data["focus_mode"]:
            enable_focus_assist()
            log_event("Focus Mode ENABLED manually from GUI")
            show_notification("Focus Mode ON", "All notifications blocked")
        else:
            disable_focus_assist()
            log_event("Focus Mode DISABLED manually from GUI")
            show_notification("Focus Mode OFF", "Notifications restored")

        update_ui(data["focus_mode"])

    toggle_btn = tk.Button(
        card,
        font=("Segoe UI", 12, "bold"),
        fg="white",
        bd=0,
        width=20,
        height=2,
        command=toggle_focus
    )
    toggle_btn.pack(pady=25)

    # ---------- Stats Button ----------
    tk.Button(
        window,
        text="View Focus Stats",
        width=20,
        height=2,
        command=open_stats
    ).pack(pady=10)

    update_ui(focus_on)
    window.mainloop()

# -------------------------
# Entry
# -------------------------
if __name__ == "__main__":
    start_gui()
