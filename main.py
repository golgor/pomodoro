from alarms import create_alarm_time, is_alarm
from time import sleep
from playsound import playsound
from decorators import timed

if __name__ == "__main__":
    print("Do you want to start the Pomodoro timer (y/n)?")
    s = input()
    if 'y' in s:
        alarm = create_alarm_time(1)
        while not is_alarm(alarm):
            print(is_alarm(alarm))
            sleep(1)
        playsound("alarm1.mp3")
