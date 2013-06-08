#!/usr/bin/python
#coding:gbk

# Tkinter 参考中最推荐使用的一个布局器。实现机制是将Widget 逻辑上分割成表格，在指
#定的位置放置想要的Widget 就可以了。

from tkinter import *
root = Tk()
root.geometry('600x400')
#--------------------------使用 grid----------------------------------------
#lb1 = Label(root,text='hello',bg='gold')
#lb2 = Label(root,text='grid',bg='yellow')
#lb1.grid()
#lb2.grid()
#grid 有两个最为重要的参数，用来指定将组件放置到什么位置，一个是row,另一个是
#column。如果不指定row,会将组件放置到第一个可用的行上，如果不指定column，则使用
#第一列。


#lb2.grid(row=0,column=1)

#Label(root,text = 'Hello').grid()
## 在第一行，第10 列放置lb2
#Label(root,text = 'Grid').grid(row = 0,column = 2)
## Lable(root,text = '3').grid(row = 0,column = 3)

# grid：布局组件
#Label(root,text = '1').grid()
# 在第1 行，第11 列放置lb2
#Label(root,text = '2',relief='groove').grid(row = 0,column = 2)
#Label(root,text = '3',relief='groove').grid(row = 0,column = 3)

#lb3 = Label(root,text='标签3')
#lb4 = Label(root,text='标签4')
#lb3.grid(row=1,column=0)
#lb4.grid(row=1,column=0)
#def forgetLabel():
#	# grid_slaves 返回grid 中(0,0)位置的所有组件
#	# grid_forget 将这个组件从grid 中移除（并未删除，可以使用grid 再将它显示出来)
#	root.grid_slaves(1,0)[0].grid_forget()

#Button(root,text='forget last',command=forgetLabel).grid(row=2,column=1)

#root.columnconfigure(2,minsize=100) #索引为2（第三列）的列的最小宽度
#root.rowconfigure(2,minsize=100) #
# 设置列或行(rowconfigure)的属性时使用父容器的方法,不是自己调用。


#-------------------组件使用多列（多行）-------------------------------
# columnspan：指定使用几列
# rowspan：指定使用几行
lbA = Label(root,text = 'A',bg = 'red')
lbB = Label(root,text = 'B',bg = 'blue')
lbC = Label(root,text = 'C',bg = 'red')
lbD = Label(root,text = 'D',bg = 'yellow')
lbE = Label(root,text = 'E',bg = 'pink')

lbA.grid(row = 0,column = 0,columnspan = 2,sticky=W)
lbB.grid(row = 1,column = 0)
lbC.grid(row = 1,column = 1)
lbD.grid(row = 2)
lbE.grid(row = 0,column = 2)

#-------------------设置对齐属性----------------------------------------------
# sticky：设置组件对齐方式
# 默认属性下，组件的对齐方式为居中，设置sticky 属性可以控制对齐方式，可用的值
#（N,S,E,W）及其组合值
root.mainloop()