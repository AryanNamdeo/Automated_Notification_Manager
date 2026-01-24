from win10toast import ToastNotifier

toaster = ToastNotifier()

def notify(title, message):
    toaster.show_toast(
        title,
        message,
        duration=5,
        threaded=True
    )
