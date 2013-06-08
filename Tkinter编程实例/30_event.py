#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
#---------------------------测试鼠标点击(Click)事件 ---------------------------------------
#<Button-1>
def printCoords(event):
	print(event.x,event.y) # 得到鼠标的坐标值
bt1 = Button(root,text='ClickMe')
bt1.bind('<Button-2>',printCoords)
bt1.grid()

#---------------------------测试鼠标移动(Motion)事件 ---------------------------------------
# 当鼠标按下后移动而产生的事件
# <Bx-Motion>  x=1,2,3分别表示左，中，右鼠标操作
bt2 = Button(root,text='leftmost button')
bt2.bind('<B1-Motion>',printCoords)
bt3 = Button(root,text='middle button')
bt3.bind('<B2-Motion>',printCoords)
bt4 = Button(root,text='rightmost button')
bt4.bind('<B3-Motion>',printCoords)
bt1.config(width=40)
bt2.config(width=40)
bt3.config(width=40)
bt4.config(width=40)

bt2.grid()
bt3.grid()
bt4.grid()
root.columnconfigure(0,minsize=200)

#---------------------------测试鼠标释放(Release)事件 ---------------------------------------
#<ButtonRelease-x>  x=1,2,3
def printCoord(event):
	print(event.x,event.y)
bt5 = Button(root,text = 'leftmost button')
bt5.bind('<ButtonRelease-1>',printCoord)
bt5.grid()

#---------------------------进入(Enter)事件---------------------------------------
bt1.bind('<Enter>',printCoords) #鼠标进入时
bt1.focus() #设置为焦点
bt1.bind('<Return>',printCoords)  #按回车时

root.mainloop()
