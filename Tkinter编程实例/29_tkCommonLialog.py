#!/usr/bin/python
#coding:gbk
from tkinter import *
from tkinter.simpledialog import *
root = Tk()
#------------------------模态对话框SimpleDialg---------------------------
# SimpleDialog： 创建一个模态对话框
# buttons:       显示的按钮
# default:       默认选中的按钮
#dlg = SimpleDialog(root,text='hello SimpleDialog',
#				   buttons=['Yes','No','cancel'],
#				   default = 0)
#执行对话框
#print(dlg.go())  #打印点击按钮在 buttons 中的索引值

# askinteger： 输入一个整数值
# askfloat：   输入一个浮点数
# askstring：  输入一个字符串

# initialvalue 指定一个初始值
# prompt       提示信息
# title        提示框标题
#askinteger(title='prompt',prompt='input a integer:',
#		   initialvalue = 100,minvalue=0,maxvalue=101)
#askstring(title = 'string',initialvalue = 'a string',
#		  prompt = 'input a string')
# 返回值为各自输入的值。

#------------------------打开文件对话框---------------------------
#from tkinter.filedialog import *
#fd = LoadFileDialog(root)
# go 方法的返回值即为选中的文本路径，如果选择"取消"返回值则为None
#print(fd.go())

#------------------------保存文件对话框---------------------------
# SaveFileDialog：保存对话框
#fs = SaveFileDialog(root)
#print(fs.go())

#------------------------使用颜色对话框---------------------------
#from tkinter.colorchooser import *
#print(askcolor())
# 调用askcolor 返回选中颜色的(R,G,B)颜色值及#RRGGBB 表示

#------------------------使用消息对话框---------------------------
# showinfo：			信息对话框
# showwarning：		警告对话框
# showerror：		错误对话框
# showquestion：		询问对话框
# showokcancel：		显示确定/取消对话框
# showyesno：		是/否对话框
# showretrycancel：	重试/取消对话框
from tkinter.messagebox import *
stds=[
	showinfo, # 显示信息消息框
	showwarning, # 显示警告消息框
	showerror, # 显示错误消息框
	askquestion, # 显示询问消息框
	askokcancel, # 显示确认/取消消息框
	askyesno, # 显示是/否消息框
	askretrycancel # 显示重试/取消消息框	  
	]
#for std in stds:
#	print(str(std),std(title=str(std),message=str(std)))
# 如果要确认点击的是那一个按钮，则可以判断这个消息框的返回值，注意各个值有所不同
# 返回值有ok/yes/True
print(askokcancel(title='quit application？',
				  message='woul you like quit this application',
				  default = OK #指定默认焦点
				  )
	  )
# 使用default 来指定默认焦点位置，ABORT/RETRY/IGNORE/OK/CANCEL/YES/NO
# 如果指定的按钮不存在，在抛出异常

root.mainloop()