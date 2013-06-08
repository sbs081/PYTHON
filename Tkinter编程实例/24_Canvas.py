#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
cv = Canvas(root,bg='#8c1557',height=600,width=800)

#----------------绘制弧形（弓形，扇形）-------------------------------------------------
#Create arc shaped region with coordinates x1,y1,x2,y2.
cv.create_arc((20,20,110,110)) #使用默认参数绘制90度得扇形
style={1:PIESLICE,2:CHORD,3:ARC}
#for i in style:
#	cv.create_arc((10,10+60*i,90,90+60*i),style=style[i]) #弓形
#cv.create_arc((80,80,210,210),style=PIESLICE)  #扇形
#cv.create_arc((90,90,210,210),style=ARC) #弧形

#----------------设置弧形（弓形，扇形）角度-------------------------------------------------
#for i in style:
#	cv.create_arc((30,30,60*i,60*i),style=style[i],start=30,extent=62) #弓形

xy = 20, 20, 180, 180 #其实形成了一个盒子，然后将下面的形状放进去
cv.create_arc(xy, start=0, extent=270, fill="red")
cv.create_arc(xy, start=270, extent=60, fill="blue")
cv.create_arc(xy, start=330, extent=30, fill="green")

#----------------绘制位图------------------------------------------------------------
bitmap = {1:'error',2:'info',3:'question',4:'hourglass'}
for i in bitmap:
	cv.create_bitmap((20*i,20*i),bitmap=bitmap[i])

#----------------绘制 gif 图象------------------------------------------------------------
pic = PhotoImage(file=r'c:\temp\format_org.gif')
cv.create_image((450,250),image=pic)

#----------------绘制直线------------------------------------------------------------
line_style=[(0,'none','bevel'),(1,'first','miter'),(2,'last','round'),(3,'both','round')]
for i in line_style:
	cv.create_line((200,30+i[0]*30,310,30+i[0]*30),width=1,
				arrow=i[1], #左箭头，右箭头，韩式两边都有箭头
				arrowshape='8 10 3', #设置箭头的形状(填充长度，箭头长度，箭头宽度)
				joinstyle = i[2], #设置
				)

#----------------绘制椭圆------------------------------------------------------------
cv.create_oval((350,20,550,120),fill='gold')

#----------------创建多边形------------------------------------------------------------
cv.create_polygon((200,200,200,300,250,300,400,400),
				  smooth = True,
				  splinesteps = 20,
				  fill='red')
# 当指定三个点的坐标时，三个点坐标必须满足三角形的定义。

#----------------绘制文本------------------------------------------------------------
# create_text：创建文本
# anchor：控制文本位置
# justify：控制文本对齐方式
txt = cv.create_text((500,500),text='绘制文本，绘制文本',font = '微软雅黑 18',anchor=W)
#-----------------选中文本------------------------------------------------------------
cv.select_from(txt,0)
cv.select_to(txt,3)

#-----------------创建组件------------------------------------------------------------
def click_me():
	from mycolor import get_color
	from random  import randint
	cv.itemconfig(txt,fill=get_color()[randint(1,400)])	
bt = Button(cv,text='ClickMe',command=click_me)
cv.create_window((540,540),window=bt,anchor=W)
cv.create_line((520,520,580,570))
cv.create_line((580,570,600,600))

cv.pack()
root.mainloop()
