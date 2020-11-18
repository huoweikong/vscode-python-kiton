#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :   tkinter1wanghui.py
@Time         :   2020/05/28 17:32:05
@Author       :   艾强云
@Contact      :   aqy0716@163.com
@Department   :   SCAU 
@Desc         :   None
'''

# here put the import lib
from tkinter import *

class WidgetDemo:
    def __init__(self):
        window=Tk()
        window.title("Widget Demo")

        frame1=Frame(window)
        frame1.pack()
        self.v1=IntVar()#int类型的变量
        cbtBold=Checkbutton(frame1,text="Bold",variable=self.v1,command=self.processCheckButton)#checkbutton可在值之间切换
        self.v2=IntVar()
        rbRed=Radiobutton(frame1,text="red",bg="red",variable=self.v2,value=1,command=self.processRadiusButton)#radiobutton单击单选变量
        rbyellow=Radiobutton(frame1,text="yellow",bg="yellow",variable=self.v2,value=2,command=self.processRadiusButton)
        cbtBold.grid(row=1,column=1)#对几个按钮进行排版
        rbRed.grid(row=1,column=2)
        rbyellow.grid(row=1,column=3)




        frame2=Frame(window)
        frame2.pack()
        label=Label(frame2,text="enter your name: ")
        self.name=StringVar()
        entryname =Entry(frame2,textvariable=self.name)
        btGetname=Button(frame2,text="get name",command=self.processButton)
        message=Message(frame2,text=" it is a widgets demo")#label可显示图像和文字，message只能显示文字
        label.grid(row=1,column=1)
        entryname.grid(row=1,column=2)
        btGetname.grid(row=1,column=3)
        message.grid(row=1,column=4)

        text=Text(window)
        text.pack()
        text.insert(END,"A\n")#从结尾处插入
        text.insert(END,"B\n")
        text.insert(END,"C\n")
        window.mainloop()

    def processCheckButton(self):
        print("check button is "+("checked"if self.v1.get()==1 else "unchecked"))
    def processRadiusButton(self):
        print(("red" if self.v2.get()==1 else "yellow")+" is selected")
    def processButton(self):
        print("your name is "+self.name.get())

WidgetDemo()
#只有window下属一个等级的要pack，其他不用