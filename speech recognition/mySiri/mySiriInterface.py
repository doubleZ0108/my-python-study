# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 647)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.flag = False

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setVisible(False)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setVisible(False)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 320, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setVisible(False)
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 230, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setVisible(False)
        self.label_4.setStyleSheet("color: rgb(241, 162, 183);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 290, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setVisible(False)
        self.label_5.setStyleSheet("color: rgb(241, 162, 183);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 350, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setVisible(False)
        self.label_6.setStyleSheet("color: rgb(241, 162, 183);")
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setVisible(True)
        self.label_7.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 250, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setVisible(True)
        self.label_8.setStyleSheet("color: rgb(223, 175, 135);")
        self.label_8.setObjectName("label_8")


        self.siriGif = QtWidgets.QLabel(self.centralwidget)
        self.siriGif.setGeometry(QtCore.QRect(70, 450, 271, 131))
        self.siriGif.setText("")
        self.gif = QMovie("Resources/icon/siri.gif")
        self.siriGif.setMovie(self.gif)
        self.gif.start()
        self.siriGif.setScaledContents(True)
        self.siriGif.setObjectName("voiceFig")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 450, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setVisible(False)
        self.label_9.setStyleSheet("color: rgb(223, 175, 135);")
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(100, 200, 401, 51))
        font = QtGui.QFont()
        self.label_10.setVisible(False)
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(241, 162, 183);")
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(100, 250, 401, 51))
        font = QtGui.QFont()
        self.label_11.setVisible(False)
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(223, 175, 135);")
        self.label_11.setObjectName("label_11")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "myKerr"))
        self.label.setText(_translate("MainWindow", "1. Enjoy music by saying"))
        self.label_2.setText(_translate("MainWindow", "2. Take some notes by saying"))
        self.label_3.setText(_translate("MainWindow", "3. Do math work by saying"))
        self.label_4.setText(_translate("MainWindow", "Play music"))
        self.label_5.setText(_translate("MainWindow", "Open Notepad"))
        self.label_6.setText(_translate("MainWindow", "Open the calculator"))
        self.label_7.setText(_translate("MainWindow", "\"Hey Kerr\" to wake me!"))
        self.label_8.setText(_translate("MainWindow", "Double Click me to know more!"))
        self.label_9.setText(_translate("MainWindow", "Sorry, I can\'t here your clearly!"))
        self.label_10.setText(_translate("MainWindow", "Kerr is here!"))
        self.label_11.setText(_translate("MainWindow", "What can I do for you?"))


import Resources_rc
