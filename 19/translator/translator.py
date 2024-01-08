import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.wordsBank = []
        self.readFromFile()

        self.ui.btn_1.clicked.connect(partial(self.try_again))
        self.ui.btn_2.clicked.connect(partial(self.translate))
        self.ui.btn_3.clicked.connect(partial(self.add))
        self.ui.btn_4.clicked.connect(partial(self.writeToDataBase))


    def translate(self):
        if self.ui.rbtn_1.isChecked():
            self.translateEn2Fa()
        elif self.ui.rbtn_2.isChecked():
            self.translateFa2En()

    def try_again(self):
        msgBox = QMessageBox()
        msgBox.setText("pay attention:\nenter english word on first text edit box and\nenter fingilish on second one")
        msgBox.exec()
        self.ui.textEdit_1.setText("")
        self.ui.textEdit_2.setText("")

    def readFromFile(self):
        if os.path.exists('D:/Python/Assignments/19/translator/translate.txt'):
            f = open('D:/Python/Assignments/19/translator/translate.txt', 'r')
            tmp = f.read().split('\n')
            for i in range(0, len(tmp) - 1, 2):
                myDic = {'en': tmp[i], 'fa': tmp[i + 1]}
                self.wordsBank.append(myDic)
            f.close
        else:
            print('file not exist:')
            exit(0)

    def writeToDataBase(self):
        f = open('D:/Python/Assignments/19/translator/translate.txt', 'w')
        for word in self.wordsBank:
            f.write(word['en'] + '\n' + word['fa'] + '\n')
        f.close
        main_window.close()

    def translateEn2Fa(self):
        userText = self.ui.textEdit_1.toPlainText()
        userWords = userText.split(' ')
        output = ''
        for userWord in userWords:
            for word in self.wordsBank:
                if userWord == word['en']:
                    output = output + (word['fa']) + ' '
                    break
            else:
                output = output + userWord + ' '
        self.ui.textEdit_2.setText(output)

    def translateFa2En(self):
        userText = self.ui.textEdit_1.toPlainText()
        userWords = userText.split(' ')
        output = ''
        for userWord in userWords:
            for word in self.wordsBank:
                if userWord == word['fa']:
                    output = output + (word['en']) + ' '
                    break
            else:
                output = output + userWord + ' '
        self.ui.textEdit_2.setText(output)

    def add(self):
        en = self.ui.textEdit_1.toPlainText()
        fa = self.ui.textEdit_2.toPlainText()
        newWord = {'en': en, 'fa': fa}
        self.wordsBank.append(newWord)
        msgBox = QMessageBox()
        msgBox.setText("new word added successfully")
        msgBox.exec()
        self.ui.textEdit_1.setText("")
        self.ui.textEdit_2.setText("")

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()