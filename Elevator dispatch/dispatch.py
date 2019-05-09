from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import time, threading
import collections
from PyQt5.QtCore import QTimer

from myElevatorInterface import *
import numpy as np
import time, threading, sched
import queue

OPEN = 0  # 开门装填
CLOSED = 1  # 关门状态

RUNNING = 2
# RUNNING_UP = 2  # 运行(向上)状态
# RUNNING_DOWN = 3  # 运行(向下)状态
STANDSTILL = 4  # 静止状态
READYSTART = 5  # 电梯即将运动
READYSTOP = 6

class Controler(object):
    def __init__(self, Elev):
        self.elev = Elev

        self.timer = QTimer()  # 初始化一个定时器
        self.timer.timeout.connect(self.updateElevState)  # 计时结束调用updateElevState()方法
        self.timer.start(1000)  # 设置计时间隔并启动

        self.messQueue = []  # 5个电梯内部消息列表(用列表代替队列)
        for i in range(0, 5):
            self.messQueue.append([])

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
            if self.elev.doorState[whichelev] == CLOSED and self.elev.elevState[
                whichelev] == STANDSTILL:  # 如果当前门是关闭状态并且电梯是静止的
                self.elev.doorState[whichelev] = OPEN  # 先将门状态更新为打开

                self.openDoor_Anim(whichelev)

        else:  # 如果用户要关门
            if self.elev.doorState[whichelev] == OPEN and self.elev.elevState[
                whichelev] == STANDSTILL:  # 如果当前门是打开状态并且电梯是静止的
                self.elev.doorState[whichelev] = CLOSED  # 先将门状态更新为关闭

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

        s = threading.Timer(1, self.setFigureTop, (whichelev,))  # 将人至于顶层
        s.start()

    # 将门至于顶层
    def setDoorTop(self, whichelev):
        self.elev.elevator_front[2 * whichelev].raise_()
        self.elev.elevator_front[2 * whichelev + 1].raise_()

    # 将小人至于顶层
    def setFigureTop(self, whichelev):
        self.elev.figure[whichelev].raise_()
        self.elev.figure[whichelev].setVisible(False)

    # 电梯运动
    def elevMove(self, whichelev, dest):
        nowFloor = self.elev.elevNow[whichelev]
        if nowFloor < dest:
            if self.elev.elevState[whichelev] == STANDSTILL:
                self.messQueue[whichelev].append(dest)
            else:
                self.messQueue[whichelev].append(dest)
                self.messQueue[whichelev].sort()


        print(self.messQueue[whichelev])


    # 更新电梯状态
    def updateElevState(self):
        # print('timer clock......')

        for i in range(0, len(self.messQueue)):
            if len(self.messQueue[i]):                      #某个电梯的消息队列不为空
                if self.elev.elevState[i]==STANDSTILL:      #电梯处于静止状态
                    self.openDoor_Anim(i)
                    self.figureIn_Anim(i)
                    self.elev.elevState[i] = READYSTART     #变为就绪运行状态
                elif self.elev.elevState[i]==READYSTART:    #电梯处于就绪运行状态
                    self.closeDoor_Anim(i)
                    self.elev.elevState[i]=RUNNING          #变为运行状态
                elif self.elev.elevState[i]==READYSTOP:     #电梯处于就绪停止状态
                    self.messQueue[i].pop(0)
                    self.closeDoor_Anim(i)
                    self.elev.elevState[i]=STANDSTILL       #变为静止状态
                else:
                    destFloor = self.messQueue[i][0]
                    if self.elev.elevNow[i] < destFloor:
                        self.elev.stateshow[i].setStyleSheet(
                                    "QGraphicsView{border-image: url(Resources/Button/state_up.png)}")
                        self.elev.elevNow[i] = self.elev.elevNow[i] + 1
                        self.elev.lcdNumber[i].setProperty("value", self.elev.elevNow[i])
                    elif self.elev.elevNow[i] == destFloor:
                        self.openDoor_Anim(i)
                        self.figureOut_Anim(i)
                        self.elev.elevState[i]=READYSTOP     #到达目的地变为就绪停止状态
                        button = self.elev.findChild(QtWidgets.QPushButton,
                                                         "button {0} {1}".format(i, self.elev.elevNow[i]))
                        button.setStyleSheet("")
                        button.setEnabled(True)




        # 电梯在运行过程中禁止点击报警键
        for i in range(0, 5):
            if self.elev.gridLayoutWidget[i].isEnabled():  # 如果这个电梯没被禁用
                if self.elev.elevState[i] == STANDSTILL:  # 如果电梯是静止的
                    self.elev.warnbtn[i].setEnabled(True)
                else:
                    self.elev.warnbtn[i].setEnabled(False)
