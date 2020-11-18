#机器学习神经网络
# here put the import lib

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1' #不用GPU 使用CPU

import tensorflow as tf 
from tensorflow import keras

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
mnist = keras.datasets.fashion_mnist
(X_train, y_train),(X_test,y_test) = mnist.load_data()

print("训练数据形状，" , X_train.shape)
print("数据最大值 " , np.max(X_train))
print("查看标签数值 " , y_train)

class_names =['top','trouser','pullover','dress','coat','sandal','shirt','sneaker','bag','ankle boot']#定义10个类别的名称

plt.figure()#可视化
plt.imshow(X_train[1])#【】里面的数据可以自己输入随便一个画出第几个的图
plt.colorbar()#加一个颜色条
plt.show()

#将数据集归一化 即降低数据集的值
X_train = X_train/255.0
X_test = X_test/255.0
plt.figure()#可视化
plt.imshow(X_train[1])#【】里面的数据可以自己输入随便一个画出第几个的图
plt.colorbar()#加一个颜色条
plt.show()

#可以看出值被缩放到0到1之间
from tensorflow.python.keras.models import Sequential #导入训练模型
from tensorflow.python.keras.layers import Flatten,Dense#导入神经网络的第一层和第二层


model = Sequential()
model.add(Flatten(input_shape = (28,28)))#此行代码是将图的大小数据转换成一维的数据
model.add(Dense(128,activation = 'relu'))#定义第一层神经网络有128个单元，并且选择的激活函数是ReLu函数，也可以是其他函数性sigmoid函数
# 这里要是不懂可以查看吴恩达老师深度学习的3.6节课
model.add(Dense(10,activation = 'softmax'))#定义输出层，有10类所以输出10，激活函数是max函数

print("查看自己写的代码的总体参数 " , model.summary())#查看自己写的代码的总体参数


#模型补充
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])#定义损失函数

#使用的优化器名叫AdamOptimizer，使用的损失函数是稀疏分类交叉熵




model.fit(X_train,y_train,epochs = 10)#进行训练，epochs是显示运行多少次

test_loss, test_acc = model.evaluate(X_test,y_test)#利用测试集测试训练下的模型的准确度
print(test_acc)

#预测模型精确度
from sklearn.metrics import accuracy_score
y_pred = model.predict_classes(X_test)

print(accuracy_score(y_test, y_pred))

#print(tf.test.is_gpu_available())


