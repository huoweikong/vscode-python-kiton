#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   atlas_protein_asfv.py
@Time    :   2020/09/14 15:22:08
@Author  :   Ai Qiangyun 
@Version :   1.0
@Contact :   aqy0716@163.com
@License :   (C)Copyright 2020 SCAU
@Desc    :   两组数据画韦恩图,显示并保存为tiff格式（600dpi）各类数据元素到CSV文件中
'''

# here put the import lib
import pandas as pd
from pandas import  DataFrame
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
from pylab import *
import os,sys

#抽提excel中需要比对的两列字符串数据
def excel_one_line_to_list(path, lieshu):
    df = pd.read_excel(path, usecols=[lieshu],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    return result

def data_operate(path):
    shiyan  = excel_one_line_to_list(path,0)
    wenxian  = excel_one_line_to_list(path,1)
    data2 = pd.read_excel(path,sheet_name=0,nrows=1,engine='xlrd')
    biaotou = data2.columns
    first_col = biaotou[0]
    second_col = biaotou[1]
    a = shiyan
    b = wenxian
    a = [a_ for a_ in a if a_ == a_]
    b = [a_ for a_ in b if a_ == a_]
    print(a)
    print(b)
    #找出相同元素
    c=[x for x in a if x in b]
    #找出不同元素
    d=[y for y in (a+b) if y not in c]
    #找出a中独有元素
    e = [x for x in d if x in a]
    #找出b中独有的元素
    f = [x for x in d if x in b]
    #去掉nan值
    c = [a_ for a_ in c if a_ == a_]
    d = [a_ for a_ in d if a_ == a_]
    e = [a_ for a_ in e if a_ == a_]
    f = [a_ for a_ in f if a_ == a_]
    print("第一列数据个数为：", len(a))
    print("第一列数据个数为：", len(b))
    print("共有的数据个数为：", len(c))
    print("非共有的数据总个数为：", len(d))
    print("第一列独占的数据个数为：", len(e))
    print("第二列独占的数据个数为：", len(f))
    #计算各列数据个数，便于最大值比较
    len_c = len(c)
    len_d = len(d)
    len_e = len(e)
    len_f = len(f)
    #蛋白质组学质谱ASFV库87.xlsx
    #填充nan值与最大补齐
    lieshu = max(len_c,len_d, len_e, len_f)
    for i in range(lieshu-len_c):
        c.append(nan)
    for i in range(lieshu-len_d):
        d.append(nan)
    for i in range(lieshu-len_e):
        e.append(nan)
    for i in range(lieshu-len_f):
        f.append(nan)
    #写入csv文件
    c_array=np.array(c)[:,np.newaxis]
    d_array=np.array(d)[:,np.newaxis]
    e_array=np.array(e)[:,np.newaxis]
    f_array=np.array(f)[:,np.newaxis]
    #print("frequence_array.shape",frequence_array.shape)
    concatenate_array=np.concatenate((c_array,d_array,e_array,f_array),axis=1)
    print("concatenate_array",concatenate_array)
    print("concatenate_array",concatenate_array.shape)
    col1 = "共有"
    col2 = "非共有"
    col3 = first_col + "独有"
    col4 = second_col + "独有"
    data=DataFrame(concatenate_array,columns=[col1,col2,col3,col4])
    data.to_csv("result_intra.csv", encoding='utf_8_sig')
    print("数据保存成功，保存在result_intra.csv文件中")
    print("最后需要将Excel中nan值全部替换为空字符")
def draw_venn(path):
    data2 = pd.read_excel(path,sheet_name=0,nrows=1,engine='xlrd')
    biaotou = data2.columns
    first_col = biaotou[0]
    second_col = biaotou[1]
    third_col = biaotou[2]

    shiyan  = excel_one_line_to_list(path,0)
    wenxian1  = excel_one_line_to_list(path,1)
    wenxian2  = excel_one_line_to_list(path,2)
    #subset1 = [set(shiyan),set(wenxian)]
    subset3 = [set(shiyan),set(wenxian1),set(wenxian2)]

    venn3(subset3,set_labels=(first_col,second_col,third_col),set_colors=('r','g','b'),alpha=0.4,normalize_to=1.0,ax=None,subset_label_formatter=None)

    #venn2(subset3,set_labels=(first_col,second_col),set_colors=('r','g'),alpha=0.4,normalize_to=1.0,ax=None,subset_label_formatter=None)
    plt.savefig("venn_picture.tif", dpi=600)
    print("图片已保存在当前文件夹中 venn_picture.tif")
    print("现已显示，可直接关闭")
    plt.show()

if __name__ == "__main__":
    os.chdir(sys.path[0])  #切换当前文件夹为工作目录
    #防止中文乱码（图片）
    mpl.rcParams['font.sans-serif']=['SimHei']
    print("欢迎来到韦恩图绘图器，您需要准备一个有表头和两栏数据的excel文件\n")
    print("可是使用相对地址，该软件同文件夹路径为父目录")
    path = input("请输入excel文件地址:\n  ")
    #data_operate(path)
    draw_venn(path)
    

