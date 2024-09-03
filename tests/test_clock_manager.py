from flexmock import flexmock
import pytest

from gng.clock_manager import ClockManager

def test_get_datetime_string_start_time():
    clock = ClockManager()
    assert clock.get_datetime_string() == "Year 1 January 1 00:00:00"

def test_get_datetime_string_adding_time():
    clock = ClockManager()
    clock.add_tick() # Only one tick is not enough to affect the end 
                     # result (unless your FPS is 1)
    clock.add_seconds(45)
    clock.add_minutes(100)
    clock.add_hours(48)
    clock.add_weeks(1)
    clock.add_months(2)
    clock.add_years(7)
    print(clock.get_datetime_string())
    assert clock.get_datetime_string() == "Year 8 March 10 01:40:45"