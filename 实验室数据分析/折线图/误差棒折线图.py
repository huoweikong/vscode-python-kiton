#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   误差棒折线图.py
@Time         :   2020/06/28 03:00:16
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib
import math
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd                                                                                                                                                                                              
import numpy as np

def analyzeError(filename):
    sampleSigma = []
    list_Error = []
    list_StdDev = []

    data = open(filename)
    lines = data.readlines()
    data.close()

    for line in lines:
        line = line.strip()
        eles = line.split()
        sampleSigma.append(float(eles[0]))
        list_Error.append(float(eles[1]))
        list_StdDev.append(float(eles[2]))

    print(sampleSigma)
    print(list_Error)
    print(list_StdDev)

    plt.errorbar(sampleSigma,list_Error,yerr=list_StdDev,fmt='ko-',ecolor='k',elinewidth=3,ms=5,mfc='wheat',mec='salmon',capsize=3)
        

    return

# main
print("hello")

#
fig = plt.figure(figsize=(4,3))
ax = plt.subplot(111)
plt.subplots_adjust(left=0.14, bottom=0.20, right=None, top=None,wspace=None, hspace=None)

#
analyzeError("log_error_0weight.txt")
analyzeError("log_error.txt")

plt.xlabel(r'$\sigma_{Ti,Aj}\ /\ dBm$',fontdict={'family' : 'Times New Roman', 'size': 12})
plt.ylabel("Error / m",fontdict={'family' : 'Times New Roman', 'size': 12})
#plt.savefig('figure-ErrorDistributionAll.png',dpi=300)
plt.show()