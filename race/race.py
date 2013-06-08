#! usr/bin/python
        # -*- coding:utf-8 -*-
        # hqwfq21@gmail.com
#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import wx
import modules.Frame1
class BoaApp(wx.App):
    def OnInit(self):
        self.main = modules.Frame1.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
