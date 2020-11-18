#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   randlist.py
@Time         :   2020/06/13 01:55:58
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib

import random


def random_list2(a):
    a_copy = a.copy()
    result = []
    count = len(a)
    for i in range(0, count):
        index = random.randint(0, len(a_copy) - 1)
        result.append(a_copy[index])
        del a_copy[index]
    return result

test = [1, 3, 4, 5, 6]
result = random_list2(test)
print(result)