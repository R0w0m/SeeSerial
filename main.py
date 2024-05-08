import os
# import threading
import time
from time import sleep
# import darkdetect
from PySide6.QtCore import QPoint, QRect, QSize, Qt, Signal
from PySide6.QtGui import QFontMetrics, QFont
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from components.DBControl import DBControl as DB
from components.FlowLay import FlowLayout
# from components.neumorph import NeumorphismEffect as NeoEffect
# from components.neumorph import InsideNeumorphismEffect as InNeoEffect
# from components.neumorph import OutsideNeumorphismEffect as OutNeoEffect
from components.player import Player as Player
# from components.StyleSheets import style
from components.StyleSheets import StyleSheets
from ui.episode import Ui_Form as EpisodeUi
from ui.LaunchUi import Ui_MainWindow

# from ui.Player_ import Ui_MainWindow as PlayerUi


class MainWindow(QMainWindow):
    fix_position_signal = Signal(int, int, int)
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.player = None
        # self.move_history = [
        #     0,
        # ]
        self.current_serial = None
        self.prev_set = ""
        self.fix_position_signal.connect(self.fix_position)

        # add shadow to buttons
        # for component in self.findChildren(QPushButton) + [
        #     self.ui.label,
        #     # self.ui.lineEdit,
        #     self.ui.serialNameLbl,
        #     self.ui.noteTextEdit,
        #     self.ui.prevSetWidget,
        # ]:
        #     if component.objectName() in ["deletePrev", "chooseFileBut"]:
        #         shadow = InNeoEffect(self)
        #         component.setGraphicsEffect(shadow)
        #         continue
        #     shadow = OutNeoEffect(self)
        #     component.setGraphicsEffect(shadow)

        # adding flow layout
        self.ui.main_flowLayout = FlowLayout(self.ui.mainContents)
        self.ui.mainContents.setLayout(self.ui.main_flowLayout)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.fav_flowLayout = FlowLayout(self.ui.favorContents)
        self.ui.favorContents.setLayout(self.ui.fav_flowLayout)

        # buttons actions
        self.ui.HomeBtn.clicked.connect(lambda: self.change_page(0))
        self.ui.AddBtn.clicked.connect(self.add)
        self.ui.SettingsBtn.clicked.connect(lambda: self.change_page(3))
        self.ui.FavorsBtn.clicked.connect(lambda: self.favorites_clicked())
        self.ui.deletePrev.clicked.connect(self.deletePrev_clicked)
        self.ui.saveSerBt.clicked.connect(self.save_set)
        self.ui.chooseFileBut.clicked.connect(self.prev_set_clicked)
        self.ui.deleteSerBt.clicked.connect(lambda: self.delete_serial(self.current_serial))
        self.ui.clearSerBt.clicked.connect(lambda: self.clear_full_progress(self.current_serial))

        # theme detection
        # self.t = threading.Thread(target=self.detect_theme)
        # self.t.daemon = True
        # self.t.start()

        # nav fix
        self.move_history.append(self.ui.stackedWidget.currentIndex())
        self.setStyles()

        # setting up DB
        self.db = DB("Main.db")
        self.restore()
        self.retranslateUI()

    def register(self):
        login = self.ui.loginEdit.text()
        password = self.ui.passwordEdit.text()
        if not login or not password:
            message = QMessageBox()
            message.setWindowTitle("Ошибка")
            message.setText("Заполните все поля")
            message.setStandardButtons(QMessageBox.Ok)
            message.setIcon(QMessageBox.Warning)
            message.exec()
            return
        self.db.insert("users", "login, password", f"'{login}', '{password}'")


    def setStyles(self):
        self.styles = StyleSheets("purple")
        self.setStyleSheet(self.styles.styles["main"])
        for component in self.findChildren(QPushButton):
            component.setStyleSheet(self.styles.styles["button"])
        # for component in self.findChildren(QLabel):
        #     component.setStyleSheet(self.styles.styles["label"])
        for component in self.findChildren(QScrollArea):
            component.setStyleSheet(self.styles.styles["scrollBar"])

    def favorited(self, serial_id, favBtn):
        is_fav = self.db.select("serial", "favorite", f"id = {serial_id}")[0][0]
        if is_fav:
            # unset favorite
            self.db.update("serial", "favorite = 0", f"id = {serial_id}")
            # set favorite button color
            favBtn.setStyleSheet(
                " \
                image: url(media/star.svg); \
                background-color: rgba(255, 255, 255, 0.7); \
                border-radius: 50%; \
                padding: 4px; \
                "
            )
        else:
            self.db.update("serial", "favorite = 1", f"id = {serial_id}")
            # set favorite button color
            favBtn.setStyleSheet(
                " \
                image: url(media/star_full.svg); \
                background-color: rgba(255, 255, 255, 0.7); \
                border-radius: 50%; \
                padding: 4px; \
                "
            )

    def favorites_clicked(self):
        # clear layout
        for i in reversed(range(self.ui.favorContents.layout().count())):
            self.ui.favorContents.layout().itemAt(i).widget().setParent(None)
        # get favorite serials
        serials = self.db.select("serial", "*", "favorite = 1")
        for serial_info in serials:
            self.add_card(serial_info, 1)
        self.change_page(5)

    # def back_clicked(self):
    #     if len(self.move_history) == 0:
    #         self.ui.stackedWidget.setCurrentIndex(0)
    #         self.move_history.append(0)
    #         self.ui.BackBtn.hide()
    #         return
    #     x = self.move_history.pop()
    #
    #     # if popped page is current page
    #     if x == self.ui.stackedWidget.currentIndex():
    #         x = self.move_history.pop()
    #
    #     # change page
    #     self.ui.stackedWidget.setCurrentIndex(x)
    #
    #     # hide back button if stack is empty
    #     if len(self.move_history) == 0:
    #         self.ui.BackBtn.hide()

    def serial_clicked(self, serial_id):
        # clear layouts
        for i in reversed(range(self.ui.episodeContents.layout().count())):
            if self.ui.episodeContents.layout().itemAt(i).widget() is not None:
                self.ui.episodeContents.layout().itemAt(i).widget().setParent(None)
            else:
                item = self.ui.episodeContents.layout().itemAt(i)
                self.ui.episodeContents.layout().removeItem(item)

        for i in reversed(range(self.ui.seasonContents.layout().count())):
            if self.ui.seasonContents.layout().itemAt(i).widget() is not None:
                self.ui.seasonContents.layout().itemAt(i).widget().setParent(None)
            else:
                item = self.ui.seasonContents.layout().itemAt(i)
                self.ui.seasonContents.layout().removeItem(item)

        # get info
        season_info = self.db.select(
            "season", "id, name, path", f"serial_id = {serial_id}"
        )
        # sort episodes by name
        if not season_info:
            self.season_clicked(serial_id, 0)
            self.change_page(2)
        else:
            # sort seasons by name
            season_info.sort(key=lambda x: x[1])
            for season in season_info:
                self.add_season(season[0], season[1])

            widget = QWidget()
            verticalSpacer = QSpacerItem(
                20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
            )
            self.ui.seasonContents.layout().addItem(verticalSpacer)
            self.change_page(1)

    def season_clicked(self, season_id: int, parent_type):
        # clear vertical layout
        for i in reversed(range(self.ui.episodeContents.layout().count())):
            if self.ui.episodeContents.layout().itemAt(i).widget() is not None:
                self.ui.episodeContents.layout().itemAt(i).widget().setParent(None)
            else:
                item = self.ui.episodeContents.layout().itemAt(i)
                self.ui.episodeContents.layout().removeItem(item)

        # get info
        episode_info = self.db.select(
            "episode",
            "id, name",
            f"parent_id = {season_id} and parent_type = {parent_type}",
        )
        # sort episodes by name
        episode_info.sort(key=lambda x: x[1])
        if not episode_info:
            # add label "No episodes" to scroll area
            label = QLabel("No episodes")
            label.setAlignment(Qt.AlignCenter)
            self.ui.episodeContents.layout().addWidget(label)
        else:
            # add episodes to vertical layout
            for episode in episode_info:
                self.add_episode(episode[0])

        widget = QWidget()
        verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )
        self.ui.episodeContents.layout().addItem(verticalSpacer)

        if self.ui.stackedWidget.currentIndex() != 2:
            self.change_page(2)

    def play(self, episode_id):
        if self.player is not None:
            self.player.close()
            self.player = None
        path, episode_id, pos, parent_id, parent_type = self.db.select(
            "episode",
            "path, id, position, parent_id, parent_type",
            f"id = {episode_id}",
        )[0]
        print(path, episode_id, pos, parent_id, parent_type)
        self.parent_info = (parent_id, parent_type)
        if not os.path.exists(path):
            dlg = QMessageBox()
            dlg.setWindowTitle("Error")
            dlg.setText("fill is not exists")
            dlg.exec()
            return
        self.player = Player(self, path, episode_id, pos, self.fix_position)
        self.player.show()

    def fix_position(self, episode_id, position, percent_pos):
        self.db.update(
            "episode",
            f"position = {position}, pos_percent = {percent_pos}",
            f"id = {episode_id}",
        )
        # if current page is episode page
        if self.ui.stackedWidget.currentIndex() == 2:
            self.season_clicked(self.parent_info[0], self.parent_info[1])
        # self.progress.setValue(percent_pos)
        # progressBar.setValue(position)
        print("Position fixed:", position)

    def detect_theme(self):
        # https://stackoverflow.com/questions/20908370/styling-with-classes-in-pyside-python
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
            dir_name = directory.split(os.path.sep)[-1]
            self.db.insert(
                "serial",
                "name, path, image_path",
                f"'{dir_name}', '{directory}', 'previwes{os.path.sep}{dir_name}.webp'",
            )
            serial_id = self.db.cursor.lastrowid

            # directory analize
            for elm in os.scandir(directory):
                if elm.is_dir():
                    self.db.insert_(
                        "season",
                        "name, path, serial_id",
                        (elm.name, elm.path, serial_id),
                    )
                    season_id = self.db.cursor.lastrowid
                    # if in directory exist subdirectorie (seasons)
                    for sub_elm in os.scandir(elm.path):
                        if sub_elm.is_file():
                            self.db.insert_(
                                "episode",
                                "name, path, parent_id, parent_type",
                                (sub_elm.name, sub_elm.path, season_id, 1),
                            )
                            print("path: ", sub_elm.path)
                elif elm.is_file():
                    self.db.insert_(
                        "episode",
                        "name, path, parent_id, parent_type",
                        (elm.name, elm.path, serial_id, 0),
                    )
                    print("path: ", elm.path)
            self.add_card(
                (serial_id, dir_name, directory, None, f"previwes/{dir_name}.webp", 0)
            )
        else:
            print("Directory not selected")

    def add_episode(self, episode_id):
        # https://stackoverflow.com/questions/63656328
        # /rounding-a-qlabels-corners-in-pyqt5
        # create form for EpisodeUi
        episode_path, episode_name, pos, pos_ms = self.db.select(
            "episode", "path, name, pos_percent, position", f"id = {episode_id}"
        )[0]
        widget = QWidget()
        self.ui.episodeContents.layout().addWidget(widget)
        episode_ui = EpisodeUi()
        episode_ui.setupUi(widget)
        if pos is None:
            pos = 0
        if pos == 0:
            episode_ui.progressBar.hide()
        else:
            episode_ui.progressBar.show()
            episode_ui.progressBar.setValue(pos)
        widget.path = episode_path

        # smaller name
        if len(episode_name) > 60:
            episode_ui.label.setText(episode_name[:20] + "...")
        else:
            episode_ui.label.setText(episode_name)
            episode_ui.label.setStyleSheet("color: black;")
        if pos_ms is not None:
            pos_s = pos_ms // 1000
            episode_ui.timeLabel.setText(time.strftime("%M:%S", time.gmtime(pos_s)))
            episode_ui.timeLabel.setStyleSheet("color: black;")
            episode_ui.clearEpBt.show()
        else:
            episode_ui.timeLabel.setText("")
            episode_ui.clearEpBt.hide()
        episode_ui.pushButton.clicked.connect(lambda: self.play(episode_id))
        episode_ui.clearEpBt.clicked.connect(lambda: self.clear_ep_progress(episode_id))

    def clear_ep_progress(self, episode_id):
        self.db.update(
            "episode", "position = NULL, pos_percent = NULL", f"id = {episode_id}"
        )
        self.season_clicked(self.parent_info[0], self.parent_info[1])

    def add_season(self, season_id, season_name):
        season_widget = Season(season_id, season_name)
        self.ui.seasonContents.layout().addWidget(season_widget.widget)
        season_widget.runBtn.clicked.connect(
            lambda: self.season_clicked(season_widget.season_id, 1)
        )

    def add_card(self, serial_info, page_num=0):
        # card = Card(serial_name, serial_id, image_path)
        card = Card(serial_info)
        pages = (
            self.ui.main_flowLayout,
            self.ui.fav_flowLayout,
        )
        pages[page_num].addWidget(card.widget)
        card.epListBtn.clicked.connect(lambda: self.serial_clicked(card.serial_id))
        card.runBtn.clicked.connect(lambda: self.play_last(card.serial_id))
        card.setBtn.clicked.connect(lambda: self.serial_settings(card.serial_id))
        card.favoriteBtn.clicked.connect(
            lambda: self.favorited(card.serial_id, card.favoriteBtn)
        )

    def play_last(self, serial_id):
        # check seasons and episodes
        season_info = self.db.select(
            "season", "id, name, path", f"serial_id = {serial_id}"
        )
        if season_info:
            # sort seasons by name
            season_info.sort(key=lambda x: x[1])
            # get last season
            for season in reversed(season_info):
                # check episodes
                season_id = season[0]
                episode_info = self.db.select(
                    "episode",
                    "id, name, position",
                    f"parent_id = {season_id} and parent_type = 1",
                )
                if episode_info:
                    # sort episodes by name
                    episode_info.sort(key=lambda x: x[1])
                    is_watched = False
                    # get last episode
                    for episode in reversed(episode_info):
                        if episode[2] is not None:
                            episode_id = episode[0]
                            is_watched = True
                            break
                    if is_watched:
                        self.play(episode_id)
                        break
                else:
                    print("No episodes")
        else:
            episode_info = self.db.select(
                "episode",
                "id, name, position",
                f"parent_id = {serial_id} and parent_type = 0",
            )
            if episode_info:
                # sort episodes by name
                episode_info.sort(key=lambda x: x[1])
                # get last watched episode
                for episode in reversed(episode_info):
                    if episode[2] is not None:
                        episode_id = episode[0]
                        # self.db.update("episode", "position = NULL, pos_percent = NULL",
                        #                 f"id = {episode_id}")
                        break
                self.play(episode_id)
            else:
                print("No episodes")

    def deletePrev_clicked(self):
        # set image to default and write it to self.prev_set
        # message box "Are you sure?"
        message = QMessageBox()
        message.setWindowTitle("Delete preview")
        message.setText("Вы уверены?")
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.setIcon(QMessageBox.Warning)
        # message.exec()
        if message.exec() == QMessageBox.Yes:
            self.ui.prevImage.setStyleSheet(
                " \
            image: url(previwes/default.png); \
            padding: 30px 15px; \
            "
            )
            self.ui.prevImage.setScaledContents(True)
            self.ui.prevImage.show()
            self.ui.prevImage.setMinimumSize(QSize(130, 200))
            self.prev_set = None

    def serial_settings(self, serial_id):
        serial_info = self.db.select(
            "serial", "name, path, image_path", f"id = {serial_id}"
        )[0]
        image_path = serial_info[2]
        if image_path is None or not os.path.exists(image_path):
            image_path = "previwes/default.png"
            self.ui.prevImage.setFixedSize(130, 200)
            self.ui.prevImage.setStyleSheet(
                " \
                image: url(previwes/default.png); \
                padding: 30px 15px; \
                "
            )
        else:
            self.ui.prevImage.setStyleSheet(
                f" \
                border-image: url({image_path}); \
                border-radius: 10%; \
                background-color: rgba(0, 0, 0, 0); \
                margin: 0 0 5 0; \
                "
            )
        self.ui.prevImage.setScaledContents(True)
        self.ui.prevImage.show()
        self.ui.prevImage.setMinimumSize(QSize(130, 200))
        self.ui.serialNameLbl.setText(serial_info[0])
        # self.ui.pushButton_3.clicked.connect(lambda: self.change_serial_name(serial_id))
        self.current_serial = serial_id
        self.prev_set = serial_info[2]
        self.change_page(4)

    def delete_serial(self, serial_id):
        # are you sure?
        message = QMessageBox()
        message.setWindowTitle("Delete")
        message.setText("Вы уверены?")
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.setIcon(QMessageBox.Warning)
        if message.exec() == QMessageBox.No:
            return

        self.db.delete("serial", f"id = {serial_id}")
        self.db.delete("season", f"serial_id = {serial_id}")
        self.db.delete("episode", f"parent_id = {serial_id} and parent_type = 0")
        # if seasons exist
        season_info = self.db.select("season", "id, name", f"serial_id = {serial_id}")
        if season_info:
            # get last season
            for season in season_info:
                self.db.delete(
                    "episode", f"parent_id = {season[0]} and parent_type = 1"
                )
        # clear serials (card) layout
        for i in reversed(range(self.ui.main_flowLayout.count())):
            self.ui.main_flowLayout.itemAt(i).widget().setParent(None)
        # restore serials
        self.restore()
        # change page
        self.change_page(0)
        message = QMessageBox()
        message.setWindowTitle("Удаление")
        message.setText("Сериал успешно удален")
        message.setStandardButtons(QMessageBox.Ok)
        message.setIcon(QMessageBox.Information)
        message.exec()

    def clear_full_progress(self, serial_id):
        self.db.update(
            "episode",
            "position = NULL, pos_percent = NULL",
            f"parent_id = {serial_id} and parent_type = 0",
        )
        # if seasons exist
        season_info = self.db.select("season", "id, name", f"serial_id = {serial_id}")
        if season_info:
            # get last season
            for season in season_info:
                self.db.update(
                    "episode",
                    "position = NULL, pos_percent = NULL",
                    f"parent_id = {season[0]} and parent_type = 1",
                )
        message = QMessageBox()
        message.setWindowTitle("Удаление")
        message.setText("Прогресс успешно сброшен")
        message.setStandardButtons(QMessageBox.Ok)
        message.setIcon(QMessageBox.Information)
        message.exec()
        # self.serial_settings(serial_id)

    def save_set(self):
        # write to db: name, note, prev_set
        name = self.ui.serialNameLbl.text()
        note = self.ui.noteTextEdit.toPlainText()
        self.db.update(
            "serial",
            f"name = '{name}', note = '{note}', image_path = '{self.prev_set}'",
            f"id = {self.current_serial}",
        )
        # clear serials (card) layout
        for i in reversed(range(self.ui.main_flowLayout.count())):
            self.ui.main_flowLayout.itemAt(i).widget().setParent(None)
        # restore serials
        self.restore()

        # change page
        self.change_page(0)

    def prev_set_clicked(self):
        # get image path
        image_path = QFileDialog.getOpenFileName(
            self, "Select Image", filter="Images (*.png *.jpg *.jpeg *.webp)"
        )[0]
        if image_path:
            self.ui.prevImage.setStyleSheet(
                f" \
                border-image: url({image_path}); \
                border-radius: 10%; \
                background-color: rgba(0, 0, 0, 0); \
                margin: 0 0 5 0; \
                "
            )
            self.ui.prevImage.setScaledContents(True)
            self.ui.prevImage.show()
            # set minimum size
            self.ui.prevImage.setMinimumSize(QSize(130, 200))
            # copy image to previwes
            os.system(
                f"cp '{image_path}' \
                'previwes/{self.ui.serialNameLbl.text()}.webp'"
            )
            self.prev_set = f"previwes/{self.ui.serialNameLbl.text()}.webp"

    def change_page(self, page):
        self.move_history.append(self.ui.stackedWidget.currentIndex())
        self.ui.stackedWidget.setCurrentIndex(page)
        # self.move_history.append(page)
        # self.ui.BackBtn.show()

    def restore(self):
        for i in reversed(range(self.ui.main_flowLayout.count())):
            self.ui.main_flowLayout.itemAt(i).widget().setParent(None)
        for i in range(8):
            self.add_card((f"Serial {i}", str(i), None, None, None, 0))
        self.db.cursor.execute("SELECT * FROM serial")
        for serial_info in self.db.cursor.fetchall():
            self.add_card(serial_info)
        self.change_page(0)

    def closeEvent(self, event):
        self.db.conn.close()
        if self.player is not None:
            self.player.close()
        event.accept()

    def retranslateUI(self):
        self.ui.label.setText("SeeSerial")
        self.ui.HomeBtn.setText("Главная")
        # self.ui.MyListBtn.setText("Просмотрено")
        self.ui.FavorsBtn.setText("Избранные")
        self.ui.AddBtn.setText("Добавить")
        self.ui.SettingsBtn.setText("Настройки")
        self.ui.userButton.setText("Пользователь")
        # self.ui.pushButton_3.setText("Поиск")
        # self.ui.label_2.setText("TextLabel")
        # self.ui.pushButton_2.setText("PushButton"))
        # self.ui.pushButton_4.setText("PushButton"))
        self.ui.label_3.setText("TextLabel")


