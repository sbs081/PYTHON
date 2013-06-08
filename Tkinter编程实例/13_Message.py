#!/usr/bin/python
#encoding:UTF-8
from tkinter import *
root = Tk()

#~~~~~~~~~~~~~~~~~~~~~~~~~~第一个Message的例子~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Message(root,text='Hello Message 你好，世界！',relief='solid').pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~改变Text的宽度~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#不能设置高度
Message(root,text='Hello Message 你好，世界！',width=200,relief='solid').pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~改变Text的高宽比例~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#aspect：指高宽比例
for i in range(10):
    Message(root,text='A'*i,aspect=500,relief='solid').pack()

#默认情况向width/height = 1.5，可以使用aspect 属性，
#设置为4，即宽为高的4 倍，可以显示10 个'A'

#~~~~~~~~~~~~~~~~~~~~~~~~~~Message 绑定变量~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# textvariable：指定与Message 绑定的变量
v = StringVar()
v.set('000')
for i in range(10):
    Message(root,text = 'A',textvariable = v).pack()
#打印当前的v 值，只要是其中的一个Message 的值发生变化，则此v 值就会改变。
print (v.get())
#绑定变量v，虽然创建Message 时使用了text 来指定Message 的值，绑定的变量优先级高，可以改变text
#指定的值。            
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~Message 绑定变量~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i in [LEFT,RIGHT,CENTER]:
    Message(root,text='ABC DEF HIJ',justify=i).pack()
    



mainloop()