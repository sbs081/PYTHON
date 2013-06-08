#!/usr/bin/python
#coding:gbk

#PaneWindow(面板)是一gm，用来管理子Widget
from tkinter import *
root = Tk()
#----------------------向PaneWindow中添加Pane---------------------------------------------
#panes = PanedWindow(orient=VERTICAL)
#panes.pack(fill='both',expand=1)
#for w in [Label,Button,Checkbutton,Radiobutton]:
#	panes.add(w(panes,text=str(w)[16:-2],relief='groove'))

#----------------------删除PaneWindow指定的pane---------------------------------------------
#删除:使用forget或remove
ws = []
panes1 = PanedWindow(orient = VERTICAL)
panes1.pack(fill='both',expand=1)
#创建4个pane
for w in [Label,Button,Checkbutton,Radiobutton]:
	ws.append(w(panes1,text=str(w)[16:-2],relief='groove'))
for w in ws:
	panes1.add(w)

panes1.forget(ws[0])
panes1.remove(ws[3])
#----------------------添加PaneWindow中指定的pane---------------------------------------------
panes1.paneconfig(Label(panes1,text='world'),after=ws[1])

#这一widget主要使用来做容器的，使用了大量的gm方法


root.mainloop()

