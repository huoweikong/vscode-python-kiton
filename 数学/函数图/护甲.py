import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0,900,1000)
y1 = [i/(100+i) for i in x1]
plt.plot(x1, y1)

x2 = np.linspace(0,900,1000)
y2 = np.linspace(0,0.9,1000)
plt.plot(x2, y2,  color='g',markerfacecolor='blue',linewidth=1.0)  


y3 = y1-y2
plt.plot(x1, y3,color ='y')

new_ticks1 = np.linspace(0, 1000, 21)
new_ticks2 = np.linspace(0, 1, 21)
plt.xticks(new_ticks1)
plt.yticks(new_ticks2)


#柱状图

x4 = np.linspace(0,900,20)
y4 = [(i/(100+i) - (i-50)/(100+(i-50))) for i in x4]
plt.bar(range(len(x4)), y4, tick_label=x4)


# new_ticks = np.linspace(0, 1, 20)
# plt.xticks(new_ticks)
# plt.yticks([-2, -1.8, -1, 1.22, 3],['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])

plt.legend()  
plt.show()


# x = np.linspace(0, 1, 50) # 从0到1，等分50分
# y = 210(x**6)((1-x)**4) # 这里是函数的表达式

# plt.figure() # 定义一个图像窗口
# plt.plot(x, y) # 绘制曲线 y

# plt.show()