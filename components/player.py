# from ui.Player_ import Ui_MainWindow as PlayerUi
import sys

from PySide6.QtCore import QPoint, QRect, Qt
from PySide6.QtMultimedia import QAudioOutput  # QMediaFormat,
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QSpacerItem,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

sys.path.append("../")
from ui.Player_ import Ui_MainWindow as PlayerUi


class Player(QMainWindow):
    def __init__(self, parent, path, episode_id, position, fix_position, settings):
        super().__init__(parent)

        # import ui from Player_.py
        self.ui = PlayerUi()
        self.ui.setupUi(self)
        self.path = path
        # self.path = "C:/Users/Rwm/Videos/Arknights/1.mp4"
        self.episode_id = episode_id
        self.parent = parent
        self.start_position = position
        self.started = False
        self.auto_fullscreen = settings[0]

        # audio
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        # bind buttons
        self.ui.playBut.clicked.connect(self._player.play)
        self.ui.fullScreenBut.clicked.connect(self.fullScreen)
        self._player.mediaStatusChanged.connect(self.init)

        # set videoWidget
        self.ui.videoWidget = QVideoWidget()
        self._player.setVideoOutput(self.ui.videoWidget)
        self.ui.widget.layout().addWidget(self.ui.videoWidget)
        # self.ui.widget.layout().addWidget(self.ui.controlWidget)
        self.ui.controlWidget.setStyleSheet("background: black")

        self._player.setSource(self.path)

    def init(self, status):
        if not self.started and status == QMediaPlayer.LoadedMedia:
            self.started = True
            if self.start_position is not None:
                self._player.setPosition(self.start_position)
            self._player.play()
            # self.ui.horizontalSlider.setRange(0, self._player.duration())
            # self.ui.horizontalSlider.setValue(self.start_position)
            # self.ui.horizontalSlider.valueChanged.connect(self._player.setPosition)
            self.ui.horizontalSlider.setRange(0, 100)
            self.ui.horizontalSlider.setValue(self.start_position * 100 // self._player.duration())
            self.ui.horizontalSlider.valueChanged.connect(
                lambda x: self._player.setPosition(x * self._player.duration() // 100)
            )
            self._player.positionChanged.connect(
                lambda x: self.ui.posLabel.setText(
                    f"{x // 60000:02}:{x // 1000 % 60:02}"
                )
            )
            self.ui.durLabel.setText(
                f"{self._player.duration() // 60000:02}:{self._player.duration() // 1000 % 60:02}"
            )
            if self.auto_fullscreen:
                self.fullScreen()


    def fullScreen(self):
        if self.isFullScreen():
            self.showNormal()
            self.ui.videoWidget.show()
            self.ui.controlWidget.show()
        else:
            self.showFullScreen()
            self.ui.controlWidget.hide()

    def keyPressEvent(self, event):
        switcher = {
            Qt.Key_Space: (
                self._player.pause
                if self._player.playbackState() == QMediaPlayer.PlayingState
                else self._player.play
            ),
            Qt.Key_F: self.fullScreen,
            Qt.Key_X: lambda: self._player.setPosition(self._player.position() + 5000),
            Qt.Key_Z: lambda: self._player.setPosition(self._player.position() - 5000),
            Qt.Key_Q: self.close,
        }
        switcher.get(event.key(), lambda: None)()
        if event.key() in range(48, 58):
            self._player.setPosition(self._player.duration() // 10 * (event.key() - 48)) 

    def closeEvent(self, event):
        print("Closing, Current position:", self._player.position())
        percent_pos = self._player.position() * 100 // self._player.duration()
        # self.fix_position(self.episode_id, self._player.position(), percent_pos)
        self.parent.fix_position_signal.emit(self.episode_id, self._player.position(), percent_pos)
        self._ensure_stopped()
        event.accept()

    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()

    # def resizeEvent(self, event):
    #     videoRect = QRect(
    #         QPoint(),
    #         self.ui.widget.sizeHint().scaled(self.size(), Qt.IgnoreAspectRatio),
    #     )
    #     videoRect.moveCenter(self.rect().center())
    #     self.ui.widget.setGeometry(videoRect)
    #     # self.ui.widget.move(0, 0)
    #     # self.ui.widget.resize(self.width(), self.height() // 2)
    #
    #     controlHeight = self.ui.controlWidget.sizeHint().height()
    #     controlRect = QRect(
    #         0, self.height() - controlHeight, self.width(), controlHeight
    #     )
    #     self.ui.controlWidget.setGeometry(controlRect)
