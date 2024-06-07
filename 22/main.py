import sys
from functools import partial
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *
from mainwindow import Ui_MainWindow
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
        new_date = self.ui.tb_date.text()
        new_description = self.ui.tb_description.toPlainText()
        is_important = self.ui.ch_important.checkState().value
        feedback = self.database.add_task(new_title, new_date, new_description, is_important)
        if feedback:
            self.read_database()
            self.ui.tb_title.setText("")
            self.ui.tb_date.setText("")
            self.ui.tb_description.setText("")
            self.ui.ch_important.setChecked(False)
        else:
            msg = QMessageBox()
            msg.setText("Error while adding task")
            msg.exec()

    def read_database(self):
        # clean layout
        layout = self.ui.gl_tasks
        for i in (range(layout.count())):
            item = layout.itemAt(i)
            widget = item.widget()
            widget.deleteLater()
        # fill layout
        tasks = self.database.get_tasks()
        for i in range(0, len(tasks)):
            new_lbl_1 = QLabel()
            new_lbl_1.setText(tasks[i][1])
            new_lbl_1.setFont("Adobe Arabic")
            new_lbl_1.setStyleSheet("font-weight:bold; font-size:22px; color:rgb(255, 255, 255)")
            new_lbl_1.mousePressEvent = partial(self.show_description, tasks, i)
            # detect and color important tasks
            if tasks[i][4] == 2:
                new_lbl_1.setStyleSheet("font-weight:bold; font-size:20px; color:rgb(255, 85, 111)")
            new_chb = QCheckBox()
            # detect and show done tasks
            if tasks[i][5] == 2:
                new_chb.setChecked(True)
            if new_chb.checkState().value == 0:
                imp_value = 2
            else:
                imp_value = 0
            new_chb.clicked.connect(partial(self.check_task, tasks[i][0], imp_value))
            new_btn = QPushButton()
            new_btn.setIcon(QIcon("bin.png"))
            new_btn.setMaximumHeight(25)
            new_btn.setMaximumWidth(25)
            new_btn.clicked.connect(partial(self.del_task, tasks[i][0]))
            # add elements to layout
            self.ui.gl_tasks.addWidget(new_chb, i, 3)
            self.ui.gl_tasks.addWidget(new_lbl_1, i, 2)
            self.ui.gl_tasks.addWidget(new_btn, i, 4)

    def del_task(self, index):
        msg = QMessageBox()
        ans = msg.question(self,'Delete Task', "Are you sure you want to delete the task?")
        if ans == 16384:
            self.database.delete_task(index)
            self.read_database()

    def check_task(self, index, value):
        self.database.update_task(index, value)
        self.read_database()

    def show_description(self, tasks, i, etc):
        new_lbl_2 = QLabel()
        new_lbl_3 = QLabel()
        new_lbl_2.setText(tasks[i][2])
        new_lbl_3.setText(tasks[i][3])
        new_lbl_2.setFont("Adobe Arabic")
        new_lbl_2.setStyleSheet("font-weight:bold; font-size:20px; color:rgb(255, 255, 255)")
        new_lbl_3.setFont("Adobe Arabic")
        if tasks[i][4] == 2:
            new_lbl_2.setStyleSheet("font-weight:bold; font-size:20px; color:rgb(255, 85, 111)")
        self.ui.gl_tasks.addWidget(new_lbl_2, i, 1)
        self.ui.gl_tasks.addWidget(new_lbl_3, i, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
