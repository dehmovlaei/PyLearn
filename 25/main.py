import sys
from functools import partial
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QFontDatabase
from mainwindow import Ui_MainWindow
from database import Database
from timerthread import TimerThread
from stopwatchthread import StopWatchThread
from worldclockthread import WorldClockThread


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

@Slot()
def show_world_clock(time):
    main_window.window().ui.lbl_clock_iran.setText(time.current_time[0])
    main_window.window().ui.lbl_clock_germany.setText(time.current_time[1])
    main_window.window().ui.lbl_clock_usa.setText(time.current_time[2])


class MainWindow(QMainWindow):
    def __init__(self):
        self.fontId = QFontDatabase.addApplicationFont('../25/res/fs-sevegment.ttf')
        self.font_family = QFontDatabase.applicationFontFamilies(self.fontId)[0]
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.database = Database()
        self.read_database()
        self.ui.lbl_stopwatch.setStyleSheet(f'font-family: {self.font_family};color: rgb(255, 0, 127);')
        self.ui.tb_hour_timer.setStyleSheet(f'font-family: {self.font_family};color: rgb(255, 0, 127);'
                                            f'background-color: rgb(0, 0, 0);')
        self.ui.tb_minute_timer.setStyleSheet(f'font-family: {self.font_family};color: rgb(255, 0, 127);'
                                              f'background-color: rgb(0, 0, 0);')
        self.ui.tb_second_timer.setStyleSheet(f'font-family: {self.font_family};color: rgb(255, 0, 127);'
                                              f'background-color: rgb(0, 0, 0);')
        self.ui.lbl_clock_iran.setStyleSheet(f'font-family: {self.font_family};color: rgb(255, 0, 127);')
        self.ui.lbl_clock_germany.setStyleSheet(f'font-family: {self.font_family};color: rgb(255, 0, 127);')
        self.ui.lbl_clock_usa.setStyleSheet(f'font-family: {self.font_family};color: rgb(255, 0, 127);')
        self.ui.btn_start_stopwatch.clicked.connect(start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(reset_stopwatch)
        self.ui.btn_start_timer.clicked.connect(start_timer)
        self.ui.btn_stop_timer.clicked.connect(stop_timer)
        self.ui.btn_reset_timer.clicked.connect(reset_timer)

    def read_database(self):
        # clean layout
        layout = self.ui.gl_alarms
        for i in (range(layout.count())):
            item = layout.itemAt(i)
            widget = item.widget()
            widget.deleteLater()
        # fill layout
        alarms_list = self.database.get_alarms()
        for i in range(0, len(alarms_list)):
            txt_1 = QTextEdit()
            txt_1.setText(alarms_list[i][1])
            initial_time_str = alarms_list[i][2]
            initial_time = QTime.fromString(initial_time_str, 'HH:mm:ss')
            tme_1 = QTimeEdit()
            tme_1.setTime(initial_time)
            tme_1.setStyleSheet(f'font-family:digital-7; 'f' font-size: 30px; color: rgb(255, 0, 127);')
            txt_1.setStyleSheet(f'font-family:digital-7; 'f' font-size: 30px; color: rgb(255, 255, 255);')
            txt_1.setMaximumWidth(252)
            txt_1.setMaximumHeight(33)
            btn_1 = QPushButton()
            btn_1.setIcon(QIcon("../25/res/bin.png"))
            btn_1.setIconSize(QSize(32, 32))
            btn_2 = QPushButton()
            btn_2.setIcon(QIcon("../25/res/pen.png"))
            btn_2.setIconSize(QSize(32, 32))
            btn_1.clicked.connect(partial(self.del_alarm, alarms_list[i][0]))
            btn_2.clicked.connect(partial(self.edit_alarm, txt_1.toPlainText(), tme_1.text(), alarms_list[i][0]))
            self.ui.gl_alarms.addWidget(txt_1, i, 1)
            self.ui.gl_alarms.addWidget(tme_1, i, 2)
            self.ui.gl_alarms.addWidget(btn_1, i, 3)
            self.ui.gl_alarms.addWidget(btn_2, i, 4)

    def del_alarm(self, alarm_id):
        msg = QMessageBox()
        ans = msg.question(self,'Delete Alarm', "Are you sure you want to delete this Alarm?")
        if ans == 16384:
            self.database.delete_alarm(alarm_id)
            self.read_database()

    def edit_alarm(self, new_name, new_time, alarm_id):
        self.database.update_alarm(new_name, new_time, alarm_id)
        self.read_database()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    thread_stopwatch = StopWatchThread()
    thread_timer = TimerThread()
    thread_world_clock = WorldClockThread()
    thread_world_clock.start()
    thread_stopwatch.signal_counter.connect(show_time_stopwatch)
    thread_timer.signal_counter.connect(show_time_timer)
    thread_world_clock.signal_counter.connect(show_world_clock)
    app.exec()
