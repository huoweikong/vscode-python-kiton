# coding= gb18030
# TCID50计算器4.0，采用REED-MUENCH两氏法
# @艾强云 2019.1.3 E-mail：1154282938@ qq.com
import os

print(" 欢迎使用TCID50计算器4.0:\n ")

a = []  # 各CPE孔数
b = []  # 各非CPE孔数
a_acc = []  # 各CPE累积孔数
b_acc = []  # 各非CPE累积孔数
ab_acc = []  # 各孔累积和
a_ratio = []  # CPE累积孔数占比

# 判断是否为标准TCID50
print("  你的重复数是否为8并且起始稀释倍数的负对数是否为-1\n  如果是请按Y，如果不是请按N ")
is8 = input("    Y or N?")
is8.upper()
if is8 != 'Y':
    replication = input("  请输入重复数：  ")
    initial = input("  请输入起始稀释倍数的对数（比如-1，-3）： ")

# 输入原始数据 ， 各稀释度CEP孔数
print("   请输入各稀释倍数的CPE孔数\
        \n 按稀释度-1到-8写：（ 不输入默认为0）\n")
for i in range(8):
    s = input(' 请输入第{}个整数：'.format(i + 1))
    a.append(s)

# 移除空字符
while '' in a:
    a.remove('')

print(a)
os.system('pause')

# 末尾自动补位0
for i in range(8 - len(a)):
    a.append(0)

print(a)
os.system('pause')
# 将列表 字符串类型转换成整型
a = list(map(int, a))

print("\n 数据输入完毕，您输入的数字为: {}\n  按下Enter键进行计算".format(a))
os.system('pause')

# 显示输入的CPE孔数
print("\n CPE孔数为：\n ", a)

# 计算 个稀释度非CPE孔数
for i in range(0, 8, 1):
    b.append(8 - a[i])

print("\n 非CPE孔素为：\n ", b)

# 计算CPE累积孔数，从高稀释倍数到低稀释倍数
s = 0
for i in reversed(a):
    s = s + i
    a_acc.append(s)

a_acc.reverse()

print("\n CPE累积为：\n ", a_acc)

# 计算非CPE累积孔数
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
        d50z = float(i)
        d50 = i
        break
print("\n  低于50%的稀释度为：{}    其比率为：{} ".format(d50z, d50))
# 计算距离
s = (float(gd50z) - 0.5) / (float(gd50z) - float(d50))
print("\n  高于50%的稀释度为：{}    其比率为：{} ".format(gd50, gd50z))
# 计算lg(TCID50) =
tcid50 = -(gd50 + 1 + s)
print('\n 原始病毒液体的滴度为：{0:.4f}                                                <---这是结果'.format(tcid50))

print()
print("计算结束，欢迎下次使用")
os.system('pause')

