import pandas as pd 
import numpy as np


dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102',periods=6))
df['F'] = s1
print('df')
print(df)
df1 = df.reindex(index=dates[0:4], columns = list(df.columns)+ ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
# print('df1')
# print(df1)
# #To drop any rows that have missing data.
# df1d = df1.dropna(how='any')
# print(df1d)

# #Filling missing data.
# df1f = df1.fillna(value=5)
# print(df1f)

# #To get the boolean mask where values are nan.
# pd.isna(df1)

#Performing a descriptive statistic:
dfm =df.mean()
print(dfm)

#Same operation on the other axis:
dfm1 = df.mean(1)
print(dfm1)

#Operating with objects that have different dimensionality and need alignment. In addition, pandas automatically
#broadcasts along the specified dimension.
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
dfsi = df.sub(s, axis='index')
print(dfsi)

# Applying functions to the data:
a = df.apply(np.cumsum)#往下累加
b = df.apply(lambda x: x.max() - x.min())
print(a)
print(b)

#See more at Histogramming and Discretization.
s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()

#String Methods
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower()

#Concatenating pandas objects together with concat():
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)

print(df[:3])

#Join
#SQL style merges. See the Database style joining section.
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print("left")
print(left)
print(right)

pdm = pd.merge(left, right, on='key')
print(pdm)