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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 733)
        MainWindow.setStyleSheet(u"\n"
"  background-color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stackedWidget_2 = QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"")
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.verticalLayout_3 = QVBoxLayout(self.mainPage)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, -1)
        self.HomeBtn = QPushButton(self.mainPage)
        self.HomeBtn.setObjectName(u"HomeBtn")
        self.HomeBtn.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"RobotoMono Nerd Font [GOOG]"])
        self.HomeBtn.setFont(font)
        self.HomeBtn.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 255, 255);\n"
"  color: #808191;\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #CFC8FF;\n"
"  color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #9D92E9;\n"
"  color: white;\n"
"}")
        icon = QIcon()
        icon.addFile(u"media/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeBtn.setIcon(icon)
        self.HomeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.HomeBtn)

        self.line = QFrame(self.mainPage)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setMaximumSize(QSize(16777215, 30))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.FavorsBtn = QPushButton(self.mainPage)
        self.FavorsBtn.setObjectName(u"FavorsBtn")
        self.FavorsBtn.setMinimumSize(QSize(0, 30))
        self.FavorsBtn.setFont(font)
        self.FavorsBtn.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 255, 255);\n"
"  color: #808191;\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #CFC8FF;\n"
"  color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #9D92E9;\n"
"  color: white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"media/star.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.FavorsBtn.setIcon(icon1)
        self.FavorsBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.FavorsBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.mainPage)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(True)
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"  background-color: rgba(255, 255, 255, 0);\n"
"  border-radius: 10px;\n"
"  color: black;\n"
"  font-size: 30px;\n"
"  padding: 8px 16px;\n"
"  text-align: center;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.userBt = QPushButton(self.mainPage)
        self.userBt.setObjectName(u"userBt")
        font2 = QFont()
        font2.setFamilies([u"RobotoMono Nerd Font [GOOG]"])
        font2.setBold(False)
        font2.setItalic(False)
        self.userBt.setFont(font2)
        self.userBt.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 255, 255);\n"
"  color: #808191;\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #CFC8FF;\n"
"  color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #9D92E9;\n"
"  color: white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"media/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userBt.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.userBt)

        self.line_2 = QFrame(self.mainPage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 0))
        self.line_2.setMaximumSize(QSize(16777215, 30))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.AddBtn = QPushButton(self.mainPage)
        self.AddBtn.setObjectName(u"AddBtn")
        self.AddBtn.setEnabled(True)
        self.AddBtn.setMinimumSize(QSize(0, 30))
        self.AddBtn.setFont(font)
        self.AddBtn.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 255, 255);\n"
"  color: #808191;\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #CFC8FF;\n"
"  color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #9D92E9;\n"
"  color: white;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"media/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AddBtn.setIcon(icon3)
        self.AddBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.AddBtn)

        self.line_3 = QFrame(self.mainPage)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 0))
        self.line_3.setMaximumSize(QSize(16777215, 30))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_3)

        self.SettingsBtn = QPushButton(self.mainPage)
        self.SettingsBtn.setObjectName(u"SettingsBtn")
        self.SettingsBtn.setMinimumSize(QSize(0, 30))
        self.SettingsBtn.setFont(font)
        self.SettingsBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.SettingsBtn.setAutoFillBackground(False)
        self.SettingsBtn.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(255, 255, 255);\n"
