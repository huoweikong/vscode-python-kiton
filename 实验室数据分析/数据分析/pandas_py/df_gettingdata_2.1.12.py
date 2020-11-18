import pandas as pd
import numpy as np
import os,sys
os.chdir(sys.path[0])

ts = pd.Series(np.random.randn(1000))
df = pd.DataFrame(np.random.randn(1000, 4), \
        index=ts.index,columns=['A', 'B', 'C', 'D'])

# df.to_csv('foo.csv')
# a = pd.read_csv('foo.csv')

# print(a.head(6))

# df.to_hdf('foo.h5', 'df')
# b = pd.read_hdf('foo.h5', 'df')
# print(b.head(6))

df.to_excel('foo.xlsx', sheet_name='Sheet1')
c = pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
print(c.head(6))