class MyTime:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

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
                print("time up")
