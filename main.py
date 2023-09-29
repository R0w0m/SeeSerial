import os
import threading
from time import sleep

# import darkdetect
# from PySide6.QtCore import *
from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtGui import QFont, QIcon #QPixmap, QColor, QPainter, QBrush
# from PySide6.QtWidgets import *
from PySide6.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QVBoxLayout, QWidget,
                                QScrollArea)

from components.DBControl import DBControl as DB
from components.FlowLay import FlowLayout
# from components.neumorph import NeumorphismEffect as NeoEffect
# from components.neumorph import InsideNeumorphismEffect as InNeoEffect
from components.neumorph import OutsideNeumorphismEffect as OutNeoEffect
from components.StyleSheets import style
from ui.episode import Ui_Form as EpisodeUi
from ui.LaunchUi import Ui_MainWindow
from ui.Player_ import Ui_MainWindow as PlayerUi

# from components.Player

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.player = None
        self.move_history = [0, ]
        
        # add shadow to buttons
        for component in self.findChildren(QPushButton) + \
        [self.ui.label, self.ui.lineEdit]:
            shadow = OutNeoEffect(self)
            component.setGraphicsEffect(shadow) 
        # adding flow layout
        self.ui.flowLayout = FlowLayout(self.ui.mainContents)
        self.ui.mainContents.setLayout(self.ui.flowLayout)
        self.ui.stackedWidget.setCurrentIndex(0) 
        # styling SCROLL BAR
        for component in self.findChildren(QScrollArea):
            component.setStyleSheet(style["scrollBar"])
        # buttons actions
        self.ui.BackBtn.clicked.connect(self.back_clicked)
        self.ui.HomeBtn.clicked.connect(lambda: self.change_page(0))
        self.ui.AddBtn.clicked.connect(self.add)
        self.ui.SettingsBtn.clicked.connect(lambda: self.change_page(3))
        

        # theme detection
        # self.t = threading.Thread(target=self.detect_theme)
        # self.t.daemon = True
        # self.t.start()
        

        # add test cards
        for i in range(50):
            self.add_card(f"Serial {i}", i)

        # setting up DB
        self.db = DB("Main.db")
        self.restore()

        # self.db.request("ALTER TABLE serial ADD COLUMN image_path TEXT")
        # self.db.update("serial", "image_path = 'previwes/rwby.webp'", "id = 2")
        # self.db.update("serial", "image_path = 'previwes/akg.webp'", "id = 1")

        self.retranslateUI()

    
    def back_clicked(self):
        x = self.move_history.pop()
        if x == self.ui.stackedWidget.currentIndex():
            x = self.move_history.pop()
        self.ui.stackedWidget.setCurrentIndex(
            self.move_history.pop() if len(self.move_history) > 1 else 0)
        if len(self.move_history) == 0:
            self.ui.BackBtn.hide()

    def serial_clicked(self, serial_id):
        # clear layouts
        for i in reversed(range(self.ui.episodeContents.layout().count())):
            self.ui.episodeContents.layout().itemAt(i).widget().setParent(None)
        for i in reversed(range(self.ui.seasonContents.layout().count())):
            self.ui.seasonContents.layout().itemAt(i).widget().setParent(None)
        print("Serial id:", serial_id)
        # get info
        season_info = self.db.select(
            "season", "id, name, path", f"serial_id = {serial_id}")
        episode_info = self.db.select(
            "episode", "name, path", f"parent_id = {serial_id} and parent_type = 0")
        print("season_info: ", bool(season_info))
        # sort episodes by name
        episode_info.sort(key=lambda x: x[0])
        if not season_info:
            if not episode_info:
                # add label "No episodes" to scroll area
                label = QLabel("No episodes")
                label.setAlignment(Qt.AlignCenter)
                self.ui.episodeContents.layout().addWidget(label)
            else:
                # add episodes to vertical layout
                for episode in episode_info:
                    self.add_episode(episode[0], episode[1])
            # change page
            # self.ui.stackedWidget.setCurrentIndex(2)
            self.change_page(2)
        else:
            # sort seasons by name
            season_info.sort(key=lambda x: x[1])
            for season in season_info:
                self.add_season(season[0], season[1])
            # change page
            # self.ui.stackedWidget.setCurrentIndex(1)
            self.change_page(1)
           

    def season_clicked(self, season_id: int):
        # clear vertical layout 
        for i in reversed(range(self.ui.episodeContents.layout().count())):
            self.ui.episodeContents.layout().itemAt(i).widget().setParent(None)
 
        # get info
        print(f"parent_id = {season_id} and parent_type = 1")
        episode_info = self.db.select("episode", "name, path", 
                                      f"parent_id = {season_id} and parent_type = 1")
        # sort episodes by name
        episode_info.sort(key=lambda x: x[0])
        if not episode_info:
            # add label "No episodes" to scroll area
            label = QLabel("No episodes")
            label.setAlignment(Qt.AlignCenter)
            self.ui.episodeContents.layout().addWidget(label)
        else:
            # add episodes to vertical layout
            for episode in episode_info:
                self.add_episode(episode[0], episode[1])
        # self.ui.stackedWidget.setCurrentIndex(2)
        self.change_page(2)
        

    def play(self, path):
        print(path)
        # os.system(f"mpv '{path}'")
        # open window with player
        if self.player is not None:
            self.player.close()
            self.player = None
        self.player = Player()
        self.player.show()
        # self.player.ui.videoWidget.setFullScreen(True)
        # self.player.ui.videoWidget.show()




    def detect_theme(self):
        while True:
            # if darkdetect.isDark():
            #     for component in self.findChildren(QPushButton):
            #         component.setStyleSheet("background-color: rgb(0, 0, 0);")
            # elif darkdetect.isLight():
            #     for component in self.findChildren(QPushButton):
            #         component.setStyleSheet("background-color: rgb(255, 255, 255);")
            # print(darkdetect.theme())
            sleep(1)


    def add(self):
        # get directory
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            dir_name = directory.split("/")[-1]
            self.db.insert("serial", "name, path, image_path", 
                           f"'{dir_name}', '{directory}', 'previwes/{dir_name}.webp'")
            serial_id = self.db.cursor.lastrowid
            print("Serial id:", serial_id)

            # directory analize
            for elm in os.scandir(directory):
                if elm.is_dir():
                    self.db.insert_("season", "name, path, serial_id",
                                    (elm.name, elm.path, serial_id))
                    print(f"Directory: {elm.name}")
                    season_id = self.db.cursor.lastrowid
                    # if in directory exist subdirectorie (seasons)
                    for sub_elm in os.scandir(elm.path):
                        if sub_elm.is_file():
                            print(f"File: {sub_elm.name}")
                            self.db.insert_("episode",
                                "name, path, parent_id, parent_type",
                                (sub_elm.name, sub_elm.path, season_id, 1))
                elif elm.is_file():
                    print(f"File: {elm.name}")
                    self.db.insert_("episode", "name, path, parent_id, parent_type",
                                    (elm.name, elm.path, serial_id, 0))
            self.add_card(dir_name, serial_id, f"previwes/{dir_name}.webp")
        else:
            print("Directory not selected")


    def add_episode(self, episode_name, episode_path):
        # create form for EpisodeUi
        widget = QWidget()
        self.ui.episodeContents.layout().addWidget(widget)
        episode_ui = EpisodeUi()
        episode_ui.setupUi(widget)
        widget.path = episode_path
        # smaller name
        if len(episode_name) > 60:
            episode_ui.label.setText(episode_name[:20] + "...")
        else:
            episode_ui.label.setText(episode_name)
        episode_ui.label_2.setText("")
        episode_ui.pushButton.clicked.connect(lambda: self.play(widget.path))
        print(widget.path)


    def add_season(self, season_id, season_name):
        season_widget = Season(season_id, season_name) 
        self.ui.seasonContents.layout().addWidget(season_widget.widget)
        season_widget.runBtn.clicked.connect(
            lambda: self.season_clicked(season_widget.season_id))

    
    def add_card(self, serial_name, serial_id, image_path = None):
        card = Card(serial_name, serial_id, image_path)
        self.ui.flowLayout.addWidget(card.widget)
        card.runBtn.clicked.connect(lambda: self.serial_clicked(card.serial_id))


    def change_page(self, page):
        self.ui.stackedWidget.setCurrentIndex(page)
        self.move_history.append(page)
        self.ui.BackBtn.show()


    def restore(self):
        self.db.cursor.execute("SELECT * FROM serial")
        for serial in self.db.cursor.fetchall():
            self.add_card(serial[1], serial[0], serial[3])
            print(serial)

    def retranslateUI(self):
        self.ui.label.setText("SeeSerial")
        self.ui.HomeBtn.setText("Главная")
        self.ui.MyListBtn.setText("Просмотрено") 
        self.ui.FavorsBtn.setText("Избранные")
        self.ui.AddBtn.setText("Добавить")
        self.ui.SettingsBtn.setText("Настройки")
        # self.ui.BackBtn.setText("")
        self.ui.pushButton_3.setText("Поиск")
        # self.ui.label_2.setText("TextLabel")
        # self.ui.pushButton_2.setText("PushButton"))
        # self.ui.pushButton_4.setText("PushButton"))
        self.ui.label_3.setText("TextLabel")

