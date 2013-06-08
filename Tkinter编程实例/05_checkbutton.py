#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
#-----------------CheckButton（复选框）---------------------------------------------------------------------------------
#复选框有两种状态，on，off
#每选一次时，回调函数被调用
def callCB():
	if sv.get()=='关闭':
		sv.set('打开')
	else:
		sv.set('关闭')

sv = StringVar()
lb = Label(root,textvariable=sv,font='幼圆 '+'-30'+' normal')
sv.set('关闭')
lb.pack(side='left',anchor='nw')
cb = Checkbutton(root,text='python',command=callCB)
cb.pack(side='left',anchor='nw')

def callCheckButton():
	v.set('check Tkinter')
v = StringVar()
v.set('check python')
Checkbutton(root,text='check python',textvariable=v,command=callCheckButton).pack(anchor='w')

#-----------------显示Checkbutton的值---------------------------------------------------------------------------------
sta = IntVar()
def callCButton():
	print(sta.get())

Checkbutton(root,variable=sta,text='checkbutton value',command=callCButton).pack(anchor='w')

#-----------------onvalue,offvalue---------------------------------------------------------------------------------
onoff = StringVar()
onoff.set(0)
def callonoff():
	print(onoff.get())

Checkbutton(root,variable = onoff, text = 'checkbutton value',
			onvalue='python',offvalue='tkinter',
			command=callonoff).pack()


mainloop()