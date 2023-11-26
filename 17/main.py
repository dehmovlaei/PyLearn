from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def sum():
    global a
    a = int(my_window.lineEdit.text())
    my_window.lineEdit.setText('')

def result():
    b = int(my_window.lineEdit.text())
    c = a + b
    my_window.lineEdit.setText(str(c))


loader = QUiLoader()
app = QApplication([])
my_window = loader.load('mainwindow.ui')
my_window.show()

my_window.btnSum.clicked.connect(sum)
my_window.btnEqual.clicked.connect(result)

app.exec()
