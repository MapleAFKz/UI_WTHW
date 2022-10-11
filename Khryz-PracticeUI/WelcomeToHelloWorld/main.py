from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QSettings #PyQt5
#from PyQt5.QtWidgets import QApplication, QWidget
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QCheckBox, QDoubleSpinBox, QRadioButton
from PySide2.QtGui import QIcon
from WTHW.gen.ui_sample import Ui_MainWindow 
from distutils.util import strtobool
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
        self.setGeometry(300,300,800,600)       # (x,y,w,h)
        # Test QIcon
        self.setIcon()
        self.displayIcon()
        # Test back/next buttons
        self.ui.nextButton.clicked.connect(lambda: self.next_page())
        self.ui.backButton.clicked.connect(lambda: self.previous_page())
        # Test enter button
        self.ui.enterBtn.clicked.connect(lambda: self.enter_button())
        # Test spinbox for weight and height - deprecated
        #self.ui.weightSpinBox.valueChanged.connect(lambda: self.set_weight())
        #self.ui.heightSpinBox.valueChanged.connect(lambda: self.set_height())
        # Test checkbox for occupation
        self.ui.writeToRegBtn.clicked.connect(lambda: self.write_to_reg())
        self.ui.readFromRegBtn.clicked.connect(lambda: self.read_from_reg())        
        # QSetting for read/write to Windows Registry
        self.settings = QSettings('Creative Electron Inc.', 'KhryzWTHW')
        print(self.settings.fileName())
        self.show() 

    # QIcon - display icon on the window
    def setIcon(self):
        appIcon = QIcon("icon.png") 
        self.setWindowIcon(appIcon)

    # QIcon - display in app
    # WIP: turn off icon when in other pages (not page_1)
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
            #label1.setVisible(False)

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

    # Writes values to registry - currently only used for ui.page_2
    # WIP: needs to write value from SpinBox to registry
    def write_to_reg(self):
        # Checkboxes - handles occupation select
        if isinstance(self.ui.checkBox, QCheckBox):
            name = self.ui.checkBox.objectName()          # assign widget name
            state_1 = self.ui.checkBox.isChecked()        # value to be written and stored into registry
            self.settings.setValue(name, state_1)         # set the state into name
        if isinstance(self.ui.checkBox_2, QCheckBox):
            name = self.ui.checkBox_2.objectName()        
            state_2 = self.ui.checkBox_2.isChecked()        
            self.settings.setValue(name, state_2)   
        if isinstance(self.ui.checkBox_3, QCheckBox):
            name = self.ui.checkBox_3.objectName()        
            state_3 = self.ui.checkBox_3.isChecked()        
            self.settings.setValue(name, state_3)
        if isinstance(self.ui.checkBox_4, QCheckBox):
            name = self.ui.checkBox_4.objectName()        
            state_4 = self.ui.checkBox_4.isChecked()        
            self.settings.setValue(name, state_4)
        if isinstance(self.ui.checkBox_5, QCheckBox):
            name = self.ui.checkBox_5.objectName()        
            state_5 = self.ui.checkBox_5.isChecked()        
            self.settings.setValue(name, state_5)
        # RadioButtons - handles gender select
        if isinstance(self.ui.genderBtn_Female, QRadioButton):
            name = self.ui.genderBtn_Female.objectName()
            isFemale = self.ui.genderBtn_Female.isChecked()
            self.settings.setValue(name, isFemale)
        if isinstance(self.ui.genderBtn_Male, QRadioButton):
            name = self.ui.genderBtn_Male.objectName()
            isMale = self.ui.genderBtn_Male.isChecked()
            self.settings.setValue(name, isMale)
        
        # Testing: Spinbox values to be saved
        if isinstance(self.ui.weightSpinBox, QDoubleSpinBox):
            name = self.ui.weightSpinBox.objectName()
            user_weight = self.ui.weightSpinBox.value()
            self.settings.setValue(name, user_weight)

        if isinstance(self.ui.heightSpinBox, QDoubleSpinBox):
            name = self.ui.heightSpinBox.objectName()
            user_height = self.ui.heightSpinBox.value()
            self.settings.setValue(name, user_height)


    # Read CheckBox state from registry, load into GUI
    # Values are from CheckBoxes(Occupation), RadioButtons(Gender), SpinBoxes(Weight and Height)
    def read_from_reg(self):
        # CheckBoxes - any # can be active/inactive
        if isinstance(self.ui.checkBox, QCheckBox):
            name = self.ui.checkBox.objectName()
            value = self.settings.value(name)       # stored value from registry
            if value != None:
                self.ui.checkBox.setChecked(strtobool(value))       # sets isChecked state based on what is stored
        if isinstance(self.ui.checkBox_2, QCheckBox):
            name = self.ui.checkBox_2.objectName()
            value = self.settings.value(name)       
            if value != None:
                self.ui.checkBox_2.setChecked(strtobool(value))    
        if isinstance(self.ui.checkBox_3, QCheckBox):
            name = self.ui.checkBox_3.objectName()
            value = self.settings.value(name)       
            if value != None:
                self.ui.checkBox_3.setChecked(strtobool(value))  

        if isinstance(self.ui.checkBox_4, QCheckBox):
            name = self.ui.checkBox_4.objectName()
            value = self.settings.value(name)       
            if value != None:
                self.ui.checkBox_4.setChecked(strtobool(value))  
        if isinstance(self.ui.checkBox_5, QCheckBox):
            name = self.ui.checkBox_5.objectName()
            value = self.settings.value(name)       
            if value != None:
                self.ui.checkBox_5.setChecked(strtobool(value))  
        # RadioButtons - only one can be active
        if isinstance(self.ui.genderBtn_Female, QRadioButton):
            name = self.ui.genderBtn_Female.objectName()
            value = self.settings.value(name)
            if value != None:
                self.ui.genderBtn_Female.setChecked(strtobool(value))
        elif isinstance(self.ui.genderBtn_Male, QRadioButton):
            name = self.ui.genderBtn_Male.objectName()
            value = self.settings.value(name)
            if value != None:
                self.ui.genderBtn_Male.setChecked(strtobool(value))

        # SpinBoxes - just needs to return a double (or int if using an int SpinBox)
        if isinstance(self.ui.weightSpinBox, QDoubleSpinBox):
            name = self.ui.weightSpinBox.objectName()
            value = self.settings.value(name)
            if value != None:
                self.ui.weightSpinBox.setValue(float(value))

        if isinstance(self.ui.heightSpinBox, QDoubleSpinBox):
            name = self.ui.heightSpinBox.objectName()
            value = self.settings.value(name)
            if value != None:
                self.ui.heightSpinBox.setValue(float(value))

# Outside of Window Class
if __name__ == "__main__": 
    myApp = QApplication(sys.argv)      # sys.argv: brings in any arguments from the system
    window = Window()
    
    myApp.exec_()
    sys.exit(0)