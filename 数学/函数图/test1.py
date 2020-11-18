#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   test1.py
@Time         :   2020/08/22 15:13:25
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib
import matplotlib.pyplot as plt  
import random
import numpy as np
x1 = list(range(10))
y1 = [random.randint(0,10) for i in range(10)]  
plt.plot(x1, y1,  color='r',markerfacecolor='blue',marker='o',linewidth=1.0)  
for a, b in zip(x1, y1):  
    plt.text(a, b, (a,b),ha='center', va='bottom', fontsize=10)  
 
x2 = np.linspace(0,900,1000)
y2 = np.linspace(0,0.9,1000)
plt.plot(x2, y2,  color='g',markerfacecolor='blue',marker='o')  
plt.legend()  
plt.show()