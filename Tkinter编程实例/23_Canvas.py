#!/usr/bin/python
#coding:gbk

from tkinter import *
root = Tk()
fm = Frame(root)
fm.pack()
cv = Canvas(root,bg='white')
#---------------------移动 item ---------------------------------------------
rt1 = cv.create_rectangle(150,40,250,140,tags=('r1','r2','r3'),width=10,outline='lightblue')
rt2 = cv.create_rectangle(10,10,110,140,tags=('s1','s2','s3'))
def move():
	cv.move(rt1,1,0) #注意是相对位移因此可以为负值
Button(fm,text='move',command=move).pack(side='left')

#---------------------删除 item ---------------------------------------------
def delete1():
	'''使用id删除rt1'''
	cv.delete(rt1)
def delete2():
	'''使用 tag 删除 rt2'''
	cv.delete('s1')
Button(fm,text='del ID',command=delete1).pack(side='left')
Button(fm,text='del tag',command=delete2).pack(side='left')

#---------------------缩放 item ---------------------------------------------
# scale: 计算公式 (coords-offset)*scale+offset
#上面的公式如何使用（还没搞清原理）
def zoom_in(): #放大
	cv.scale(rt3,1,2,2,2)
def zoom_out(): #缩小
	cv.scale(rt3,0,0,0.5,0.5)
rt3 = cv.create_rectangle(2,2,3,3,fill='blue')
cv.lower(rt3)
Button(fm,text='放大',command=zoom_in).pack(side='left')
Button(fm,text='缩小',command=zoom_out).pack(side='left')

#---------------------绑定 item 与 event ---------------------------------------------
def change_color(event):
	cv.itemconfig('r1',fill='red')
def change_color1(event):
	cv.itemconfig('r1',fill='springgreen')
cv.tag_bind('r1','<Button-1>',change_color)
cv.tag_bind('r1','<Button-3>',change_color1)
# 只有点击到矩形的边框时才会触发事件
cv.create_line(10,200,100,200,width = 15,tags = 'r1')

cv.pack()
mainloop()