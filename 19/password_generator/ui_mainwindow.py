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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(537, 206)
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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit_1 = QTextEdit(self.centralwidget)
        self.textEdit_1.setObjectName(u"textEdit_1")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(18)
        font.setBold(True)
        self.textEdit_1.setFont(font)

        self.gridLayout.addWidget(self.textEdit_1, 0, 0, 1, 2)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(111)
        sizePolicy1.setVerticalStretch(111)
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_1.setMinimumSize(QSize(111, 111))
        self.btn_1.setMaximumSize(QSize(333, 333))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.btn_1.setFont(font1)
        self.btn_1.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(49, 196, 190)\n"
"}")

        self.gridLayout.addWidget(self.btn_1, 1, 0, 4, 1)

        self.rbtn_2 = QRadioButton(self.centralwidget)
        self.rbtn_2.setObjectName(u"rbtn_2")

        self.gridLayout.addWidget(self.rbtn_2, 3, 1, 1, 1)

        self.rbtn_1 = QRadioButton(self.centralwidget)
        self.rbtn_1.setObjectName(u"rbtn_1")

        self.gridLayout.addWidget(self.rbtn_1, 2, 1, 1, 1)

        self.rbtn_3 = QRadioButton(self.centralwidget)
        self.rbtn_3.setObjectName(u"rbtn_3")

        self.gridLayout.addWidget(self.rbtn_3, 4, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"dehmovlaei", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.rbtn_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.rbtn_1.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.rbtn_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
    # retranslateUi

