#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
fm1 = Frame(root)
fm1.pack(anchor=W)
fm2 = Frame(root)
fm2.pack(anchor=W)
fm3 = Frame(root)
fm3.pack(anchor=W)
#Listbox为列表框控件
#可以包含一个或多个文本项，
#可以设置为单选或多选

#---------------------创建一个Listbox-------------------------------------------------------------------------------------
lb = Listbox(fm1)
item = ['python','tkinter','widget']
for i in item:
	lb.insert(END,i)
lb.pack(side='left')

#---------------------Listbox可以选中多个item-----------------------------------------------------------------------------
#selectmode:SINGLE, BROWSE, MULTIPLE, or EXTENDED. Default is BROWSE
listbox = Listbox(fm1,selectmode=SINGLE)
for i in item:
	listbox.insert(END,i)
listbox.pack(side='left')

#---------------------使Listbox支持鼠标移动选中位置-------------------------------------------------------------------------
#selectmode：设置为BROWSE（默认）可以拖动鼠标，也可用上下键，
#但SINGEL就不支持此种操作
lb1 = Listbox(fm1,selectmode=SINGLE)
for i in item:
	lb1.insert(END,i)
lb1.pack(side='left')

#---------------------使Listbox支持Shift和Control-----------------------------------------------------------------------
#selectmode:EXTENDED
lb2 = Listbox(fm1,selectmode=EXTENDED)
for i in item:
	lb2.insert(END,i)
lb2.pack(side='left')

#---------------------向Listbox中添加一个item----------------------------------------------------------------------------
lb3 = Listbox(fm1)
for i in item:
	lb3.insert(END,i)
lb3.insert(0,['linux','win','unix'])
lb3.insert(0,'linux','win','unix')
lb3.pack(side='left')
def ins():
	lb3.insert(ACTIVE,'mac OS') #ACTIVE向当前选中项增加一条
Button(fm1,text='增加',command=ins).pack(side='left')

#---------------------删除Listbox中item------------------------------------------------------------------------------
lb4 = Listbox(fm2)
for i in range(10):
	lb4.insert(END,str(i))
lb4.delete(1,3)
lb4.pack(side='left')

#---------------------选中或取消Listbox中item---------------------------------------------------------------------------
lb5 = Listbox(fm2)
for i in range(10):
	lb5.insert(END,str(i))
lb5.selection_set(0,9)		#选中0——9
lb5.pack(side='left')
lb5.selection_clear(1,3)	#取消0——2

#---------------------得到当前Listbox中item个数--------------------------------------------------------------------------
lb6 = Listbox(fm2)
for i in range(10):
	lb6.insert(END,str(i))
lb6.delete(3)
lb6.delete(3)
print(lb6.size())
lb6.pack(side='left')

#---------------------返回指定索引的item(一个或多个)-----------------------------------------------------------------------
lb7 = Listbox(fm2)
for i in range(10):
	lb7.insert(END,str(i*100))
lb7.pack(side='left')
print(lb7.get(3))
print(lb7.get(3,7))

#---------------------返回当前选中的item的索引(一个或多个)------------------------------------------------------------------
lb8 = Listbox(fm2)
for i in range(100):
	lb8.insert(END,str(i*100))
lb8.selection_set(3,8)
print(lb8.curselection())
lb8.pack(side='left')

#---------------------判断一个item是否被选中------------------------------------------------------------------------------
lb9 = Listbox(fm3)
for i in range(10):
	lb9.insert(END,str(i*100))
lb9.selection_set(3,8)
print(lb9.selection_includes(8))
print(lb9.selection_includes(0))
lb9.pack(side='left')

#---------------------Listbox与变量的绑定------------------------------------------------------------------------------
lbvar = StringVar()
lb10 = Listbox(fm3,listvariable=lbvar)
for i in range(10):
	lb10.insert(END,str(i*100))
#打印当前列表中的所有item值
print(lbvar.get())
lbvar.set(('1000','200'))
lb10.pack(side='left')

#---------------------Listbox与事件绑定------------------------------------------------------------------------------
def printList(event):
	print(lb11.get(lb11.curselection()))
lb11 = Listbox(fm3)
lb11.bind('<Double-Button-1>',printList) #双击
for i in range(10):
	lb11.insert(END,str(i*100))
lb11.pack()
# 它不支持command 属性来设置回调函数了，使用bind 来指定回调函数,打印当前选中的值


mainloop()