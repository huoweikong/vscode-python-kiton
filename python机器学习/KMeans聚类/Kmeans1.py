#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   Kmeans1.py
@Time         :   2020/06/20 23:03:28
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib
# -*- coding: utf-8 -*
 
 
 
from matplotlib import pyplot as plt
 
from sklearn.cluster import k_means
 
import pandas as pd
 
from sklearn.metrics import silhouette_score
 
 
 
file = pd.read_csv("cluster_data.csv", header=0)
 
x = file['x']
 
y = file['y']
 
plt.scatter(x,y)
 
#plt.show()
 
# from matplotlib import pyplot as plt
 
 
 
model = k_means(file,n_clusters = 3)
 
cluster_centers = model[0] # 聚类中心数组
 
cluster_labels = model[1] # 聚类标签数组
 
plt.scatter(x, y, c=cluster_labels) # 绘制样本并按聚类标签标注颜色
 
# 绘制聚类中心点，标记成五角星样式，以及红色边框
 
# for center in cluster_centers:
 
#     plt.scatter(center[0], center[1], marker="p", edgecolors="red")
 
 
 
plt.show() # 显示图#print model
 
 
 
#print file
