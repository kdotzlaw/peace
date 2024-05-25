import sys

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        self.home = None
        self.label = QLabel("Home")
        self.setCentralWidget(self.label)


if __name__ == "__main__":
    app = QApplication([])
    gui=Home()
    gui.show()
    app.exec()