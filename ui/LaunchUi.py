# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LaunchUi.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)

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
        font1 = QFont()
        font1.setFamilies([u"FreeSans"])
        self.HomeBtn.setFont(font1)
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
        font2 = QFont()
        font2.setFamilies([u"FreeSans"])
        font2.setBold(False)
        self.MyListBtn.setFont(font2)
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
        self.FavorsBtn.setFont(font1)
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
        self.AddBtn.setFont(font1)
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.SettingsBtn = QPushButton(self.centralwidget)
        self.SettingsBtn.setObjectName(u"SettingsBtn")
        self.SettingsBtn.setMinimumSize(QSize(0, 50))
        self.SettingsBtn.setFont(font1)
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
        self.mainContents.setGeometry(QRect(0, 0, 100, 30))
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
        self.seasonContents.setGeometry(QRect(0, 0, 100, 30))
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
        self.serSettingsPage = QWidget()
        self.serSettingsPage.setObjectName(u"serSettingsPage")
        self.verticalLayout_10 = QVBoxLayout(self.serSettingsPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.prevSetWidget = QWidget(self.serSettingsPage)
        self.prevSetWidget.setObjectName(u"prevSetWidget")
        self.prevSetWidget.setStyleSheet(u"\n"
"border-radius: 10px;")
        self.gridLayout_6 = QGridLayout(self.prevSetWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 9)
        self.prevImage = QLabel(self.prevSetWidget)
        self.prevImage.setObjectName(u"prevImage")

        self.verticalLayout_6.addWidget(self.prevImage)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, 9, -1)
        self.chooseFileBut = QPushButton(self.prevSetWidget)
        self.chooseFileBut.setObjectName(u"chooseFileBut")
        self.chooseFileBut.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(218, 228, 237);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  color: black;\n"
"  padding: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #fafafa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #eeeeee;\n"
"}:w")
        icon5 = QIcon()
        icon5.addFile(u"media/image-redo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.chooseFileBut.setIcon(icon5)
        self.chooseFileBut.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.chooseFileBut)

        self.deletePrev = QPushButton(self.prevSetWidget)
        self.deletePrev.setObjectName(u"deletePrev")
        self.deletePrev.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(218, 228, 237);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  color: black;\n"
"  padding: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #fafafa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #eeeeee;\n"
"}:w")
        icon6 = QIcon()
        icon6.addFile(u"media/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deletePrev.setIcon(icon6)
        self.deletePrev.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.deletePrev)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.prevSetWidget)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.serSettingsPage)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setFamilies([u"FreeSans"])
        font3.setPointSize(14)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: black")

        self.verticalLayout_11.addWidget(self.label_5)

        self.serialNameLbl = QLineEdit(self.serSettingsPage)
        self.serialNameLbl.setObjectName(u"serialNameLbl")
        self.serialNameLbl.setStyleSheet(u"QLineEdit {\n"
"  background-color: rgb(218, 228, 237);\n"
"  border: none;\n"
"  border-radius: 13px;\n"
"  color: black;\n"
"  font-size: 18px;\n"
"  padding: 4px 10px;\n"
"  text-align: left;\n"
"}")

        self.verticalLayout_11.addWidget(self.serialNameLbl)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)


        self.horizontalLayout_10.addLayout(self.verticalLayout_11)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.label_4 = QLabel(self.serSettingsPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: black")

        self.verticalLayout_10.addWidget(self.label_4)

        self.noteTextEdit = QTextEdit(self.serSettingsPage)
        self.noteTextEdit.setObjectName(u"noteTextEdit")
        self.noteTextEdit.setStyleSheet(u"color: black;\n"
"padding: 5px;")

        self.verticalLayout_10.addWidget(self.noteTextEdit)

        self.label_6 = QLabel(self.serSettingsPage)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.saveSerBt = QPushButton(self.serSettingsPage)
        self.saveSerBt.setObjectName(u"saveSerBt")
        self.saveSerBt.setMinimumSize(QSize(0, 40))
        self.saveSerBt.setFont(font3)
        self.saveSerBt.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(218, 228, 237);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  color: black;\n"
"  padding: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #fafafa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #eeeeee;\n"
"}:w")
        icon7 = QIcon()
        icon7.addFile(u"media/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveSerBt.setIcon(icon7)
        self.saveSerBt.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.saveSerBt)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.clearSerBt = QPushButton(self.serSettingsPage)
        self.clearSerBt.setObjectName(u"clearSerBt")
        self.clearSerBt.setMinimumSize(QSize(0, 40))
        self.clearSerBt.setFont(font3)
        self.clearSerBt.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(218, 228, 237);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  color: black;\n"
"  padding: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #fafafa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #eeeeee;\n"
"}:w")
        icon8 = QIcon()
        icon8.addFile(u"media/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearSerBt.setIcon(icon8)
        self.clearSerBt.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.clearSerBt)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.deleteSerBt = QPushButton(self.serSettingsPage)
        self.deleteSerBt.setObjectName(u"deleteSerBt")
        self.deleteSerBt.setMinimumSize(QSize(0, 40))
        self.deleteSerBt.setFont(font3)
        self.deleteSerBt.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(218, 228, 237);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  color: black;\n"
"  padding: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #fafafa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #eeeeee;\n"
"}:w")
        self.deleteSerBt.setIcon(icon6)
        self.deleteSerBt.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.deleteSerBt)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.serSettingsPage)

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

        self.stackedWidget.setCurrentIndex(4)


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
        self.prevImage.setText("")
        self.chooseFileBut.setText("")
        self.deletePrev.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.label_6.setText("")
        self.saveSerBt.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.clearSerBt.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.deleteSerBt.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

