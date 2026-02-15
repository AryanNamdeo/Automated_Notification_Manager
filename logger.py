from datetime import datetime

LOG_FILE = "logs.txt"

def log_event(message):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time_stamp}] {message}\n")
