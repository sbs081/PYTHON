#! usr/bin/python
# -*- coding:utf-8 -*-
#Boa:Frame:Frame1

import wx
from wx.lib.anchors import LayoutAnchors
import wx.lib.scrolledpanel
import wx.lib.dialogs
from wx.lib.wordwrap import wordwrap
import timer

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1STATUSBAR1, wxID_FRAME1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(3)]

[wxID_FRAME1MENUHELPITEMS0, wxID_FRAME1MENUHELPITEMS1, 
] = [wx.NewId() for _init_coll_menuHelp_Items in range(2)]

[wxID_FRAME1MENUFILEITEMS2] = [wx.NewId() for _init_coll_menuFile_Items in range(1)]

[wxID_FRAME1TIMER1] = [wx.NewId() for _init_utils in range(1)]

class Frame1(wx.Frame):
    state=0
    TTime=10#设置总的录入时间为10分钟，可以更改为自己需要的时间
    UsedTime=0#记录使用的时间，每秒加1
    
    UseCheat=0#是否使用了Ctrl+V、Ctrl+Z、鼠标右键
        
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuFile, title=u'\u6587\u4ef6(&F)')
        parent.Append(menu=self.menuHelp, title=u'\u5e2e\u52a9(&H)')

    def _init_coll_menuHelp_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MENUHELPITEMS1,
              kind=wx.ITEM_NORMAL, text=u'\u8bf4\u660e')
        parent.Append(help='', id=wxID_FRAME1MENUHELPITEMS0,
              kind=wx.ITEM_NORMAL, text=u'\u5173\u4e8e...')
        self.Bind(wx.EVT_MENU, self.OnMenuHelpItems1Menu,
              id=wxID_FRAME1MENUHELPITEMS1)
        self.Bind(wx.EVT_MENU, self.OnMenuHelpItems0Menu,
              id=wxID_FRAME1MENUHELPITEMS0)

    def _init_coll_menuFile_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MENUFILEITEMS2,
              kind=wx.ITEM_NORMAL, text=u'\u9000\u51fa')
        self.Bind(wx.EVT_MENU, self.OnMenuFileItems2Menu,
              id=wxID_FRAME1MENUFILEITEMS2)

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(3)

        parent.SetStatusText(number=0, text=u'字数：')
        parent.SetStatusText(number=1, text=u'剩余时间：10:00')
        parent.SetStatusText(number=2,
              text=u'速度：')

        parent.SetStatusWidths([-1, -1, -1])

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar1 = wx.MenuBar()

        self.menuFile = wx.Menu(title='')

        self.menuHelp = wx.Menu(title='')
        
        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_menuFile_Items(self.menuFile)
        self._init_coll_menuHelp_Items(self.menuHelp)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(243, 201), size=wx.Size(723, 496),
              style=wx.DEFAULT_FRAME_STYLE, title=u'\u6253\u5b57\u6d4b\u901f')
        self.SetIcon(wx.Icon(u'boa.ico',wx.BITMAP_TYPE_ICO))
        self._init_utils()
        self.SetClientSize(wx.Size(715, 462))
        self.SetMenuBar(self.menuBar1)
        self.SetToolTipString(u'')
        self.Bind(wx.EVT_CHAR, self.OnFrame1Char)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self.statusBar1.SetFieldsCount(3)
        self.statusBar1.SetStatusText(u'')
        self.statusBar1.SetToolTipString(u'')
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(715, 420),
              style=wx.TE_MULTILINE,
              value=u'\u6309\u4efb\u610f\u952e\u5f00\u59cb\u8ba1\u65f6\u6d4b\u901f')
        self.textCtrl1.SetToolTipString(u'')
        self.textCtrl1.Bind(wx.EVT_KEY_DOWN, self.OnTextCtrl1KeyDown)
        self.textCtrl1.Bind(wx.EVT_RIGHT_DOWN, self.OnTextCtrl1RightDown)
    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnMenuFileItems2Menu(self, event):
        self.Close()
        event.Skip()

    def OnMenuHelpItems1Menu(self, event):
        '''读取并显示说明文档文件'''
        f = open(u"说明文档.txt", "r")
        msg = f.read().decode('utf-8')
        f.close()

        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, u"使用说明")
        dlg.ShowModal()
        event.Skip()

    def OnMenuHelpItems0Menu(self, event):
        '''提示软件基本信息'''
        info = wx.AboutDialogInfo()
        info.Name = u"打字测速"
        info.Version = u"0.1"
        info.Description = wordwrap(
            u"用于检验打字录入的速度，本软件可以用于学习 Python"
            u"\n\n祝您使用愉快:)",
            350, wx.ClientDC(self))
        info.WebSite = (u"http://code.google.com/p/Pythontools/",      
                        u"Python小工具")
        info.Developers = [ "910971030@qq.com" ]
        
        wx.AboutBox(info)
        event.Skip()

    def OnFrame1Char(self, event):
        keycode = event.GetKeyCode()
        if keycode==19:
            self.EasterEggs(event)
        event.Skip()

    def OnTimer1Timer(self, event):
        '''相应计时器，每秒进行一次'''
        if self.state==1:
            
            #如果输入使用了Ctrl+V、Ctrl+Z和鼠标右键，清空输入的内容
            if self.UseCheat==1:
                self.textCtrl1.SetValue("")
                self.UseCheat=0
            
            self.UsedTime=self.UsedTime+1               
            s=self.textCtrl1.GetValue()
            WordNum=len(s)
            LeftTime=60*self.TTime-self.UsedTime            
            
            s21='0'+str(LeftTime/60)
            
            if LeftTime%60>10: 
                s22=str(LeftTime%60) 
            else:
                s22='0'+str(LeftTime%60)
            
            s1="字数："+str(WordNum)+"字"
            s2="剩余时间："+s21+":"+s22
            s3="速度："+str(int(WordNum/(self.UsedTime/float(60))))+"字/分钟"
            
            self.SetStatusText(s1.decode("utf-8"),0)
            self.SetStatusText(s2.decode("utf-8"),1)
            self.SetStatusText(s3.decode("utf-8"),2)  
            
            #清除变量占用的内存
            s=""
            
            #录入时间到了后，提示录入速度,并且准备开始新一轮测速
            if LeftTime==0:
                self.timer1.Stop()
                dlg = wx.MessageDialog(self, '时间到!你的录入%s'%s3,
                               '提示',
                               wx.OK | wx.ICON_INFORMATION
                               )
                dlg.ShowModal()
                dlg.Destroy()
                #重置状态栏，提示信息，等待重新开始
                self.textCtrl1.SetValue("按任意键开始测速")
                self.SetStatusText("字数：",0)
                self.SetStatusText("剩余时间：",1)
                self.SetStatusText("速度：",2) 
                self.state=0
                self.UsedTime=0 
                event.Skip()                            
        event.Skip() 

    def OnTextCtrl1KeyDown(self, event):
        keycode = event.GetKeyCode()
        #在测速系统里，应该禁用Ctrl+V和粘贴功能，发现则关闭软件
        if keycode==86:#如果是Ctrl+V，关闭测速系统，现在没有更好的方法
            self.UseCheat=1
            event.Skip()
        if keycode==26:
            self.UseCheat=1
            event.Skip()
        if self.state==0:
            wx.TheClipboard.Close()
            self.timer1 = wx.Timer(id=wxID_FRAME1TIMER1, owner=self)
            self.Bind(wx.EVT_TIMER, self.OnTimer1Timer, id=wxID_FRAME1TIMER1)
            self.timer1.Start(1000)#每一秒响应一次
            self.textCtrl1.SetValue("")
            self.state=1                      
        event.Skip()
    #定义鼠标右键的处理动作，关闭测速系统，现在没有更好的方法    
    def OnTextCtrl1RightDown(self, event):
        self.UseCheat=1
        event.Skip()

