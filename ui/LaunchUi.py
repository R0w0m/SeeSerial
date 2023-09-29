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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(760, 580)
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

        self.MyListBtn = QPushButton(self.centralwidget)
        self.MyListBtn.setObjectName(u"MyListBtn")
        self.MyListBtn.setMinimumSize(QSize(150, 50))
        self.MyListBtn.setStyleSheet(u"QPushButton {\n"
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
        self.MyListBtn.setIcon(icon)
        self.MyListBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.MyListBtn)

        self.FavorsBtn = QPushButton(self.centralwidget)
        self.FavorsBtn.setObjectName(u"FavorsBtn")
        self.FavorsBtn.setMinimumSize(QSize(150, 50))
        self.FavorsBtn.setStyleSheet(u"QPushButton {\n"
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
        self.FavorsBtn.setIcon(icon)
        self.FavorsBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.FavorsBtn)

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

        self.SettingsBtn = QPushButton(self.centralwidget)
        self.SettingsBtn.setObjectName(u"SettingsBtn")
        self.SettingsBtn.setMinimumSize(QSize(0, 50))
        self.SettingsBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.SettingsBtn.setAutoFillBackground(False)
        self.SettingsBtn.setStyleSheet(u"QPushButton {\n"
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
        self.SettingsBtn.setIcon(icon2)
        self.SettingsBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.SettingsBtn)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(9)
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
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.gridLayout = QGridLayout(self.main_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.main_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none;\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.mainContents = QWidget()
        self.mainContents.setObjectName(u"mainContents")
        self.mainContents.setGeometry(QRect(0, 0, 566, 482))
        self.scrollArea.setWidget(self.mainContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.main_page)
        self.season_page = QWidget()
        self.season_page.setObjectName(u"season_page")
        self.gridLayout_3 = QGridLayout(self.season_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea_3 = QScrollArea(self.season_page)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.seasonContents = QWidget()
        self.seasonContents.setObjectName(u"seasonContents")
        self.seasonContents.setGeometry(QRect(0, 0, 548, 464))
        self.verticalLayout_2 = QVBoxLayout(self.seasonContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_3.setWidget(self.seasonContents)

        self.gridLayout_3.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.season_page)
        self.episode_page = QWidget()
        self.episode_page.setObjectName(u"episode_page")
        self.gridLayout_2 = QGridLayout(self.episode_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.episode_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.episodeContents = QWidget()
        self.episodeContents.setObjectName(u"episodeContents")
        self.episodeContents.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_5 = QVBoxLayout(self.episodeContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_2.setWidget(self.episodeContents)

        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.episode_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.gridLayout_4 = QGridLayout(self.settings_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea_4 = QScrollArea(self.settings_page)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.settingsContents = QWidget()
        self.settingsContents.setObjectName(u"settingsContents")
        self.settingsContents.setGeometry(QRect(0, 0, 169, 62))
        self.formLayout = QFormLayout(self.settingsContents)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.settingsContents)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.pushButton_2 = QPushButton(self.settingsContents)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pushButton_2)

        self.pushButton_4 = QPushButton(self.settingsContents)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pushButton_4)

        self.label_3 = QLabel(self.settingsContents)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.scrollArea_4.setWidget(self.settingsContents)

        self.gridLayout_4.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 760, 24))
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.AddBtn, self.SettingsBtn)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SeeSerial", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SeeSerial", None))
        self.HomeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.MyListBtn.setText(QCoreApplication.translate("MainWindow", u"My list", None))
        self.FavorsBtn.setText(QCoreApplication.translate("MainWindow", u"Favorites", None))
        self.AddBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.SettingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.BackBtn.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

