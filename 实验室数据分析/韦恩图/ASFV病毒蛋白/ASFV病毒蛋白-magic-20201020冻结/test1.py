import csv


import pandas as pd
#a和b的长度必须保持一致，否则报错
a = [x for x in range(5)]
b = [x for x in range(5,10)]
#字典中的key值即为csv中列名
dataframe = pd.DataFrame({'a_name':a,'b_name':b})

#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv(r"test.csv",sep=',')