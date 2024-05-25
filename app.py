import sys

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from home import Home


class Window(QDialog): #has to be QDialog for form to show
    def __init__(self):
        super(Window, self).__init__()
        # create this window
        self.setWindowTitle("Login")
        # set this window dimensions
        self.setGeometry(100, 100, 400, 450)
        # create the group for the login form
        self.formGroupBox = QGroupBox('login')
        # init second window
        #self.home = None

        # init login form
        self.createForm()
        # create main layout for this window
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)

    def onLoginClick(self):
        print("clicked")
        #get input
        usr = self.username.text()
        pwd = self.password.text()
        host = self.host.text()
        db = self.db.text()
        print("Username: "+usr+"\nPassword: "+pwd+"\nHost: "+host+"\nDB: "+db)
        #if login info is verified

        self.home = Home()
        self.home.show()
        #close login window
        gui.close()

    def createForm(self):
        layout = QFormLayout()
        bLogin = QPushButton("Login", self)
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.host = QLineEdit()
        self.db = QLineEdit()
        #layout.addRow(QLabel("Username:"), QLineEdit())
        layout.addRow(QLabel("Username:"), self.username)
        layout.addRow(QLabel("Password:"), self.password)
        layout.addRow(QLabel("Host:"), self.host)
        layout.addRow(QLabel("Database:"), self.db)
        layout.addRow(bLogin)
        bLogin.clicked.connect(self.onLoginClick)
        # set layout
        self.formGroupBox.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    gui.show()
    app.exec()
