import subprocess

def enable_focus_assist():
    subprocess.run(
        [
            "powershell",
            "-Command",
            "New-ItemProperty -Path HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings "
            "-Name NOC_GLOBAL_SETTING_TOASTS_ENABLED -PropertyType DWord -Value 0 -Force"
        ],
        shell=True
    )

def disable_focus_assist():
    subprocess.run(
        [
            "powershell",
            "-Command",
            "New-ItemProperty -Path HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings "
            "-Name NOC_GLOBAL_SETTING_TOASTS_ENABLED -PropertyType DWord -Value 1 -Force"
        ],
        shell=True
    )
