from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import  math

def clear():
    my_window.lineEdit.setText('')

def print_result(c):
    my_window.lineEdit.setText(str(c))
def define_opr(op):
    global a, operator
    a = float(my_window.lineEdit.text())
    operator = op
    clear()

def result():
    b = my_window.lineEdit.text()
    if operator == '+':
        c = a + float(b)
    elif operator == '-':
        c = a - float(b)
    elif operator == '*':
        c = a * float(b)
    elif operator == '/':
        c = a / float(b)
    # elif operator == 'sqrt':
    #     c = math.sqrt(a)
    print_result(c)
def line_string(input):
    if input == '':
        clear()
    else:
        new_equation = my_window.lineEdit.text() + input
        my_window.lineEdit.setText(new_equation)


loader = QUiLoader()
app = QApplication([])
my_window = loader.load('mainwindow.ui')
my_window.show()

my_window.btnAc.clicked.connect(clear)
my_window.btnEqual.clicked.connect(result)
my_window.btnSqrt.clicked.connect(lambda: print_result(math.sqrt(float(my_window.lineEdit.text()))))
my_window.btnTan.clicked.connect(lambda: print_result(math.tan(float(my_window.lineEdit.text()))))
my_window.btnSin.clicked.connect(lambda: print_result(math.sin(float(my_window.lineEdit.text()))))
my_window.btnCos.clicked.connect(lambda: print_result(math.cos(float(my_window.lineEdit.text()))))
my_window.btnLog.clicked.connect(lambda: print_result(math.log(float(my_window.lineEdit.text()))))
my_window.btnSum.clicked.connect(lambda: define_opr('+'))
my_window.btnSub.clicked.connect(lambda: define_opr('-'))
my_window.btnMul.clicked.connect(lambda: define_opr('*'))
my_window.btnDiv.clicked.connect(lambda: define_opr('/'))
my_window.btn1.clicked.connect(lambda: line_string('1'))
my_window.btn2.clicked.connect(lambda: line_string('2'))
my_window.btn3.clicked.connect(lambda: line_string('3'))
my_window.btn4.clicked.connect(lambda: line_string('4'))
my_window.btn5.clicked.connect(lambda: line_string('5'))
my_window.btn6.clicked.connect(lambda: line_string('6'))
my_window.btn7.clicked.connect(lambda: line_string('7'))
my_window.btn8.clicked.connect(lambda: line_string('8'))
my_window.btn9.clicked.connect(lambda: line_string('9'))
my_window.btn0.clicked.connect(lambda: line_string('0'))
my_window.btnDot.clicked.connect(lambda: line_string('.'))
my_window.btnRND.clicked.connect(lambda: print_result(round((float(my_window.lineEdit.text())),3)))

app.exec()
