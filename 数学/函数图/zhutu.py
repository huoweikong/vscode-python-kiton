import matplotlib.pyplot as plt  
import random
import numpy as np

x4 = np.linspace(0,300,31)
y4 = [(i/(100+i) - (i-10)/(100+(i-10))) for i in x4]
plt.bar(range(len(x4)), y4, tick_label = x4)


# new_ticks = np.linspace(0, 1, 20)
# plt.xticks(new_ticks)
# plt.yticks([-2, -1.8, -1, 1.22, 3],['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])

plt.legend()  
plt.show()