import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from mainwindow import Ui_MainWindow
from timerthread import TimerThread
from stopwatchthread import StopWatchThread


@Slot()
def start_stopwatch():
    thread_stopwatch.start()

@Slot()
def stop_stopwatch():
    thread_stopwatch.terminate()

@Slot()
def reset_stopwatch():
    main_window.window().ui.lbl_stopwatch.setText("0:0:0")
    thread_stopwatch.reset()

@Slot()
def show_time_stopwatch(time):
    main_window.window().ui.lbl_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")


@Slot()
def start_timer():
    thread_timer.time.hour = int(main_window.ui.tb_hour_timer.text())
    thread_timer.time.minute = int(main_window.ui.tb_minute_timer.text())
    thread_timer.time.second = int(main_window.ui.tb_second_timer.text())
    thread_timer.start()

@Slot()
def stop_timer():
    thread_timer.terminate()

@Slot()
def reset_timer():
    main_window.ui.tb_hour_timer.setText("00")
    main_window.ui.tb_minute_timer.setText("15")
    main_window.ui.tb_second_timer.setText("30")
    thread_timer.time.time_up = False
    thread_timer.terminate()
    thread_stopwatch.reset()


@Slot()
def show_time_timer(time):
    main_window.window().ui.tb_hour_timer.setText(str(time.hour))
    main_window.window().ui.tb_minute_timer.setText(str(time.minute))
    main_window.window().ui.tb_second_timer.setText(str(time.second))
    if thread_timer.time.time_up:
        notification = QMessageBox()
        notification.setWindowTitle("Xx0xX")
        notification.setText("Time UP")
        notification.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_start_stopwatch.clicked.connect(start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(reset_stopwatch)
        self.ui.btn_start_timer.clicked.connect(start_timer)
        self.ui.btn_stop_timer.clicked.connect(stop_timer)
        self.ui.btn_reset_timer.clicked.connect(reset_timer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.window().ui.lbl_stopwatch.setText("0:0:0")
    thread_stopwatch = StopWatchThread()
    thread_timer = TimerThread()
    thread_stopwatch.signal_counter.connect(show_time_stopwatch)
    thread_timer.signal_counter.connect(show_time_timer)
    app.exec()
