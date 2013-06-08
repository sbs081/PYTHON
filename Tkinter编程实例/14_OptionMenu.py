#!/usr/bin/python
#encoding:UTF-8

from tkinter import *
root = Tk()
#---------------------创建OptionMenu----------------------------------------------------
v = StringVar(root)
v.set('Ruby')
OptionMenu(root,v,'Python','PHP','Java').pack()
##注意OptionMenu的创建需要两个必要的参数，与当前值绑定的变量，
##通常为StringVar变量，另一个是可选的内容列表。

#--------------------打印OptionMenu显示值-----------------------------------------------------
def printOption(event):
	print(v1.get())
v1 = StringVar(root)
v1.set('Ruby')
om1 = OptionMenu(root,v1,'Python','PHP','Java')
om1.bind('<Button-1>',printOption)
om1.pack()

##--------------------使用List作为OptionMenu的选项(这里有问题，apply函数没法使用)-----------------------------------------------------
#Lang = ['Python','PHP','Java','CPP']
#v2 = StringVar(root)
#v2.set('Tkinter')
#def printOption2(event):
#	print(v2.get())
#om2 = apply(OptionMenu(root,v)+tuple(Lang))
#om2.bind('<Button-2>',printOption2)
#om2.pack()



mainloop()