class Season:
    def __init__(self, season_id: int, season_name: str):
        super().__init__()

        self.season_name = season_name.split("/")[-1]
        self.season_id = season_id

        self.widget = QWidget()
        self.widget.setStyleSheet(
            """
            background-color: rgb(255, 255, 255);
            border-radius: 5px;"""
        )
        self.widget.setObjectName("widget")

        label = QLabel(self.widget)
        label.setStyleSheet("color: rgb(0, 0, 0);")
        label.setAlignment(Qt.AlignLeft)
        label.setAlignment(Qt.AlignVCenter)
        label.setText(self.season_name)

        self.runBtn = QPushButton(self.widget)
        self.runBtn.setStyleSheet(
            """
            background-color: rgb(150, 255, 200);
            border-radius: 5px;
            image: url(media/play.svg);
            padding: 10px;
            """
        )
        # self.runBtn.setText("Run")
        self.runBtn.setFixedWidth(40)
        self.runBtn.setFixedHeight(40)
        self.runBtn.setObjectName("runBtn")

        hLayout = QHBoxLayout(self.widget)
        hLayout.setObjectName("horizontalLayout")
        hLayout.addWidget(label)
        hLayout.addWidget(self.runBtn)


class Card:
    def __init__(self, serial_info):
        super().__init__()

        self.serial_id = serial_info[0]
        self.serial_name = serial_info[1].split(os.path.sep)[-1]
        image_path = serial_info[4]
        is_fav = serial_info[5]

        print("serial_info:", serial_info)

        self.widget = QWidget()
        self.widget.setFixedHeight(265)
        self.widget.setFixedWidth(130)
        self.widget.setStyleSheet(
            """
            background-color: #CFC8FF;
            border-radius: 10px;
            padding: 0 0 10 0;
            border: 3px solid #CFC8FF;
            """
        )
        self.widget.setObjectName("widget")

        # add image
        PixLabel = QLabel(self.widget)
        PixLabel.setAlignment(Qt.AlignCenter)
        PixLabel.setObjectName("label")
        PixLabel.setFixedSize(130, 200)
        if image_path is None or not os.path.exists(image_path):
            image_path = "previwes/default.png"
            PixLabel.setFixedSize(130, 200)
            PixLabel.setStyleSheet(
                " \
                image: url(previwes/default.png); \
                background-color: rgb(255, 255, 255); \
                padding: 30px 15px; \
                "
            )
        else:
            PixLabel.setStyleSheet(
                f" \
                border-image: url({image_path}); \
                border-radius: 10%; \
                background-color: rgba(0, 0, 0, 0); \
                margin: 0 0 5 0; \
                "
            )
        PixLabel.setScaledContents(True)

        font = QFont()
        font.setFamilies([u"RobotoMono Nerd Font [GOOG]"])

        # add name
        label = QLabel(self.widget)
        label.setStyleSheet("color: rgb(0, 0, 0); border: none;")
        label.setAlignment(Qt.AlignCenter)
        label.setObjectName("label")
        label.setFont(font)
        font_metrics = QFontMetrics(label.font())
        elided_text = font_metrics.elidedText(self.serial_name, Qt.ElideRight, 120)
        label.setText(elided_text)

        # ep list button
        self.epListBtn = QPushButton(self.widget)
        self.epListBtn.setGeometry(QRect(0, 0, 28, 28))
        self.epListBtn.setMaximumSize(QSize(28, 28))
        self.epListBtn.setStyleSheet(
            " \
            background-color: rgba(218, 228, 237, 255); \
            border-radius: 10%; \
            image: url(media/menu.svg); \
            padding: 5 px; \
            "
        )

        # add run button
        self.runBtn = QPushButton(self.widget)
        # self.runBtn.setGeometry(QRect(0, 0, 50, 50))
        self.runBtn.setMinimumSize(QSize(28, 28))
        self.runBtn.setStyleSheet(
            " \
            background-color: rgb(150, 255, 200); \
            border-radius: 10%; \
            image: url(media/play.svg); \
            padding: 6 px; \
            "
        )

        # settings button
        self.setBtn = QPushButton(self.widget)
        self.setBtn.setGeometry(QRect(0, 0, 28, 28))
        self.setBtn.setMaximumSize(QSize(28, 28))
        self.setBtn.setStyleSheet(
            " \
            image: url(media/settings_gear.svg); \
            border-radius: 10%; \
            background-color: rgba(218, 228, 237, 255); \
            padding: 4 px; \
            "
        )

        # favorite button
        self.favoriteBtn = QPushButton(self.widget)
        self.favoriteBtn.setGeometry(QRect(95, 5, 28, 28))
        self.favoriteBtn.setMaximumSize(QSize(28, 28))
        if is_fav:
            self.favoriteBtn.setStyleSheet(
                " \
                image: url(media/star_full.svg); \
                background-color: rgba(255, 255, 255, 0); \
                border-radius: 50%; \
                padding: 4px; \
                border: none; \
                "
            )
        else:
            self.favoriteBtn.setStyleSheet(
                " \
                image: url(media/star.svg); \
                background-color: rgba(255, 255, 255, 0); \
                border-radius: 50%; \
                padding: 4px; \
                border: none; \
                "
            )

        # add layouts
        vLayout = QVBoxLayout(self.widget)
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.setSpacing(0)

        hLayout = QHBoxLayout()
        hLayout.setContentsMargins(9, 0, 9, 9)
        hLayout.setSpacing(6)

        # add widgets to layouts
        vLayout.addWidget(PixLabel)
        vLayout.addWidget(label)
        vLayout.addLayout(hLayout)

        hLayout.addWidget(self.epListBtn)
        hLayout.addWidget(self.runBtn)
        hLayout.addWidget(self.setBtn)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
