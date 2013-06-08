#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()

def printReturn(event):
	print ('<Return>',event.keycode)
def printEvent(event):
	print ('<Key>',event.keycode)
root.bind('<Return>',printReturn)
root.bind('<Key>',printEvent)
# 当按键为Return 时，由printReturn 来处理,即由最“近”的那个事件处理（什么事最“近”）


## 在 instance 级别与 printEvent 绑定
#bt1 = Button(root,text = 'instance event')
#bt1.bind('<Return>',printEvent)
## 在 bt1 的Toplevel 级别与 printToplevel 绑定
#bt1.winfo_toplevel().bind('<Return>',printToplevel)
## 在class 级别绑定事件printClass
#root.bind_class('Button','<Return>',printClass)
## 在application all 级别绑定printAppAll
#bt1.bind_all('<Return>',printAppAll)
#bt1.focus_set()
#bt1.grid()
## Return 向高级别进行了“传递",调用顺序为instance/class/toplevel/all

# bind_class：绑定整个类的事件处理函数，将影响所有这个类的instance
# root.bind_class('Button','<Return>',printClass)
# 即所有的Button 对Return 事件进行响应。

def printProtocol():
	print('WM_DELETE_WINDOW')
	root.destroy()
# 使用protocol 将WM_DELETE_WINDOW 与printProtocol 绑定
root.protocol('WM_DELETE_WINDOW',printProtocol)
root.mainloop()
# 程序在退出时打印'WM_DELETE_WINDOW'

root.mainloop()