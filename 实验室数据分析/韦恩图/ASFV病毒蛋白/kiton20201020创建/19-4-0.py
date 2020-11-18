import pandas as pd
import numpy as np
import os,sys
os.chdir(sys.path[0])

# library
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

import pandas as pd

from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']

"L:\研究生\文章发表-Kiton\ASFV蛋白质组学\蛋白质组学 质谱ASFV库 87.xlsx"
def excel_one_line_to_list(lieshu):
    df = pd.read_excel(r"F:\vscode-python-kiton\实验室数据分析\韦恩图\original_data\19-4-0.xlsx", usecols=[lieshu],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    return result

shiyan  = excel_one_line_to_list(0)
wenxian  = excel_one_line_to_list(1)

a=shiyan
b=wenxian

#找出相同元素
c=[x for x in a if x in b]

#找出不同元素
d=[y for y in (a+b) if y not in c]
print(c)
print(d)
#找出a中独有元素
e = [x for x in d if x in a]
#找出b中独有的元素
f = [x for x in d if x in b]
print(e)
print(f)


subset1 = [set(shiyan),set(wenxian)]



venn2(subset1,set_labels=('6h','24h'),set_colors=('r','g'),alpha=0.4,normalize_to=1.0,ax=None,subset_label_formatter=None)
plt.show()
# # 第一种方法，10，5为两组的大小，2为两组交叉大小;
# # set_labels为组名
# venn2(subsets = (10, 5, 2), set_labels = ('Group A', 'Group B'));
# # 设置两组ABCD和DEF
# venn2([set(['A', 'B', 'C', 'D']), set(['D', 'E', 'F'])]);