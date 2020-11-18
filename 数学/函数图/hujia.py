#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   hujia.py
@Time         :   2020/08/22 15:08:35
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib
import numpy as np
import math
import matplotlib.pyplot as plt
plt.figure(1)
x=[]
y=[]
a=np.linspace(0,500,1000)
def f1(x):
    y=1
    return y
def f2(x):
    y=1/(x*x+1)
    #y1 = y/x
    return y
def f3(x):
    #y=math.sin(x)/(math.exp(x)+1)
    y = x/(x+100)
    return y
for i in a:
    x.append(i)
    y.append(f3(i))
plt.plot(x,y)
plt.show()