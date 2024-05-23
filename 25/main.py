import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from mainwindow import Ui_MainWindow


def start_stopwatch():
    thread_stopwatch.start()


def stop_stopwatch():
    thread_stopwatch.terminate()


def reset_stopwatch():
    main_window.window().ui.lbl_stopwatch.setText(str(0))
    thread_stopwatch.rest()


def get_counter(second):
    print(second)
    main_window.window().ui.lbl_stopwatch.setText(str(second))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_start_stopwatch.clicked.connect(start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(reset_stopwatch)


class MyThread(QThread):
    signal_counter = Signal(int)

    def __init__(self):
        super().__init__()
        self.second = 0

    def run(self):
        while True:
            self.second += 1
            self.signal_counter.emit(self.second)
            time.sleep(1)

    def rest(self):
        self.second = 0


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
thread_stopwatch = MyThread()
thread_stopwatch.signal_counter.connect(get_counter)

app.exec()
