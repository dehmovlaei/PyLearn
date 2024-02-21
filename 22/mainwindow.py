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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(303, 407)
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
        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.gridLayout.addLayout(self.gl_tasks, 1, 0, 1, 1)

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
        font1 = QFont()
        font1.setFamilies([u"Adobe Arabic"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.label_9.setPalette(palette2)
        self.label_9.setFont(font1)
        self.label_9.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.label_9)

        self.tb_title = QLineEdit(self.centralwidget)
        self.tb_title.setObjectName(u"tb_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tb_title.sizePolicy().hasHeightForWidth())
        self.tb_title.setSizePolicy(sizePolicy2)
        self.tb_title.setMinimumSize(QSize(45, 0))
        self.tb_title.setMaximumSize(QSize(200, 45))
        self.tb_title.setFont(font1)
        self.tb_title.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.tb_title)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.label_10.setPalette(palette3)
        self.label_10.setFont(font1)
        self.label_10.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.label_10)

        self.tb_date = QLineEdit(self.centralwidget)
        self.tb_date.setObjectName(u"tb_date")
        sizePolicy2.setHeightForWidth(self.tb_date.sizePolicy().hasHeightForWidth())
        self.tb_date.setSizePolicy(sizePolicy2)
        self.tb_date.setMinimumSize(QSize(45, 0))
        self.tb_date.setMaximumSize(QSize(200, 45))
        self.tb_date.setFont(font1)
        self.tb_date.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.tb_date)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.label_11.setPalette(palette4)
        self.label_11.setFont(font1)
        self.label_11.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.label_11)

        self.tb_description = QTextEdit(self.centralwidget)
        self.tb_description.setObjectName(u"tb_description")
        self.tb_description.setMinimumSize(QSize(0, 0))
        self.tb_description.setMaximumSize(QSize(250, 100))
        self.tb_description.setFont(font1)
        self.tb_description.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.tb_description)

        self.ch_important = QCheckBox(self.centralwidget)
        self.ch_important.setObjectName(u"ch_important")
        self.ch_important.setFont(font1)
        self.ch_important.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.ch_important)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        self.btn_new_task.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btn_new_task.sizePolicy().hasHeightForWidth())
        self.btn_new_task.setSizePolicy(sizePolicy2)
        self.btn_new_task.setMinimumSize(QSize(55, 55))
        self.btn_new_task.setMaximumSize(QSize(55, 55))
        palette5 = QPalette()
        brush4 = QBrush(QColor(49, 196, 190, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.btn_new_task.setPalette(palette5)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(48)
        font2.setBold(True)
        self.btn_new_task.setFont(font2)
        self.btn_new_task.setMouseTracking(False)
        self.btn_new_task.setLayoutDirection(Qt.RightToLeft)
        self.btn_new_task.setAutoFillBackground(False)
        self.btn_new_task.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 196, 190)\n"
"}\n"
"QPushButton{\n"
"border-radius: 15px\n"
"}")
        self.btn_new_task.setText(u"+")
        self.btn_new_task.setIconSize(QSize(16, 16))
        self.btn_new_task.setAutoDefault(True)
        self.btn_new_task.setFlat(False)

        self.verticalLayout.addWidget(self.btn_new_task)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_new_task.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"dehmovlaei", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0644\u06cc\u0633\u062a \u06a9\u0627\u0631\u0647\u0627", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0646\u0648\u0627\u0646", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u0648 \u0633\u0627\u0639\u062a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0631\u062d", None))
        self.ch_important.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u06cc\u06cc\u0646 \u0627\u0648\u0644\u0648\u06cc\u062a \u0628\u0627\u0644\u0627", None))
    # retranslateUi

