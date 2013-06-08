#!/usr/bin/python
#encoding:UTF-8

#这是一个过时的控件，从TK8.0开始将不再使用，而是用Menu来代替
from tkinter import *
root = Tk()

mbLang = Menubutton(root,text='Larguage')
mbLang.add_command(label='Ruby')
mbLang.pack()
#mbLang.menu = Menu(mbLang)
#
#for item in ['python','php','cpp','c','java']:
#    mbLang.menu.add_command(label=item)
#mbLang['menu'] = mbLang.menu
#mbLang.pack(side='left')
#
#mbOS = Menubutton(root,text='OS')
#mbOS.menu = Menu(mbOS)
#for item in ['unix','linux','soloris','windows']:
#    mbOS.menu.add_checkbutton(lable=item)
#mbOS['menu'] = mbOS.menu
#mbOS.pack(side = 'left')
#
#mbLinux = Menubutton(root,text='linux')
#mbLinux.menu = Menu(mbLinux)
#for item in ['redhat','fedra','suse','ubuntu','debian']:
#    mbLinux.menu.add_radiobutton(label=item)
#mbLinux['menu'] = mbLang.menu
#mbLinux.pack(side='left')
#
#mbLang.menu.add_separator()
#mbLang.menu.add_command(label = 'Ruby')
#mbOS.menu.insert_separator(2)
#mbOS.menu.insert_checkbutton(3,label='FreeBSD')
#mbLinux.menu.delete(5)


root.mainloop()


