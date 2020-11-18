import pandas as pd
import numpy as np
import os,sys
os.chdir(sys.path[0])

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
pdsr5 = pd.Series(np.random.randn(5))
d = {'b': 1, 'a': 0, 'c': 2}
pdsd = pd.Series(d)
print(s)
# print(pdsr5)
# print(pdsd)

# pdsd = pd.Series(d)
# a = pd.Series(d)
# b = pd.Series(d, index=['b', 'c', 'd', 'a'])
# print(a)
# print(b)

# #If data is a scalar value, an index must be provided. The value will be repeated to match the length of index.
# a = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
# print(a)

print(s[0])
print(s[:3])
print(s[s > s.median()])
print(s[[4, 3, 1]])
print(np.exp(s))
print(s.array)
print(s.dtype)
print(s.to_numpy())

#A Series is like a fixed-size dict in that you can get and set values by index label:
s['a']
s['e'] = 12.
'e' in s
'f' in s

#When working with raw NumPy arrays, looping through value-by-value is usually not necessary. The same is true
#when working with Series in pandas. Series can also be passed into most NumPy methods expecting an ndarray.
s + s
s * 2
np.exp(s)
s[1:] + s[:-1] #hether the Series involved have the same labels.


# Name attribute
# Series can also have a name attribute:
s = pd.Series(np.random.randn(5), name='something')
s.name
s2 = s.rename("different")
s2.name
