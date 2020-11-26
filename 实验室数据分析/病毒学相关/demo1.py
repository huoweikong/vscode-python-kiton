# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tcid50_4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os

import PyQt5.sip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap

# icon
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tcid50_4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tcid50_4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tcid50_4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 844)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 1041, 411))
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
        self.pushButton.setGeometry(QtCore.QRect(720, 300, 141, 81))
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
        self.groupBox_2.setGeometry(QtCore.QRect(30, 430, 911, 281))
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
        self.lineEdit_22.setGeometry(QtCore.QRect(520, 170, 111, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(640, 180, 21, 21))
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
        self.pushButton_3.setGeometry(QtCore.QRect(730, 170, 141, 71))
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
        self.pushButton_5.setGeometry(QtCore.QRect(1000, 530, 81, 141))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(620, 760, 81, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(340, 760, 221, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(990, 769, 101, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 23))
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
        self.pushButton_2.clicked.connect(self.lineEdit_11.clear)
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
        self.pushButton_7.setText(_translate("MainWindow", "帮助"))
        self.pushButton_8.setText(_translate("MainWindow", "Copyright © 2020 SCAU"))
        self.label_11.setText(_translate("MainWindow", "版本号：4.0.1"))



    ##与UI窗体类对应的业务逻辑类
import math
import sys
#import os
#from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow

#from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt, pyqtSlot
import PyQt5.QtWidgets as qw


def jisuan(a, repeatNum):
    # a = []  # 各CPE孔数
    b = []  # 各非CPE孔数
    a_acc = []  # 各CPE累积孔数
    b_acc = []  # 各非CPE累积孔数
    ab_acc = []  # 各孔累积和
    a_ratio = []  # CPE累积孔数占比

    # 将列表 字符串类型转换成整型
    a = list(map(int, a))
    # 显示输入的CPE孔数
    print("\n CPE孔数为：\n ", a)

    # 计算 个稀释度非CPE孔数
    for i in range(0, 8, 1):
        b.append(repeatNum - a[i])

    print("\n 非CPE孔素为：\n ", b)

    # 计算CPE累积孔数，从高稀释倍数到低稀释倍数
    s = 0
    for i in reversed(a):
        s = s + i
        a_acc.append(s)

    a_acc.reverse()

    print("\n CPE累积为：\n ", a_acc)

    #计算非CPE累积孔数
    s = 0
    for i in b:
        s = s + i
        b_acc.append(s)
    print("\n 非CPE累积为：\n ", b_acc)
    # 计算总累积孔数

    for m, n in zip(a_acc, b_acc):
        ab_acc.append(m + n)
    print("\n 孔累积和为：\n ", ab_acc)

    # 计算各CPE累积孔数 占 总累积孔数（CPE累积和非CPE累积）的 比例
    for m, n in zip(a_acc, ab_acc):
        a_ratio.append(m / n)
    for i, n in zip(range(8), a_ratio):
        a_ratio[i] = '{0:.4f}'.format(a_ratio[i])

    print("\n CPE累积占比为：\n ", a_ratio)
    # 寻找大于等于最接近于50%的稀释度

    # 寻找大于等于最接近于50%的稀释度 占率
    gd50 = 0
    for i, i2 in zip(reversed(a_ratio), range(8)):

        if round(float(i)) >= 0.5:
            gd50z = float(i)
            gd50 = 8 - i2 - 1
            break

    # 寻找小于50%且最近于50%的稀释度 占率
    for i in a_ratio:
        if round(float(i)) < 0.5:
            d50 = i
            break
    # 计算距离
    s = (float(gd50z) - 0.5) / (float(gd50z) - float(d50))
    print("\n  高于50%的稀释度为：{}    其比率为：{} ".format(gd50, gd50z))
    # 计算lg(TCID50) =
    tcid50 = -(gd50 + 1 + s)
    print(tcid50)
    # tcid50 = format(tcid50, '.4f')
    return tcid50


def test_virus_volume(tcid50_value_init, volume_index):
    if volume_index == 0:
        tcid50 = tcid50_value_init - 1
    elif volume_index == 1:
        tcid50 = tcid50_value_init - math.log(5, 10)
    else:
        tcid50 = tcid50_value_init
    return tcid50


def test_init_dilution_factor(tcid50_value, initFactor):
    tcid50 = tcid50_value + 1 + initFactor

    return tcid50


def virus_volume_need(tcid_fuzhi, cell_xi, cell_zhi, moi_value):
    cell_count = cell_xi * (10 ** cell_zhi)
    denominator = 0.7 * (10 ** (-tcid_fuzhi))
    virus_volume = ((moi_value * cell_count) / denominator) * 1000  # 变微升
    virus_volume = format(virus_volume, '.2f')
    print(tcid_fuzhi)
    print(cell_xi)
    print(cell_zhi)
    print(moi_value)
    print(cell_count)
    print(denominator)

    print(virus_volume)

    return str(virus_volume)


def infect_rate(moi_value):
    p0 = math.e ** (-moi_value)
    p1 = (1 - p0) * 100
    p1 = format(p1, '.2f')
    m = -math.log(p0, math.e)
    print("p0", p0)
    print("moi", m)

    return str(p1)


class QmyDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.setWindowTitle('TCID50计算器 4.0.1')
        # self.setWindowIcon(QIcon("./favicon.icon"))
        # self.setWindowIcon(QIcon(QPixmap(os.path.join('icons', "./favicon.icon"))))
        # self.setFixedWidth(200)
        # self.setFixedHeight(200)
        #self.initUI()
    # def initUI(self):
    #     # x轴位置，y轴位置,x轴长度，y轴长度
    #     #self.setGeometry(300, 300, 300, 300)
    #     self.setWindowTitle('TCID50计算器 4.0.1')
    #     self.setWindowIcon(QIcon("./favivon.icon"))
    #     self.show()


    @pyqtSlot()  # 确保弹窗只弹一次，否则会弹两次
    def on_pushButton_clicked(self):

        a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = 0
        a = [a1, a2, a3, a4, a5, a6, a7, a8]
        if self.ui.lineEdit.text() == "":

            msgBox = qw.QMessageBox()
            msgBox.setWindowTitle(u'提示')
            msgBox.setText(u"\n警告!\n请输入正确的数据\n请确认是否输入数据！")
            # qw.QMessageBox.about(self, "警告", "请输入正确的数据！")
            msgBox.exec_()  # 模态对话框

        else:
            try:
                a1 = float(self.ui.lineEdit.text())
                a2 = float(self.ui.lineEdit_2.text())
                a3 = float(self.ui.lineEdit_3.text())
                a4 = float(self.ui.lineEdit_4.text())
                a5 = float(self.ui.lineEdit_5.text())
                a6 = float(self.ui.lineEdit_6.text())
                a7 = float(self.ui.lineEdit_7.text())
                a8 = float(self.ui.lineEdit_8.text())

            except:
                msgBox = qw.QMessageBox()
                msgBox.setWindowTitle(u'提示')
                msgBox.setText(u"\n警告!\n请输入正确的数据\n请确认输入数据是否完整！")
                msgBox.exec_()  # 模态对话框
            else:
                # a_sum = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8

                # 输入数据无异常，进行计算初试TCID50
                a = [a1, a2, a3, a4, a5, a6, a7, a8]
                repeatNum = int(self.ui.lineEdit_9.text())
                print(repeatNum)
                tcid50_value_init = float(jisuan(a, repeatNum))

                # 考虑毒液测试体积，通常为100uL，index为0
                volume_index = self.ui.comboBox.currentIndex()
                tcid50 = test_virus_volume(tcid50_value_init, volume_index)

                # 考虑起始稀释倍数,负对数通常为-1
                initFactor = int(self.ui.lineEdit_10.text())
                tcid50 = test_init_dilution_factor(tcid50, initFactor)

                # 格式化输出
                tcid50 = format(tcid50, '.4f')
                self.ui.lineEdit_11.setText(str(tcid50))

    @pyqtSlot()  # 确保弹窗只弹一次，否则会弹两次
    def on_pushButton_3_clicked(self):
        try:
            tcid_fuzhi = float(self.ui.lineEdit_12.text())  # TCID50
            cell_xi = float(self.ui.lineEdit_14.text())  # 细胞数量 系数
            cell_zhi = float(self.ui.lineEdit_15.text())  # 细胞数量 指数
            moi_value = float(self.ui.lineEdit_13.text())  # MOI值
        except:
            msgBox = qw.QMessageBox()
            msgBox.setWindowTitle(u'提示')
            msgBox.setText(u"\n警告!\n请输入正确的数据\n请确认输入数据是否完整！\n")
            # qw.QMessageBox.about(self, "警告", "请输入正确的数据！")
            msgBox.exec_()  # 模态对话框
        else:
            virus_volume_uL = virus_volume_need(tcid_fuzhi, cell_xi, cell_zhi, moi_value)

            self.ui.lineEdit_22.setText(virus_volume_uL)

            infect_rate100 = infect_rate(moi_value)
            self.ui.lineEdit_16.setText(infect_rate100)

    @pyqtSlot()  # 确保弹窗只弹一次，否则会弹两次
    def on_pushButton_6_clicked(self):
        tcid_last = self.ui.lineEdit_11.text()
        self.ui.lineEdit_12.setText(tcid_last)

    @pyqtSlot()  # 确保弹窗只弹一次，否则会弹两次


    def on_pushButton_7_clicked(self):
        msgBox = qw.QMessageBox()
        msgBox.setWindowTitle(u'帮助')
        msgBox.setText(u"\n本款TCID50计算器采用Reed-Muench两氏法，可用于计算TCID50， EID50等.\
                       \nTCID50,median tissue culture infective dose,半数组织培养感染剂量,即指能在培养板孔或试管内引起半数细胞病变或死亡(cytopathic effect, CPE)所需的病毒量，用以表征病毒的滴度。\
                       \n\n注意：这里的病毒量不是具体的浓度，而是将原始样品稀释的倍数。\
                       比如，1 mL培养液，稀释1000倍后恰好导致50%的细胞感染，则TCID50为1000/mL。意思是每mL样品中含有的病毒导致50%细胞感染需要稀释的倍数。\
                       可根据测试病毒体积，起始稀释倍数等参数计算TCID50\
                       \n\n版本号：4.0.1\
                       \n更新日期：2020/11/26\
                       \n作者：艾强云\
                       \n联系方式(E-mail)：11542829382@qq.com"
                       )
        msgBox.exec_()  # 模态对话框

    @pyqtSlot()  # 确保弹窗只弹一次，否则会弹两次
    def on_pushButton_8_clicked(self):
        msgBox = qw.QMessageBox()
        msgBox.setWindowTitle(u'版权信息')
        msgBox.setText(u"\n华南农业大学兽医学院传染病教研室制品\n版权所有，侵权必究\n欢迎使用！\n \nCopyright © 2020 SCAU")
        msgBox.exec_()  # 模态对话框


if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    app_icon = QIcon("./favicon (2).ico")
    app.setWindowIcon(app_icon)
    form = QmyDialog()  # 创建窗体

    form.show()

    sys.exit(app.exec_())
    os.system('pause')
