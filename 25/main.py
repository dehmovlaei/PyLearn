import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from mainwindow import Ui_MainWindow
from mytime import MyTime


def start_stopwatch():
    thread_stopwatch.start()


def stop_stopwatch():
    thread_stopwatch.terminate()


def reset_stopwatch():
    main_window.window().ui.lbl_stopwatch.setText("0:0:0")
    thread_stopwatch.reset()


def get_counter(time_sw):
    print(f"{time_sw.hour}:{time_sw.minutes}:{time_sw.second}")
    main_window.window().ui.lbl_stopwatch.setText(f"{time_sw.hour}:{time_sw.minutes}:{time_sw.second}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_start_stopwatch.clicked.connect(start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(reset_stopwatch)


class MyThread(QThread):
    signal_counter = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time_sw = MyTime(0, 0, 0)

    def run(self):
        while True:
            self.time_sw.plus()
            self.signal_counter.emit(self.time_sw)
            time.sleep(1)

    def reset(self):
        self.time_sw.second = 0
        self.time_sw.minutes = 0
        self.time_sw.hour = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.window().ui.lbl_stopwatch.setText("0:0:0")
    thread_stopwatch = MyThread()
    thread_stopwatch.signal_counter.connect(get_counter)
    app.exec()
