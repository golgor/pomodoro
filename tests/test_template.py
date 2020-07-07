import test_importer
from datetime import datetime as dt
from datetime import timedelta
import pomodoro.alarms as alarms


def test_create_alarm():
    alarm = alarms.create_alarm_time()
    assert isinstance(alarm, dt)


def test_2():
    # Test 32bit (stride = 2) and 64bit (stride = 4)
    assert 1 == 0


def test_3():
    assert 1 == 0
