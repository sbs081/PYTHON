#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
#root.geometry('400x300')
#---------------Button 功能是能触发事件-----------------------------------------------------------------------------------------------------------------
def Hello():
	print('Hello World')
Button(root,text = 'SayHello',command=Hello).pack()

#---------------Button relief属性（风格）-----------------------------------------------------------------------------------------------------------------
X=[RAISED, SUNKEN,GROOVE ,RIDGE,FLAT,SOLID]
for key in X:
	Button(root,text = '%s'%key,relief = key).pack(side='left',expand=1)

#---------------Button 显示图像和文本-----------------------------------------------------------------------------------------------------------------
pic = PhotoImage(file=r'C:\temp\ButtonQuit.gif')
Button(root,text='按钮',image=pic,compound='left').pack(side = 'left')

#---------------控件焦点问题-----------------------------------------------------------------------------------------------------------------
def cb1():print('button1 clicked')
def cb2(event):print('button2 clicked')
def cb3():print('button3 clicked')
b1 = Button(root,text='button1',command=cb1)
b2 = Button(root,text='button2',command=cb1)
b2.bind('<Return>',cb2)
b3 = Button(root,text='button3',command=cb1)
b1.pack(side='left');b2.pack(side='left');b3.pack(side='left')
b2.focus_set()

#---------------事件信息-----------------------------------------------------------------------------------------------------------------
def printEvenInfo(event):
	print('event.time = ',event.time)
	print('event.type = ',event.type)
	print('event.WidgetId = ',event.widget)
	print('event.KeySymbol = ',event.keysym)
	print('event.time = ',event.time)
b = Button(root,text='Information')
##按回车键时，打印事件信息
##<Enter>：表示当鼠标进入时打印信息
b.bind('<Return>',printEvenInfo)
b.pack()
##定位到按钮 b，此时按回车有效
#b.focus_set()

mainloop()
