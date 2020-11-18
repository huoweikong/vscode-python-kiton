## Venn上的自定义标签 Custom label on Venn
# Import the library
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
from matplotlib_venn import venn3_circles
import pandas as pd
from pandas import  DataFrame
import numpy as np
import matplotlib.pyplot as plt

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

# Custom text labels: change the label of group A
v=venn3(subsets = (10, 8, 22, 6,9,4,2), set_labels = ('Group A', 'Group B', 'Group C'))
# 单独改变A的标签
v.get_label_by_id('A').set_text('My Favourite group!')
plt.show()

## 自定义维恩图上圆的线条 Custom Circles lines on Venn
# Line style: can be 'dashed' or 'dotted' for example
# 设置维恩图
v = venn3(subsets = (10, 8, 22, 6,9,4,2), set_labels = ('Group A', 'Group B', 'Group C'))
# 画圆，linestyle线条类型，linewith线宽，color线条颜色
c = venn3_circles(subsets = (10, 8, 22, 6,9,4,2), linestyle='dashed', linewidth=1, color="grey")
plt.show()

A = ["fd","fs","rr","yy"]
B = ["fd","fs","vr","vy"]
C = ["fd","ys","yr","vy"]
AB = A.intersection(B).difference(C)
ABC = A.intersection(B).intersection(C)
print(A)
print(AB)
print(ABC)