from datetime import datetime as dt
from datetime import timedelta


def create_alarm_time(minutes=40):
    return dt.now() + timedelta(minutes=minutes)


def is_alarm(alarm):
    return (alarm - dt.now()).total_seconds() <= 0
