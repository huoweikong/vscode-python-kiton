#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   sushu.py
@Time         :   2020/05/24 13:19:50
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib

#素数判断
def sushu(i):
    if i == 1:
        return False
    for num in range(2,i):
        if i % num == 0:
            return False
        else:
            return True

#获取所有日期数
def huoquriqi():
    riqi = []
    for i in range(13):
        for j in range(32):
            shu = i*100 + j
            riqi.append(shu)
    #有些不能作为日期要移除
    yichu = [3,5,7,9,231,431,631,931,1131]
    for i in yichu:
        riqi.remove(i)
    return riqi

#主程序入口
if __name__ == '__main__':
    #打开文本准备写入
    f = open(r'所有素数日期.txt','a') 
    f.write('\n******以下为所有素数日期数：\n')
    f.write("-" * 110 + '\n')
    print( '\n******以下为所有素数日期数：')
    print("-" * 150, '\n')
    
    #获取日期数列表
    riqi = huoquriqi()

    #判断每一个日期数是否为素数
    sushuriqi = []
    for i in riqi:
        if sushu(i):
            sushuriqi.append(i)
    
    #格式化输出，每行10个日期数
    count = 0
    for i in sushuriqi:
        count += 1
        print(i,  '\t',end="")
        f.write(str(i) +' \t')
        if count % 10 == 0:
            print("")
            f.write("\n")
    print(count)
    print('\n'*2, "-" * 150, '\n')
    f.write('\n' + "-" * 110)
    f.close()



