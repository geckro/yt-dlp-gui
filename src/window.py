from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QCheckBox, QMainWindow, QPushButton, QComboBox, \
    QStatusBar, QHBoxLayout, QLabel
import __init__
from download_video import download_video
from read_toml import read_toml

TITLE = 'yt-dlp GUI'
STATUS_BAR_INFO = (__init__.__version__, __init__.__license__, __init__.__author__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(TITLE)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.input_download_layout = QHBoxLayout()

        self.option_layout = QVBoxLayout()
        self.video_audio_layout = QVBoxLayout()

        self.data = read_toml()

        self.init_ui()  # Calls init_ui

        self.option_layout.addLayout(self.video_audio_layout)
        self.layout.addLayout(self.input_download_layout)
        self.layout.addLayout(self.option_layout)
        self.central_widget.setLayout(self.layout)

    def init_ui(self) -> None:
        """Initializes the UI for the MainWindow class."""
        self.setup_status_bar()
        self.setup_show_all_opts()
        self.setup_input_field()
        self.setup_options_area()
        self.setup_download_btn()

    def setup_status_bar(self):
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        for info in STATUS_BAR_INFO:
            status_bar.addWidget(QLabel(info))

    def setup_show_all_opts(self):
        show_all_opts_cb = QCheckBox("Show all options")
        self.input_download_layout.addWidget(show_all_opts_cb)

    def setup_input_field(self):
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter URL here...")
        self.input_download_layout.addWidget(self.input_field)

    def setup_options_area(self):
        # Options area
        video_audio_cb = QComboBox()
        video_audio_cb.addItems((
            self.data['video']['name'],
            self.data['audio']['name'],
        ))
        video_audio_cb.setPlaceholderText('Choose video/audio...')
        video_audio_cb.setCurrentIndex(-1)
        self.input_download_layout.addWidget(video_audio_cb)
        video_audio_cb.currentIndexChanged.connect(self.check_if_video_or_audio)

        thumbnail_title = QLabel("Thumbnail")
        self.option_layout.addWidget(thumbnail_title)

        embed_thumbnail_opt = QCheckBox(self.data['thumbnail']['embedthumbnail']['name'])
        save_thumbnail_opt = QCheckBox(self.data['thumbnail']['savethumbnail']['name'])
        self.option_layout.addWidget(embed_thumbnail_opt)
        self.option_layout.addWidget(save_thumbnail_opt)

        shortcut_title = QLabel("Shortcuts")
        self.option_layout.addWidget(shortcut_title)

        write_win_link = QCheckBox(self.data['shortcuts']['writeurllink']['name'])
        write_mac_link = QCheckBox(self.data['shortcuts']['write_webloc_link']['name'])
        write_lin_link = QCheckBox(self.data['shortcuts']['write_desktop_link']['name'])
        self.option_layout.addWidget(write_win_link)
        self.option_layout.addWidget(write_mac_link)
        self.option_layout.addWidget(write_lin_link)

    def check_if_video_or_audio(self, index):
        """Handles selection of either video or audio download."""
        # Clear layout to remove existing widgets
        for i in reversed(range(self.video_audio_layout.count())):
            widget = self.video_audio_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        if index == 0:
            self.create_video_widgets()
        elif index == 1:
            self.create_audio_widgets()

    def setup_download_btn(self):
        download_btn = QPushButton("Download")
        download_btn.clicked.connect(self.download_yt_video)
        self.input_download_layout.addWidget(download_btn)

    def create_video_widgets(self):
        remux_video = QComboBox()
        remux_video.setPlaceholderText(self.data['video']['remux']['name'])
        remux_video.setCurrentIndex(-1)
        remux_video.addItems(self.data['video']['remux']['opts_fancy'])
        self.video_audio_layout.addWidget(remux_video)

        embed_subtitles = QCheckBox()
        embed_subtitles.setText(self.data['video']['embed_subtitles']['name'])
        self.video_audio_layout.addWidget(embed_subtitles)

    def create_audio_widgets(self):
        audio_format = QComboBox()
        audio_format.setPlaceholderText(self.data['audio']['format']['name'])
        audio_format.setCurrentIndex(-1)
        audio_format.addItems(self.data['audio']['format']['opts_fancy'])
        self.video_audio_layout.addWidget(audio_format)

    def download_yt_video(self):
        yt_url = download_video(self.input_field.text())


