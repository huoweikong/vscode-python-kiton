import pandas as pd
import numpy as np
df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
    })
print (df2)

print(df2.dtypes)
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
c = df.head()
print(df)
#c=df.to_numpy()
#df2_np = df2.to_numpy()
#print(c)
#print(df2_np)
#print(df.describe())
#print(df.T)
df_sort = df.sort_index(axis =1, ascending=False)
print("df_sort后\n", df_sort)
df_sort_B = df.sort_values(by='B')
print("df_sort_B按B列排序\n", df_sort_B)
print("df_A")
print(df['A'])
df_2_4 = df['20130102':'20130104']
print("df_2_4")
print(df_2_4)

#取某一行 索引数组
dates0 = df.loc[dates[0]]
print("dates0")
print(dates0)

#取行列，行为切片
dfAB = df.loc[:, ['A', 'B']]
print(dfAB)

#取行列，行为索引
df0A = df.at[dates[0],'A']
print(df0A)

#取某一行
df_3 = df.iloc[3]
print(df_3)

df_35_02 = df.iloc[3:5, 0:2]
print("dff_35_02")
print(df_35_02)
df.iloc[[1, 2, 4], [0, 2]]
df.iloc[1:3, :]
df.iloc[1, 1]
df.iat[1, 1]

df[df['A'] > 0]
dfbig0 = df[df > 0]
print("dfbig0")
print(dfbig0)
df2 = df.copy()

df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']

dfdf = df2[df2['E'].isin(['two', 'four'])]
print(dfdf)


s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102',periods=6))
print('s1')
print(s1)
df['F'] = s1
df.at[dates[0], 'A'] = 0
df.iat[0, 1] = 0
df.loc[:, 'D'] = np.array([5] * len(df))
print(df)
df2 = df.copy()
df2[df2 < 0] = -df2
print(df2)