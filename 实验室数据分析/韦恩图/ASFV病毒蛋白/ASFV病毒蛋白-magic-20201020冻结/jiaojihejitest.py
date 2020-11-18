

from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles

A = set(['DPEP1', 'CDC42BPA', 'GNG4', 'RAPGEFL1', 'MYH7B', 'SLC13A3', 'PHACTR3', 'SMPX', 'NELL2', 'PNMAL1', 'KRT23', 'PCP4', 'LOX', 'CDC42BPA'])
B = set(['ABLIM1','CDC42BPA','VSNL1','LOX','PCP4','SLC13A3'])
C = set(['PLCB4', 'VSNL1', 'TOX3', 'VAV3'])
# print(A)
# print(B)
# print(C)

A = [a_ for a_ in a if a_ == a_]
B = [a_ for a_ in b if a_ == a_]
C = [a_ for a_ in c if a_ == a_]

# A, B, AB_C, C, AC_B, BC_A, ABC
# A B AB-c C AC-B BC-A ABC
A_B_C = A.difference(B).difference(C)
B_A_C = B.difference(A).difference(C)
AB_C = A.intersection(B).difference(C)
C_B_A = C.difference(B).difference(A)
AC_B = A.intersection(C).difference(B)
BC_A = B.intersection(C).difference(A)
ABC = A.intersection(B).intersection(C)
print(A_B_C, B_A_C, AB_C, C_B_A, AC_B, BC_A, ABC)


f = [a_ for a_ in f if a_ == a_]

v = venn3([A,B,C], ('GCPromoters', 'OCPromoters', 'GCSuppressors'))

ppp=v.get_label_by_id('100').set_text('\n'.join(A_B_C))
v.get_label_by_id('110').set_text('\n'.join(AB_C))
v.get_label_by_id('011').set_text('\n'.join(BC_A))
v.get_label_by_id('001').set_text('\n'.join(C_B_A))
v.get_label_by_id('010').set_text('\n'.join(B_A_C))
v.get_label_by_id('101').set_text('\n'.join(AC_B))
v.get_label_by_id('111').set_text('\n'.join(ABC))
plt.annotate(',\n'.join(B-A-C), xy=v.get_label_by_id('010').get_position() +
             np.array([0, 0.2]), xytext=(-20,40), ha='center',
             textcoords='offset points', 
             bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
             arrowprops=dict(arrowstyle='->',              
                             connectionstyle='arc',color='gray'))
plt.show()
