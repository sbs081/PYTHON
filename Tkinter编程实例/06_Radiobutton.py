#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
#-----------------Radiobutton控件---------------------------------------------------------------------------------
#Radiobutton控件有组的概念：下面的例子未指定组，每个控件自成一组
Radiobutton(root,text='python' ).pack()
Radiobutton(root,text='tkinter').pack()
Radiobutton(root,text='widget' ).pack()

#-----------------创建组，绑定变量---------------------------------------------------------------------------------
v = IntVar()
v.set(1)
for i in range(3):
	Radiobutton(root,variable=v,text='python',value=i).pack()

#-----------------创建两个不同的组---------------------------------------------------------------------------------
vLang = IntVar()
vOS = IntVar()
vLang.set(1)
vOS.set(2)

for var in [vLang,vOS]:
	for i in range(3):
		Radiobutton(root,variable=var,value=i,text='python'+str(i)).pack()

#-----------------RadioButton：indicatoron属性默认为1----------------------------------------------------------------
idon = IntVar()
idon.set(1)
for i in range(3):
	Radiobutton(root,variable=idon,indicatoron=0,text = 'python & tkinter',value=i).pack()
#indicatoron=0时，用的是按钮的按下或弹起来表示选中


mainloop()