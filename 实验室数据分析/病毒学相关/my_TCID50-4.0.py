##与UI窗体类对应的业务逻辑类

import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow

from PyQt5.QtGui import QPalette

from PyQt5.QtCore import Qt, pyqtSlot


from ui_tcid50_4 import Ui_MainWindow


class QmyDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面

    def on_pushButton_clicked(self):
        # if self.ui.lineEdit.text() or self.ui.lineEdit_2.text() or self.ui.lineEdit_3.text() or self.ui.lineEdit_4.text() or self.ui.lineEdit_5.text() or \
        #    self.ui.lineEdit_6.text() or self.ui.lineEdit_7.text() or self.ui.lineEdit_8.text() == '':
        if self.ui.lineEdit.text() == "":
            a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = 0
            msgBox = QtGui.QMessageBox()
            # msgBox.setWindowTitle(u'提示')
            # msgBox.setText(u"\nAuthor: 望月又一(&Xu)!\n当前版本 v1.0.0")

            # msgBox.exec_()  # 模态对话框

        else:
            a1 = float(self.ui.lineEdit.text())
            a2 = float(self.ui.lineEdit_2.text())
            a3 = float(self.ui.lineEdit_3.text())
            a4 = float(self.ui.lineEdit_4.text())
            a5 = float(self.ui.lineEdit_5.text())
            a6 = float(self.ui.lineEdit_6.text())
            a7 = float(self.ui.lineEdit_7.text())
            a8 = float(self.ui.lineEdit_8.text())
        print(a1)
        try:
            a_sum = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
            strTa = str(a_sum)
            self.ui.lineEdit_11.setText(strTa)
        except:
            print("fsd")

    # ## 由connectSlotsByName() 自动与组件的信号连接的槽函数
    # ##    @pyqtSlot()
    # def on_btnClear_clicked(self):  # "清空"按钮
    #     self.ui.textEdit.clear()
    #
    # ##    @pyqtSlot()
    # def on_chkBoxBold_toggled(self, checked):  # "Bold"复选框
    #     font = self.ui.textEdit.font()
    #     font.setBold(checked)  # 函数参数checked表示了勾选状态
    #     self.ui.textEdit.setFont(font)
    #
    # ##    @pyqtSlot()
    # def on_chkBoxUnder_clicked(self):  # "Underline"复选框
    #     checked = self.ui.chkBoxUnder.isChecked()  # 读取勾选状态
    #     font = self.ui.textEdit.font()
    #     font.setUnderline(checked)
    #     self.ui.textEdit.setFont(font)
    #
    # @pyqtSlot(bool)  # 修饰符指定参数类型，用于overload型的信号
    # def on_chkBoxItalic_clicked(self, checked):  # "Italic"复选框
    #     font = self.ui.textEdit.font()
    #     font.setItalic(checked)
    #     self.ui.textEdit.setFont(font)
    #
    # ## 自定义槽函数
    # def do_setTextColor(self):
    #     plet = self.ui.textEdit.palette()  # 获取 palette
    #
    #     if (self.ui.radioBlack.isChecked()):
    #         plet.setColor(QPalette.Text, Qt.black)  # black
    #     elif (self.ui.radioRed.isChecked()):
    #         plet.setColor(QPalette.Text, Qt.red)  # red
    #     elif (self.ui.radioBlue.isChecked()):
    #         plet.setColor(QPalette.Text, Qt.blue)  # blue
    #
    #     self.ui.textEdit.setPalette(plet)  # 设置palette


if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序

    form = QmyDialog()  # 创建窗体

    form.show()

    sys.exit(app.exec_())
