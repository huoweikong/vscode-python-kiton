#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   tiqu-dict.py
@Time         :   2020/05/31 00:27:51
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
data = pd.read_csv(r'附件1_蛋白质鉴定列表.csv')
print(data.columns)#获取列索引值
print(data.index)#获取行索引值
data1  = data['Protein'] #获取名字为flow列的数据
data2  =data['Protein Name']
data_list = data1.values.tolist()#将csv文件中flow列中的数据保存到列表中
print(data)
print(data_list)
pp_dict = dict(zip(data1, data2))
print(pp_dict)

data = pd.read_csv(r'annotation.csv')
print(data.columns)#获取列索引值
print(data.index)#获取行索引值
data3  = data['Protein IDs'] #获取名字为flow列的数据
print("data3-----------------------------")
print(data3)


p1_dict = {key: value for key, value in pp_dict.items() if any(key in s for s in data3)}
print("-----------fdsfs---")
print(p1_dict)
print("-----------fdsfs---")

f='p1_dict.txt'
#d={('dsaa','dsa'):1.2132,('fdsfsd','dsada'):2.3243}
with open(f,'w') as fo:
    for k,v in p1_dict.items():
        print("%s  %s" %(k ,v),sep='',file=fo)

proteinID = []
proteinName = []
for k,v in p1_dict.items():
    proteinID.append(k)
    proteinName.append(v)



#字典中的key值即为csv中列名
dataframe = pd.DataFrame({'proteinID':proteinID,'proteinName':proteinName})


#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv(r"my_csv.csv",sep=',')


# #pandas将列表写入CSV
# import pandas as pd
# a = [proteinID,proteinName]
# my_df = pd.DataFrame(a)
# my_df.to_csv('my_csv.csv', index=False, header=True)




#将TXT转化为CSV，空格会造成过度分栏！！！
# import csv
# csvFile = open("./p1_dict.csv",'w',newline='',encoding='utf-8')
# writer = csv.writer(csvFile)
# csvRow = []
# f = open("p1_dict.txt",'r',encoding='GB2312')
# for line in f:
#     csvRow = line.split()
#     writer.writerow(csvRow)
# f.close()
# csvFile.close()


#将词典写入json，只能机器读！！！
# import json
# jsObj = json.dumps(p1_dict)
# fileObject = open(r'p1_dic2.json', 'w')
# fileObject.write(jsObj)
# fileObject.close()



