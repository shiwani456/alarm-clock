from datetime import datetime, timedelta
import platform
import time


TIME_FORMATS = [
    "%H:%M",
    "%I:%M %p",
]


def parse_time(value: str) -> str:
    """
    Accepts

    07:30
    23:15
    7:30 PM

    Returns

    HH:MM (24-hour)
    """

    value = value.strip()

    for fmt in TIME_FORMATS:
        try:
            dt = datetime.strptime(value, fmt)
            return dt.strftime("%H:%M")
        except ValueError:
            pass

    raise ValueError("Invalid time format.")


def current_time():
    return datetime.now().strftime("%H:%M")


def current_datetime():
    return datetime.now()


def next_snooze(minutes=5):
    return (
        datetime.now() + timedelta(minutes=minutes)
    ).strftime("%H:%M")


def beep():
    """
    Cross-platform beep
    """

    system = platform.system()

    if system == "Windows":
        import winsound

        for _ in range(5):
            winsound.Beep(1000, 700)

    else:
        for _ in range(5):
            print("\a")
            time.sleep(1)