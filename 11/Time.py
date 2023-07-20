class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s
        self.fix_time()
        
    def time_to_second(self):
        seconds = (self.hour * 3600) + (self.minute * 60) + self.second
        return seconds
    
    def second_to_time(self, seconds):
        seconds = seconds % (24 * 3600)
        self.hour = seconds // 3600
        seconds %= 3600
        self.minute = seconds // 60
        self.second = seconds % 60
        result = Time(self.hour, self.minute, self.second)
        return result
    
    def change_local(self):
        self.minute += 30
        if self.minute >= 60:
            self.minute %= 60
            self.hour += 1
        else:
            self.hour += 3        

    def sum(self, other):
        h_new = self.hour + other.hour
        m_new = self.minute + other.minute
        s_new = self.second + other.second
        result = Time(h_new, m_new, s_new)
        return result
    
    def sub(self, other):
        h_new = self.hour - other.hour
        m_new = self.minute - other.minute
        s_new = self.second - other.second
        result = Time(h_new, m_new, s_new)
        return result
    
    def fix_time(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        
        if self.second < 0:
            self.second += 60
            self.minute -= 1

        if self.minute < 0:
            self.minute += 60
            self.hour -= 1

    def show(self):
        print(self.hour, ':', self.minute, ':', self.second)

t1 = Time(3, 45, 17)
t1.show()

t2 = Time(4, 13, 2)
t2.show()

t3 = t1.sum(t2)
t3.show()

t4 = Time(0, 0, 0)
t4.second_to_time(6999)
t4.show()

print(t4.time_to_second())

t5 = Time(1, 33, 0)
t5.change_local()
t5.show()