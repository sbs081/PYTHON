#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: selfimpr
@blog: http://blog.csdn.net/lgg201
@mail: lgg860911@yahoo.com.cn
@date: 2010-3-7
'''

def f1():
    try:
        print ''
        f2()
        print ''
    except:
        pass
    print 'aaa'
def f2():
    print ''
    raise Exception
    f3()
    print ''
def f3():
    print ''
    f4()
    print ''
def f4():
    pass