class Season():
    def __init__(self, season_id: int, season_name: str):
        super().__init__()

        self.season_name = season_name.split("/")[-1]
        self.season_id = season_id

        self.widget = QWidget()
        self.widget.setStyleSheet("""
            background-color: rgb(255, 255, 255);
            border-radius: 5px;""")
        self.widget.setObjectName("widget")
        
        label = QLabel(self.widget)
        label.setStyleSheet("color: rgb(0, 0, 0);")
        label.setAlignment(Qt.AlignLeft)
        label.setText(self.season_name)

        self.runBtn = QPushButton(self.widget)
        self.runBtn.setStyleSheet("""
            background-color: rgb(0, 0, 0);
            border-radius: 5px;
            color: rgb(255, 255, 255);""")
        self.runBtn.setText("Run")
        self.runBtn.setFixedWidth(50)
        self.runBtn.setFixedHeight(50)
        self.runBtn.setObjectName("runBtn")

        # self.widget.setLayout(QHBoxLayout())
        # self.widget.layout().addWidget(label)
        # self.widget.layout().addWidget(self.runBtn)
        # self.widget.layout().setContentsMargins(0, 0, 0, 0)
        hLayout = QHBoxLayout(self.widget)
        hLayout.setObjectName("horizontalLayout")
        hLayout.addWidget(label)
        hLayout.addWidget(self.runBtn)




