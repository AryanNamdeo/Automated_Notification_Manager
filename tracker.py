import psutil

def kill_blocked_apps(blocked_apps):
    for proc in psutil.process_iter(['name']):
        try:
            process_name = proc.info['name']
            if process_name:
                for app in blocked_apps:
                    if app.lower() in process_name.lower():
                        proc.kill()
        except:
            pass
