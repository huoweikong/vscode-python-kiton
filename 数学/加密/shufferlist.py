#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''

 @File         :   shufferlist.py
 @Time         :   2020/06/13 01:59:18
 @Author       :   艾强云
 @Contact      :   aqy0716@163.com
 @Department   :   SCAU 
 @Desc         :   生成密钥对
 '''
 # 生成密钥对
 # here put the import lib
 
import random

str1 = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

#str1 = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+{}:<>`1234567890-=[];',./|?\""
#字符串转化为列表
str1List = []
for i in str1:
    str1List.append(i)

print(str1List)
#str3 = str1.split('')
random.shuffle(str1List)
print(str1List)