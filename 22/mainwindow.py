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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(445, 281)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(85, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        brush3 = QBrush(QColor(25, 42, 50, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.label_8.setPalette(palette1)

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.gridLayout.addLayout(self.gl_tasks, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.tb_title = QLineEdit(self.centralwidget)
        self.tb_title.setObjectName(u"tb_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tb_title.sizePolicy().hasHeightForWidth())
        self.tb_title.setSizePolicy(sizePolicy2)
        self.tb_title.setMinimumSize(QSize(0, 0))
        self.tb_title.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.tb_title.setFont(font1)
        self.tb_title.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.tb_title)

        self.tb_description = QTextEdit(self.centralwidget)
        self.tb_description.setObjectName(u"tb_description")
        self.tb_description.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.tb_description)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        sizePolicy2.setHeightForWidth(self.btn_new_task.sizePolicy().hasHeightForWidth())
        self.btn_new_task.setSizePolicy(sizePolicy2)
        self.btn_new_task.setMinimumSize(QSize(85, 45))
        self.btn_new_task.setMaximumSize(QSize(85, 45))
        palette2 = QPalette()
        brush4 = QBrush(QColor(242, 178, 55, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        brush5 = QBrush(QColor(49, 196, 190, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.btn_new_task.setPalette(palette2)
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.btn_new_task.setFont(font2)
        self.btn_new_task.setMouseTracking(False)
        self.btn_new_task.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(242, 178, 55)\n"
"}\n"
"QPushButton{\n"
"border-radius: 15px\n"
"}")

        self.verticalLayout.addWidget(self.btn_new_task)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"dehmovlaei", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Type Here", None))
        self.btn_new_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

