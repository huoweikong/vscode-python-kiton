#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   jiami_zimu.py
@Time         :   2020/06/13 23:29:51
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib

#英文加密算法
# str1-->str2 加密算法
# text为明文， s为加密后密文
# str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+{}:\"<>\?`1234567890-=[];',./\|"
# text = "i love china"
import random

# 密钥 str1-->str2
str1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',\
     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', \
         'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', \
             'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', \
                 '9', '0']
str2 = ['4', 'M', '3', 'Q', 'O', 'p', 'd', 'X', 'A', '2', 'k', '8', 'E', 'j', 'n', \
    'q', 'z', '7', 'g', 'y', 'h', 'B', '0', 'f', 'b', 'V', 'R', 'e', 'J', 'S', 'l', \
        'c', 't', '5', '6', 'P', 'N', 'K', 'm', 'v', 'D', 'r', 'a', 's', 'T', '9',\
             'L', 'H', 'w', 'x', 'C', 'G', 'I', 'i', 'Y', 'o', 'F', 'Z', '1', 'u', \
                 'U', 'W']

#定义加密函数
def  jiami(minwen):
    text = minwen
    s = ""
    for i in  text:
        if i in str1:
            k = str1.index(i)
            s = s + str2[k]
        else:
            s = s + i
    #print(s)
    return s

#定义解密函数1

def jiemi(miwen):
    s = miwen
    s_to_m = ""
    for i in s:
        if i in str2:
            k = str2.index(i)
            s_to_m = s_to_m + str1[k]
        else:
            s_to_m = s_to_m + i
    #print(s2m)
    return s_to_m

#主程序入口
if __name__ == "__main__":
    print("欢迎使用密文系统")
    count = 0
    while True:
        count = count +1
        print("\n-------------------------------程序运行第 " + str(count) + " 次-------------------------------")
        selectway = input("请选择需要的操作：\n 1.加密\n 2.解密\n 3.退出\n   -->请输入数字1或2或3：")
        if selectway == '1':
            mingwen = input("\n-->请输入明文：")
            print("---------------- 结果如下 ----------------")
            postEncrypt = jiami(mingwen)
            print('----->[  ' + str(mingwen) + '  ]<--' +  "\n\n加密后为： \n\n" + '----->[  ' + str(postEncrypt)+ '  ]<--' +'\n ')
            input("------------------------------- 程序继续还是终止？ -------------------------------")

        elif selectway== '2':
            miwen = input("\n-->请输入密文：")
            print("----------------结果如下--------------")
            postDecode = jiemi(miwen)
            print('----->[  ' + str(miwen) + '  ]<--' +' \n\n解密后为： \n\n' + '----->[  ' + str(postDecode) + '  ]<--' +'\n ')
            input("------------------------------- 程序继续还是终止？ -------------------------------")

        elif selectway== '3':
            print("------------------------------- 感谢您的使用，再见！-------------------------------")
            break

        else:
            print("-------------------------------- 输入错误，程序退出 --------------------------------")
            break
          

