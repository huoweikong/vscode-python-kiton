from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles
import matplotlib.pyplot as plt
import pandas as pd
from pandas import  DataFrame
from pylab import *
import os,sys
os.chdir(sys.path[0])  #切换当前文件夹为工作目录
    #防止中文乱码（图片）
mpl.rcParams['font.sans-serif']=['SimHei']
print("欢迎来到韦恩图绘图器，您需要准备一个有表头和两栏数据的excel文件\n")
print("可是使用相对地址，该软件同文件夹路径为父目录")
path = input("请输入excel文件地址:\n  ")

def excel_one_line_to_list(path, lieshu):
    df = pd.read_excel(path, usecols=[lieshu],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    return result
data2 = pd.read_excel(path,sheet_name=0,nrows=1,engine='xlrd')
biaotou = data2.columns
first_col = biaotou[0]
second_col = biaotou[1]
third_col = biaotou[2]
shiyan  = excel_one_line_to_list(path,0)
wenxian1  = excel_one_line_to_list(path,1)
wenxian2  = excel_one_line_to_list(path,2)

subset3 = [set(shiyan),set(wenxian1),set(wenxian2)]

# A = set(['DPEP1', 'CDC42BPA', 'GNG4', 'RAPGEFL1', 'MYH7B', 'SLC13A3', 'PHACTR3', 'SMPX', 'NELL2', 'PNMAL1', 'KRT23', 'PCP4', 'LOX', 'CDC42BPA'])
# B = set(['ABLIM1','CDC42BPA','VSNL1','LOX','PCP4','SLC13A3'])
# C = set(['PLCB4', 'VSNL1', 'TOX3', 'VAV3'])
A = set(shiyan)
B = set(wenxian1)
C = set(wenxian2)


my_dpi=100
plt.figure(figsize=(1800/my_dpi, 1800/my_dpi), dpi=my_dpi)
v = venn3(subset3,set_labels=(first_col,second_col,third_col),set_colors=('r','g','b'),
            alpha=0.4,normalize_to=1.0,ax=None,subset_label_formatter=None)




# A, B, AB_C, C, AC_B, BC_A, ABC
# A B AB-c C AC-B BC-A ABC
A_B_C = A.difference(B).difference(C)
B_A_C = B.difference(A).difference(C)
AB_C = A.intersection(B).difference(C)
C_B_A = C.difference(B).difference(A)
AC_B = A.intersection(C).difference(B)
BC_A = B.intersection(C).difference(A)
ABC = A.intersection(B).intersection(C)
print(A_B_C, B_A_C, AB_C, C_B_A, AC_B, BC_A, ABC)
A_B_C = [a_ for a_ in A_B_C if a_ == a_]
B_A_C = [a_ for a_ in B_A_C if a_ == a_]
AB_C = [a_ for a_ in AB_C if a_ == a_]
C_B_A = [a_ for a_ in C_B_A if a_ == a_]
AC_B = [a_ for a_ in AC_B if a_ == a_]
BC_A = [a_ for a_ in BC_A if a_ == a_]
ABC = [a_ for a_ in ABC if a_ == a_]


v.get_label_by_id('100').set_fontsize(8)#1的大小设置为20
v.get_label_by_id('110').set_fontsize(8)#1的大小设置为20
v.get_label_by_id('011').set_fontsize(8)#1的大小设置为20
v.get_label_by_id('001').set_fontsize(8)#1的大小设置为20
v.get_label_by_id('010').set_fontsize(8)#1的大小设置为20
v.get_label_by_id('101').set_fontsize(8)#1的大小设置为20
v.get_label_by_id('111').set_fontsize(8)#1的大小设置为20

v.get_label_by_id('100').set_text('\n'.join(A_B_C))
v.get_label_by_id('110').set_text('\n'.join(AB_C))
v.get_label_by_id('011').set_text('\n'.join(BC_A))
v.get_label_by_id('001').set_text('\n'.join(C_B_A))
v.get_label_by_id('010').set_text('\n'.join(B_A_C))
v.get_label_by_id('101').set_text('\n'.join(AC_B))
v.get_label_by_id('111').set_text('\n'.join(ABC))
# plt.annotate(',\n'.join(B_A_C), xy=v.get_label_by_id('010').get_position() + 
#              np.array([0, 0.2]), xytext=(-20,40), ha='center',
#              textcoords='offset points', 
#              bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
#              arrowprops=dict(arrowstyle='->',               
#                              connectionstyle='arc',color='gray'))
# plt.savefig("daas.tif",dpi= 300)
plt.savefig("daas.png",dpi= 300)
plt.show()


#病毒蛋白组学对比.xlsx