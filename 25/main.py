import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from mainwindow import Ui_MainWindow
from mytime import MyTime


def start_stopwatch():
    thread_stopwatch.start()


def start_timer():
    thread_timer.start()


def stop_stopwatch():
    thread_stopwatch.terminate()


def reset_stopwatch():
    main_window.window().ui.lbl_stopwatch.setText("0:0:0")
    thread_stopwatch.reset()


def show_time_stopwatch(time):
    main_window.window().ui.lbl_stopwatch.setText(f"{time.hour}:{time.minutes}:{time.second}")


def show_time_timer(time):
    print(f"{time.hour}:{time.minutes}:{time.second}")
    main_window.window().ui.tb_hour_timer.setText(str(time.hour))
    main_window.window().ui.tb_minutes_timer.setText(str(time.minutes))
    main_window.window().ui.tb_second_timer.setText(str(time.second))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_start_stopwatch.clicked.connect(start_stopwatch)
        self.ui.btn_start_timer.clicked.connect(start_timer)
        self.ui.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(reset_stopwatch)


class TimerThread(QThread):
    signal_counter = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(00, 15, 30)

    def run(self):
        while True:
            self.time.minus()
            self.signal_counter.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.second = 0
        self.time.minutes = 0
        self.time.hour = 0


class StopWatchMyThread(QThread):
    signal_counter = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 0, 0)

    def run(self):
        while True:
            self.time.plus()
            self.signal_counter.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.second = 0
        self.time.minutes = 0
        self.time.hour = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.window().ui.lbl_stopwatch.setText("0:0:0")
    thread_stopwatch = StopWatchMyThread()
    thread_timer = TimerThread()
    thread_stopwatch.signal_counter.connect(show_time_stopwatch)
    thread_timer.signal_counter.connect(show_time_timer)
    app.exec()
