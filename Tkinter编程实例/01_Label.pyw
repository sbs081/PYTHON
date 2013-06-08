#!/usr/bin/python
#encoding:gbk

from tkinter import *

root = Tk()
root.minsize(300,200)
root.title('Hello World')

#---------------标签-----------------------------------------------------------------------------------------------------------------
Label(root,text='Hello World',relief=GROOVE).pack()

#---------------标签：使用位图---------------------------------------------------------------------------------------------------------
#x = ["error","gray12","gray25","gray50","gray75",
#     "hourglass","info","question","warning"]
#bm = BitmapImage(file=r'c:\temp\bitmap.bmp')   #如何使用外部位图，这里有错误
Label(root,bitmap='gray50',relief=GROOVE).pack()

#---------------标签：使用图片---------------------------------------------------------------------------------------------------------
pic = PhotoImage(file=r'c:\temp\python.gif')
Label(root,image=pic,relief=GROOVE).pack()

#---------------标签：前景色，背景色----------------------------------------------------------------------------------------------------
Label(root,text='世界你好',fg='lightskyblue',bg='white').pack()
Label(root,text='世界你好',fg='#000000',bg='#A0FC96').pack()

#---------------标签：宽度，高度--------------------------------------------------------------------------------------------------------
Label(root,text='世界你好',height=2,width=20,fg='#000000',bg='#FFFC96').pack()

#---------------标签：图片，文本的混合---------------------------------------------------------------------------------------------------
#compoound属性的使用，不设置该属性时如果既有文本又有图片则只显示图片
#属性值：left,right,top,bottom,center,
pic1 = PhotoImage(file=r'C:\temp\re.gif')
Label(root,text='文本与图片的混合',image=pic1,compound='right',relief=GROOVE).pack()
Label(root,text='文本与图片的混合',image=pic1,compound='center',relief=GROOVE).pack()
Label(root,text='文本与图片的混合',image=pic1,compound='top',relief=GROOVE).pack()
Label(root,text='文本与图片的混合',image=pic1,compound='left',relief=GROOVE).pack()
Label(root,text='文本与图片的混合',image=pic1,compound='bottom',relief=GROOVE).pack()

#---------------标签：自动换行----------------------------------------------------------------------------------------------------------
#wraplength：指定多少个单位后开始换行
#justify：指定多行的对齐方式
#手动换行 \n
Label(root,text='世人都晓神仙好，惟有功名忘不了！',height=3,width=30,wraplength=120,justify='left',fg='#000000',bg='#FFFCFF').pack()

#---------------标签：指定文本或图像在Label中的显示位置-------------------------------------------------------------------------------------
#anchor
#nw		n		ne
#w	  center    e
#sw		s		se
Label(root,text='世人都晓神仙好',width=40,height=3,anchor='ne',relief=GROOVE).pack()


mainloop()
