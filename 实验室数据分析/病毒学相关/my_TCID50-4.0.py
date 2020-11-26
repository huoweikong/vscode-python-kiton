##与UI窗体类对应的业务逻辑类
import math
import sys
import os
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
import PyQt5.sip
from PyQt5.QtGui import QPalette

from PyQt5.QtCore import Qt, pyqtSlot

from ui_tcid50_4 import Ui_MainWindow
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


if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序

    form = QmyDialog()  # 创建窗体

    form.show()

    sys.exit(app.exec_())
    os.system(pause)
