#导入依赖packages
import matplotlib.pyplot as plt
from matplotlib_venn import venn2,venn2_circles#记得安装matplotlib_venn(pip install matplotlib_venn 或者conda install matplotlib_venn)
 
 
# subsets参数
#绘图数据的格式，以下5种方式均可以，注意异同
subset = [[{1,2,3},{1,2,4}],#列表list(集合1，集合2)
          ({1,2,3},{1,2,4}),#元组tuple(集合1，集合2)
          {'10': 1, '01': 1, '11': 2},#字典dict(A独有，B独有，AB共有)
          (3, 3, 2),####元组tuple（A有，B有，AB共有），注意和其它几种方式的异同点
          [3,3,2]#列表list（A有，B有，AB共有）           
         ]

import pandas as pd


def excel_one_line_to_list():
    df = pd.read_excel("/Users/Devintern/Documents/pachong/ML_flow/pachong/qmp/files/投资事件导出20190303.xlsx", usecols=[1],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    print(result)


if __name__ == '__main__':
    excel_one_line_to_list()

a=["fjds",'fd',"fdfsf"]
subset1 = [set(a),set(["fdf","df","fd"])]



venn2(subset1,set_labels=('A','B'),set_colors=('r','g'),alpha=0.4,normalize_to=1.0,ax=None,subset_label_formatter=None)
plt.show()