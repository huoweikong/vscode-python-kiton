#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   0424.py
@Time         :   2020/05/08 19:50:34
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib
import csv
import pandas as  pd
import time

f = pd.read_csv(r"F:\vscode-python-kiton\lab-calc\proteomics\0424updown.csv")
print(f)
print(len(f))

df_li = f.values.tolist()
up04 = []
down04 =[]
up424=[]
down424=[]
for s_li in df_li:
    up04.append(s_li[0])
    down04.append(s_li[1])
    up424.append(s_li[2])
    down424.append(s_li[3])
print(up04,'\n', down04, '\n',up424, '\n', down424)
sup04 = set(up04)
sdown04 =set(down04)
sup424=set(up424)
sdown424=set(down424)
print(sup04,'\n', sdown04, '\n',sup424, '\n', sdown424)
# sup04.remove(nan)
# sdown04.remove(nan)
# sup424.remove(nan)
# sdown424.remove(nan)
# print(sup04,'\n', sdown04, '\n',sup424, '\n', sdown424)

#计算04和424的共同蛋白
all04 = (sup04 | sdown04)
all424 = (sup424 | sdown424)
intersection0424 = (all04 & all424)
#计算0424 一直上升或一直下降蛋白变化
raise024 = (sup04 & sup424)
decline024 = (sdown04 & sdown424)

print(intersection0424,'\n', raise024, '\n', decline024)

l_inter = list(intersection0424)
l_raise = list(raise024)
l_decline = list(decline024)
print(l_inter, '\n', l_raise, '\n', l_decline)
l_inter.remove(l_inter[0])
l_raise.remove(l_raise[0])
l_decline.remove(l_decline[0])
with open(r"F:\vscode-python-kiton\lab-calc\proteomics\0424updown.txt", 'w' ) as f:
    f.write("-"*20 + "蛋白质组学蛋白研究蛋白筛选" + "-"*20 + '\n\n')
    
    f.write("-"*20 + "0h-4h-24h共同出现变化的蛋白" + "-"*20 +'\n')
    f.write("-"*70 + '\n')
    for i in l_inter:
        f.write(' '*20 + str(i)+'\n')
    f.write("-"*70 + '\n\n')

    
    f.write("-"*20 + "0h-4h-24h表达量持续增大的蛋白" + "-"*20 +'\n')
    f.write("-"*70 + '\n')
    for i in l_raise:
        f.write(' '*20 + str(i)+'\n')
    f.write("-"*70 + '\n\n')

    f.write("-"*20 + "0h-4h-24h表达量持续下降的蛋白" + "-"*20 +'\n')
    f.write("-"*70 + '\n')
    for i in l_decline:
        f.write(' '*20 + str(i)+'\n')
    f.write("-"*70 + '\n\n')


    localtime = time.asctime( time.localtime(time.time()) )
    
    f.write("保存时间为 :" + localtime)




# a = list(filter(nan, l_raise))
# print(a)



# with open(r"F:\vscode-python-kiton\lab-calc\proteomics\0424updown.csv",encoding='gb18030',errors='ignore') as csvfile:
#     reader = csv.reader(csvfile,delimiter = 't')
#     column1 = [row['04up'] for row in reader]
#     column2 = [row[2] for row in reader]
#     column3 = [row[3] for row in reader]
#     column4 = [row[4] for row in reader]
#     print(column1)
#     print(column2)
#     print(column3)
#     print(column4)


