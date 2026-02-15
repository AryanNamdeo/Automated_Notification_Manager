import psutil

def get_running_apps():
    apps = []
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name']:
                apps.append(proc.info['name'].lower())
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return apps
