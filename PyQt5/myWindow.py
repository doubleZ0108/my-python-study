import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from myQt import *

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

    #定义槽函数
    def myButtonClick(self):
        QtWidgets.QMessageBox.information(self.pushButton,"标题","这是第一个PyQt5 GUI程序")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec())
