import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.buttons = [[self.ui.btn_01, self.ui.btn_02, self.ui.btn_03, self.ui.btn_04],
                        [self.ui.btn_05, self.ui.btn_06, self.ui.btn_07, self.ui.btn_08],
                        [self.ui.btn_09, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
                        [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16]]

        my_list = random.sample(range(1,17), 16)
        index = 0
        for i in range(4):
            for j in range(4):
                self.buttons[i][j].setText(str(my_list[index]))
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))
                if my_list[index] == 16:
                    self.buttons[i][j].setVisible(False)
                    self.empty_i = i
                    self.empty_j = j
                index += 1

    def play(self,i, j):
        if i == self.empty_i and abs(j - self.empty_j) == 1 or j == self.empty_j and abs(i - self.empty_i) == 1:
            self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText("16")

            self.buttons[self.empty_i][self.empty_j].setVisible(True)
            self.buttons[i][j].setVisible(False)
            self.empty_i = i
            self.empty_j = j
        if self.check_win() == True:
            msgBox = QMessageBox()
            msgBox.setText("YOU WIN ❤️")
            msgBox.exec()

    def check_win(self):
        index = 1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                index += 1
        return True

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()