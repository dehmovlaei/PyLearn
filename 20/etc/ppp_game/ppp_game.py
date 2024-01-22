import sys
import random
import string

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QPushButton
from ui_mainwindow import Ui_MainWindow
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.user_side, self.cpu1_side, self.cpu2_side = 2, 2, 2
        self.user_point, self.cpu1_point, self.cpu2_point, self.draw = 0, 0, 0, 0

        self.ui.btn_8.clicked.connect(partial(self.play, 0))
        self.ui.btn_9.clicked.connect(partial(self.play, 1))

    def play(self, i):
        self.user_side = i
        if self.user_side == 0:
            self.ui.btn_2.setIcon(QIcon('back.png'))
            self.cpu_play()
        elif self.user_side == 1:
            self.ui.btn_2.setIcon(QIcon('front.png'))
            self.cpu_play()

    def cpu_play(self):
        self.cpu1_side = random.randint(0,1)
        if self.cpu1_side == 0:
            self.ui.btn_1.setIcon(QIcon('back.png'))
        elif self.cpu1_side == 1:
            self.ui.btn_1.setIcon(QIcon('front.png'))

        self.cpu2_side = random.randint(0, 1)
        if self.cpu2_side == 0:
            self.ui.btn_3.setIcon(QIcon('back.png'))
        elif self.cpu2_side == 1:
            self.ui.btn_3.setIcon(QIcon('front.png'))

        if self.cpu1_side == self.cpu2_side == self.user_side:
            self.draw += 1
            self.ui.btn_7.setText(f"DRAW\n{self.draw}")
        elif self.user_side == self.cpu1_side != self.cpu2_side:
            self.cpu2_point += 1
            self.ui.btn_6.setText(f"CPU II\n{self.cpu2_point}")
        elif self.user_side == self.cpu2_side != self.cpu1_side:
            self.cpu1_point += 1
            self.ui.btn_4.setText(f"CPU I\n{self.cpu1_point}")
        else:
            self.user_point += 1
            self.ui.btn_5.setText(f"YOU\n{self.user_point}")

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()