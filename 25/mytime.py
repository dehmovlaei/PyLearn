class MyTime:
    def __init__(self, h, m, s):
        self.hour = h
        self.minutes = m
        self.second = s

    def plus(self):
        self.second += 1
        if self.second >= 60:
            self.minutes += 1
            self.second -= 60
        if self.minutes >= 60:
            self.hour += 1
            self.minutes -= 60
