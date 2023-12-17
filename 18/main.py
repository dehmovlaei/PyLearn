import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

app = QApplication(sys.argv)

loader = QUiLoader()
ui = loader.load("mainwindow.ui")


app.exec()