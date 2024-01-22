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
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(363, 422)
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
        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(111)
        sizePolicy1.setVerticalStretch(111)
        sizePolicy1.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy1)
        self.btn_9.setMinimumSize(QSize(111, 111))
        self.btn_9.setMaximumSize(QSize(333, 333))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(72)
        font.setBold(True)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(31, 53, 64)\n"
"}")
        icon = QIcon()
        icon.addFile(u"front.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_9.setIcon(icon)
        self.btn_9.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btn_9, 2, 2, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)
        self.btn_2.setMinimumSize(QSize(111, 111))
        self.btn_2.setMaximumSize(QSize(333, 333))
        palette1 = QPalette()
        brush2 = QBrush(QColor(31, 53, 64, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        brush3 = QBrush(QColor(49, 196, 190, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_2.setPalette(palette1)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")
        self.btn_2.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy1.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy1)
        self.btn_7.setMinimumSize(QSize(111, 111))
        self.btn_7.setMaximumSize(QSize(333, 333))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.btn_7.setFont(font1)
        self.btn_7.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(49, 196, 190)\n"
"}")

        self.gridLayout.addWidget(self.btn_7, 2, 1, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy1.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy1)
        self.btn_5.setMinimumSize(QSize(111, 111))
        self.btn_5.setMaximumSize(QSize(333, 333))
        self.btn_5.setFont(font1)
        self.btn_5.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(255, 85, 127)\n"
"}")

        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_1.setMinimumSize(QSize(111, 111))
        self.btn_1.setMaximumSize(QSize(333, 333))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_1.setPalette(palette2)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")
        self.btn_1.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)
        self.btn_3.setMinimumSize(QSize(111, 111))
        self.btn_3.setMaximumSize(QSize(333, 333))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_3.setPalette(palette3)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")
        self.btn_3.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btn_3, 0, 2, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)
        self.btn_4.setMinimumSize(QSize(111, 111))
        self.btn_4.setMaximumSize(QSize(333, 333))
        self.btn_4.setFont(font1)
        self.btn_4.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(242, 178, 55)\n"
"}")

        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy1.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy1)
        self.btn_6.setMinimumSize(QSize(111, 111))
        self.btn_6.setMaximumSize(QSize(333, 333))
        self.btn_6.setFont(font1)
        self.btn_6.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(242, 178, 55)\n"
"}")

        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy1.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy1)
        self.btn_8.setMinimumSize(QSize(111, 111))
        self.btn_8.setMaximumSize(QSize(333, 333))
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(31, 53, 64)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_8.setIcon(icon1)
        self.btn_8.setIconSize(QSize(100, 100))

        self.gridLayout.addWidget(self.btn_8, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"triple P", None))
        self.btn_9.setText("")
        self.btn_2.setText("")
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"DRAW", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"YOU", None))
        self.btn_1.setText("")
        self.btn_3.setText("")
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"CPU I", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"CPU II", None))
        self.btn_8.setText("")
    # retranslateUi

