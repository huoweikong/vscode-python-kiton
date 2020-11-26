# coding= gb18030
# TCID50������4.0������REED-MUENCH���Ϸ�
# @��ǿ�� 2019.1.3 E-mail��1154282938@ qq.com
import os

print(" ��ӭʹ��TCID50������4.0:\n ")

a = []  # ��CPE����
b = []  # ����CPE����
a_acc = []  # ��CPE�ۻ�����
b_acc = []  # ����CPE�ۻ�����
ab_acc = []  # �����ۻ���
a_ratio = []  # CPE�ۻ�����ռ��

# �ж��Ƿ�Ϊ��׼TCID50
print("  ����ظ����Ƿ�Ϊ8������ʼϡ�ͱ����ĸ������Ƿ�Ϊ-1\n  ������밴Y����������밴N ")
is8 = input("    Y or N?")
is8.upper()
if is8 != 'Y':
    replication = input("  �������ظ�����  ")
    initial = input("  ��������ʼϡ�ͱ����Ķ���������-1��-3���� ")

# ����ԭʼ���� �� ��ϡ�Ͷ�CEP����
print("   �������ϡ�ͱ�����CPE����\
        \n ��ϡ�Ͷ�-1��-8д���� ������Ĭ��Ϊ0��\n")
for i in range(8):
    s = input(' �������{}��������'.format(i + 1))
    a.append(s)

# �Ƴ����ַ�
while '' in a:
    a.remove('')

print(a)
os.system('pause')

# ĩβ�Զ���λ0
for i in range(8 - len(a)):
    a.append(0)

print(a)
os.system('pause')
# ���б� �ַ�������ת��������
a = list(map(int, a))

print("\n ����������ϣ������������Ϊ: {}\n  ����Enter�����м���".format(a))
os.system('pause')

# ��ʾ�����CPE����
print("\n CPE����Ϊ��\n ", a)

# ���� ��ϡ�Ͷȷ�CPE����
for i in range(0, 8, 1):
    b.append(8 - a[i])

print("\n ��CPE����Ϊ��\n ", b)

# ����CPE�ۻ��������Ӹ�ϡ�ͱ�������ϡ�ͱ���
s = 0
for i in reversed(a):
    s = s + i
    a_acc.append(s)

a_acc.reverse()

print("\n CPE�ۻ�Ϊ��\n ", a_acc)

# �����CPE�ۻ�����
s = 0
for i in b:
    s = s + i
    b_acc.append(s)
print("\n ��CPE�ۻ�Ϊ��\n ", b_acc)
# �������ۻ�����

for m, n in zip(a_acc, b_acc):
    ab_acc.append(m + n)
print("\n ���ۻ���Ϊ��\n ", ab_acc)

# �����CPE�ۻ����� ռ ���ۻ�������CPE�ۻ��ͷ�CPE�ۻ����� ����
for m, n in zip(a_acc, ab_acc):
    a_ratio.append(m / n)
for i, n in zip(range(8), a_ratio):
    a_ratio[i] = '{0:.4f}'.format(a_ratio[i])

print("\n CPE�ۻ�ռ��Ϊ��\n ", a_ratio)
# Ѱ�Ҵ��ڵ�����ӽ���50%��ϡ�Ͷ�


# Ѱ�Ҵ��ڵ�����ӽ���50%��ϡ�Ͷ� ռ��
gd50 = 0
for i, i2 in zip(reversed(a_ratio), range(8)):

    if round(float(i)) >= 0.5:
        gd50z = float(i)
        gd50 = 8 - i2 - 1
        break

# Ѱ��С��50%�������50%��ϡ�Ͷ� ռ��
for i in a_ratio:
    if round(float(i)) < 0.5:
        d50z = float(i)
        d50 = i
        break
print("\n  ����50%��ϡ�Ͷ�Ϊ��{}    �����Ϊ��{} ".format(d50z, d50))
# �������
s = (float(gd50z) - 0.5) / (float(gd50z) - float(d50))
print("\n  ����50%��ϡ�Ͷ�Ϊ��{}    �����Ϊ��{} ".format(gd50, gd50z))
# ����lg(TCID50) =
tcid50 = -(gd50 + 1 + s)
print('\n ԭʼ����Һ��ĵζ�Ϊ��{0:.4f}                                                <---���ǽ��'.format(tcid50))

print()
print("�����������ӭ�´�ʹ��")
os.system('pause')

