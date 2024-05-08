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
    def __init__(self, parent, path, episode_id, position, fix_position):
        super().__init__(parent)

        # import ui from Player_.py
        self.ui = PlayerUi()
        self.ui.setupUi(self)
        self.path = path
        self.episode_id = episode_id
        # self.fix_position = fix_position
        self.parent = parent
        self.start_position = position
        self.started = False

        # audio
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        # bind buttons
        self.ui.playBut.clicked.connect(self._player.play)
        self.ui.fullScreenBut.clicked.connect(self.showFullScreen)
        # self._player.positionChanged.connect(self.on_position_changed)
        self._player.mediaStatusChanged.connect(self.set_start_position)

        # set videoWidget
        self.ui.videoWidget = QVideoWidget()
        self._player.setVideoOutput(self.ui.videoWidget)
        self.ui.widget.layout().addWidget(self.ui.videoWidget)
        # self.ui.widget.layout().addWidget(self.ui.controlWidget)
        self.ui.controlWidget.setStyleSheet("background: black")

        # set durLabel
        self.ui.durLabel.setText(
            f"{self._player.duration() // 60000}:\
        {self._player.duration() // 1000 % 60}"
        )
        self._player.setSource(self.path)

    def set_start_position(self, status):
        if not self.started and status == QMediaPlayer.LoadedMedia:
            self.started = True
            if self.start_position is not None:
                self._player.setPosition(self.start_position)
            self._player.play()
            self.ui.horizontalSlider.setRange(0, self._player.duration())
            self.ui.horizontalSlider.setValue(self.start_position)
            self.ui.horizontalSlider.valueChanged.connect(self._player.setPosition)

    def on_position_changed(self, position):
        print("Position changed:", position)

    def keyPressEvent(self, event):
        switcher = {
            Qt.Key_Space: (
                self._player.pause
                if self._player.playbackState() == QMediaPlayer.PlayingState
                else self._player.play
            ),
            Qt.Key_F: self.showNormal if self.isFullScreen() else self.showFullScreen,
            Qt.Key_X: lambda: self._player.setPosition(self._player.position() + 5000),
            Qt.Key_Z: lambda: self._player.setPosition(self._player.position() - 5000),
            Qt.Key_Q: self.close,
        }
        switcher.get(event.key(), lambda: None)()

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

    def resizeEvent(self, event):
        videoRect = QRect(
            QPoint(),
            self.ui.widget.sizeHint().scaled(self.size(), Qt.IgnoreAspectRatio),
        )
        videoRect.moveCenter(self.rect().center())
        self.ui.widget.setGeometry(videoRect)
        # self.ui.widget.move(0, 0)
        # self.ui.widget.resize(self.width(), self.height() // 2)

        controlHeight = self.ui.controlWidget.sizeHint().height()
        controlRect = QRect(
            0, self.height() - controlHeight, self.width(), controlHeight
        )
        self.ui.controlWidget.setGeometry(controlRect)
