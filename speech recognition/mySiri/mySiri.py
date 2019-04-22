import sys
import os

from PyQt5.QtWidgets import *

from untitled import *

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)


    #定义槽函数
    def mouseDoubleClickEvent(self, event):
        os.system("C:\\Windows\\System32\\calc.exe")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec())
