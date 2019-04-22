import sys
import threading
import time

from PyQt5.QtWidgets import *

from untitled import *

import speech_recognition as sr

r = sr.Recognizer()

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

    # 语音识别函数
    def siri_recognition(self):
        global timer
        # 在定时器执行函数内部重复构造定时器
        timer = threading.Timer(5.0, self.siri_recognition)  # 之后是2s执行一次
        timer.start()

        # Working with Microphones
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)  # 直到检测到静音时自动停止

        try:
            command = r.recognize_sphinx(audio)
        except:
            print("无法读取内容")
        else:
            print('The statement you said is {' + command + '}')

    #定义槽函数
    def mouseDoubleClickEvent(self, event):
        self.label_7.setVisible(self.flag)
        self.label_8.setVisible(self.flag)

        # 交替显示
        if self.flag==True:
            self.flag=False
        else:
            self.flag=True

        # 操作指南 开/关
        self.label.setVisible(self.flag)
        self.label_2.setVisible(self.flag)
        self.label_3.setVisible(self.flag)
        self.label_4.setVisible(self.flag)
        self.label_5.setVisible(self.flag)
        self.label_6.setVisible(self.flag)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = mywindow()
    window.show()

    timer = threading.Timer(0, window.siri_recognition)  # 第一次执行0s后开始
    timer.start()

    # time.sleep(15)  # 15s之后停止定时器
    # print("Timer is end...")
    # timer.cancel()

    sys.exit(app.exec())
