import sys
from window import MainWindow
from PySide6.QtWidgets import QApplication
from log import log

if __name__ == "__main__":
    log('info', "Showing window")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
