# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(479, 352)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(43, 45, 48, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(64, 67, 72, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(53, 56, 60, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(21, 22, 24, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 30, 32, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush8 = QBrush(QColor(255, 255, 255, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush9 = QBrush(QColor(21, 22, 24, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        brush10 = QBrush(QColor(30, 32, 34, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush10)
        MainWindow.setPalette(palette)
        self.menu_new = QAction(MainWindow)
        self.menu_new.setObjectName(u"menu_new")
        self.menu_open = QAction(MainWindow)
        self.menu_open.setObjectName(u"menu_open")
        self.menu_about = QAction(MainWindow)
        self.menu_about.setObjectName(u"menu_about")
        self.menu_exit = QAction(MainWindow)
        self.menu_exit.setObjectName(u"menu_exit")
        self.menu_solve = QAction(MainWindow)
        self.menu_solve.setObjectName(u"menu_solve")
        self.menu_help = QAction(MainWindow)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_theme = QAction(MainWindow)
        self.menu_theme.setObjectName(u"menu_theme")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(5, 5, 469, 338))
        self.tabWidget.setBaseSize(QSize(0, 0))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush11 = QBrush(QColor(30, 31, 34, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush11)
        brush12 = QBrush(QColor(45, 47, 51, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush12)
        brush13 = QBrush(QColor(37, 39, 42, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        brush14 = QBrush(QColor(15, 16, 17, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush14)
        brush15 = QBrush(QColor(20, 21, 23, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush16 = QBrush(QColor(15, 15, 17, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush16)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush16)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush17 = QBrush(QColor(15, 16, 17, 127))
        brush17.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Accent, brush4)
        self.tabWidget.setPalette(palette1)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setToolTipDuration(3)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        palette2 = QPalette()
        brush18 = QBrush(QColor(36, 36, 35, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        brush19 = QBrush(QColor(47, 47, 46, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush19)
        brush20 = QBrush(QColor(70, 70, 69, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush20)
        brush21 = QBrush(QColor(58, 58, 57, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush21)
        brush22 = QBrush(QColor(23, 23, 23, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush22)
        brush23 = QBrush(QColor(31, 31, 31, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush23)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        brush24 = QBrush(QColor(51, 51, 50, 255))
        brush24.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush24)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush19)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush22)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush19)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush20)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush21)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush22)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush23)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush24)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush19)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush22)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush22)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush20)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush21)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush22)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush23)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush22)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush22)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush19)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush19)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush25 = QBrush(QColor(23, 23, 23, 127))
        brush25.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush25)
#endif
        brush26 = QBrush(QColor(33, 33, 32, 255))
        brush26.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.Accent, brush26)
        self.tab_4.setPalette(palette2)
        self.tab_4.setAutoFillBackground(True)
        self.lbl_stopwatch = QLabel(self.tab_4)
        self.lbl_stopwatch.setObjectName(u"lbl_stopwatch")
        self.lbl_stopwatch.setGeometry(QRect(160, 30, 141, 81))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush27 = QBrush(QColor(25, 42, 50, 255))
        brush27.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush27)
        brush28 = QBrush(QColor(37, 63, 75, 255))
        brush28.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush28)
        brush29 = QBrush(QColor(31, 52, 62, 255))
        brush29.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush29)
        brush30 = QBrush(QColor(12, 21, 25, 255))
        brush30.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush30)
        brush31 = QBrush(QColor(17, 28, 33, 255))
        brush31.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush31)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush27)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush30)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette3.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush27)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush28)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush29)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush30)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush31)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush27)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush30)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush30)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush27)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush28)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush29)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush30)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush31)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush30)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush30)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush27)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush27)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush27)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush32 = QBrush(QColor(12, 21, 25, 127))
        brush32.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush32)
#endif
        brush33 = QBrush(QColor(18, 30, 35, 255))
        brush33.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.Accent, brush33)
        self.lbl_stopwatch.setPalette(palette3)
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        font1.setPointSize(44)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.lbl_stopwatch.setFont(font1)
        self.lbl_stopwatch.setAlignment(Qt.AlignCenter)
        self.btn_start_stopwatch = QPushButton(self.tab_4)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(70, 180, 151, 71))
        font2 = QFont()
        font2.setFamilies([u"Courier New"])
        font2.setPointSize(28)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.btn_start_stopwatch.setFont(font2)
        self.btn_stop_stopwatch = QPushButton(self.tab_4)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(240, 180, 151, 71))
        self.btn_stop_stopwatch.setFont(font2)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Clock", None))
        self.menu_new.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.menu_open.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.menu_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.menu_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menu_solve.setText(QCoreApplication.translate("MainWindow", u"Solve sudoku", None))
        self.menu_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menu_theme.setText(QCoreApplication.translate("MainWindow", u"Switch Theme", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"StopWatch", None))
        self.lbl_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

