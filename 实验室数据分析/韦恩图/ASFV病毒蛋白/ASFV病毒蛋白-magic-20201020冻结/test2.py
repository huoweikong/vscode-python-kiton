# Import the library
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
 
# Make the diagram
# A B AB-c C AC-B BC-A ABC
venn3(subsets = (10, 8, 22, 6,9,4,2))

plt.show()







# Operation   Equivalent  Result
# len(s)      number of elements in set s (cardinality)
# x in s      test x for membership in s
# x not in s      test x for non-membership in s
# s.issubset(t)   s <= t  test whether every element in s is in t
# s.issuperset(t)     s >= t  test whether every element in t is in s
# s.union(t)  s | t   new set with elements from both s and t
# s.intersection(t)   s & t   new set with elements common to s and t
# s.difference(t)     s - t   new set with elements in s but not in t
# s.symmetric_difference(t)   s ^ t   new set with elements in either s or t but not both
# s.copy()        new set with a shallow copy of s