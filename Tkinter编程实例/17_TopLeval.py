#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
## TopLevel 与 Frame 类似，但它包含窗体属性（eg.title）
##-----------------------创建简单的 TopLevel --------------------------------
#tl = Toplevel(root)
#Label(tl,text='hello label').pack()

##-----------------------设置 TopLevel 的属性 --------------------------------
#tl.title('TopLevel')
#tl.geometry('400x300')

#-----------------------使用 TopLevel 自己制作提示框 --------------------------------
mbYes ,mbYesNo, mbYesNoCancel, mbYesNoAbort=0,1,2,3
def MessageBox(mbType):
	textShow='YesNo'
	print(mbType)
	if mbType == mbYes:
		textShow = 'Yes'
	if mbType == mbYesNo:
		textshow = 'YesNo'
	if mbType == mbYesNoCancel:
		textShow = 'YesNoCancel'
	if mbType == mbYesNoAbort:
		textShow = 'YesNoAbort'
	tl = Toplevel(root,height=200,width=400)
	Label(tl,text=textShow).pack()
cmd = mbYesNoAbort
Button(root,text='click me',command =lambda:MessageBox(cmd)).pack()



root.mainloop()