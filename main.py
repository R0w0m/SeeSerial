import os
import threading
from time import sleep

import darkdetect
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui.LaunchUi import Ui_MainWindow
from components.StyleSheets import style
from components.FlowLay import FlowLayout
from components.DBControl import DBControl as DB
from components.neumorph import NeumorphismEffect as NeoEffect
from components.neumorph import InsideNeumorphismEffect as InNeoEffect
from components.neumorph import OutsideNeumorphismEffect as OutNeoEffect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # setting up DB
        self.db = DB("Main.db")
        self.db.print_db()
        # adding flow layout
        self.ui.flowLayout = FlowLayout(self.ui.scrollAreaWidgetContents)
        self.ui.scrollAreaWidgetContents.setLayout(self.ui.flowLayout)
        # styleing SCROLL BAR
        self.ui.scrollArea.setStyleSheet(style["scrollBar"])
        self.ui.scrollArea.setFrameShape(QFrame.NoFrame)
        # theme detection
        self.t = threading.Thread(target=self.detect_theme)
        self.t.daemon = True
        # self.t.start()
        # buttons actions
        self.ui.BackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.AddBtn.clicked.connect(self.add)
        # restore from DB
        self.restore()


        # add shadow to buttons
        for component in self.findChildren(QPushButton) + \
        [self.ui.label, self.ui.lineEdit]:
            shadow = OutNeoEffect(self)
            component.setGraphicsEffect(shadow)
        shadow = OutNeoEffect(self)
        self.ui.stackedWidget.setGraphicsEffect(shadow)


        # add test cards
        # for i in range(50):
        #     self.add_card(f"Serial {i}", i)
            # card = Card("Some_serial")
            # self.ui.flowLayout.addWidget(card.widget)
            # card.runBtn.clicked.connect(lambda: self.serial_clicked(card.serial_id))
            # shadow = QGraphicsDropShadowEffect(self)
            # shadow.setBlurRadius(20)
            # shadow.setXOffset(2)
            # shadow.setYOffset(2)
            # shadow.setColor(QColor(0, 0, 0, 50))
            # shadow = InNeoEffect(self)
            # card.setGraphicsEffect(shadow)


    def serial_clicked(self, serial_id):
        self.ui.stackedWidget.setCurrentIndex(1)
        print("Serial id:", serial_id)
        # get serial info
        serial_info = self.db.select("serial", "name, path", f"id = {serial_id}")[0]
        print(serial_info)


    def detect_theme(self):
        while True:
            if darkdetect.isDark():
                for component in self.findChildren(QPushButton):
                    component.setStyleSheet("background-color: rgb(0, 0, 0);")
            elif darkdetect.isLight():
                for component in self.findChildren(QPushButton):
                    component.setStyleSheet("background-color: rgb(255, 255, 255);")
            print(darkdetect.theme())
            sleep(1)


    def add(self):
        # get directory
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.db.insert("serial", "name, path", f"'{directory.split('/')[-1]}', '{directory}'")
            serial_id = self.db.cursor.lastrowid
            print("Serial id:", serial_id)

            # directory analize
            for elm in os.scandir(directory):
                if elm.is_dir():
                    self.db.insert_("season", "name, path, serial_id", (elm.name, elm.path, serial_id))
                    print(f"Directory: {elm.name}")
                    season_id = self.db.cursor.lastrowid
                    for sub_elm in os.scandir(elm.path):
                        if sub_elm.is_file():
                            print(f"File: {sub_elm.name}")
                            self.db.insert_("episode", "name, path, parent_id", (sub_elm.name, sub_elm.path, season_id))
                elif elm.is_file():
                    print(f"File: {elm.name}")
                    self.db.insert_("episode", "name, path, parent_id", (elm.name, elm.path, serial_id))
            # self.ui.flowLayout.addWidget(Card(directory.split("/")[-1], serial_id).widget)
            self.add_card(directory.split("/")[-1], serial_id)
        else:
            print("Directory not selected")

    
    def add_card(self, serial_name, serial_id):
        card = Card(serial_name, serial_id)
        self.ui.flowLayout.addWidget(card.widget)
        card.runBtn.clicked.connect(lambda: self.serial_clicked(card.serial_id))
        card.runBtn.dropShadowEffect = InNeoEffect(card.runBtn)


    def restore(self):
        self.db.cursor.execute("SELECT * FROM serial")
        for serial in self.db.cursor.fetchall():
            self.add_card(serial[1], serial[0])
            print(serial)

class Card(QWidget):
    def __init__(self, serial_name, serial_id = 0):
        super().__init__()

        self.serial_name = serial_name.split("/")[-1]
        self.serial_id = serial_id

        self.widget = QWidget()
        self.widget.setFixedHeight(150)
        self.widget.setFixedWidth(100)
        self.widget.setStyleSheet("""
            background-color: rgb(255, 255, 255);
            border-radius: 10px;""")
        self.widget.setObjectName("widget")

        label = QLabel(self.widget)
        label.setStyleSheet("color: rgb(0, 0, 0);")
        label.setAlignment(Qt.AlignCenter)
        label.setObjectName("label")
        label.setText(self.serial_name)

        # add run button
        self.runBtn = QPushButton(self.widget)
        self.runBtn.setGeometry(QRect(0, 0, 50, 50))
        self.runBtn.setStyleSheet("background-color: rgb(150, 255, 200);")
        self.runBtn.setText("Смотерть")
        self.runBtn.setObjectName("runBtn")


        vLayout = QVBoxLayout(self.widget)
        vLayout.setObjectName("horizontalLayout")
        vLayout.addWidget(label)
        vLayout.addWidget(self.runBtn)



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
