import sys

from PyQt5.QtWidgets import *

from untitled import *

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)


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
    sys.exit(app.exec())
