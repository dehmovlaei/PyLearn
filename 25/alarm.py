from PySide6.QtCore import *
from database import Database
from mytime import MyTime


class Alarm(QThread):
    signal_counter = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 0, 0)
        self.database = Database()

    def run(self):
        alarms_list = self.database.get_alarms()
        while True:
            self.time.alarm(alarms_list)
            self.signal_counter.emit(self.time)