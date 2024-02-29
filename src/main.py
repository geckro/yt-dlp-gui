import os
import sys
from window import MainWindow
from PySide6.QtWidgets import QApplication
from log import log

if __name__ == "__main__":
    log('info', "Showing window")
    log('debug', f"Current directory is: {os.getcwd()}")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