"  color: #808191;\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  padding: 8px 16px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #CFC8FF;\n"
"  color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #9D92E9;\n"
"  color: white;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"media/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingsBtn.setIcon(icon4)
        self.SettingsBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.SettingsBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.mainPage)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.gridLayout = QGridLayout(self.main_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.scrollArea = QScrollArea(self.main_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none;\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.mainContents = QWidget()
        self.mainContents.setObjectName(u"mainContents")
        self.mainContents.setGeometry(QRect(0, 0, 68, 16))
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
        self.seasonContents.setGeometry(QRect(0, 0, 68, 18))
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
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_13, 0, 4, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)

        self.scrollArea_4 = QScrollArea(self.settings_page)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMinimumSize(QSize(700, 0))
        self.scrollArea_4.setWidgetResizable(True)
        self.settingsContents = QWidget()
        self.settingsContents.setObjectName(u"settingsContents")
        self.settingsContents.setGeometry(QRect(0, 0, 700, 609))
        self.formLayout = QFormLayout(self.settingsContents)
        self.formLayout.setObjectName(u"formLayout")
        self.label_11 = QLabel(self.settingsContents)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.comboBox = QComboBox(self.settingsContents)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_7.addWidget(self.comboBox)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.label_2 = QLabel(self.settingsContents)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.color_purple_Bt = QPushButton(self.settingsContents)
        self.color_purple_Bt.setObjectName(u"color_purple_Bt")
        self.color_purple_Bt.setMaximumSize(QSize(40, 16777215))
        icon5 = QIcon()
        icon5.addFile(u"media/colors/purple.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.color_purple_Bt.setIcon(icon5)
        self.color_purple_Bt.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.color_purple_Bt)

        self.color_orange_Bt = QPushButton(self.settingsContents)
        self.color_orange_Bt.setObjectName(u"color_orange_Bt")
        self.color_orange_Bt.setMaximumSize(QSize(40, 16777215))
        icon6 = QIcon()
        icon6.addFile(u"media/colors/orange.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.color_orange_Bt.setIcon(icon6)
        self.color_orange_Bt.setIconSize(QSize(48, 48))
        self.color_orange_Bt.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.color_orange_Bt)

        self.color_pink_Bt = QPushButton(self.settingsContents)
        self.color_pink_Bt.setObjectName(u"color_pink_Bt")
        self.color_pink_Bt.setMaximumSize(QSize(40, 16777215))
        icon7 = QIcon()
        icon7.addFile(u"media/colors/pink.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.color_pink_Bt.setIcon(icon7)
        self.color_pink_Bt.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.color_pink_Bt)

        self.color_blue_Bt = QPushButton(self.settingsContents)
        self.color_blue_Bt.setObjectName(u"color_blue_Bt")
        self.color_blue_Bt.setMaximumSize(QSize(40, 16777215))
        icon8 = QIcon()
        icon8.addFile(u"media/colors/blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.color_blue_Bt.setIcon(icon8)
        self.color_blue_Bt.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.color_blue_Bt)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.label_13 = QLabel(self.settingsContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.label_13)

        self.label_3 = QLabel(self.settingsContents)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)

        self.checkBox = QCheckBox(self.settingsContents)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_9.addWidget(self.checkBox)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.checkBox_2 = QCheckBox(self.settingsContents)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_11.addWidget(self.checkBox_2)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_11)

        self.line_4 = QFrame(self.settingsContents)
        self.line_4.setObjectName(u"line_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setMinimumSize(QSize(100, 1))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.line_4)

        self.label_12 = QLabel(self.settingsContents)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_12)

        self.scrollArea_4.setWidget(self.settingsContents)

        self.gridLayout_4.addWidget(self.scrollArea_4, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.settings_page)
        self.serSettingsPage = QWidget()
        self.serSettingsPage.setObjectName(u"serSettingsPage")
        self.verticalLayout_10 = QVBoxLayout(self.serSettingsPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.prevSetLayout = QVBoxLayout()
        self.prevSetLayout.setObjectName(u"prevSetLayout")
        self.prevSetWidget = QWidget(self.serSettingsPage)
        self.prevSetWidget.setObjectName(u"prevSetWidget")
        self.prevSetWidget.setStyleSheet(u"\n"
"border-radius: 10px;")
        self.gridLayout_7 = QGridLayout(self.prevSetWidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
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
        icon9 = QIcon()
        icon9.addFile(u"media/image-redo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.chooseFileBut.setIcon(icon9)
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
        icon10 = QIcon()
        icon10.addFile(u"media/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deletePrev.setIcon(icon10)
        self.deletePrev.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.deletePrev)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.gridLayout_7.addLayout(self.verticalLayout_6, 0, 0, 1, 1)


        self.prevSetLayout.addWidget(self.prevSetWidget)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.prevSetLayout.addItem(self.verticalSpacer_4)


        self.horizontalLayout_10.addLayout(self.prevSetLayout)

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

        self.label_4 = QLabel(self.serSettingsPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: black")

        self.verticalLayout_11.addWidget(self.label_4)

        self.noteTextEdit = QTextEdit(self.serSettingsPage)
        self.noteTextEdit.setObjectName(u"noteTextEdit")
        self.noteTextEdit.setStyleSheet(u"color: black;\n"
"padding: 5px;")

        self.verticalLayout_11.addWidget(self.noteTextEdit)


        self.horizontalLayout_10.addLayout(self.verticalLayout_11)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

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
        icon11 = QIcon()
        icon11.addFile(u"media/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveSerBt.setIcon(icon11)
        self.saveSerBt.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.saveSerBt)

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
        icon12 = QIcon()
        icon12.addFile(u"media/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearSerBt.setIcon(icon12)
        self.clearSerBt.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.clearSerBt)

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
        self.deleteSerBt.setIcon(icon10)
        self.deleteSerBt.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.deleteSerBt)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.serSettingsPage)
        self.favor_page = QWidget()
        self.favor_page.setObjectName(u"favor_page")
        self.gridLayout_5 = QGridLayout(self.favor_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.favor_page)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.favorContents = QWidget()
        self.favorContents.setObjectName(u"favorContents")
        self.favorContents.setGeometry(QRect(0, 0, 100, 30))
        self.scrollArea_5.setWidget(self.favorContents)

        self.gridLayout_5.addWidget(self.scrollArea_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.favor_page)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.stackedWidget_2.addWidget(self.mainPage)
        self.registrationPage = QWidget()
        self.registrationPage.setObjectName(u"registrationPage")
        self.gridLayout_6 = QGridLayout(self.registrationPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.registerBt = QPushButton(self.registrationPage)
        self.registerBt.setObjectName(u"registerBt")

        self.gridLayout_6.addWidget(self.registerBt, 4, 3, 1, 1)

        self.loginInput = QLineEdit(self.registrationPage)
        self.loginInput.setObjectName(u"loginInput")

        self.gridLayout_6.addWidget(self.loginInput, 2, 3, 1, 1)

        self.passInput = QLineEdit(self.registrationPage)
        self.passInput.setObjectName(u"passInput")

        self.gridLayout_6.addWidget(self.passInput, 3, 3, 1, 1)

        self.label_8 = QLabel(self.registrationPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_8, 2, 1, 1, 1)

        self.label_9 = QLabel(self.registrationPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_9, 3, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 1, 4, 1, 1)

        self.gotoLoginBt = QPushButton(self.registrationPage)
        self.gotoLoginBt.setObjectName(u"gotoLoginBt")

        self.gridLayout_6.addWidget(self.gotoLoginBt, 4, 1, 1, 1)

        self.label_7 = QLabel(self.registrationPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_7, 1, 1, 1, 3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.skipRegBt = QPushButton(self.registrationPage)
        self.skipRegBt.setObjectName(u"skipRegBt")

        self.gridLayout_6.addWidget(self.skipRegBt, 5, 1, 1, 3)

        self.stackedWidget_2.addWidget(self.registrationPage)
        self.usersPage = QWidget()
        self.usersPage.setObjectName(u"usersPage")
        self.gridLayout_8 = QGridLayout(self.usersPage)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer_7 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_8.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.label_10 = QLabel(self.usersPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_10, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 2, 0, 1, 1)

        self.usersListScrollArea = QScrollArea(self.usersPage)
        self.usersListScrollArea.setObjectName(u"usersListScrollArea")
        self.usersListScrollArea.setWidgetResizable(True)
        self.usersWidgetContents = QWidget()
        self.usersWidgetContents.setObjectName(u"usersWidgetContents")
        self.usersWidgetContents.setGeometry(QRect(0, 0, 54, 16))
        self.usersListScrollArea.setWidget(self.usersWidgetContents)

        self.gridLayout_8.addWidget(self.usersListScrollArea, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 2, 2, 1, 1)

        self.gotoRegisterBt = QPushButton(self.usersPage)
        self.gotoRegisterBt.setObjectName(u"gotoRegisterBt")

        self.gridLayout_8.addWidget(self.gotoRegisterBt, 3, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 4, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.usersPage)
        self.authPage = QWidget()
        self.authPage.setObjectName(u"authPage")
        self.gridLayout_9 = QGridLayout(self.authPage)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_8, 4, 1, 1, 1)

        self.userNameLbl = QLabel(self.authPage)
        self.userNameLbl.setObjectName(u"userNameLbl")
        self.userNameLbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.userNameLbl, 1, 1, 1, 2)

        self.passEnterToLogin = QLineEdit(self.authPage)
        self.passEnterToLogin.setObjectName(u"passEnterToLogin")

        self.gridLayout_9.addWidget(self.passEnterToLogin, 3, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_9, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_9, 1, 3, 1, 1)

        self.finLogBt = QPushButton(self.authPage)
        self.finLogBt.setObjectName(u"finLogBt")
        icon13 = QIcon()
        icon13.addFile(u"media/login.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.finLogBt.setIcon(icon13)

        self.gridLayout_9.addWidget(self.finLogBt, 3, 2, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer_10, 2, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.authPage)

        self.horizontalLayout_3.addWidget(self.stackedWidget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1026, 20))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SeeSerial", None))
        self.HomeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.FavorsBtn.setText(QCoreApplication.translate("MainWindow", u"Favorites", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SeeSerial", None))
        self.userBt.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.AddBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.SettingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043d\u0430\u044f", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430\u044f", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442\u043e\u0432\u0430\u044f \u0441\u0445\u0435\u043c\u0430", None))
        self.color_purple_Bt.setText("")
        self.color_orange_Bt.setText("")
#if QT_CONFIG(shortcut)
        self.color_orange_Bt.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.color_pink_Bt.setText("")
        self.color_blue_Bt.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043b\u0435\u0435\u0440\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0433\u043e \u044d\u043f\u0438\u0437\u043e\u0434\u0430", None))
        self.checkBox.setText("")
        self.checkBox_2.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043a\u043c \u043e\u0442\u043a\u0440\u044b\u0432\u0430\u0442\u044c \u043f\u043b\u0435\u0435\u0440 \u043d\u0430 \u043f\u043e\u043b\u043d\u044b\u0439 \u044d\u043a\u0440\u0430\u043d", None))
        self.prevImage.setText("")
        self.chooseFileBut.setText("")
        self.deletePrev.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.label_6.setText("")
        self.saveSerBt.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.clearSerBt.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.deleteSerBt.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.registerBt.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.gotoLoginBt.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.skipRegBt.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.gotoRegisterBt.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.userNameLbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

