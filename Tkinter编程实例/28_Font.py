#!/usr/bin/python
#coding:gbk

from tkinter import *
root = Tk()
#-----------------------字体的使用----------------------------------------------------------
for ft in ('Arial',('Courier New',),('Comic Sans MS',),'Fixdsys',('MS Sans Serif',),('MS Serif',),'Symbol','System',('Times New Roman',),'Verdana'):
	Label(root,text='hello World',font=ft).grid()
# 在Windows 上测试字体显示，注意字体中包含有空格的字体名称必须指定为 tuple 类型。

#-----------------------使用系统已有字体----------------------------------------------------------
# Font: 指定字体名称
# family：指定字体名称
# size：指定字体大小
# wight：样式
from tkinter.font import *
ft = Font(family = '微软雅黑',size = 20,weight = BOLD)
Label(root,text = 'hello sticky',font = ft ).grid()

for ft in ('ansi','ansifixed','device','oemfixed','system','systemfixed'):
	Label(root,text = 'hello font',font = ft ).grid()
for ft in ('Times','Helvetica','Courier','Symbol',):
	Label(root,text = 'hello font',font = ('-*-%s-*-*-*--*-240-*')%(ft)).grid()
root.mainloop()










###获取系统字体的程序段
#import os
#import glob
#os.chdir(r'c:\windows\fonts')
#name = glob.glob('*.*')
#name = name[::]
#fonts = []
#for i in range(len(name)):
#	(shortname,ext)=os.path.splitext(name[i])
#	fonts.append(shortname)
#print(fonts)
#r,col = 0,0
#for font in fonts:
#	Label(root,text='M',font=font).grid(row=r,column=col)
#	col = col + 1
#	if col%80==0:
#		r = r + 1
#		col = 0