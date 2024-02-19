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
        self.read_database()
        self.ui.btn_new_task.clicked.connect(self.new_task)

    def new_task(self):
        new_title = self.ui.tb_title.text()
        new_description = self.ui.tb_description.toPlainText()
        feedback = self.database.add_task(new_title, new_description)
        if feedback == True:
            self.read_database()
            self.ui.tb_title.setText("")
            self.ui.tb_description.setText("")
        else:
            msg = QMessageBox()
            msg.setText("Error while adding task")
            msg.exec()

    def read_database(self):
        tasks = self.database.get_tasks()
        for i in range(0, len(tasks)):
            new_chb = QCheckBox()
            new_lbl = QLabel()
            new_lbl_2 = QLabel()
            new_lbl.setText(tasks[i][1])
            new_lbl_2.setText(tasks[i][2])
            new_btn =QPushButton()
            new_btn.setText("✖️")
            new_btn.resize(50, 50)

            if tasks[i][3] > 0:
                new_lbl.setStyleSheet("font-weight:bold; font-size:16px; color:rgb(255, 0, 0)")
                new_lbl_2.setStyleSheet("font-weight:bold; font-size:16px; color:rgb(255, 0, 0)")
            if tasks[i][5] == 1:
                new_chb.toggle()

            self.ui.gl_tasks.addWidget(new_chb, i, 2)
            self.ui.gl_tasks.addWidget(new_lbl, i, 1)
            self.ui.gl_tasks.addWidget(new_lbl_2, i, 0)
            self.ui.gl_tasks.addWidget(new_btn, i, 3)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()