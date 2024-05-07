import sys

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


# create login window
class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        # set title
        self.setWindowTitle("DB Interface")
        # set window dimensions
        self.setGeometry(100, 100, 300, 400)
        # create group
        self.formGroupBox = QGroupBox('login-form')

        #init form
        self.createForm()
        #create main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        #set layout
        self.setLayout(mainLayout)

    def createForm(self):
        layout = QFormLayout()
        layout.addRow(QLabel("Username:"), QLineEdit())
        layout.addRow(QLabel("Password:"), QLineEdit())
        layout.addRow(QLabel("Host:"),QLineEdit())
        layout.addRow(QLabel("Database:"),QLineEdit())
        # set layout
        self.formGroupBox.setLayout(layout)
if __name__=='__main__':
    #init app
    app=QApplication(sys.argv)
    window=Window()
    window.show() #manditory
    sys.exit(app.exec())

