# By “group by” we are referring to a process involving one or more of the following steps:
# • Splitting the data into groups based on some criteria
# • Applying a function to each group independently
# • Combining the results into a data structure
# See the Grouping section.
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
    'A': ['foo', 'bar', 'foo', 'bar',
    'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three',    'two', 'two', 'one', 'three'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)
    }
    )

print(df)
dfgA = df.groupby('A').sum()
print(dfgA)

dfgB = df.groupby(['A', 'B']).sum()
print(dfgB)
