#!/usr/bin/python
#coding:gbk
# Scale 为输出限定范围的数字区间，可以为之指定最大值，最小值及步距值
from tkinter import *
root = Tk()
root.geometry('400x400')
#=====================创建Scale（滑块）=================================================
Scale(root).pack()
#默认最大100，最小0，步长1，垂直放置

#=====================增加参数，创建Scale（滑块）=========================================
Scale(root,
	  from_ = -500,
	  to = 500,
	  resolution = 5,	#步长
	  orient = HORIZONTAL #水平方向
	  ).pack()

#=====================Scale绑定变量=====================================================
v1 = StringVar()
s = Scale(root,
	  orient = HORIZONTAL, #水平方向
	  variable = v1
	  )
s.pack()
print(v1.get())
#v的值与Scale的值一致

#=====================Scale之事件处理函数=====================================================
#这个回调函数有一个参数，这个值就是当前Scale的值
def printScale(text):
	print('text = ',text)
	print('   v = ',v.get())
v = StringVar()
scale = Scale(root,
			  resolution = 0.0001,
			  orient = HORIZONTAL,
			  variable = v,
			  command = printScale
			  ).pack()
print(v.get())

#=====================控制Scale显示位数===================================================================
def printScale(text):
	print('text = ',text)
	print('   v = ',var.get())
var = StringVar()
scale = Scale(root,
			  resolution = 0.0001,
			  orient = HORIZONTAL,
			  digits = 9,	#位数以最大数的为准，且包含整数部分（即为：数字的总位数）
			  variable = var,
			  command = printScale
			  ).pack(fill='x')
print(var.get())

#=====================设置/取得Scale的值=====================================================
s2 = Scale(root,label='请选择：',font='楷体 -18',orient=HORIZONTAL)
s2.set(50)
print(s2.get())
s2.pack(fill='x')

s


mainloop()