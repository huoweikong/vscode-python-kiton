#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   添加蛋白质名称.py
@Time         :   2020/05/30 23:59:44
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib

import os

print(os.getcwd()) # 打印当前工作目录

os.chdir(r'F:/vscode-python-kiton/实验室数据分析/分泌组学2nd') # 将当前工作目录改变为`/Users/<username>/Desktop/`

import csv

with open('annotation.csv', 'r') as f:
    reader = csv.reader(f)
    print(type(reader))
   
    for row in reader:
        print(row)
        