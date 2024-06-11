import time

from PySide6.QtCore import *
from mytime import MyTime


class WorldClockThread(QThread):
    signal_counter = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 0, 0)

    def run(self):
        zone = ["Iran", "Europe/Berlin", "America/New_York"]
        while True:
            self.time.time_zone(zone)
            self.signal_counter.emit(self.time)
            time.sleep(1)