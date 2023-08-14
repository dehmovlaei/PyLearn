class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s
        self.fix_time()
        
    def time_to_second(self):
        seconds = (self.hour * 3600) + (self.minute * 60) + self.second
        return seconds
    
    @staticmethod
    def second_to_time(seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minute = seconds // 60
        second = seconds % 60
        result = Time(hour, minute, second)
        return result
    
    def change_local(self):
        """
        self.minute += 30
        if self.minute >= 60:
            self.minute %= 60
            self.hour += 1
        else:
            self.hour += 3        
        """
        tehran_time = self.sum(Time(3, 30, 0))
        return tehran_time      

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

t4 = Time.second_to_time(6999)
t4.show()

print(t4.time_to_second())

t5 = Time(1, 33, 0)
t6 = t5.change_local()
t5.show()
t6.show()