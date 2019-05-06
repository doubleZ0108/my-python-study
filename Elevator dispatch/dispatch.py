from myElevatorInterface import *
import numpy as np
import time

class Controler(object):
    def __init__(self, Elev):
        self.elev = Elev

    def warnCtrl(self, whichele):
        whichele = int(whichele)

        self.elev.elevEnabled[whichele] = False  #该电梯禁用

        self.elev.warnbtn[whichele].setEnabled(False)           #报警键禁用
        self.elev.gridLayoutWidget[whichele].setEnabled(False)  #楼层按键禁用
        self.elev.openbtn[whichele].setEnabled(False)           #开门键禁用
        self.elev.closebtn[whichele].setEnabled(False)          #关门键禁用
        self.elev.elevator[whichele].setEnabled(False)          #电梯禁用
        self.elev.label[whichele].setEnabled(False)             #电梯文字禁用
        self.elev.lcdNumber[whichele].setEnabled(False)         #数码管禁用
        self.elev.stateshow[whichele].setEnabled(False)         #上下行标志禁用

        arr = np.array(self.elev.elevEnabled)
        #五部电梯全部禁用
        if((arr == False).all()):
            self.elev.comboBox.setEnabled(False)        #下拉框禁用
            self.elev.chooselabel.setEnabled(False)     #文字禁用
            self.elev.upbtn.setEnabled(False)           #上行按钮禁用
            self.elev.downbtn.setEnabled(False)         #下行按钮禁用

            time.sleep(0.5)
            self.MessBox = QtWidgets.QMessageBox.information(self.elev, "警告","所有电梯已损坏!")
