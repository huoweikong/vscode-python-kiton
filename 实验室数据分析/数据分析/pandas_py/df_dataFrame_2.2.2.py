import pandas as pd
import numpy as np
import os,sys
os.chdir(sys.path[0])

d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),\
    'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

a = pd.DataFrame(d, index=['d', 'b', 'a'])
b = pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
print(a)
print(b)
df.index
df.columns

d = {'one': [1., 2., 3., 4.],\
    'two': [4., 3., 2., 1.]}
pd.DataFrame(d)
pd.DataFrame(d, index=['a', 'b', 'c', 'd'])
data = np.zeros((2, ), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
pd.DataFrame(data)
pd.DataFrame(data, index=['first', 'second'])
pd.DataFrame(data, columns=['C', 'A', 'B'])

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
pd.DataFrame(data2)
pd.DataFrame(data2, index=['first', 'second'])
pd.DataFrame(data2, columns=['a', 'b'])

#From a dict of tuples
pdtuple = pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},\
    ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},\
    ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},\
    ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},\
    ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
print(pdtuple)

# From a Series
from dataclasses import make_dataclass
Point = make_dataclass("Point", [("x", int), ("y", int)])
pdmd = pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
print(pdmd)

#DataFrame.from_dict
pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]))

pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]),\
    orient='index', columns=['one', 'two', 'three'])

#DataFrame.from_records
data
pd.DataFrame.from_records(data, index='C')

#Column selection, addition, deletion
df['one']
df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2

#Columns can be deleted or popped like with a dict
del df['two']
three = df.pop('three')

#When inserting a scalar value, it will naturally be propagated to fill the column
df['foo'] = 'bar'

#When inserting a Series that does not have the same index as the DataFrame, it will be conformed to the DataFrame’s index:
df['one_trunc'] = df['one'][:2]

#You can insert raw ndarrays but their length must match the length of the DataFrame’s index.
##By default, columns get inserted at the end. The insert function is available to insert at a particular location in the
#columns
df.insert(1, 'bar', df['one'])
