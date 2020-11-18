import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

plt.close('all')
ts = pd.Series(np.random.randn(1000))
ts=ts.cumsum()
ts.plot()
df = pd.DataFrame(np.random.randn(1000, 4), \
        index=ts.index,columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()