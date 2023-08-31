import os
import threading
from time import sleep

import darkdetect
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui.LaunchUi import Ui_MainWindow
from ui.episode import Ui_Form as EpisodeUi
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
        
        # add shadow to buttons
        for component in self.findChildren(QPushButton) + \
        [self.ui.label, self.ui.lineEdit]:
            shadow = OutNeoEffect(self)
            component.setGraphicsEffect(shadow)
        # self.ui.stackedWidget.setGraphicsEffect(InNeoEffect(self))
        # self.ui.label.setGraphicsEffect(InNeoEffect(self))
        
        # adding flow layout
        self.ui.flowLayout = FlowLayout(self.ui.scrollAreaWidgetContents)
        self.ui.scrollAreaWidgetContents.setLayout(self.ui.flowLayout)
        self.ui.stackedWidget.setCurrentIndex(0)
        
        # add vertical layout to scroll area 2
        # self.ui.scrollAreaWidgetContents_2.setLayout(QVBoxLayout())
        
        # styling SCROLL BAR
        self.ui.scrollArea.setStyleSheet(style["scrollBar"])
        # self.ui.scrollArea.setFrameShape(QFrame.NoFrame)
        self.ui.scrollArea_2.setStyleSheet(style["scrollBar"])
        
        # theme detection
        self.t = threading.Thread(target=self.detect_theme)
        self.t.daemon = True
        # self.t.start()
        
        # buttons actions
        self.ui.BackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.AddBtn.clicked.connect(self.add)

        # setting up DB
        self.db = DB("Main.db")
        self.restore()


        # add test cards
        for i in range(50):
            self.add_card(f"Serial {i}", i)
        #     card = Card("Some_serial")
        #     self.ui.flowLayout.addWidget(card.widget)
            # card.runBtn.clicked.connect(lambda: self.serial_clicked(card.serial_id))
            # shadow = QGraphicsDropShadowEffect(self)
            # shadow.setBlurRadius(20)
            # shadow.setXOffset(2)
            # shadow.setYOffset(2)
            # shadow.setColor(QColor(0, 0, 0, 50))
            # shadow = InNeoEffect(self)
            # card.setGraphicsEffect(shadow)


    def serial_clicked(self, serial_id):
        # clear vertical layout
        for i in reversed(range(self.ui.scrollAreaWidgetContents_2.layout().count())):
            self.ui.scrollAreaWidgetContents_2.layout().itemAt(i).widget().setParent(None)
            # self.ui.scrollAreaWidgetContents_2.layout().itemAt(i).widget().deleteLater()
        print("Serial id:", serial_id)
        # get serial info
        serial_info = self.db.select("serial", "name, path", f"id = {serial_id}")
        season_info = self.db.select("season", "name, path", f"serial_id = {serial_id}")
        episode_info = self.db.select("episode", "name, path", f"parent_id = {serial_id}")
        print(serial_info)
        print(episode_info)
        # sort episodes by name
        episode_info.sort(key=lambda x: x[0])
        if not episode_info:
            # add label "No episodes" to scroll area
            label = QLabel("No episodes")
            label.setAlignment(Qt.AlignCenter)
            self.ui.scrollAreaWidgetContents_2.layout().addWidget(label)
        else:
            # add episodes to vertical layout
            for episode in episode_info:
                # create form for EpisodeUi
                widget = QWidget()
                episode_ui = EpisodeUi()
                episode_ui.setupUi(widget)
                episode_ui.label.setText(episode[0])
                # episode_ui.pushButton.setGraphicsEffect(OutNeoEffect(self, lightColor = QColor("#3CEE95")))
                episode_ui.pushButton.clicked.connect(lambda: self.play(episode[1]))
                self.ui.scrollAreaWidgetContents_2.layout().addWidget(widget)
        # change page
        self.ui.stackedWidget.setCurrentIndex(1)


    def play(self, path):
        print(path)
        # do command mpv path
        os.system(f"mpv '{path}'")


    def detect_theme(self):
        while True:
            # if darkdetect.isDark():
            #     for component in self.findChildren(QPushButton):
            #         component.setStyleSheet("background-color: rgb(0, 0, 0);")
            # elif darkdetect.isLight():
            #     for component in self.findChildren(QPushButton):
            #         component.setStyleSheet("background-color: rgb(255, 255, 255);")
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
        effect = OutNeoEffect(self)
        card.runBtn.setGraphicsEffect(effect)


    def restore(self):
        self.db.cursor.execute("SELECT * FROM serial")
        for serial in self.db.cursor.fetchall():
            self.add_card(serial[1], serial[0])
            print(serial)



class Card():
    def __init__(self, serial_name, serial_id = 0):
        super().__init__()

        self.serial_name = serial_name.split("/")[-1]
        self.serial_id = serial_id

        self.widget = QWidget()
        self.widget.setFixedHeight(200)
        self.widget.setFixedWidth(130)
        # self.widget.setStyleSheet("""
        #     background-color: rgb(218, 228, 237);
        #     border-radius: 10px;""")
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
        # set min size
        self.runBtn.setMinimumSize(QSize(100, 28))
        self.runBtn.setStyleSheet("background-color: rgb(150, 255, 200);")
        self.runBtn.setText("Смотреть")
        font = QFont()
        font.setPointSize(12)
        self.runBtn.setFont(font)
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
