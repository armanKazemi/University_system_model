import datetime


class Time:
    """
    Time model for class time.
    """

    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def __init__(self):
        self._date = None       # date (type: datetime)
        self._day_of_week = ''  # weekday
        self._start_clock = None  # start clock (type: datetime)
        self._end_clock = None  # end clock (type: datetime)

    def get_date(self):
        return self._date

    def set_date(self, year, month, day):
        self._date = datetime.datetime(year, month, day)

    def get_day_of_week(self):
        return self._day_of_week

    def set_day_of_week(self, day_number):
        self._day_of_week = self.weekday[day_number - 1]

    def get_start_clock(self):
        return self._start_clock

    def set_start_clock(self, hour=8, minute=0):
        self._start_clock = datetime.time(hour, minute)

    def get_end_clock(self):
        return self._end_clock

    def set_end_clock(self, hour=10, minute=0):
        self._end_clock = datetime.time(hour, minute)

    def get_duration_time(self):
        return datetime.time(self._end_clock.hour - self._start_clock.hour,
                             self._end_clock.minute - self._start_clock.minute)

    def __str__(self):
        return f"{self._day_of_week}" + '' if self._date is None else self._date + f", {self._start_clock} " \
                                                                                   f"to {self._end_clock}"

