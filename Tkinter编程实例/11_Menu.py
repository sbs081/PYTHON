#!/usr/bin/python
#encoding:UTF-8
from tkinter import *
root = Tk()
##----------------menu创建----------------------------------------------------------
##add-command:为菜单添加项（这里不是下拉菜单）
#def hello():
#    print('hello menu')
#
#menubar = Menu(root)
#for item in ['python','php','ruby','cpp']:
#    menubar.add_command(label=item,command=hello)


##----------------添加下拉菜单----------------------------------------------------------
##add_command:添加菜单项
##add_cascade（翻译：小瀑布）：添加下拉菜单
#filemenu = Menu(menubar,tearoff=0)
#for item in ['python','php','ruby','cpp']:
#    filemenu.add_command(label=item,command=hello)
#menubar.add_cascade(label='Python',menu=filemenu)
###其实就是向菜单中再添加菜单
#
#root['menu'] = menubar
##------------------向菜单中添加Checkbutton项---------------------------------------------
menubar =   Menu(root)

def printItem():
    print('Python= ',vPython.get())
    print('     C= ',vC.get())
    print('  Java= ',vJava.get())
    print('  Ruby= ',vRuby.get())
vPython =   StringVar()
vC      =   StringVar()
vJava   =   StringVar()
vRuby   =   StringVar()

filemenu = Menu(menubar,bg='lightblue',tearoff=0)
for k,v in {'Python':vPython,
            'C':vC,
            'Java':vJava,
            'Ruby':vRuby}.items():
    #绑定变量与回调函数
    filemenu.add_checkbutton(label=k,command=printItem,variable=v)

#-------------------分割符-----------------------------------------------------
filemenu.add_separator()

##------------------向菜单中添加Radiobutton项---------------------------------------------
#menubar = Menu(root)
vLang = StringVar()

def printItem1():
    print('vLang = ',vLang.get())
    
for k in ['python','php','java','ruby']:
    #指定的变量vLang将这几项划为一组
    filemenu.add_radiobutton(label=k,command=printItem1,variable=vLang)

menubar.add_cascade(label='Language',menu=filemenu)

#root['menu'] = menubar

##------------------（右击时弹出的）快捷菜单---------------------------------------------
##需要取消与root 菜单的关联
def printItem2():
    print('popup menu')
def popup(event):
    menubar.post(event.x_root,event.y_root)
root.bind('<Button-3>',popup)

##------------------菜单项的操作方法---------------------------------------------
#insert_command:
#insert_checkbutton:
#insett_radiobutton:
#delete:
def add_sep():
    print('add_seprarator')
filemenu1 = Menu(menubar,tearoff=0)
for k in range(5):
    filemenu1.add_command(label=str(k),command=add_sep)
menubar.add_cascade(label='数字',menu=filemenu1)

filemenu1.insert_command(1,label='1000',command=printItem2)
filemenu1.insert_checkbutton(2,label='2000',command=printItem2)
filemenu1.insert_radiobutton(3,label='3000',command=printItem2)
filemenu1.insert_separator(1)
filemenu1.insert_separator(5)

filemenu1.delete(0)
root['menu']=menubar

mainloop()