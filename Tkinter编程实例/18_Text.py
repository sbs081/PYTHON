#!/usr/bin/python
#coding:gbk
from tkinter import *
root = Tk()
#--------------------Text 例子--------------------------------------------
t = Text(root,height=10,font='微软雅黑 12')
t.pack()
#--------------------Text 例子(使用 line.col 索引)-----------------------------------------
#向第一行，第一列添加文本 0123456789
#t.insert(0.0,'0123456789')
#t.insert('2.end','\n\n')
#t.insert(1.0,'ABCDEFGHIJ')
#可以看到，使用indexes时，如果其值超过了Text 的buffer，程序不会
#抛出异常，会向给定值靠近

#-------------------- 使用内置的 mark 控制位置-----------------------------------------
#演示使用内置的mark：
#INSERT	  ：  光标的位置
#CURRENT  ：  当前鼠标所在位置
#END	  ：  整个buffer的最后
#SEL_FIRST：  选中文本的开始
#SEL_LAST ：  选中文本的最后
#mark = [INSERT,CURRENT,END,SEL_FIRST,SEL_LAST]
#for i in range(10):
#	t.insert(1.0,'*'*i+'\n')

#def text_fun():
#	def fun(flag):	#使用"闭合"技术
#		t.insert(flag,flag)
#	return fun
#def fun1():
#	t.insert(CURRENT,'  current  ')
#for i in range(len(mark)):
#	Button(root,text='insert jcodeer at '+mark[i],
#		width=20,command=lambda x=mark[i]:text_fun()(x)).pack()
	
#不能用 Button(root,text='insert jcodeer at '+mark[i],command=lambda :text_fun()(mark[i])).pack()
#这样传递参数是有问题的。（lambda 函数参数使用时应该小心）
#如果没有选定字符，则 sel.first 和 sel.end 位置会出现异常。

#-------------------- 使用使用表达式来增强 mark -----------------------------------------
for i in range(1,10):
	t.insert(1.0,'0123456789\n')
a = 'test_mark'
def forwardChars():
	t.mark_set(a,CURRENT+'+5c')
def backwardChars():
	t.mark_set(a,CURRENT+'-5c')
def forwardLines():
	t.mark_set(a,CURRENT+'-5l')
def backwardLines():
	t.mark_set(a,CURRENT+'-5l')
def lineStart():
	t.mark_set(a,CURRENT+' linestart')
def lineEnd():
	t.mark_set(a,CURRENT+' lineend')
def wordStart():
	t.mark_set(a,CURRENT+' wordstart')
def wordEnd():
	t.mark_set(a,CURRENT+' wordend')

t.mark_set(a,CURRENT)
Button(root,text='forward 5 chars ', command=forwardChars ).pack(fill=X)
Button(root,text='backward 5 chars ',command=backwardChars).pack(fill=X)
Button(root,text='forward 5 lines ', command=forwardLines ).pack(fill=X)
Button(root,text='backward 5 lines ',command=backwardLines).pack(fill=X)
Button(root,text='line start ',		 command=lineStart	  ).pack(fill=X)
Button(root,text='line end ',		 command=lineEnd	  ).pack(fill=X)
Button(root,text='word start ',		 command=wordStart	  ).pack(fill=X)
Button(root,text='word end ',		 command=wordEnd	  ).pack(fill=X)

def insertText():
	t.insert(INSERT,'insert')
def currentText():
	t.insert(CURRENT,'current')
def markText():
	t.insert(a,'mark')
Button(root,text = 'insert jcodeer',command=insertText).pack(fill=X)
Button(root,text = 'insert jcodeer',command=currentText).pack(fill=X)
Button(root,text = 'insert jcodeer',command=markText).pack(fill=X)


root.mainloop()

