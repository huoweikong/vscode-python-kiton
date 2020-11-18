import pandas as pd
import os,sys
a = os.getcwd()
os.chdir(sys.path[0])
b = os.getcwd()
print(a)
print(b)
data = pd.read_csv('data.csv')
print(data)

data.to_csv( 'todata.csv' , index=None)
data.to_csv( 'todata2.csv' )

print(data.shape)
c = data.describe()
print(c)
data[ column_1 ].plot()