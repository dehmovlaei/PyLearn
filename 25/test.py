from PySide6.QtGui import QIcon
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QFontDatabase
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Create a QTimeEdit widget and set the initial time
        initial_time_str = "12:30:00"  # Replace with your desired time string
        initial_time = QTime.fromString(initial_time_str, 'HH:mm:ss')
        self.time_edit = QTimeEdit()
        self.time_edit.setTime(initial_time)

        layout.addWidget(self.time_edit)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()