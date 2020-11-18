import pandas as pd
import re

with open("I:/vscode-python-kiton/snps.csv") as f:
    df = pd.read_csv(f)
f.close()


data=df.ix[:,['FTYPE','EFFECT']].values#读所有行的title以及data列的值，这里需要嵌套列表
print("读取指定行的数据：\n{0}".format(data))

count = 0
count_shift = 0
zi = 'frameshift_variant'
for item in data:
    if item[0] == 'CDS':
        count = count + 1
    
    result = zi in str(item[1])
    if result:
        count_shift  = count_shift + 1
    
        
print("CDS变异共有：" + str(count) + "种！")
print("移码变异共有：" + str(count_shift) + "种！")

# count_shift = 0
# for item  in dat


