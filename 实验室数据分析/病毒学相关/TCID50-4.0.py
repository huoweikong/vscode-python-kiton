# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCID50-4.0.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 787)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 1041, 411))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(340, 280, 51, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 180, 281, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(340, 190, 81, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 280, 251, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(40, 330, 341, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_9.setGeometry(QtCore.QRect(340, 240, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(480, 350, 71, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(420, 280, 121, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 971, 71))
        self.horizontalLayoutWidget.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        spacerItem4 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout.addWidget(self.lineEdit_6)
        spacerItem5 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout.addWidget(self.lineEdit_7)
        spacerItem6 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout.addWidget(self.lineEdit_8)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 50, 571, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(730, 310, 131, 71))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_11.setGeometry(QtCore.QRect(380, 320, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 160, 111, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 240, 261, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 450, 891, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(480, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(340, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(40, 40, 311, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(440, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(40, 180, 131, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(270, 180, 371, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(180, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(40, 120, 131, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(160, 120, 51, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(270, 100, 41, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(320, 130, 21, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_22.setGeometry(QtCore.QRect(530, 170, 81, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(620, 180, 21, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(220, 130, 51, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 180, 111, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(40, 230, 241, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(270, 220, 61, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setGeometry(QtCore.QRect(340, 230, 21, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 40, 91, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(150, 200, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setGeometry(QtCore.QRect(270, 250, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(360, 130, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 30, 51, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setAutoExclusive(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(950, 590, 91, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(self.lineEdit_12.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_13.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_22.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_16.clear)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_3.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_4.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_5.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_6.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_7.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_8.clear)
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.pushButton_6.clicked.connect(self.lineEdit_12.show)
        self.pushButton.clicked.connect(self.lineEdit_11.show)
        self.pushButton_3.clicked.connect(self.lineEdit_22.show)
        self.pushButton_3.clicked.connect(self.lineEdit_16.show)
        self.pushButton_3.clicked.connect(self.lineEdit_13.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "TCID50 计算"))
        self.lineEdit_10.setText(_translate("MainWindow", "-1"))
        self.label_2.setText(_translate("MainWindow", "稀释梯度为10倍，每孔上液量为"))
        self.comboBox.setItemText(0, _translate("MainWindow", "100uL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "200uL"))
        self.comboBox.setItemText(2, _translate("MainWindow", "1mL"))
        self.label_4.setText(_translate("MainWindow", "最低稀释倍数的lg负对数为:"))
        self.label_6.setText(_translate("MainWindow", "待检原液的TCID50的值为：  10"))
        self.lineEdit_9.setText(_translate("MainWindow", "8"))
        self.label_7.setText(_translate("MainWindow", "/mL"))
        self.label_5.setText(_translate("MainWindow", "(如-2， -4)"))
        self.lineEdit.setText(_translate("MainWindow", "8"))
        self.lineEdit_2.setText(_translate("MainWindow", "8"))
        self.lineEdit_3.setText(_translate("MainWindow", "7"))
        self.lineEdit_4.setText(_translate("MainWindow", "3"))
        self.lineEdit_5.setText(_translate("MainWindow", "1"))
        self.lineEdit_6.setText(_translate("MainWindow", "0"))
        self.lineEdit_7.setText(_translate("MainWindow", "0"))
        self.lineEdit_8.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "请填写各稀释度的病变孔数（从低稀释倍数开始填）（自然数）"))
        self.pushButton.setText(_translate("MainWindow", "计算 TCID50"))
        self.pushButton_2.setText(_translate("MainWindow", "清除数据"))
        self.label_3.setText(_translate("MainWindow", "每个稀释度重复数为:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "MOI 计算"))
        self.lineEdit_12.setText(_translate("MainWindow", "-6"))
        self.label_9.setText(_translate("MainWindow", "原液的TCID50的值为：  10"))
        self.label_10.setText(_translate("MainWindow", "/mL"))
        self.label_12.setText(_translate("MainWindow", "要计算MOI为"))
        self.label_13.setText(_translate("MainWindow", "时，需要加入的病毒液的量为"))
        self.lineEdit_13.setText(_translate("MainWindow", "1"))
        self.label_14.setText(_translate("MainWindow", "细胞数量为："))
        self.lineEdit_14.setText(_translate("MainWindow", "2"))
        self.lineEdit_15.setText(_translate("MainWindow", "6"))
        self.label_15.setText(_translate("MainWindow", "个"))
        self.lineEdit_22.setText(_translate("MainWindow", "100"))
        self.label_22.setText(_translate("MainWindow", "uL"))
        self.label_23.setText(_translate("MainWindow", "X 10"))
        self.pushButton_3.setText(_translate("MainWindow", "计算 MOI"))
        self.label_24.setText(_translate("MainWindow", "此时，感染的细胞比例为："))
        self.lineEdit_16.setText(_translate("MainWindow", "90"))
        self.label_25.setText(_translate("MainWindow", "%"))
        self.pushButton_4.setText(_translate("MainWindow", "清除"))
        self.label_26.setText(_translate("MainWindow", "（PFU / cell_count）"))
        self.label_27.setText(_translate("MainWindow", "（0-99.99）"))
        self.label_28.setText(_translate("MainWindow", "(六孔板一般为：2x10^6个细胞)"))
        self.pushButton_6.setText(_translate("MainWindow", "填充"))
        self.pushButton_5.setText(_translate("MainWindow", "退出"))
