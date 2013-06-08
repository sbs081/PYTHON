#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
#root.geometry('800x600')
#----------------使用绝对坐标将组件放到指定的位置----------------------
#lb = Label(root,text='绝对 Place',relief='groove')
#lb.place(x=0,y=0,anchor=NW)

##----------------使用相对坐标将组件放到指定的位置----------------------

#lb1 = Label(root,text='相对 Place',relief='groove')
#lb1.place(relx=0.5,rely=0.5,anchor=CENTER)

#-----------------指定多个组件------------------------------------------
#v = IntVar()
#for i in range(5):
#	Radiobutton(
#	root,
#	text = 'Radio' + str(i),
#	variable = v,
#	value = i
#	).place(y = 25* i,anchor = NW)

##-----------------同时使用相对和绝对坐标------------------------------------------
#lb1 = Label(root,text='标签1',fg='green')
#lb2 = Label(root,text='标签2',fg='red')
#lb1.place(relx=0.5,rely=0.5,anchor=CENTER,x=-100,y=-100)
#lb2.place(relx=0.5,rely=0.5,anchor=CENTER,x=-200,y=-200)
## 同时使用相对和绝对坐标时，相对坐标优先操作，然后是在这个相对坐标的基础上进行偏移

##-----------------使用 in 来指定放置的容器------------------------------------------
#bt1 = Button(root,text='按钮1',fg='red')
#bt2 = Button(root,text='按钮2',fg='yellow')
#bt1.place(in_=lb1,anchor=W)
#bt2.place(anchor=W)

#-----------------深入使用 in 来指定放置的容器------------------------------------------

#fm1 = Frame(root,bg='red',width=200,height=200)
#fm2 = Frame(root,bg='blue',width=100,height=100)
#fm3 = Frame(fm1,bg='yellow',width=100,height=100)

#lb1 = Label(fm1,text='labe1',fg='green')
#lb1.place(in_=fm1,relx=0.5,rely=0.5,anchor=CENTER)

#bt1 = Button(fm2,text='button',fg='red')
#bt1.place(in_ = fm2,x=50,y=50,anchor = CENTER)
#fm1.pack(fill=BOTH)
#fm2.pack()
#fm3.pack()
# in 不是可以随意指定放置的组件的，如果使用in 这个参数这个组件必需满足：是其父容器
#或父容器的子组件

#-------------------事件与Place 结合使用--------------------------------------
#使用两个place 方法来动态改变两个Frame 的大小。
split = 0.5
fm1 = Frame(root,bg='red')
fm2 = Frame(root,bg='blue')
#单击fm1时增大它的占有区域0.1
def incFm1(event):
	global split
	if split<1:
		split+=0.01
	fm1.place(rely=0,relheight=split,relwidth=1)
	fm2.place(rely=split,relheight=1-split,relwidth=1)
#单击fm2时增大它的占有区域0.1
def incFm2(event):
	global split #该语句说明使用的全局变量（变量扩展）
	if split>0:
		split -= 0.01
	fm1.place(rely=0,relheight=split,relwidth=1)
	fm2.place(rely=split,relheight=1-split,relwidth=1)
# 这两语句要使用，不然开始看不到两个frame，也就没法点击它们了
fm1.place(rely = 0,relheight = split,relwidth = 1)
fm2.place(rely = split,relheight = 1 - split,relwidth = 1)
# 绑定单击事件
fm1.bind('<Button-1>',incFm1)
fm2.bind('<Button-1>',incFm2)
# 为SplitWindow 的原型了，再改动一下就可以实现一个SplitWindow 了。


root.mainloop()
