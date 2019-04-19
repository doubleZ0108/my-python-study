import sys
import os

from PyQt5.QtWidgets import *

from myQt import *

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)


    #定义槽函数
    def messboxBtnClick(self):
        QtWidgets.QMessageBox.information(self.pushButton,"标题","这是第一个PyQt5 GUI程序")

    def calcBtnClick(self):
        os.system("C:\\Windows\\System32\\calc.exe")

    def musicBtnClick(self):
        os.startfile(r"Resources\CHINA-2.mp3")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec())
