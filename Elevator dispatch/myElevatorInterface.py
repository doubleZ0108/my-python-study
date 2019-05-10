# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from dispatch import Controler
from PyQt5.QtCore import *

OPEN = 0  # 开门装填
CLOSED = 1  # 关门状态

STANDSTILL = 0  # 静止状态
RUNNING_UP = 1  # 电梯上行状态
RUNNING_DOWN = 2  # 电梯下行状态

NOPE = 0  # 空动画
READYSTART = 1  # 电梯即将运动
READYSTOP = 2  # 电梯即将停止

GOUP = 1  # 用户要上行
GODOWN = 2  # 用户要下行


class Ui_MainWindow(object):
    def __init__(self):
        self.Ctrl = Controler(self)
        self.elevEnabled = [True] * 5  # 电梯状态(可使用/禁用)标志位
        self.doorState = [CLOSED] * 5  # 电梯门状态(开门/关门)标志位
        self.elevState = [STANDSTILL] * 5  # 电梯状态(/运行向上/运行向下/静止)标志位
        self.animState = [NOPE] * 5
        self.elevNow = [1] * 5  # 电梯楼层

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 700)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # region 墙模型
        wall_pos = [10, 280, 560, 840, 1120, 1390]
        self.wall = []
        for i in range(0, len(wall_pos)):
            self.wall.append(QtWidgets.QGraphicsView(self.centralwidget))
            self.wall[i].setGeometry(QtCore.QRect(wall_pos[i], 120, 10, 560))
            self.wall[i].setAutoFillBackground(False)
            self.wall[i].setStyleSheet("background-color: rgb(0, 0, 0);")
            self.wall[i].setObjectName("wall" + str(i))
        # endregion

        # region 电梯模型
        elevator_pos = [30, 300, 580, 860, 1140]
        self.elevator_back = []
        self.elevator_front = []
        self.elevator_Anim = []
        for i in range(0, len(elevator_pos)):
            # 后面的电梯背景
            self.elevator_back.append(QtWidgets.QGraphicsView(self.centralwidget))
            self.elevator_back[i].setGeometry(QtCore.QRect(elevator_pos[i], 470, 131, 161))
            self.elevator_back[i].setStyleSheet("background-color: rgb(87, 87, 87);")
            self.elevator_back[i].setObjectName("elevator_back" + str(i))

            # 前面的两扇电梯门
            self.elevator_front.append(QtWidgets.QGraphicsView(self.centralwidget))
            self.elevator_front[2 * i].setGeometry(QtCore.QRect(elevator_pos[i], 470, 64, 161))
            self.elevator_front[2 * i].setStyleSheet("background-color: rgb(160, 160, 160);")
            self.elevator_front[2 * i].setObjectName("elevator_front" + str(2 * i))
            self.elevator_Anim.append(QPropertyAnimation(self.elevator_front[2 * i], b"geometry"))
            self.elevator_Anim[2 * i].setDuration(1000)  # 设定动画时间
            self.elevator_Anim[2 * i].setStartValue(QtCore.QRect(elevator_pos[i], 470, 64, 161))  # 设置起始大小
            self.elevator_Anim[2 * i].setEndValue(QtCore.QRect(elevator_pos[i], 470, 8, 161))  # 设置终止大小

            self.elevator_front.append(QtWidgets.QGraphicsView(self.centralwidget))
            self.elevator_front[2 * i + 1].setGeometry(QtCore.QRect(elevator_pos[i] + 67, 470, 64, 161))
            self.elevator_front[2 * i + 1].setStyleSheet("background-color: rgb(160, 160, 160);")
            self.elevator_front[2 * i + 1].setObjectName("elevator_front" + str(2 * i + 1))
            self.elevator_Anim.append(QPropertyAnimation(self.elevator_front[2 * i + 1], b"geometry"))
            self.elevator_Anim[2 * i + 1].setDuration(1000)
            self.elevator_Anim[2 * i + 1].setStartValue(QtCore.QRect(elevator_pos[i] + 67, 470, 64, 161))
            self.elevator_Anim[2 * i + 1].setEndValue(QtCore.QRect(elevator_pos[i] + 123, 470, 8, 161))
        # endregion

        # region 电梯文字模型
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        label_pos = [70, 340, 620, 900, 1180]
        self.label = []
        for i in range(0, len(label_pos)):
            self.label.append(QtWidgets.QLabel(self.centralwidget))
            self.label[i].setGeometry(QtCore.QRect(label_pos[i], 640, 51, 21))
            self.label[i].setFont(font)
            self.label[i].setStyleSheet("font: 10pt \"AcadEref\";\n"
                                        "background-color: rgb(160, 160, 160);")
            self.label[i].setObjectName("label" + str(i))
        # endregion

        # region 电梯楼层数码管
        lcdNumber_pos = [50, 320, 600, 880, 1160]
        self.lcdNumber = []
        for i in range(0, len(lcdNumber_pos)):
            self.lcdNumber.append(QtWidgets.QLCDNumber(self.centralwidget))
            self.lcdNumber[i].setGeometry(QtCore.QRect(lcdNumber_pos[i], 420, 51, 41))
            self.lcdNumber[i].setDigitCount(2)
            self.lcdNumber[i].setProperty("value", 1.0)
            self.lcdNumber[i].setObjectName("lcdNumber" + str(i))
        # endregion

        # region 电梯上下行标志
        stateshow_pos = [95, 365, 645, 925, 1205]
        self.stateshow = []
        for i in range(0, len(stateshow_pos)):
            self.stateshow.append(QtWidgets.QGraphicsView(self.centralwidget))
            self.stateshow[i].setGeometry(QtCore.QRect(stateshow_pos[i], 410, 71, 61))
            self.stateshow[i].setStyleSheet("QGraphicsView{border-image: url(Resources/Button/state.png)}")
            self.stateshow[i].setObjectName("stateshow" + str(i))
        # endregion

        # region 门口按钮
        doorbtn_pos = [157, 427, 707, 987, 1267]
        self.updoorbtn = []
        self.downdoorbtn = []
        for i in range(0, len(doorbtn_pos)):
            # 上行按钮
            self.updoorbtn.append(QtWidgets.QPushButton(self.centralwidget))
            self.updoorbtn[i].setGeometry(QtCore.QRect(doorbtn_pos[i], 550, 35, 30))
            self.updoorbtn[i].setStyleSheet("QPushButton{border-image: url(Resources/Button/doorup.png)}"
                                            "QPushButton:hover{border-image: url(Resources/Button/doorup_hover.png)}"
                                            "QPushButton:pressed{border-image: url(Resources/Button/doorup_pressed.png)}")
            self.updoorbtn[i].setObjectName("updoorbtn" + str(i))

            # 上行按钮
            self.downdoorbtn.append(QtWidgets.QPushButton(self.centralwidget))
            self.downdoorbtn[i].setGeometry(QtCore.QRect(doorbtn_pos[i], 585, 35, 30))
            self.downdoorbtn[i].setStyleSheet("QPushButton{border-image: url(Resources/Button/doordown.png)}"
                                              "QPushButton:hover{border-image: url(Resources/Button/doordown_hover.png)}"
                                              "QPushButton:pressed{border-image: url(Resources/Button/doordown_pressed.png)}")
            self.downdoorbtn[i].setObjectName("downdoorbtn" + str(i))

            self.updoorbtn[i].clicked.connect(MainWindow.chooseClick)
            self.downdoorbtn[i].clicked.connect(MainWindow.chooseClick)
        # endregion

        # region 报警器模型
        warnbtn_pos = [190, 460, 740, 1020, 1300]
        self.warnbtn = []
        for i in range(0, len(warnbtn_pos)):
            self.warnbtn.append(QtWidgets.QPushButton(self.centralwidget))
            self.warnbtn[i].setGeometry(QtCore.QRect(warnbtn_pos[i] + 10, 620, 56, 31))
            self.warnbtn[i].setStyleSheet("background-color: rgb(180, 0, 0);")
            self.warnbtn[i].setObjectName("warnbtn" + str(i))
            self.warnbtn[i].isEnabled()

        # 绑定点击事件
        for i in range(0, len(self.warnbtn)):
            self.warnbtn[i].clicked.connect(MainWindow.warningClick)

        # endregion

        # region 楼层按键建模
        gridLayoutWidget_pos = [180, 450, 730, 1010, 1290]
        self.gridLayoutWidget = []
        self.gridLayout = []
        for i in range(0, len(gridLayoutWidget_pos)):
            self.gridLayoutWidget.append(QtWidgets.QWidget(self.centralwidget))
            self.gridLayoutWidget[i].setGeometry(QtCore.QRect(gridLayoutWidget_pos[i] + 10, 120, 81, 451))
            self.gridLayoutWidget[i].setObjectName("gridLayoutWidget" + str(i))
            self.gridLayout.append(QtWidgets.QGridLayout(self.gridLayoutWidget[i]))
            self.gridLayout[i].setContentsMargins(0, 0, 0, 0)
            self.gridLayout[i].setObjectName("gridLayout" + str(i))

        names = ['19', '20', '17', '18', '15', '16', '13', '14', '11', '12', '9', '10', '7', '8', '5', '6', '3', '4',
                 '1', '2']

        positions = [(i, j) for i in range(10) for j in range(2)]  # 构造五行四列的格子
        for i in range(0, len(gridLayoutWidget_pos)):
            for position, name in zip(positions, names):
                button = QtWidgets.QPushButton(name)
                button.setObjectName("button " + str(i) + ' ' + name)
                button.setStyleSheet("")
                button.clicked.connect(MainWindow.btnClick)
                self.gridLayout[i].addWidget(button, *position)  # 放到布局里
        # endregion

        # region 开关键模型
        openbtn_pos = [180, 450, 730, 1010, 1290]
        closebtn_pos = [230, 500, 780, 1060, 1340]
        self.openbtn = []
        self.closebtn = []
        for i in range(0, len(openbtn_pos)):
            self.openbtn.append(QtWidgets.QPushButton(self.centralwidget))
            self.openbtn[i].setGeometry(QtCore.QRect(openbtn_pos[i] + 10, 580, 31, 31))
            self.openbtn[i].setObjectName("openbtn" + str(i))
            self.closebtn.append(QtWidgets.QPushButton(self.centralwidget))
            self.closebtn[i].setGeometry(QtCore.QRect(closebtn_pos[i] + 10, 580, 31, 31))
            self.closebtn[i].setObjectName("closebtn" + str(i))

            self.openbtn[i].clicked.connect(MainWindow.doorClick)
            self.closebtn[i].clicked.connect(MainWindow.doorClick)
        # endregion

        # region 下拉框模型
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(630, 55, 111, 31))
        self.comboBox.setObjectName("comboBox")
        for i in range(0, 20):
            self.comboBox.addItem(str(i + 1))

        self.chooselabel = QtWidgets.QLabel(self.centralwidget)
        self.chooselabel.setGeometry(QtCore.QRect(450, 60, 161, 21))
        self.chooselabel.setObjectName("chooselabel")

        # 上行按钮
        self.upbtn = QtWidgets.QPushButton(self.centralwidget)
        self.upbtn.setGeometry(QtCore.QRect(760, 40, 51, 51))
        self.upbtn.setStyleSheet("QPushButton{border-image: url(Resources/Button/up.png)}"
                                 "QPushButton:hover{border-image: url(Resources/Button/up_hover.png)}"
                                 "QPushButton:pressed{border-image: url(Resources/Button/up_pressed.png)}")
        self.upbtn.setObjectName("upbtn")

        # 上行按钮
        self.downbtn = QtWidgets.QPushButton(self.centralwidget)
        self.downbtn.setGeometry(QtCore.QRect(810, 40, 51, 51))
        self.downbtn.setStyleSheet("QPushButton{border-image: url(Resources/Button/down.png)}"
                                   "QPushButton:hover{border-image: url(Resources/Button/down_hover.png)}"
                                   "QPushButton:pressed{border-image: url(Resources/Button/down_pressed.png)}")
        self.downbtn.setObjectName("downbtn")

        self.upbtn.clicked.connect(MainWindow.chooseClick)
        self.downbtn.clicked.connect(MainWindow.chooseClick)
        # endregion

        # region 小人模型
        figure_pos = [30, 300, 580, 860, 1140]
        self.figure = []
        self.figure_Anim = []
        for i in range(0, len(figure_pos)):
            self.figure.append(QtWidgets.QGraphicsView(self.centralwidget))
            self.figure[i].setGeometry(QtCore.QRect(figure_pos[i] - 20, 590, 71, 71))
            self.figure[i].setStyleSheet("QGraphicsView{border-image: url(Resources/Figure/people.png)}")
            self.figure[i].setVisible(False)
            self.figure[i].setObjectName("figure" + str(i))
            self.figure_Anim.append(QPropertyAnimation(self.figure[i], b"geometry"))
            self.figure_Anim[i].setDuration(1500)
            self.figure_Anim[i].setStartValue(QtCore.QRect(figure_pos[i] - 20, 590, 71, 71))
            self.figure_Anim[i].setEndValue(QtCore.QRect(figure_pos[i] + 10, 510, 111, 121))
        # endregion

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chooselabel.setText(_translate("MainWindow", "请选择你所在的楼层"))

        for i in range(0, len(self.label)):
            self.label[i].setText(_translate("MainWindow", "电梯" + str(i)))
            self.warnbtn[i].setText(_translate("MainWindow", "报警器"))
            self.openbtn[i].setText(_translate("MainWindow", "开"))
            self.closebtn[i].setText(_translate("MainWindow", "关"))

    def warningClick(self):
        which_warnbtn = int(self.sender().objectName()[-1])
        print("点击了{0}号报警器".format(which_warnbtn))
        self.warnbtn[which_warnbtn].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MessBox = QtWidgets.QMessageBox.information(self.warnbtn[int(which_warnbtn)], "警告",  # 弹出警告框
                                                         "第" + str(which_warnbtn) + "号电梯已损坏, 不能继续使用")
        self.warnbtn[which_warnbtn].setStyleSheet("background-color: rgb(180, 0, 0);")

        self.Ctrl.warnCtrl(which_warnbtn)  # 调用控制器进行warnCtrl处理

    def btnClick(self):
        whichbtn = self.sender()

        btn_name = whichbtn.objectName()
        buf = [int(s) for s in btn_name.split() if s.isdigit()]  # 提取字符串中的数字
        whichelev = buf[0]
        whichfloor = buf[1]
        print("{0}号电梯, {1}按键被按".format(whichelev, whichfloor))

        whichbtn.setStyleSheet("background-color: rgb(255, 150, 3);")
        whichbtn.setEnabled(False)
        self.Ctrl.elevMove(whichelev, whichfloor)

    def chooseClick(self):
        whichfloor = int(self.comboBox.currentText())
        whichbtn = self.sender().objectName()
        if whichbtn[0] == 'd':
            choice = GODOWN
        else:
            choice = GOUP

        print("用户选择了 {0} {1}".format(whichfloor, choice))

        self.Ctrl.chooseCtrl(whichfloor, choice)

    def doorClick(self):
        objectName = self.sender().objectName()
        whichelev = int(objectName[-1])
        whichcommand = 0 if objectName[0] == 'o' else 1  # 0 => 开门    1 => 关门
        print("{0}号电梯, 命令是{1}".format(whichelev, whichcommand))

        self.Ctrl.doorCtrl(whichelev, whichcommand)
