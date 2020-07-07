from time import sleep
from playsound import playsound
from pomodoro.decorators import timed, timed_avg, logged
from pomodoro.alarms import create_alarm_time, is_alarm


if __name__ == "__main__":
    print("Running Main.py!")