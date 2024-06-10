import time

from PySide6.QtCore import *
from mytime import MyTime

class AlarmThread(QThread):
    signal_counter = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 0, 0)

    def run(self):
        while True:
            self.signal_counter.emit(self.time)
            time.sleep(15)