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

        self.ui.btn_2.clicked.connect(partial(self.line_break_remove))
        self.ui.btn_1.clicked.connect(partial(self.try_again))

    def line_break_remove(self):
        py_string = ""
        self.ui.textEdit_1.setText(py_string)

    def try_again(self):
        self.ui.textEdit_1.setText("")

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()