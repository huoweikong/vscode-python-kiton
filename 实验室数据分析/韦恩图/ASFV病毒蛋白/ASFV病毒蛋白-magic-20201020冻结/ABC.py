from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles


A = set(['DPEP1', 'CDC42BPA', 'GNG4', 'RAPGEFL1', 'MYH7B', 'SLC13A3', 'PHACTR3', 'SMPX', 'NELL2', 'PNMAL1', 'KRT23', 'PCP4', 'LOX', 'CDC42BPA'])
B = set(['ABLIM1','CDC42BPA','VSNL1','LOX','PCP4','SLC13A3'])
C = set(['PLCB4', 'VSNL1', 'TOX3', 'VAV3'])

v = venn3([A,B,C], ('GCPromoters', 'OCPromoters', 'GCSuppressors'))

ppp=v.get_label_by_id('100').set_text('\n'.join(A-B-C))
v.get_label_by_id('110').set_text('\n'.join(A&B-C))
v.get_label_by_id('011').set_text('\n'.join(B&C-A))
v.get_label_by_id('001').set_text('\n'.join(C-A-B))
v.get_label_by_id('010').set_text('')
plt.annotate(',\n'.join(B-A-C), xy=v.get_label_by_id('010').get_position() +
             np.array([0, 0.2]), xytext=(-20,40), ha='center',
             textcoords='offset points', 
             bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
             arrowprops=dict(arrowstyle='->',              
                             connectionstyle='arc',color='gray'))
plt.show()