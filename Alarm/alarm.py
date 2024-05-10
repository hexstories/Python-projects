import time
from datetime import datetime
from plyer import notification
import winsound

def set_alarm(hour, minuite):
    #get the current time
    now = datetime.now()
    alarm_time = datetime(now.year, now.month, now.day, hour, minuite, 0)

    #calculate the time difference
    time_difference = alarm_time - now

    #wait until the alarm time
    time.sleep(time_difference.total_seconds())

    #play sound
    #winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)

    #show notification
    notification.notify(
        title = "Alarm",
        message = " Oya get up and be Productive!!",
        app_icon=None,
        timeout = 10 #notification timeout in seconds
    )

    winsound.Beep(1000, 1000) # beep at 1000 hz for 1 second


set_alarm(10, 30)