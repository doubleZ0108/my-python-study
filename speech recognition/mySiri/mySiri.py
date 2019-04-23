import sys, threading, time, difflib
from PyQt5.QtWidgets import *
import speech_recognition as sr

from untitled import *


r = sr.Recognizer()

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

    # 语音识别函数
    def siri_recognition(self):
        global timer
        # 在定时器执行函数内部重复构造定时器
        timer = threading.Timer(5.0, self.siri_recognition)  # 之后是5s执行一次
        timer.start()
        print("Time clock...")

        # Working with Microphones
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)  # 直到检测到静音时自动停止

        try:
            command = r.recognize_sphinx(audio)
        except:
            print("无法读取内容")
            self.RecognitionFailed()
        else:
            print('The statement you said is {' + command + '}')
            similar = string_similar(command, "Hey Kerr")
            print("The similar is ", similar)

            if similar > 0.1 or string_similar(command, "what") > 0.5:    # 第二个条件是为了提高唤醒概率(测试用)
                self.WakeSuccess()
            else:
                 self.WakeFailed()


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

    def RecognitionFailed(self):
        self.label_9.setVisible(True)
        time.sleep(2)
        self.label_9.setVisible(False)

    def WakeSuccess(self):
        print("wake success!")
        global timer
        timer.cancel()
        self.label_7.setVisible(False)
        self.label_8.setVisible(False)
        self.label_10.setVisible(True)
        self.label_11.setVisible(True)


        time.sleep(5)


        self.label_7.setVisible(True)
        self.label_8.setVisible(True)
        self.label_10.setVisible(False)
        self.label_11.setVisible(False)
        timer = threading.Timer(0, self.siri_recognition)
        timer.start()

    def WakeFailed(self):
        print("wake failed!")


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
