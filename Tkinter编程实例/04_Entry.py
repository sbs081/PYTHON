#!/usr/bin/python
#coding:gbk
from tkinter import *

root = Tk()
root.geometry('200x200')
#---------------用Entry来输入单行文本-------------------------------------------------------------------------------------
Entry(root,text='input your text here',bg='peach puff').pack()
#说明：Entry的text与Button和Label的text不同
#     并不能显示文本

#---------------Entry中设定初始值：使用textvariable将变量与Entry绑定-------------------------------------------------------------------------------------
e = StringVar()
entry = Entry(root,textvariable = e)
e.set('init value')
entry.pack()

#---------------Entry中设定只读-------------------------------------------------------------------------------------
e1 = StringVar()
st = ['normal','disabled','readonly']
for s in st:
	entry1 = Entry(root,textvariable=e1,state=s)
	e1.set('input your text here')
	entry1.pack()

#---------------设置为密码输入框-------------------------------------------------------------------------------------
e2 = StringVar()
entry2 = Entry(root,textvariable = e2)
e2.set('password')
entry2.pack()
entry2.configure(show='*')

#---------------验证输入的内容是否符合要求-------------------------------------------------------------------------------------
#e3 = StringVar()
#def validateText(contents):
#	print(contents)
#	return contents.isanum()

#entry3 = Entry(root, validate = 'key', textvariable = e3, validatecommand = validateText)
#entry3.pack()

#---------------获得输入框内容-------------------------------------------------------------------------------------
def gtc(even=None):
	key = ent.get()
	sv.set('['+key+']')
	print(key)
sv = StringVar()
ent = Entry(root,textvariable=sv)
ent.bind('<Return>',gtc)
ent.pack()

but = Button(root,text='加括号',command=gtc)
but.pack()



mainloop()
