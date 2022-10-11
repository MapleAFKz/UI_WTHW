# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sample.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 535)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(150, 410, 491, 80))
        self.pagebuttons = QHBoxLayout(self.horizontalLayoutWidget)
        self.pagebuttons.setObjectName(u"pagebuttons")
        self.pagebuttons.setContentsMargins(0, 0, 0, 0)
        self.backButton = QPushButton(self.horizontalLayoutWidget)
        self.backButton.setObjectName(u"backButton")

        self.pagebuttons.addWidget(self.backButton)

        self.nextButton = QPushButton(self.horizontalLayoutWidget)
        self.nextButton.setObjectName(u"nextButton")

        self.pagebuttons.addWidget(self.nextButton)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 10, 751, 391))
        self.frame_pages = QVBoxLayout(self.verticalLayoutWidget_3)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.verticalLayoutWidget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.welcomeLabel = QLabel(self.page_1)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        self.welcomeLabel.setGeometry(QRect(280, 100, 169, 78))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcomeLabel.sizePolicy().hasHeightForWidth())
        self.welcomeLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.welcomeLabel.setFont(font)
        self.verticalLayoutWidget = QWidget(self.page_1)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(190, 190, 321, 71))
        self.formLayout_2 = QFormLayout(self.verticalLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.enterNamePrompt = QLabel(self.verticalLayoutWidget)
        self.enterNamePrompt.setObjectName(u"enterNamePrompt")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.enterNamePrompt)

        self.nameFieldLE = QLineEdit(self.verticalLayoutWidget)
        self.nameFieldLE.setObjectName(u"nameFieldLE")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.nameFieldLE)

        self.DOBPrompt = QLabel(self.verticalLayoutWidget)
        self.DOBPrompt.setObjectName(u"DOBPrompt")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.DOBPrompt)

        self.DOBFieldLE = QLineEdit(self.verticalLayoutWidget)
        self.DOBFieldLE.setObjectName(u"DOBFieldLE")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.DOBFieldLE)

        self.enterBtn = QPushButton(self.page_1)
        self.enterBtn.setObjectName(u"enterBtn")
        self.enterBtn.setGeometry(QRect(300, 280, 151, 51))
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayoutWidget_2 = QWidget(self.page_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(590, 70, 131, 71))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.genderLabel = QLabel(self.verticalLayoutWidget_2)
        self.genderLabel.setObjectName(u"genderLabel")

        self.verticalLayout.addWidget(self.genderLabel)

        self.genderBtn_Male = QRadioButton(self.verticalLayoutWidget_2)
        self.genderBtn_Male.setObjectName(u"genderBtn_Male")

        self.verticalLayout.addWidget(self.genderBtn_Male)

        self.genderBtn_Female = QRadioButton(self.verticalLayoutWidget_2)
        self.genderBtn_Female.setObjectName(u"genderBtn_Female")

        self.verticalLayout.addWidget(self.genderBtn_Female)

        self.formLayoutWidget = QWidget(self.page_2)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(290, 70, 166, 161))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.occLabel = QLabel(self.formLayoutWidget)
        self.occLabel.setObjectName(u"occLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.occLabel)

        self.checkBox = QCheckBox(self.formLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.checkBox)

        self.checkBox_2 = QCheckBox(self.formLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.formLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.formLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.formLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.checkBox_5)

        self.formLayoutWidget_2 = QWidget(self.page_2)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(40, 70, 151, 51))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.weightLabel = QLabel(self.formLayoutWidget_2)
        self.weightLabel.setObjectName(u"weightLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.weightLabel)

        self.heightLabel = QLabel(self.formLayoutWidget_2)
        self.heightLabel.setObjectName(u"heightLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.heightLabel)

        self.weightSpinBox = QDoubleSpinBox(self.formLayoutWidget_2)
        self.weightSpinBox.setObjectName(u"weightSpinBox")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.weightSpinBox)

        self.heightSpinBox = QDoubleSpinBox(self.formLayoutWidget_2)
        self.heightSpinBox.setObjectName(u"heightSpinBox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.heightSpinBox)

        self.horizontalLayoutWidget_2 = QWidget(self.page_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(220, 300, 301, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.readFromRegBtn = QPushButton(self.horizontalLayoutWidget_2)
        self.readFromRegBtn.setObjectName(u"readFromRegBtn")

        self.horizontalLayout.addWidget(self.readFromRegBtn)

        self.writeToRegBtn = QPushButton(self.horizontalLayoutWidget_2)
        self.writeToRegBtn.setObjectName(u"writeToRegBtn")

        self.horizontalLayout.addWidget(self.writeToRegBtn)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(20, 10, 701, 291))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayoutWidget_3 = QWidget(self.tab)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(150, 40, 361, 171))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.formLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_4 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_8 = QLabel(self.formLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_3 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_9 = QLabel(self.formLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_5 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.lineEdit_5)

        self.label_10 = QLabel(self.formLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_10)

        self.label_12 = QLabel(self.formLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.label_11 = QLabel(self.formLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_6 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.lineEdit_8)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayoutWidget_5 = QWidget(self.tab_2)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(150, 40, 361, 171))
        self.formLayout_6 = QFormLayout(self.formLayoutWidget_5)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.formLayoutWidget_5)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_19)

        self.lineEdit_15 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.lineEdit_15)

        self.label_20 = QLabel(self.formLayoutWidget_5)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_20)

        self.lineEdit_16 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.lineEdit_16)

        self.label_21 = QLabel(self.formLayoutWidget_5)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_21)

        self.lineEdit_17 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.lineEdit_17)

        self.label_22 = QLabel(self.formLayoutWidget_5)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.label_22)

        self.label_23 = QLabel(self.formLayoutWidget_5)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_6.setWidget(5, QFormLayout.LabelRole, self.label_23)

        self.label_24 = QLabel(self.formLayoutWidget_5)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_6.setWidget(6, QFormLayout.LabelRole, self.label_24)

        self.lineEdit_18 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.lineEdit_18)

        self.lineEdit_19 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.formLayout_6.setWidget(5, QFormLayout.FieldRole, self.lineEdit_19)

        self.lineEdit_20 = QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.formLayout_6.setWidget(6, QFormLayout.FieldRole, self.lineEdit_20)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.formLayoutWidget_4 = QWidget(self.tab_3)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(150, 40, 361, 171))
        self.formLayout_5 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.formLayoutWidget_4)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_9 = QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.lineEdit_9)

        self.label_14 = QLabel(self.formLayoutWidget_4)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_10 = QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.lineEdit_10)

        self.label_15 = QLabel(self.formLayoutWidget_4)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_15)

        self.lineEdit_11 = QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_16 = QLabel(self.formLayoutWidget_4)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(self.formLayoutWidget_4)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_17)

        self.label_18 = QLabel(self.formLayoutWidget_4)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.label_18)

        self.lineEdit_12 = QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.lineEdit_12)

        self.lineEdit_13 = QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.lineEdit_14)

        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayoutWidget_3 = QWidget(self.page_3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(230, 310, 271, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.loadPreBtn = QPushButton(self.horizontalLayoutWidget_3)
        self.loadPreBtn.setObjectName(u"loadPreBtn")

        self.horizontalLayout_2.addWidget(self.loadPreBtn)

        self.savePreBtn = QPushButton(self.horizontalLayoutWidget_3)
        self.savePreBtn.setObjectName(u"savePreBtn")

        self.horizontalLayout_2.addWidget(self.savePreBtn)

        self.stackedWidget.addWidget(self.page_3)

        self.frame_pages.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 780, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.welcomeLabel.setText(QCoreApplication.translate("MainWindow", u"Welcome to HelloWorld!", None))
        self.enterNamePrompt.setText(QCoreApplication.translate("MainWindow", u"Enter your name", None))
        self.DOBPrompt.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.enterBtn.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.genderLabel.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.genderBtn_Male.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.genderBtn_Female.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.occLabel.setText(QCoreApplication.translate("MainWindow", u"Occupation:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Twitch Streamer", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Software Engineer", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Chef", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Police", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Secret Agent", None))
        self.weightLabel.setText(QCoreApplication.translate("MainWindow", u"Weight (kg)", None))
        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"Height (m)", None))
        self.readFromRegBtn.setText(QCoreApplication.translate("MainWindow", u"Read from Windows Registry", None))
        self.writeToRegBtn.setText(QCoreApplication.translate("MainWindow", u"Write to Windows Registry", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Date of Birth:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Occupation:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Weight:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Preset 1", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Date of Birth:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Occupation:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Weight:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Preset 2", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Date of Birth:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Occupation:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Weight:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Preset 3", None))
        self.loadPreBtn.setText(QCoreApplication.translate("MainWindow", u"Load Preset", None))
        self.savePreBtn.setText(QCoreApplication.translate("MainWindow", u"Save Preset", None))
    # retranslateUi

