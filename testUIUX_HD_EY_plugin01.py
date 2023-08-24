# C:\Users\besti\Documents\Autodesk\Vred-15.0\ScriptPlugins\testUIUX_01
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(489, 639)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 40, 141, 41))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 90, 441, 191))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 50, 101, 41))
        self.comboBox.setAutoFillBackground(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 251, 21))
        self.radioButton = QRadioButton(self.frame)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(200, 50, 51, 31))
        self.radioButton_2 = QRadioButton(self.frame)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(310, 50, 71, 31))
        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(20, 120, 101, 41))
        self.comboBox_2.setAutoFillBackground(False)
        self.radioButton_3 = QRadioButton(self.frame)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(200, 120, 51, 31))
        self.radioButton_4 = QRadioButton(self.frame)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(310, 120, 71, 31))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(210, 50, 131, 23))
        self.progressBar.setValue(24)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(380, 290, 91, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"func_Tumbler", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"func_creditCard", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"func_powerBank", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc81c\uc5b4\ud560 \ubb3c\ub958\ub97c \uc120\ud0dd\ud558\uace0 On/Off \ud558\uc138\uc694", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"func_Tumbler", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"func_creditCard", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"func_powerBank", None))

        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi