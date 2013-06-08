#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
cv = Canvas(root,bg='white')
#---------------------创建 item 的 tags------------------------------------
#rt = cv.create_rectangle(10,10,110,110,tags='r1') #使用 tags 指定一个tag('r1')
#print(cv.gettags(rt))
#cv.itemconfig(rt,tags=('r1','r2','r3','r4')) #使用tags 属性指定多个tags,即重新设置tags 的属性
#print(cv.gettags(rt))

##---------------------多个 item 使用同一个 tag------------------------------------
#rt1 = cv.create_rectangle(120,10,220,110,tags='r1')
#print(cv.find_withtag('r1'))

##---------------------通过 tag 来访问 item------------------------------------
## 得到了tag 值也就得到了这个item，可以对这个item 进行相关的设置
#for item in cv.find_withtag('r1'):
#	cv.itemconfig(item,outline='cyan')

#---------------------向其它 item 添加 tag------------------------------------
#addtag_above：向上一个item添加tag
#addtag_below：向下一个item添加tag
rt2 = cv.create_rectangle(120,120,180,70,tags=('r1','r2','r3'))
rt3 = cv.create_rectangle(190,120,250,70,tags=('s1','s2','s3'))
rt4 = cv.create_rectangle(260,120,310,70,tags=('t1','t2','t3'))
cv.addtag_above('r4',rt3)
cv.addtag_below('r5',rt3)
for item in [rt2,rt3,rt4]:
	print(cv.gettags(item))
#Canvas 使用了stack 的技术，新创建的item 总是位于前一个创建的item 之上，故调用above
#时，它会查找rt3 上面的item 为rt4,故rt4 中添加了tag('r4')，同样add_below 会查找下面的
#item。

#---------------------返回其它item--------------------------------------------
cv.itemconfig(cv.find_above(rt3),outline='red')
cv.itemconfig(cv.find_below(rt3),outline='green')

#---------------------改变item在stack中的顺序--------------------------------------------
cv.tag_lower(rt4)	#将rt4放在 stack 的底部
cv.tag_raise(rt2)	#将rt1放在 stack 的顶部
cv.itemconfig(cv.find_above(rt3),outline='red')
cv.itemconfig(cv.find_below(rt3),outline='green')


cv.pack()
mainloop()