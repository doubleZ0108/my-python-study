from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import time, threading
import collections

from myElevatorInterface import *
import numpy as np
import time, threading, sched
import queue

OPEN = 0
CLOSED = 1


class Controler(object):
    def __init__(self, Elev):
        self.elev = Elev

        update = threading.Timer(0.1, self.updateElevState)  # 第一次执行是0s之后
        update.start()

        self.messQueue = [queue.Queue()]*5   # 5个电梯内部消息队列


    # 警报器槽函数
    def warnCtrl(self, whichelev):
        self.elev.elevEnabled[whichelev] = False  # 该电梯禁用

        self.elev.warnbtn[whichelev].setEnabled(False)  # 报警键禁用
        self.elev.gridLayoutWidget[whichelev].setEnabled(False)  # 楼层按键禁用
        self.elev.openbtn[whichelev].setEnabled(False)  # 开门键禁用
        self.elev.closebtn[whichelev].setEnabled(False)  # 关门键禁用
        self.elev.elevator_back[whichelev].setEnabled(False)  # 电梯背景禁用
        self.elev.elevator_front[2 * whichelev].setEnabled(False)  # 电梯前门禁用
        self.elev.elevator_front[2 * whichelev + 1].setEnabled(False)  # 电梯前门禁用
        self.elev.elevator_Anim[2 * whichelev].stop()  # 停止动画
        self.elev.elevator_Anim[2 * whichelev + 1].stop()  # 停止动画
        self.elev.label[whichelev].setEnabled(False)  # 电梯文字禁用
        self.elev.lcdNumber[whichelev].setEnabled(False)  # 数码管禁用
        self.elev.stateshow[whichelev].setEnabled(False)  # 上下行标志禁用

        arr = np.array(self.elev.elevEnabled)
        # 五部电梯全部禁用
        if ((arr == False).all()):
            self.elev.comboBox.setEnabled(False)  # 下拉框禁用
            self.elev.chooselabel.setEnabled(False)  # 文字禁用
            self.elev.upbtn.setEnabled(False)  # 上行按钮禁用
            self.elev.downbtn.setEnabled(False)  # 下行按钮禁用

            time.sleep(0.5)
            self.MessBox = QtWidgets.QMessageBox.information(self.elev, "警告", "所有电梯已损坏!")

    # 开关门槽函数
    def doorCtrl(self, whichelev, whichcommand):
        if whichcommand == 0:  # 如果用户要开门
            if self.elev.elevState[whichelev] == CLOSED:  # 如果当前门是关闭状态
                self.elev.elevState[whichelev] = OPEN  # 先将门状态更新为打开

                self.openDoor_Anim(whichelev)

        else:  # 如果用户要关门
            if self.elev.elevState[whichelev] == OPEN:  # 如果当前门是打开状态
                self.elev.elevState[whichelev] = CLOSED  # 先将门状态更新为关闭

                self.closeDoor_Anim(whichelev)

    # 开门动画
    def openDoor_Anim(self, whichelev):
        self.elev.elevator_Anim[2 * whichelev].setDirection(QAbstractAnimation.Forward)  # 正向设定动画
        self.elev.elevator_Anim[2 * whichelev + 1].setDirection(QAbstractAnimation.Forward)
        self.elev.elevator_Anim[2 * whichelev].start()  # 开始播放
        self.elev.elevator_Anim[2 * whichelev + 1].start()

    # 关门动画
    def closeDoor_Anim(self, whichelev):
        self.elev.elevator_Anim[2 * whichelev].setDirection(QAbstractAnimation.Backward)  # 反向设定动画
        self.elev.elevator_Anim[2 * whichelev + 1].setDirection(QAbstractAnimation.Backward)
        self.elev.elevator_Anim[2 * whichelev].start()  # 开始播放
        self.elev.elevator_Anim[2 * whichelev + 1].start()

    # 小人进电梯动画
    def figureIn_Anim(self, whichelev):
        self.elev.figure[whichelev].setVisible(True)
        self.elev.figure_Anim[whichelev].setDirection(QAbstractAnimation.Forward)
        self.elev.figure_Anim[whichelev].start()

        s = threading.Timer(1.5, self.setDoorTop, (whichelev,))  # 1.5秒之后把门至于顶层
        s.start()

    # 小人出电梯动画
    def figureOut_Anim(self, whichelev):
        self.elev.figure[whichelev].setVisible(True)
        self.elev.figure_Anim[whichelev].setDirection(QAbstractAnimation.Backward)
        self.elev.figure_Anim[whichelev].start()

        s = threading.Timer(0, self.setFigureTop, (whichelev,))  # 将人至于顶层
        s.start()

    # 将门至于顶层
    def setDoorTop(self, whichelev):
        self.elev.elevator_front[2 * whichelev].raise_()
        self.elev.elevator_front[2 * whichelev + 1].raise_()

    # 将小人至于顶层
    def setFigureTop(self, whichelev):
        self.elev.figure[whichelev].raise_()

    # 电梯运动
    def elevMove(self, whichelev, source, dest):

        if source < dest:
            for i in range(source + 1, dest + 1, 1):
                self.elev.elevNow[whichelev] = i
                self.messQueue[whichelev].put([whichelev, i])

        elif source > dest:
            for i in range(source, dest - 1, -1):
                self.elev.elevNow[whichelev] = i
                self.messQueue[whichelev].put((whichelev, i))

    # 更新电梯状态
    def updateElevState(self):
        print('timer clock......')

        global update
        # 必须在定时器执行函数内部重复构造定时器
        update = threading.Timer(1, self.updateElevState)  # 之后是2s执行一次
        update.start()

        try:
            for i in range(0, 5):
                [whichelev, nowFloor] = self.messQueue[i].get()
                print(whichelev, nowFloor)
                self.elev.lcdNumber[whichelev].setProperty("value", nowFloor)
        except:
            print("消息队列为空...")
