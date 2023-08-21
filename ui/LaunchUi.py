# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LaunchUi.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(645, 417)
        MainWindow.setStyleSheet(u"\n"
"  background-color: rgb(221, 231, 239);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Carlito"])
        font.setBold(False)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"\n"
"  background-color: rgb(218, 228, 237);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  color: black;\n"
"  font-size: 30px;\n"
"  padding: 8px;\n"
"  text-align: center;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.HomeBtn = QPushButton(self.centralwidget)
        self.HomeBtn.setObjectName(u"HomeBtn")
        self.HomeBtn.setMinimumSize(QSize(150, 50))
        self.HomeBtn.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(218, 228, 237);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  color: black;\n"
"  font-size: 16px;\n"
"  padding: 8px 16px;\n"
"\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #fafafa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #eeeeee;\n"
"}:w")
        icon = QIcon()
        icon.addFile(u"media/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeBtn.setIcon(icon)
        self.HomeBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.HomeBtn)

        self.AddBtn = QPushButton(self.centralwidget)
        self.AddBtn.setObjectName(u"AddBtn")
        self.AddBtn.setEnabled(True)
        self.AddBtn.setMinimumSize(QSize(0, 50))
        self.AddBtn.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(218, 228, 237);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  color: black;\n"
"  font-size: 16px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #fafafa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #eeeeee;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"media/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AddBtn.setIcon(icon1)
        self.AddBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.AddBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(218, 228, 237);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  color: black;\n"
"  font-size: 16px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #fafafa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #eeeeee;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"media/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BackBtn = QPushButton(self.centralwidget)
        self.BackBtn.setObjectName(u"BackBtn")
        self.BackBtn.setMinimumSize(QSize(0, 0))
        self.BackBtn.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(218, 228, 237);\n"
"  border: none;\n"
"  color: black;\n"
"  font-size: 16px;\n"
"	padding: 3 0 3 2;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #fafafa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #eeeeee;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"media/left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BackBtn.setIcon(icon3)
        self.BackBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.BackBtn)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"  background-color: rgb(218, 228, 237);\n"
"  border: none;\n"
"  border-radius: 13px;\n"
"  color: black;\n"
"  font-size: 18px;\n"
"  padding: 4px 10px;\n"
"  text-align: left;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 0))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(218, 228, 237);\n"
"	border: none;\n"
"	padding: 7 10;\n"
"	color: black;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #fafafa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #eeeeee;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"media/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QSize(14, 14))

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(218, 228, 237);\n"
"border: 2px;\n"
"border-color: red;\n"
"border-color: rgb(222, 221, 218);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none;\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 433, 298))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea_2 = QScrollArea(self.page_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 82, 16))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 645, 24))
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.HomeBtn, self.AddBtn)
        QWidget.setTabOrder(self.AddBtn, self.pushButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SeeSerial", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SeeSerial", None))
        self.HomeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.AddBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.BackBtn.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi

