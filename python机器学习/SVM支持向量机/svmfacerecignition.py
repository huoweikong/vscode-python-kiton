# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tanghong

# 在python2.x版本中要使用Python3.x的特性,可以使用__future__模块导入相应的接口，减少对当前低版本影响
# from __future__ import print_function

# 计时，程序运行时间
from time import time
# 打印程序进展时的一些信息
import logging
# 最后识别出来的人脸通过绘图打印出来
import matplotlib.pyplot as plt
# DeprecationWarning: `imread` is deprecated! `imread` is deprecated in SciPy
# 1.0.0,and will be removed in 1.2.0.
from PIL import Image
from scipy import ndimage

# 当import 一个模块比如如下模块cross_validation时，会有删除横线，表示该模块在当前版本可能已经被删除,在新版本中改为model_selection模块
# DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection
# module into which all the refactored classes and functions are moved.
# Also note that the interface of the new CV iterators are different from that of this module.
# This module will be removed in 0.20."This module will be removed in 0.20.", DeprecationWarning)
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_lfw_people
# grid_search已经被移除
# from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
# Class RandomizedPCA is deprecated; RandomizedPCA was deprecated in 0.18 and will be removed in 0.20. 
# Use PCA(svd_solver='randomized') instead. The new implementation DOES NOT store whiten ``components_``.
# Apply transform to get them.
from sklearn.decomposition import PCA
from sklearn.svm import SVC
# 导入混淆矩阵模块confusion_matrix()
from sklearn.metrics import confusion_matrix

print(__doc__)

# Display progress logs on stdout程序进展的信息打印出来
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

###############################################################################
# Download the data, if not already on disk and load it as numpy arrays
# 下载人脸库 http://vis-www.cs.umass.edu/lfw/
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# introspect the images arrays to find the shapes (for plotting)
n_samples, h, w = lfw_people.images.shape

# for machine learning we use the 2 data directly (as relative pixel
# positions info is ignored by this model)
# 获取特征向量矩阵
X = lfw_people.data
# 特征向量的维度(列数)或者称特征点的个数
n_features = X.shape[1]

# the label to predict is the id of the person
# 返回每一组的特征标记
y = lfw_people.target
target_names = lfw_people.target_names
# 返回多少类(多少行)，也就是多少个人进行人脸识别
n_classes = target_names.shape[0]

print("Total dataset size:")
print("n_samples: %d" % n_samples)
print("n_features: %d" % n_features)
print("n_classes: %d" % n_classes)

###############################################################################
# Split into a training set and a test set using a stratified k fold
# split into a training and testing set
# 将数据集拆分成四个部分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

###############################################################################
# PCA降维方法，减少特征值，降低复杂度。
# Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled
# dataset): unsupervised feature extraction / dimensionality reduction
n_components = 150

print("Extracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0]))
t0 = time()
pca = PCA(n_components=n_components, whiten=True).fit(X_train)

print("done in %0.3fs" % (time() - t0))

# 提取特征值
eigenfaces = pca.components_.reshape((n_components, h, w))

print("Projecting the input data on the eigenfaces orthonormal basis")
t0 = time()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print("done in %0.3fs" % (time() - t0))

###############################################################################
# Train a SVM classification model

print("Fitting the classifier to the training set")
t0 = time()
param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5], 'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
# clf = GridSearchCV(SVC(kernel='rbf', class_weight='auto'), param_grid)
clf = GridSearchCV(SVC(kernel='rbf'), param_grid)
clf = clf.fit(X_train_pca, y_train)
print("done in %0.3fs" % (time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)

###############################################################################
# Quantitative evaluation of the model quality on the test set

print("Predicting people's names on the test set")
t0 = time()
y_pred = clf.predict(X_test_pca)
print("done in %0.3fs" % (time() - t0))

print(classification_report(y_test, y_pred, target_names=target_names))
print(confusion_matrix(y_test, y_pred, labels=range(n_classes)))


###############################################################################
# Qualitative evaluation of the predictions using matplotlib

def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())


# plot the result of the prediction on a portion of the test set

def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]].rsplit(' ', 1)[-1]
    true_name = target_names[y_test[i]].rsplit(' ', 1)[-1]
    return 'predicted: %s\ntrue:      %s' % (pred_name, true_name)


prediction_titles = [title(y_pred, y_test, target_names, i)
                     for i in range(y_pred.shape[0])]

plot_gallery(X_test, prediction_titles, h, w)

# plot the gallery of the most significative eigenfaces

eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()
