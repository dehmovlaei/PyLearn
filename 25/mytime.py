from datetime import datetime
import pytz


class MyTime:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s
        self.time_up = False
        self.current_time = [""] * 3

    def plus(self):
        self.second += 1
        if self.second >= 60:
            self.minute += 1
            self.second -= 60
        if self.minute >= 60:
            self.hour += 1
            self.minute -= 60

    def minus(self):
        self.second -= 1
        if self.second <= 0:
            if self.minute > 0:
                self.minute -= 1
                self.second += 60
            elif self.hour > 0:
                self.hour -= 1
                self.minute += 59
                self.second += 60
            elif self.minute == self.hour == 0:
                self.second = 0
                self.minute = 0
                self.hour = 0
                if not self.time_up:
                    self.time_up = True

    def time_zone(self, zone):
        for index, t_zone in enumerate(zone):
            if t_zone == "Iran":
                tz = pytz.timezone("Iran")
                time_tz = datetime.now(tz)
                self.current_time[index] = time_tz.strftime("%H:%M:%S")
            elif t_zone == "Europe/Berlin":
                tz = pytz.timezone("Europe/Berlin")
                time_tz = datetime.now(tz)
                self.current_time[index] = time_tz.strftime("%H:%M:%S")
            elif t_zone == "America/New_York":
                tz = pytz.timezone("America/New_York")
                time_tz = datetime.now(tz)
                self.current_time[index] = time_tz.strftime("%H:%M:%S")
