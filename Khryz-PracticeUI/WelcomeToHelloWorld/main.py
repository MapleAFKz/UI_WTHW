from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QSettings, QObject
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QCheckBox, QDoubleSpinBox, QRadioButton, QLineEdit, QSpinBox
from PySide2.QtGui import QIcon

#from WTHW.gen.ui_sample import Ui_MainWindow        # Test WTHW UI
from WTHW.gen.ui_Preset_Setup import Ui_Preset_Setup

from distutils.util import strtobool        # For read_from_reg function

import logging
import base64
import uuid
import sys

# Window inherits from QtWidget -> has functions from QtWidgets.QMainWindow Class
# Inherits from Ui_MainWindow from ui_sample.py -> can use and adjust values from the QT Designer UI you made
class Window(QMainWindow):
    def __init__(self):
        # Required 
        super().__init__()
        self.ui = Ui_Preset_Setup()
        self.ui.setupUi(self)
        self.uuid = uuid.uuid4()    # For testing purpose: use uuid4() to generate random uuid (session based), otherwise use uuid1() for machine based
        
        # Preset values
        #self.ui.Voltage_Preset_spinBox.valueChanged.connect(lambda: self.ui.Voltage_Preset_spinBox.setValue())
        #self.ui.Amperage_Preset_spinBox.valueChanged.connect(lambda: self.ui.Amperage_Preset_spinBox.setValue())
        #self.ui.Exposure_Preset_spinBox.valueChanged.connect(lambda: self.ui.Exposure_Preset_spinBox.setValue())
        #self.ui.Averaging_Preset_spinBox.valueChanged.connect(lambda: self.ui.Averaging_Preset_spinBox.setValue())
        # Positions (x, y, z)
        #self.ui.posX_Preset_doubleSpinBox.valueChanged.connect(lambda: self.ui.posX_Preset_doubleSpinBox.setValue())
        #self.ui.posY_Preset_doubleSpinBox.valueChanged.connect(lambda: self.ui.posY_Preset_doubleSpinBox.setValue())
        #self.ui.posZ_Preset_doubleSpinBox.valueChanged.connect(lambda: self.ui.posZ_Preset_doubleSpinBox.setValue())

        #self.ui.Load_CurrentValues_Button.clicked.connect(lambda: self.load_preset())
        self.ui.Create_NewPreset_Button.clicked.connect(lambda: self.create_preset())      # Need to rename
        self.settings = QSettings('Creative Electron Inc.', 'TruView NEXT')  
        self.show() 

   

    #   create_preset()
    #   saves into registry
    def create_preset(self):
        # CheckBoxes - the state of each checkbox to be used in the include to preset check
        if isinstance(self.ui.Voltage_Preset_checkBox, QCheckBox):
            name = self.ui.Voltage_Preset_checkBox.objectName()                  # assign widget name
            Include_Voltage = self.ui.Voltage_Preset_checkBox.isChecked()        # value to be written and stored into registry
            #self.settings.setValue(name, Include_Voltage)                        # set the state into name(obj)
        if isinstance(self.ui.Amperage_Preset_checkBox, QCheckBox):
            name = self.ui.Amperage_Preset_checkBox.objectName()        
            Include_Amperage = self.ui.Amperage_Preset_checkBox.isChecked()        
            #self.settings.setValue(name, Include_Amperage)   
        if isinstance(self.ui.Exposure_Preset_checkBox, QCheckBox):
            name = self.ui.Exposure_Preset_checkBox.objectName()        
            Include_Exposure = self.ui.Exposure_Preset_checkBox.isChecked()        
            #self.settings.setValue(name, Include_Exposure)
        if isinstance(self.ui.Averaging_Preset_checkBox, QCheckBox):
            name = self.ui.Averaging_Preset_checkBox.objectName()        
            Include_Averaging = self.ui.Averaging_Preset_checkBox.isChecked()        
            #self.settings.setValue(name, Include_Averaging)
        if isinstance(self.ui.Position_Preset_checkBox, QCheckBox):
            name = self.ui.Position_Preset_checkBox.objectName()        
            Include_Position = self.ui.Position_Preset_checkBox.isChecked()        
            #self.settings.setValue(name, Include_Position)

        # SpinBoxes - numerical values for Voltage, Amperage, Exposure, Averaging
        if isinstance(self.ui.Voltage_Preset_spinBox, QSpinBox):
            name = self.ui.Voltage_Preset_spinBox.objectName()
            voltage_value = self.ui.Voltage_Preset_spinBox.value()
            #self.settings.setValue(name, voltage_value)

        if isinstance(self.ui.Amperage_Preset_spinBox, QSpinBox):
            name = self.ui.Amperage_Preset_spinBox.objectName()
            amperage_value = self.ui.Amperage_Preset_spinBox.value()
            #self.settings.setValue(name, amperage_value)

        if isinstance(self.ui.Exposure_Preset_spinBox, QSpinBox):
            name = self.ui.Exposure_Preset_spinBox.objectName()
            exposure_value = self.ui.Exposure_Preset_spinBox.value()
            #self.settings.setValue(name, exposure_value)

        if isinstance(self.ui.Averaging_Preset_spinBox, QSpinBox):
            name = self.ui.Averaging_Preset_spinBox.objectName()
            averaging_value = self.ui.Averaging_Preset_spinBox.value()
            #self.settings.setValue(name, averaging_value)

        if isinstance(self.ui.Voltage_Preset_spinBox, QSpinBox):
            name = self.ui.Voltage_Preset_spinBox.objectName()
            voltage_value = self.ui.Voltage_Preset_spinBox.value()
            #self.settings.setValue(name, voltage_value)

        # DoubleSpinBoxes - Position X, Z, Y
        if isinstance(self.ui.posX_Preset_doubleSpinBox, QDoubleSpinBox):
            name = self.ui.posX_Preset_doubleSpinBox.objectName()
            posx_value = self.ui.posX_Preset_doubleSpinBox.value()
            #self.settings.setValue(name, float(posx_value))
        if isinstance(self.ui.posZ_Preset_doubleSpinBox, QDoubleSpinBox):
            name = self.ui.posZ_Preset_doubleSpinBox.objectName()
            posz_value = self.ui.posZ_Preset_doubleSpinBox.value()
            #self.settings.setValue(name, float(posz_value))
        if isinstance(self.ui.posY_Preset_doubleSpinBox, QDoubleSpinBox):
            name = self.ui.posY_Preset_doubleSpinBox.objectName()
            posy_value = self.ui.posY_Preset_doubleSpinBox.value()
            #self.settings.setValue(name, float(posy_value))

        # Save the state of CheckBoxes for Voltage, Amperage, Exposure, Averaging, Position
        self.settings.setValue(f'presets/{self.uuid}/Include_Voltage', Include_Voltage)
        self.settings.setValue(f'presets/{self.uuid}/Include_Amperage', Include_Amperage)
        self.settings.setValue(f'presets/{self.uuid}/Include_Exposure', Include_Exposure)
        self.settings.setValue(f'presets/{self.uuid}/Include_Averaging', Include_Averaging)
        self.settings.setValue(f'presets/{self.uuid}/Include_Position', Include_Position)
        # Save values for Voltage, Amperage, Exposure, Averaging, Position
        self.settings.setValue(f'presets/{self.uuid}/Voltage', voltage_value)
        self.settings.setValue(f'presets/{self.uuid}/Amperage', amperage_value)
        self.settings.setValue(f'presets/{self.uuid}/Exposure', exposure_value)
        self.settings.setValue(f'presets/{self.uuid}/Averaging', averaging_value)
        # Save values for PosX, Z, Y
        self.settings.setValue(f'presets/{self.uuid}/Position X', float(posx_value))
        self.settings.setValue(f'presets/{self.uuid}/Position Z', float(posz_value))
        self.settings.setValue(f'presets/{self.uuid}/Position Y', float(posy_value))

    def load(self):
        pass

   
    def delete(self):     
       self.settings2.beginGroup("presets")   
       self.settings2.remove(self.uuid)
       self.app.user_info_logging("deleted a presets")
       ll.info("User deleted a preset")


    @staticmethod
    def get_uuids():     
        self.settings.beginGroup("presets")    # stores uuid's keys into Computer\HKEY_CURRENT_USER\SOFTWARE\Creative Electron Inc.\TruView NEXT\users\presets 
        uuids = settings.childGroups() # returns all the keys from presets into uuids?
        return uuids

  

# Runner
if __name__ == "__main__": 
    myApp = QApplication(sys.argv)      # sys.argv: brings in any arguments from the system
    window = Window()
    
    myApp.exec_()
    sys.exit(0)