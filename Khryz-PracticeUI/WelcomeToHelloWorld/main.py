from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
#from PySide2.QtCore import QSettings
from PySide2.QtGui import QIcon
from WTHW.gen.ui_sample import Ui_MainWindow 
import sys

# Window inherits from QtWidget -> has functions from QtWidgets.QMainWindow Class
# Inherits from Ui_MainWindow from ui_sample.py -> can use and adjust values from the QT Designer UI you made
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set window properties: title, size, icon
        self.setWindowTitle("Welcome to Hello World!")
        self.setGeometry(300,300,800,600) #(x,y,w,h)
        # Test QIcon
        self.setIcon()
        self.displayIcon()
        # Test back/next buttons
        self.ui.nextButton.clicked.connect(lambda: self.next_page())
        self.ui.backButton.clicked.connect(lambda: self.previous_page())
        # Test enter button
        self.ui.enterBtn.clicked.connect(lambda: self.enter_button())
        self.show() #show window
    # QIcon - display icon on the window
    def setIcon(self):
        appIcon = QIcon("icon.png") #need to find an image for this
        self.setWindowIcon(appIcon)

    # QIcon - display in app
    # WIP: turn off icon when in other pages
    def displayIcon(self):
        icon1 = QIcon("icon.png")
        label1 = QLabel('Logo', self)
        #label1.setIconSize(label1.size(100,100))
        if(self.ui.stackedWidget.currentIndex() == 0):
            pixmap1 = icon1.pixmap(100,100,QIcon.Normal,QIcon.On)
            label1.setPixmap(pixmap1)
            label1.move(175,130)
        else:
            label1 = icon1.pixmap(0,0,QIcon.Disabled,QIcon.Off)

    # next_page - next page via nextButton
    # WIP: turn off next button if on page_1
    def next_page(self):
         current_page = self.ui.stackedWidget.currentIndex()
         i = int(current_page) + 1
         self.ui.stackedWidget.setCurrentIndex(i)
    # previous_page - go back 1 page via backButton
    # WIP: turn off back button on page_3
    def previous_page(self):
        current_page = self.ui.stackedWidget.currentIndex()
        i = int(current_page) - 1
        self.ui.stackedWidget.setCurrentIndex(i)
    # enter_button - handles enter button in page_1
    # Takes in user input name and date of birth (DOB)
    # Should change Welcome text to Welcome {user name input}. Your DOB is{user DOB}
    # WIP: Line Edit fields should != NULL, provide empty field check -> display error message to user and do nothing (Set label: "Cannot be empty!")
    def enter_button(self):
        user_name = self.ui.nameFieldLE
        user_DOB = self.ui.DOBFieldLE
        self.ui.welcomeLabel.setText(f"Welcome {user_name.text()}. \nYour DOB is {user_DOB.text()}") 
        self.ui.welcomeLabel.adjustSize()

# Outside of Window Class
if __name__ == "__main__": 
    myApp = QApplication(sys.argv) #sys.argv: brings in any arguments from the system
    window = Window()
    
    myApp.exec_()
    sys.exit(0)