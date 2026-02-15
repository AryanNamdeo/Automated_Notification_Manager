import subprocess

def enable_focus_assist():
    subprocess.run([
        "powershell",
        "-Command",
        "New-ItemProperty -Path HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings "
        "-Name NOC_GLOBAL_SETTING_TOASTS_ENABLED -Value 0 -PropertyType DWORD -Force"
    ], shell=True)

def disable_focus_assist():
    subprocess.run([
        "powershell",
        "-Command",
        "New-ItemProperty -Path HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings "
        "-Name NOC_GLOBAL_SETTING_TOASTS_ENABLED -Value 1 -PropertyType DWORD -Force"
    ], shell=True)
