from sklearn import svm
import numpy as np

x = [[2, 0], [1, 1], [2, 3]]
y = [0, 0, 1]
clf = svm.SVC(kernel = 'linear')  #definite classify filter
clf.fit(x, y)

print (clf)

# get support vectors
print (clf.support_vectors_)
# get indices of support vectors
print (clf.support_)
# get number of support vectors for each class
print (clf.n_support_)

#predict
list1=[3,.0]
list_shape = np.array(list1)
print(list_shape)
list2 = [[1.5,.0],[6,0]]
print(clf.predict(list_shape.reshape(1,-1)))
print(clf.predict(list2))