#!/usr/bin/python
#encoding:gbk

from tkinter import *
root = Tk()
# Frame 就是屏幕上的一块矩形区域，一般是用作容器（container）来布局窗体

##------------------创建 Frame ------------------------------
import mycolor
colorDB = mycolor.get_color()
#for color in colorDB[:20]:
#	Frame(height=20,width=400,bg=color).pack()

##------------------创建 Frame 并向其中添加Widget ------------------------------
#fm = []
#for color in ['red','blue','green']:
#	fm.append(Frame(height=200,width=400,bg=color))
#Label(fm[0],text = 'Hello Color Lebal').pack()
##Label(fm[1],text = 'Hello Color Lebal').pack()
##Label(fm[2],text = 'Hello Color Lebal').pack()
#fm[0].pack()
#fm[1].pack()
#fm[2].pack()
##要添加标签，必须在 fm.pack()之前添加，否则添加不进去

##------------------ LabelFrame 添加了Title的支持 ------------------------------
for color in colorDB[90:100]:
	lf = LabelFrame(height=40,width=300,text=color,bg=color)
	lf.pack(fill='both')





mainloop()
