from PyQt5 import QtWidgets, QtGui, QtCore, uic

import os
import speech_recognition as sr

from asrInterface import Ui_MainWindow
import sys

import speech_recognition as sr

class myWindow(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def voiceBtnClick(self):
        r = sr.Recognizer()

        # Working with Microphones
        mic = sr.Microphone()
        with mic as source:
            # r.adjust_for_ambient_noise(source)
            audio = r.listen(source)        # 直到检测到静音时自动停止

        string = r.recognize_sphinx(audio)
        print("The statment you say is {",string,"}")
        if string.find("music",0, len(string)) != -1 or string.find("song",0,len(string))!=-1:
            os.startfile(r"Resources\CHINA-2.mp3")



app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())

