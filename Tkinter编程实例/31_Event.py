#!/usr/bin/python
#coding:gbk

from tkinter import *
root = Tk()
def printCoords(event):
	print(event.x,event.y)

#----------------------鼠标离开（Leave）时事件--------------------------------
#bt1 = Button(root,text='leftmost button')
#bt1.bind('<Leave>',printCoords)
#bt1.grid()

#----------------------相应特殊键（Special Key）--------------------------------
#def printSK(event):
#	print('   event.char = ',event.char)
#	print('event.keycode = ',event.keycode)
#bt2 = Button(root,text='Press BackSpace')
#bt2.bind('<BackSpace>',printSK)
#bt2.grid()

#----------------------相应所有的按键(key)事件--------------------------------
ms = Message(root,text='请按键',font='微软雅黑 18',relief='solid',width=400)
def printAllKey(event):
	ms.config(text='char:'+event.char+'\tkeycode:'+str(event.keycode))

bt = Button(root,text='All Key')
bt.bind('<Key>',printAllKey)
ms.grid()
bt.grid()
bt.focus()

# 一般的按键直接使用就可以了，这样书写'key',不是'<key>'; 如：'a','A'
# 但有两个需要特别注意:空格与小于的处理，使用方式为'<space>和<less>


#----------------------相应组合按键事件--------------------------------
#<Shift-Up>
#<Ctrl-Up>
#<Ctrl-Shift>
#<Ctrl-Alt-a>
#不能使用 <Ctrl-Alt>

# configure：改变组件大小事件
# 当组件的大小改变时触发。evnet.width/height 分别返回改变后的宽度和高度。
def printSize(event):
	print (event.width,event.height)
root.bind('<Configure>',printSize)
#----------------------改变组件大小事件--------------------------------
# 各个组件间焦点的切换可以使用TAB 键。
# 特殊键 
#Cancel
#Break
#BackSpace
#Tab
#Return
#Sift_L
#Shift_R
#Control_L
#Control_R
#Alt_L
#Alt_R
#Pause
#Caps_Loack
#Escape
#Prior(Page Up)
#Next(PageDown)
#End
#Home
#Left
#Up
#Right
#Down
#Print
#Insert
#Delete

# F1-12
#Num_Lock
#Scroll_Lock

# 这些键的char 是不可打印的，可以使用event.keycode 查看。



root.mainloop()