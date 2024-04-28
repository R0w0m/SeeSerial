# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Player_.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(634, 372)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.controlWidget = QWidget(self.centralwidget)
        self.controlWidget.setObjectName(u"controlWidget")
        self.controlWidget.setGeometry(QRect(0, 174, 304, 55))
        self.controlWidget.setMaximumSize(QSize(16777215, 55))
        self.controlWidget.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 202), stop:1 rgba(255, 255, 255, 0))")
        self.verticalLayout = QVBoxLayout(self.controlWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 0, 9, 9)
        self.horizontalSlider = QSlider(self.controlWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"QSlider{\n"
"	background: rgba(255, 255, 255, 0)\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border: 0px;\n"
"    background: rgba(255, 255, 255, 0);\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #f00, stop: 1 #f00);\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #ddd;\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ccc);\n"
"    border: 0px;\n"
"    width: 10px;\n"
"	height: 10px;\n"
"    margin-top: -3px;\n"
"    margin-bottom: -3px;\n"
"    border-radius: 5px;\n"
"}")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.prvBut = QPushButton(self.controlWidget)
        self.prvBut.setObjectName(u"prvBut")
        self.prvBut.setMaximumSize(QSize(30, 16777215))
        self.prvBut.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"background: rgba(255, 255, 255, 0);")
        icon = QIcon()
        icon.addFile(u"media/previous_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.prvBut.setIcon(icon)
        self.prvBut.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.prvBut)

        self.playBut = QPushButton(self.controlWidget)
        self.playBut.setObjectName(u"playBut")
        self.playBut.setMaximumSize(QSize(30, 30))
        self.playBut.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"background: rgba(255, 255, 255, 0);")
        icon1 = QIcon()
        icon1.addFile(u"media/play_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playBut.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.playBut)

        self.nextBut = QPushButton(self.controlWidget)
        self.nextBut.setObjectName(u"nextBut")
        self.nextBut.setMaximumSize(QSize(30, 16777215))
        self.nextBut.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"background: rgba(255, 255, 255, 0);")
        icon2 = QIcon()
        icon2.addFile(u"media/forward_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nextBut.setIcon(icon2)
        self.nextBut.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.nextBut)

        self.posLabel = QLabel(self.controlWidget)
        self.posLabel.setObjectName(u"posLabel")
        self.posLabel.setStyleSheet(u"background: rgba(255, 255, 255, 0)")

        self.horizontalLayout_3.addWidget(self.posLabel)

        self.durLabel = QLabel(self.controlWidget)
        self.durLabel.setObjectName(u"durLabel")
        self.durLabel.setStyleSheet(u"background: rgba(255, 255, 255, 0)")

        self.horizontalLayout_3.addWidget(self.durLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.fullScreenBut = QPushButton(self.controlWidget)
        self.fullScreenBut.setObjectName(u"fullScreenBut")
        self.fullScreenBut.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"background: rgba(255, 255, 255, 0);")
        icon3 = QIcon()
        icon3.addFile(u"media/expand_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fullScreenBut.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.fullScreenBut)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 241, 131))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VideoPlayer", None))
        self.prvBut.setText("")
        self.playBut.setText("")
        self.nextBut.setText("")
        self.posLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.durLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.fullScreenBut.setText("")
    # retranslateUi

