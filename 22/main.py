import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from mainwindow import  Ui_MainWindow
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.database = Database()
        tasks = self.database.get_tasks()
        print(tasks)

        for i in range(0, len(tasks)):
            new_chb = QCheckBox()
            new_lbl = QLabel()
            new_lbl_2 = QLabel()
            new_lbl.setText(tasks[i][1])
            new_lbl_2.setText(tasks[i][2])
            self.ui.gl_tasks.addWidget(new_chb, i, 2)
            self.ui.gl_tasks.addWidget(new_lbl, i, 1)
            self.ui.gl_tasks.addWidget(new_lbl_2, i, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()