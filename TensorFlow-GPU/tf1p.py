#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   tf1p.py
@Time         :   2020/05/28 19:08:05
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib

import tensorflow as tf 

#raise RuntimeError('The Session graph is empty.  Add operations to the '
#RuntimeError: The Session graph is empty.  Add operations to the graph before calling run().
tf.compat.v1.disable_eager_execution()
#******************************

a=tf.constant([1.0,2.0,3.0],shape=[3],name='a')
b=tf.constant([1.0,2.0,3.0],shape=[3],name='b')
c=a+b


#通过log_device_placement参数来输出运行每一个运算的设备
sess=tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))

print (sess.run(c))