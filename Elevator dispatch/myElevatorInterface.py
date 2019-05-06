# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myElevatorInterface.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 700)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 墙模型
        wall_pos = [10, 280, 560, 840, 1120, 1380]
        self.wall = []
        for i in range(0, len(wall_pos)):
            self.wall.append(QtWidgets.QGraphicsView(self.centralwidget))
            self.wall[i].setGeometry(QtCore.QRect(wall_pos[i], 120, 10, 560))
            self.wall[i].setAutoFillBackground(False)
            self.wall[i].setStyleSheet("background-color: rgb(0, 0, 0);")
            self.wall[i].setObjectName("wall" + str(i))

        #电梯模型
        elevator_pos = [30, 300, 580, 860, 1140]
        self.elevator = []
        for i in range(0,len(elevator_pos)):
            self.elevator.append(QtWidgets.QGraphicsView(self.centralwidget))
            self.elevator[i].setGeometry(QtCore.QRect(elevator_pos[i], 470, 131, 161))
            self.elevator[i].setStyleSheet("background-color: rgb(160, 160, 160);")
            self.elevator[i].setObjectName("elevator" + str(i))


        #电梯文字模型
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


        #电梯楼层数码管
        lcdNumber_pos = [70, 340, 620, 900, 1180]
        self.lcdNumber = []
        for i in range(0, len(lcdNumber_pos)):
            self.lcdNumber.append(QtWidgets.QLCDNumber(self.centralwidget))
            self.lcdNumber[i].setGeometry(QtCore.QRect(lcdNumber_pos[i], 420, 51, 41))
            self.lcdNumber[i].setDigitCount(2)
            self.lcdNumber[i].setProperty("value", 1.0)
            self.lcdNumber[i].setObjectName("lcdNumber" + str(i))


        # 报警器模型
        warnbtn_pos = [190, 470, 750, 1030, 1310]
        self.warnbtn = []
        for i in range(0, len(warnbtn_pos)):
            self.warnbtn.append(QtWidgets.QPushButton(self.centralwidget))
            self.warnbtn[i].setGeometry(QtCore.QRect(warnbtn_pos[i], 620, 56, 31))
            self.warnbtn[i].setStyleSheet("background-color: rgb(180, 0, 0);")
            self.warnbtn[i].setObjectName("warnbtn" + str(i))

        #绑定点击事件
        for i in range(0, len(self.warnbtn)):
            self.warnbtn[i].clicked.connect(MainWindow.warningClick)



        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(180, 580, 31, 31))
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_3.setGeometry(QtCore.QRect(230, 580, 31, 31))
        # self.pushButton_3.setObjectName("pushButton_3")

        #楼层按键建模
        gridLayoutWidget_pos = [180, 450, 730, 1010, 1290]
        self.gridLayoutWidget = []
        self.gridLayout = []
        for i in range(0, len(gridLayoutWidget_pos)):
            self.gridLayoutWidget.append(QtWidgets.QWidget(self.centralwidget))
            self.gridLayoutWidget[i].setGeometry(QtCore.QRect(gridLayoutWidget_pos[i], 120, 81, 451))
            self.gridLayoutWidget[i].setObjectName("gridLayoutWidget" + str(i))
            self.gridLayout.append(QtWidgets.QGridLayout(self.gridLayoutWidget[i]))
            self.gridLayout[i].setContentsMargins(0, 0, 0, 0)
            self.gridLayout[i].setObjectName("gridLayout" + str(i))

        names = [
            '19', '20',
            '17', '18',
            '15', '16',
            '13', '14',
            '11', '12',
            '9', '10',
            '7', '8',
            '5', '6',
            '3', '4',
            '1', '2'
        ]

        positions = [(i, j) for i in range(10) for j in range(2)]  # 构造五行四列的格子
        for i in range(0,len(gridLayoutWidget_pos)):
            for position, name in zip(positions, names):
                button = QtWidgets.QPushButton(name)
                button.setObjectName("button_"+str(i)+'_'+name)
                button.clicked.connect(MainWindow.btnClick)
                self.gridLayout[i].addWidget(button, *position)  # 放到布局里




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
        for i in range(0, len(self.label)):
            self.label[i].setText(_translate("MainWindow", "电梯" + str(i)))
            self.warnbtn[i].setText(_translate("MainWindow", "报警器"))




    def warningClick(self):
        which_warnbtn = self.sender().objectName()[-1]
        print(which_warnbtn)
        QtWidgets.QMessageBox.information(self.warnbtn[int(which_warnbtn)], "警告", "第"+which_warnbtn+"号电梯已坏, 不能继续使用")

        # self.warnbtn[0].setEnabled(False)   #设置按钮不可用

    def btnClick(self):
        whichbtn = self.sender()

        btn_name = whichbtn.objectName()
        print(btn_name)

        whichbtn.setStyleSheet("background-color: rgb(100, 0, 0);")
