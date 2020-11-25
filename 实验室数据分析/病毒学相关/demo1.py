from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys


class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()


def initUI(self):
    self.setWindowTitle('校验器')
    # 创建表单布局**
    formLayout = QFormLayout()
    intLineEdit = QLineEdit()
    doubleLineEdit = QLineEdit()
    validatorLineEdit = QLineEdit()
    formLayout.addRow('整数类型', intLineEdit)
    formLayout.addRow('浮点类型', doubleLineEdit)
    formLayout.addRow('数字和字母', validatorLineEdit)

    intLineEdit.setPlaceholderText('整型')
    doubleLineEdit.setPlaceholderText('浮点型')
    validatorLineEdit.setPlaceholderText('数字和字母')

     # 整数校验器[1,99]**
    intValidator = QIntValidator()
    intValidator.setRange(1, 99)

     # 浮点校验器[-360,360]，精度小数点后2位**
    doubleValidator = QDoubleValidator()
    doubleValidator.setRange(-360, 360)
    doubleValidator.setNotation(QDoubleValidator.StandardNotation)
    # 设置精度**
    doubleValidator.setDecimals(2)

    # 数字字母校验器**
    reg = QRegExp('[a-zA-Z0-9]+$')
    validator = QRegExpValidator(self)
    validator.setRegExp(reg)

    # 设置校验器**
    intLineEdit.setValidator(intValidator)
    doubleLineEdit.setValidator(doubleValidator)
    validatorLineEdit.setValidator(validator)

   # 设置布局**
    self.setLayout(formLayout)
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序

    form = QLineEditValidator()  # 创建窗体

    form.show()

    sys.exit(app.exec_())