#!/usr/bin/python
#encoding:UTF-8

from tkinter import *
root = Tk()
#与Entry类似，但可以指定输入范围值

#------------------Spinbox创建--------------------------------------------------------------
Spinbox(root).pack()

#------------------Spinbox创建时指定参数--------------------------------------------------------------
Spinbox(root,from_=0,to=100,increment=5).pack()

#------------------设置Spinbox的值--------------------------------------------------------------
sb1 = Spinbox(root,values=(0,2,4,20,40,-1),increment=2)
sb1.pack()
print(sb1['values'])
##这儿使用的是索引，increment=2不用

#------------------绑定变量--------------------------------------------------------------
v2 = StringVar()
sb2 = Spinbox(root,values=(0,2,-1),increment=2,textvariable=v2)
v2.set(2)
print(v2.get())
sb2.pack()

#------------------设置事件处理函数--------------------------------------------------------------
def printSprin():
    print('Sprinbox',sb3.get())
sb3 = Spinbox(root,from_=0, to=10,command=printSprin)
sb3.pack()
    
#------------------删除SprinBox字符（注意是字符）--------------------------------------------------------------
def printSprin1():
    print(sb4.delete(0))
    print(sb4.get())
sb4 = Spinbox(root,from_=100,to=120,command=printSprin1)
sb4.pack()

#------------------在SprinBox指定位置插入字符（注意是字符）--------------------------------------------------------------
def printSprin2():
    sb5.insert(END,'0')
    print(sb5.get())
sb5 = Spinbox(root,from_=10,to=20,increment=10,command=printSprin2)
sb5.pack()

mainloop()

