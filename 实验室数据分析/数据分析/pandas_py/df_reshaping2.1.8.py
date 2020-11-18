import numpy as np 
import pandas as pd
tuples = list(
    zip(
        *[
    ['bar', 'bar', 'baz', 'baz',
    'foo', 'foo', 'qux', 'qux'],
    ['one', 'two', 'one', 'two',
    'one', 'two', 'one', 'two']
    ]
    )
    )

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
print(df)
# The stack() method “compresses” a level in the DataFrame’s columns.
stacked = df2.stack()
print(stacked)
# We can produce pivot tables from this data very easily:
#pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])

rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
t = ts.resample('5Min').sum()
print(t)
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
ps = ts.to_period()
print(ts)