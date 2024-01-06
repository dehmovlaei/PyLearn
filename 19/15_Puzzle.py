import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

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
                index += 1

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()