class Card():
    def __init__(self, serial_name, serial_id = 0, image_path = "previwes/default.png"):
        super().__init__()

        self.serial_name = serial_name.split("/")[-1]
        self.serial_id = serial_id

        self.widget = QWidget()
        self.widget.setFixedHeight(265)
        self.widget.setFixedWidth(130)
        self.widget.setStyleSheet("""
            background-color: rgb(255, 255, 255);
            border-radius: 10px;
            padding: 0 0 10 0;""")
        self.widget.setObjectName("widget")


        # add image
        PixLabel = QLabel(self.widget)
        PixLabel.setAlignment(Qt.AlignCenter)
        PixLabel.setObjectName("label")
        PixLabel.setFixedSize(130, 200)
        if image_path is None:
            image_path = "previwes/default.png"
            PixLabel.setFixedSize(130, 200)
            PixLabel.setStyleSheet(" \
                image: url(previwes/default.png); \
                padding: 30px 15px; \
                ")
        else:
            PixLabel.setStyleSheet(f" \
                border-image: url({image_path}); \
                border-radius: 10%; \
                background-color: rgba(0, 0, 0, 0); \
                margin: 0 0 5 0; \
                ")
        PixLabel.setScaledContents(True)

        # add name
        label = QLabel(self.widget)
        label.setStyleSheet("color: rgb(0, 0, 0);")
        label.setAlignment(Qt.AlignCenter)
        label.setObjectName("label")
        label.setText(self.serial_name)

        # add run button
        self.runBtn = QPushButton(self.widget)
        self.runBtn.setGeometry(QRect(0, 0, 50, 50))
        self.runBtn.setMinimumSize(QSize(50, 28))
        self.runBtn.setStyleSheet(" \
            background-color: rgb(150, 255, 200); \
            border-radius: 10%; \
            image: url(media/play.svg); \
            padding: 5 px; \
            ")
        effect = OutNeoEffect(self.widget)
        self.runBtn.setGraphicsEffect(effect)
        # settings button
        self.setBtn = QPushButton(self.widget)
        self.setBtn.setGeometry(QRect(0, 0, 28, 28))
        self.setBtn.setMaximumSize(QSize(28, 28))
        self.setBtn.setStyleSheet(" \
            image: url(media/settings_gear.svg); \
            border-radius: 10%; \
            background-color: rgba(218, 228, 237, 255); \
            padding: 4 px; \
            ")
        effect = OutNeoEffect(self.widget)
        self.setBtn.setGraphicsEffect(effect)
        # icon = QIcon()
        # icon.addFile("media/settings_gear.svg", QSize(), QIcon.Normal, QIcon.Off)
        # self.setBtn.setIcon(icon)
        # self.setBtn.setIconSize(QSize(20, 20))

        vLayout = QVBoxLayout(self.widget)
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.setSpacing(0)

        hLayout = QHBoxLayout()
        hLayout.setContentsMargins(9, 0, 9, 9)
        hLayout.setSpacing(6)

        vLayout.addWidget(PixLabel)
        vLayout.addWidget(label)
        vLayout.addLayout(hLayout)

        hLayout.addWidget(self.runBtn)
        hLayout.addWidget(self.setBtn)



class Player(QMainWindow):
    def __init__(self):
        super().__init__()

        # import ui from Player_.py
        self.ui = PlayerUi()
        self.ui.setupUi(self)

        # resize ui.videoWidget to fit window
        self.ui.videoFrame.resize(self.ui.centralwidget.size())
        # resize controlWidget to bottom of window
        self.ui.controlWidget.move(0, self.ui.centralwidget.height() - 100)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
