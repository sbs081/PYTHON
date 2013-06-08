#!/usr/bin/python
#coding:gbk

from tkinter import *
root = Tk()
t = Text(root,font='微软雅黑 12')

#-------------------使用 tag 来指定文本的属性--------------------------------------

t.tag_config('b',foreground='red')
t.tag_config('a',foreground='blue')
t.insert(1.0,'0123456xxx',('b','a')) #不是按照('b','a')的顺序来设定的，而是按照'b','a'的创建顺序来设定的
t.insert(1.0,'0123456','b')
t.pack()

#-------------------控制 tag 的级别--------------------------------------
#tag_lower
#tag_raise
t.tag_lower('b')
t.insert(1.0,'abcde',('b','a'))

#-------------------对文本块添加一个tag--------------------------------------
t.tag_config('c',foreground='lightblue')
t.tag_lower('c')
for i in range(4):
	t.insert(1.0,'!@$%^&*()_+\n')
t.tag_add('c','2.5','4.end')

#-------------------使用自定义 mark 对文本块添加 tag--------------------------------------
t.tag_config('d',foreground='gray')
t.tag_lower('d')
for i in range(4):
	t.insert(1.0,'*******\n')
t.mark_set('ab','3.1')
t.mark_set('cd','4.2')
t.tag_add('d','ab','cd')

#-------------------使用 indexes 获得 Text 中的内容--------------------------------------
t.tag_config('e',foreground='cyan')
t.mark_set('ea','1.0')
t.mark_set('eb','4.0')
t.tag_add('e','ea','eb')
ea = '3.3'
t.delete('1.0','3.0') #仅仅删除文本，不会删除与之相关的属性
print(t.get(ea,'eb'))
t.tag_delete('e') #删除tag，所有与之相关的属性均不存在






root.mainloop()