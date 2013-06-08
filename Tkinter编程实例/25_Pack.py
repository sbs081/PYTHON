#!/usr/bin/python
#coding:gbk
# Pack 为一布局管理器，可将它视为一个弹性的容器
from tkinter import *
root = Tk()

#---------------------第一个 pack --------------------------------------------
# 查看当前root 下的子组件,解释器没有报异常，说明Pack 已创建，并可以使用,此时的输出
#为空，即root 没有任何子组件。
#print( root.pack_slaves() )
#Label(root,text='pack',relief='groove').pack()
# 再次打印出root 的子组件，可以看到已经包含一个组件，即刚才创建的Label，说明Label
#调用pack()是将自己加入到了root 中。
print( root.pack_slaves() )
# pack_salves 打印当前组件拥有的子组件，通过这个函数可以查看各个组件是否有包含关系。

#--------------------- pack 与 root 的关系 --------------------------------------------
#root.geometry('80x80+400+300')  #设置大小和位置（长80，款80，初始坐标）
#可以看出Pack 的结果没有什么变化，它不对root 产生影响，也就是说Pack 可以“缩小”
#至只包含一个Label 组件，root 可以自己控件自己的大小。

#----------------------向Pack 中添加多个组件------------------------------------------

#print(root.pack_slaves())
#for i in range(5):
#	Label(root,text = 'pack' + str(i)).pack()
#print(root.pack_slaves())
#Label(root,
#	text = 'pack1',
#	bg = 'red').pack(fill = Y,expand=1,side=LEFT)
#Label(root,
#	text = 'pack2',
#	bg = 'blue').pack(fill = BOTH,expand=1,side=RIGHT)
#Label(root,
#	text = 'pack3',
#	bg = 'green').pack(fill = X,expand=0,side=LEFT)

#----------------------组件之间的间隙大小------------------------------------------
L1 = LabelFrame(root,text='pack1',bg='red')
L1.pack(side=LEFT,ipadx=20)
Label(L1,text='inside',bg='blue').pack(expand=1,side=LEFT)

Label(root,text='pack2',bg='blue').pack(fill=BOTH,expand=1,side=LEFT,padx=10)

Label(root,text='pack3',bg='green').pack(fill=X,expand=0,side=LEFT,padx=10)

root.mainloop()