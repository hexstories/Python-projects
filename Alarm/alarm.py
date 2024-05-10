import time
from datetime import datetime, timedelta
from plyer import notification
import winsound

def set_alarm(hour, minute):
    # Get the current time
    now = datetime.now()
    alarm_time = datetime(now.year, now.month, now.day, hour, minute, 0)

    # Calculate the time difference
    time_difference = alarm_time - now

    # Check if the time difference is negative
    if time_difference.total_seconds() < 0:
        # Handle negative time difference, for example by setting it to zero
        time_difference = timedelta(seconds=0)

    # Sleep for the calculated time difference
    time.sleep(time_difference.total_seconds()) 

    # Show notification
    notification.notify(
        title="Alarm",
        message="Oya get up and be Productive!!",
        app_icon=None,
        timeout=20  # notification timeout in seconds
    )

    # Play sound
    winsound.Beep(2000, 1000)  # beep at 1000 Hz for 1 second

set_alarm(20, 10)
