import sys

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        #self.home = None
        self.label = QLabel("Home")
        #set window size to be screen width
        self.showMaximized()
        layout = QHBoxLayout()
        #create dropdown for table selection
        self.cb = QComboBox()
        self.cb.addItem("volunteers")
        self.cb.addItem("jobs")
        #self.cb.currentIndexChanged.connect(self.showTableOptions)
        #add dropdown to layout
        layout.addWidget(self.cb)

        # based on dropdown selection, display options for queries
        # on query click, open dialog box with form to fillout (if needed)
        # on form submit (if needed), display results below

        #set widget layout
        self.setLayout(layout)
        self.show()





    def showTableOptions(self, text):
        print("showing options for ",text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui=Home()
    gui.show()
    sys.exit(app.exec())