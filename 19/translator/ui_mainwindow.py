# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(349, 713)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(242, 178, 55, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(25, 42, 50, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.textEdit_1 = QTextEdit(self.centralwidget)
        self.textEdit_1.setObjectName(u"textEdit_1")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        font.setBold(True)
        self.textEdit_1.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.textEdit_1)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.textEdit_2.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.textEdit_2)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(111)
        sizePolicy1.setVerticalStretch(111)
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_1.setMinimumSize(QSize(111, 111))
        self.btn_1.setMaximumSize(QSize(333, 333))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.btn_1.setFont(font2)
        self.btn_1.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(49, 196, 190)\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.btn_1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)
        self.btn_2.setMinimumSize(QSize(111, 111))
        self.btn_2.setMaximumSize(QSize(333, 333))
        self.btn_2.setFont(font2)
        self.btn_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(242, 178, 55)\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.btn_2)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)
        self.btn_4.setMinimumSize(QSize(111, 111))
        self.btn_4.setMaximumSize(QSize(333, 333))
        self.btn_4.setFont(font2)
        self.btn_4.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(49, 196, 190)\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.btn_4)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)
        self.btn_3.setMinimumSize(QSize(111, 111))
        self.btn_3.setMaximumSize(QSize(333, 333))
        self.btn_3.setFont(font2)
        self.btn_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(242, 178, 55)\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.btn_3)

        self.rbtn_2 = QRadioButton(self.centralwidget)
        self.rbtn_2.setObjectName(u"rbtn_2")
        palette1 = QPalette()
        brush2 = QBrush(QColor(220, 162, 50, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        self.rbtn_2.setPalette(palette1)
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.rbtn_2.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.rbtn_2)

        self.rbtn_1 = QRadioButton(self.centralwidget)
        self.rbtn_1.setObjectName(u"rbtn_1")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        self.rbtn_1.setPalette(palette2)
        self.rbtn_1.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.rbtn_1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"dehmovlaei", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"Add Word", None))
        self.rbtn_2.setText(QCoreApplication.translate("MainWindow", u"Fa > En", None))
        self.rbtn_1.setText(QCoreApplication.translate("MainWindow", u"En > Fa", None))
    # retranslateUi

