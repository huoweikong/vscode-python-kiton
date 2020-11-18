#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   pt3.py
@Time         :   2020/05/22 00:59:30
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib
from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf 

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

#minist = tf.keras.datasets.mnist


(x_train, y_strain), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train /255.0, x_test /255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)