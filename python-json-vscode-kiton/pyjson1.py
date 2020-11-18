#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pyjson1.py
@Time    :   2019/12/31 23:12:34
@Author  :   Ai Qiangyun 
@Version :   1.0
@Contact :   1154282938@qq.com
@License :   (C)Copyright 2019
Device  :   Kiton vscode
'''

# here put the import lib
from  tinydb import TinyDB
db = TinyDB('./python-json-vscode-kiton/db.json')
db.insert({'name':'Eason', 'age':'22'})
db.insert({'title':'Python', 'price':29.00})
db.insert({'title':'Flask', 'price':49.00})
# print(db)
for items in db:
    print(items)
