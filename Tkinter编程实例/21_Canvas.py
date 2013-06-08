#!/usr/bin/python
#coding:gbk
# 画布
#提供可以用来进行绘图的Container，支持基本的几何元素，使用Canvas 进行绘图时，所
#有的操作都是通过Canvas，不是通过它的元素
#元素的表示可以使用handle 或tag
from tkinter import *
root = Tk()
#------------------创建画布------------------------------------------
cv = Canvas(root,bg = 'white')

#------------------创建一个项(矩形，填充色,边框)------------------------------------------
cv.create_rectangle(10,10,110,110,fill='skyblue',outline = 'red',width=5)

#------------------创建一个项(线条)------------------------------------------
#如何画一条 sin() 的曲线
#import math
#x = range(0,1000)
#y = [math.sin(x[i]) for i in x]
#y = [int(y[i]*1000)+1000 for i in x]
cv.create_line(10,10,110,120,150,180,smooth=1,width=2,fill='blue')

#-------------------画虚线------------------------------------------------------------
cv.create_rectangle(120,10,220,110,dash = 2,fill='green')

#-------------------使用画刷填充------------------------------------------------------------
rt = cv.create_rectangle(230,10,330,110,outline='red',stipple='gray12',fill='green')

#-------------------修改 item 的坐标------------------------------------------------------------
cv.coords(rt,(300,10,340,110))


cv.pack()
mainloop()


