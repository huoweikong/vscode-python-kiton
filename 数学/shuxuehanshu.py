#!coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.size'] = 14
 
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
 
plt.plot([-10,10],[0,0],'gray',':')
plt.plot([0,0],[-10,10],'gray',':')
 
x1 = np.arange(-10,0,0.1)
y1 = 1/x1
plt.plot(x1,y1)
 
x2 = np.arange(0.1,10,0.1)
y2 = 1/x2
plt.plot(x2,y2)
 
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(range(-10,11,2))
plt.yticks(range(-10,11,2))
ax.set_yticklabels(range(-10,11,2))
plt.axis([-10,10,-10,10])
plt.title(u'$y=\\frac{1}{x}$')
plt.grid(True)
 
plt.savefig(u"反比例函数.png")
plt.show()