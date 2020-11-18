#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   tf1.py
@Time         :   2020/05/28 18:40:39
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())