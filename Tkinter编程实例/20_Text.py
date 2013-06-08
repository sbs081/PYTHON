#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
t = Text(root,height=50)
#-------------------------自定义 tag 的两个内置属性--------------------------
t.tag_config('b',foreground='skyblue')
for i in range(10):
	t.insert(1.0,'0123456789\n')
t.mark_set('ab','3.1')
t.mark_set('cd',END)
t.tag_add('b','ab','cd')
# 在tag('b')之前插入'first'
t.insert('b.first','first\n')
# 在tag('b')之后插入'last'
t.insert('b.last','last\n')
# 注意：first 没有使用tag('b')属性，last 使用了tag('b')属性
	##如果 mark: 'cd' 不是 END，则在last后也不会使用 tag('b')的属性。

#-------------------------在 Text 中创建按钮（绑定一个滚动条）---------------------------------
def printbt():
	t.insert('2.0','button in text')
bt = Button(t,text='button',command=printbt,cursor='hand2')
t.window_create('1.0',window=bt)

sb3 = Scrollbar(root)
sb3.pack(fill=Y,side='right')
t['yscrollcommand'] = sb3.set 
sb3['command'] = t.yview #指定Scrollbar的command事件处理函数为yview

#-------------------------在 Text 中创建一个图像---------------------------------
pic = PhotoImage(file = r'c:\temp\bee.gif')
t.image_create('20.0',image=pic)
print(t.image_names())

#-------------------------绑定 tag 与事件----------------------------------------
t.tag_config('a',foreground='lightskyblue',underline=1)
def enterTag(event):
	print('Enter Event')
t.tag_bind('a','<Enter>',enterTag)
t.insert(2.0,'Enter event\n\n','a')

#-------------------------使用 edit_xxx 实现常用的编辑功能----------------------------------------
def undoText():
	t.edit_undo()
def insertText():
	t.insert(1.0,'insert text')

Button(root,text='undo',command=undoText).pack(fill=X)
Button(root,text='insert text',command=insertText).pack(fill=X)
#t.edit_undo()函数有点问题，不能实现。

t.pack(fill='both')
mainloop()