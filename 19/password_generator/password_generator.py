import sys
import random
import string
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.normal = string.ascii_lowercase + string.digits
        self.strong = string.ascii_letters + string.digits
        self.expert = string.ascii_letters + string.digits + string.punctuation

        self.ui.btn_1.clicked.connect(partial(self.generate))

    def generate(self):
        self.ui.textEdit_1.setText("")
        if self.ui.rbtn_1.isChecked():
            pwd = ''.join(random.choice(self.normal) for i in range(6))
        elif self.ui.rbtn_2.isChecked():
            pwd = ''.join(random.choice(self.strong) for i in range(8))
        elif self.ui.rbtn_3.isChecked():
            pwd = ''.join(random.choice(self.expert) for i in range(12))

        self.ui.textEdit_1.setText(pwd)

    def try_again(self):
        self.ui.textEdit_1.setText("")



app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()