import math

import gng.global_constants as gc

class ClockManager:
    def __init__(self):
        self.ticks_passed = 0
        # TODO: possibly fantasy-ize months
        self.list_of_months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        # Helpful for calculations: ------------------------------------
        self.number_of_months_in_one_year = len(self.list_of_months)
        self.number_of_days_in_one_month = 30
        self.number_of_days_in_one_week = 7
        self.number_of_hours_in_one_day = 24
        self.number_of_minutes_in_one_hour = 60
        self.number_of_seconds_in_one_minute = 60

        self.number_of_ticks_in_one_second = gc.FPS
        self.number_of_ticks_in_one_minute = \
            self.number_of_ticks_in_one_second \
            * self.number_of_seconds_in_one_minute
        self.number_of_ticks_in_one_hour = \
            self.number_of_ticks_in_one_minute \
            * self.number_of_minutes_in_one_hour
        self.number_of_ticks_in_one_day = \
            self.number_of_ticks_in_one_hour \
            * self.number_of_hours_in_one_day
        self.number_of_ticks_in_one_week = \
            self.number_of_ticks_in_one_day \
            * self.number_of_days_in_one_week
        self.number_of_ticks_in_one_month = \
            self.number_of_ticks_in_one_day \
            * self.number_of_days_in_one_month
        self.number_of_ticks_in_one_year = \
            self.number_of_ticks_in_one_month \
            * self.number_of_months_in_one_year
        # --------------------------------------------------------------
        # Clock starts January 1 at 00:00 midnight on year 0.

    def add_tick(self):
        self.ticks_passed += 1

    def add_seconds(self, number):
        self.ticks_passed += number*self.number_of_ticks_in_one_second

    def add_minutes(self, number):
        self.add_seconds(self.number_of_seconds_in_one_minute*number)

    def add_hours(self, number):
        self.add_minutes(self.number_of_minutes_in_one_hour*number)

    def add_days(self, number):
        self.add_hours(self.number_of_hours_in_one_day*number)

    def add_weeks(self, number):
        self.add_days(self.number_of_days_in_one_week*number)

    def add_months(self, number):
        self.add_days(self.number_of_days_in_one_month*number)

    def add_years(self, number):
        self.add_months(self.number_of_months_in_one_year*number)

    def get_datetime_string(self):
        year = (math.floor(
            self.ticks_passed/self.number_of_ticks_in_one_year
        )) + 1
        month_index = math.floor(
            self.ticks_passed/self.number_of_ticks_in_one_month
        ) % self.number_of_months_in_one_year
        day = (math.floor(
            self.ticks_passed/self.number_of_ticks_in_one_day
        ) % self.number_of_days_in_one_month) + 1
        hour = math.floor(
            self.ticks_passed/self.number_of_ticks_in_one_hour
        ) % self.number_of_hours_in_one_day
        if hour <= 9:
            hour = f"0{hour}"
        minute = math.floor(
            self.ticks_passed/self.number_of_ticks_in_one_minute
        ) % self.number_of_minutes_in_one_hour
        if minute <= 9:
            minute = f"0{minute}"
        second = math.floor(
            self.ticks_passed/self.number_of_ticks_in_one_second
        ) % self.number_of_seconds_in_one_minute
        if second <= 9:
            second = f"0{second}"
        return (
            f"Year {year} {self.list_of_months[month_index]} {day} "\
            f"{hour}:{minute}:{second}"
        )





        

