#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   numpy_add_proname.py
@Time         :   2020/05/31 00:18:48
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib
import os

print(os.getcwd()) # 打印当前工作目录

os.chdir(r'F:/vscode-python-kiton/实验室数据分析/分泌组学2nd') # 将当前工作目录改变

import pandas as pd
import numpy as np
data = pd.read_csv(r'annotation.csv')
print(data.columns)#获取列索引值
print(data.index)#获取行索引值
data1  = data['Protein IDs'] #获取名字为flow列的数据
data_list = data1.values.tolist()#将csv文件中flow列中的数据保存到列表中
print(data)
print(data_list)
