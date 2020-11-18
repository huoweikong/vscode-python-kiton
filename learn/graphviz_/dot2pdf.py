#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   dot2pdf.py
@Time         :   2020/06/19 01:27:51
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dot2pdf.py
@Time    :   2020/06/10 19:21:46
@Author  :   Ai Qiangyun 
@Version :   1.0
@Contact :   aqy0716@163.com
@License :   (C)Copyright 2020 SCAU
@Desc    :   None
'''
#通过.gv文件渲染转化为PDF和JPG文件
# here put the import lib

from graphviz import Source

#打开.gv有向图元文件，渲染格式为PDF
path = r'G:\BaiduNetdiskDownload\最新python爬虫神经网络深度学习算法\04.深度神经网络算法之基础精讲\机器学习深度神经网络学习基础一  29课\代码与素材\代码与素材(1)\01DTree\allElectronicInformationGainOri.dot'
s = Source.from_file(path,format='pdf')
print(s.source)

#打开渲染引擎，保存为。字符文件和指定的pdf文件，清除字符文件，------最后只剩下一个指定路径下和指定前缀名的PDF文件------
s.view(r"G:\BaiduNetdiskDownload\最新python爬虫神经网络深度学习算法\04.深度神经网络算法之基础精讲\机器学习深度神经网络学习基础一  29课\代码与素材\代码与素材(1)\01DTree\fff1",cleanup=True)