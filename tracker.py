import psutil

def get_running_apps():
    apps = set()
    for proc in psutil.process_iter(['name']):
        try:
            apps.add(proc.info['name'].lower())
        except:
            pass
    return apps
