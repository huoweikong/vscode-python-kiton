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



plt.figure( dpi=200)
v = venn3(subset3,set_labels=(first_col,second_col,third_col),set_colors=('r','g','b'),
            alpha=0.4,normalize_to=1.0,ax=None,subset_label_formatter=None)





plt.savefig("daasshuzi.png",dpi= 600)
plt.show()


#病毒蛋白组学对比.xlsx