#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   pt1.py
@Time         :   2020/05/21 22:33:38
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib
# 微信阅读教程tensorflow
import tensorflow as tf
import numpy as np 

tf.compat.v1.disable_eager_execution()

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

### create tensorflow structure start ###
Weights = tf.Variable(tf.random.uniform([1],-1.0,1.0))  #ensorflow显示没有random_uniform模块 解决办法：tf2.0里改名字了，用tf.random.uniform代替
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.5)
tf.compat.v1.disable_eager_execution()
train = optimizer.minimize(loss)

init = tf.compat.v1.initialize_all_variables()
### create tensorflow structure end ###

sess = tf.compat.v1.Session()
sess.run(init)  #Very important
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights),sess.run(biases))
