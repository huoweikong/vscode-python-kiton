import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
plt.figure(figsize=(4, 4))
#venn2(subsets=(3, 2, 1))
# 设置三组ABCD、DEF、ADG
venn3([set(['A', 'B', 'C', 'D']), set(['D', 'E', 'F']), set(['A', 'D', 'G','F'])]);
plt.show()