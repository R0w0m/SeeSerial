# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'episode.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(591, 62)
        Form.setMinimumSize(QSize(0, 62))
        Form.setStyleSheet(u"background-color: rgb(218, 228, 237);\n"
"background-color: white;\n"
"border: 2px;\n"
"border-color: red;\n"
"border-radius: 10px;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(18, -1, 18, -1)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"  background-color: #2CDE85;\n"
"  border: none;\n"
"  font-size: 16px;\n"
"  padding: 7 2 7 6;\n"
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
        icon = QIcon()
        icon.addFile(u"media/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.timeLabel = QLabel(self.widget)
        self.timeLabel.setObjectName(u"timeLabel")

        self.horizontalLayout_3.addWidget(self.timeLabel)

        self.clearEpBt = QPushButton(self.widget)
        self.clearEpBt.setObjectName(u"clearEpBt")
        icon1 = QIcon()
        icon1.addFile(u"media/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearEpBt.setIcon(icon1)
        self.clearEpBt.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.clearEpBt)


        self.verticalLayout.addWidget(self.widget)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 4))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: #ddd;\n"
"	color: white;\n"
"	margin: 0 0 0 0;\n"
"	border-color: green;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: red;\n"
"	color: red;\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.timeLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.clearEpBt.setText("")
        self.progressBar.setFormat("")
    # retranslateUi

