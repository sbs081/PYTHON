#!/usr/bin/python
#encoding:UTF-8

from tkinter import *
root = Tk()
#————————————————Scrollbar创建——————————————————————————————
##滚动条可以单独使用，但更多的是与其他空间（listbox，text，Canvas等）结合使用
Scrollbar(root,orient=HORIZONTAL).pack(fill='x')
sb = Scrollbar(root,orient=HORIZONTAL)
sb.set(0.5,0)#初始化时放置在1/2的位置
sb.pack(fill='x')
#————————————————设置slider的位置——————————————————————————————
sb1 = Scrollbar(root,orient=HORIZONTAL)
sb1.set(0.5,1)#占据一半的位置
sb1.pack(fill='x')

#————————————————事件处理函数（不建议使用，有问题）——————————————————————————————
def scrollCall(moveto,pos):
    sb2.set(pos,0)
    print(sb2.get())
sb2 = Scrollbar(root,orient=HORIZONTAL,command=scrollCall)
sb2.pack(fill='x')

#————————————————Scrollbar与Listbox的绑定——————————————————————————————
lb = Listbox(root)
sb3 = Scrollbar(root)
sb3.pack(fill=Y,side='right')

lb['yscrollcommand'] = sb3.set #Listbox的yscrollbar处理函数
for i in range(100):
    lb.insert(END,str(i))
lb.pack(side=LEFT)
sb3['command'] = lb.yview #指定Scrollbar的command事件处理函数为yview
#当Listbox改变时，Scrollbar调用set以改变slider的位置
#当Scrollbar改变了slider的位置的时候，Listbox调用yview显示新的list项


mainloop()