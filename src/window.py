from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QCheckBox, QMainWindow, QPushButton, QComboBox, \
    QStatusBar
from __init__ import __version__, __author__, __license__

class MainWindow(QMainWindow):
    def __init__(self, title: str = 'yt-dlp gui'):
        """
        Initializes the MainWindow class.
        title: The title of the window. Defaults to 'yt-dlp gui'.
        """
        super().__init__()
        self.setWindowTitle(title)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.video_audio_layout = QVBoxLayout()

        self.init_ui()

        self.layout.addLayout(self.video_audio_layout)
        self.central_widget.setLayout(self.layout)

    def init_ui(self):
        """Initializes the UI for the MainWindow class."""

        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage(__version__)

        input_field = QLineEdit()
        input_field.setPlaceholderText("Enter URL here...")

        self.layout.addWidget(input_field)

        video_audio_cb = QComboBox()
        video_audio_cb.addItems((
            "Video",
            "Audio"
        ))
        video_audio_cb.setPlaceholderText('Choose video/audio')
        video_audio_cb.setCurrentIndex(-1)
        self.layout.addWidget(video_audio_cb)
        video_audio_cb.currentIndexChanged.connect(self.video_audio_cb)

        download_btn = QPushButton("Download")
        self.layout.addWidget(download_btn)

    def video_audio_cb(self, index):

        # Clear layout to remove existing widgets
        for i in reversed(range(self.video_audio_layout.count())):
            widget = self.video_audio_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        if index == 0:  # Video selected
            self.video_cb = QComboBox()
            self.video_audio_layout.addWidget(self.video_cb)
        elif index == 1:  # Audio selected
            self.audio_le = QLineEdit()
            self.video_audio_layout.addWidget(self.audio_le)

    def checkbox_options(self):
        checkboxes = []
        option_list = (
            "Audio",
            "options"
        )
        for option in option_list:
            checkbox = QCheckBox(option)
            checkboxes.append(checkbox)
            self.layout.addWidget(checkbox)
