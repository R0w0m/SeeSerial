# from ui.Player_ import Ui_MainWindow as PlayerUi
import sys

from PySide6.QtCore import QPoint, QRect, Qt
from PySide6.QtMultimedia import QAudioOutput  # QMediaFormat,
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QMainWindow, QMessageBox,
                               QPushButton, QScrollArea, QSpacerItem,
                               QVBoxLayout)

sys.path.append("../")
from ui.Player_ import Ui_MainWindow as PlayerUi


class Player(QMainWindow):
    def __init__(self, path, episode_id, position, fix_position):
        super().__init__()

        # import ui from Player_.py
        self.ui = PlayerUi()
        self.ui.setupUi(self)
        # self.path = path
        self.path = "C:/Users/Rwm/Videos/Arknights/1.mp4"
        print(self.path)
        self.episode_id = episode_id
        self.fix_position = fix_position
        self.start_position = position
        self.started = False

        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        self.ui.playBut.clicked.connect(self._player.play)
        # self._player.positionChanged.connect(self.on_position_changed)
        self._player.mediaStatusChanged.connect(self.set_start_position)

        self.ui.videoWidget = QVideoWidget()
        self._player.setVideoOutput(self.ui.videoWidget)
        self.ui.widget.layout().addWidget(self.ui.videoWidget)
        self.ui.videoWidget.lower()
        self.ui.widget.lower()
        # self.ui.widget.layout().addWidget(self.ui.controlWidget)
        self.ui.controlWidget.setStyleSheet("background: black")
        self.ui.controlWidget.raise_()

        # bind horisontal slider to players pos
        # self.ui.horizontalSlider.setRange(0, self._player.duration())
        # self.ui.horizontalSlider.setValue(self.start_position)
        # self.ui.horizontalSlider.valueChanged.connect(self._player.setPosition)
        # self._player.positionChanged.connect(self.ui.horizontalSlider.setValue)

        # set durLabel
        self.ui.durLabel.setText(
            f"{self._player.duration() // 60000}:\
        {self._player.duration() // 1000 % 60}"
        )
        self.open()

    def set_start_position(self, status):
        if not self.started and status == QMediaPlayer.LoadedMedia:
            self.started = True
            if self.start_position is not None:
                self._player.setPosition(self.start_position)
            self._player.play()

    # @Slot()
    def open(self):
        self._player.setSource(self.path)
        # print("start pos:", self.start_position)
        # self._player.setPosition(self.start_position)
        # self._player.play()

    # @Slot()
    def on_position_changed(self, position):
        print("Position changed:", position)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            if self._player.playbackState() == QMediaPlayer.PlayingState:
                self._player.pause()
            else:
                self._player.play()
        elif event.key() == Qt.Key_X:
            self._player.setPosition(self._player.position() + 5000)
        elif event.key() == Qt.Key_Z:
            self._player.setPosition(self._player.position() - 5000)
        elif event.key() == Qt.Key_Q:
            self.close()
        elif event.key() in range(48, 58):
            self._player.setPosition(self._player.duration() // 10 * (event.key() - 48))

    def closeEvent(self, event):
        print("Closing, Current position:", self._player.position())
        percent_pos = self._player.position() * 100 // self._player.duration()
        self.fix_position(self.episode_id, self._player.position(), percent_pos)
        self._ensure_stopped()
        event.accept()

    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()

    def resizeEvent(self, event):
        videoRect = QRect(
            QPoint(),
            self.ui.widget.sizeHint().scaled(self.size(), Qt.IgnoreAspectRatio),
        )
        videoRect.moveCenter(self.rect().center())
        self.ui.widget.setGeometry(videoRect)

        controlHeight = self.ui.controlWidget.sizeHint().height()
        controlRect = QRect(
            0, self.height() - controlHeight, self.width(), controlHeight
        )
        self.ui.controlWidget.setGeometry(controlRect)
