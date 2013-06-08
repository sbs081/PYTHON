#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: selfimpr
@blog: http://blog.csdn.net/lgg201
@mail: lgg860911@yahoo.com.cn
@date: 2009-12-7
'''
from time import *
from thread import *

def function1():
    print 'function1 start at:', ctime()
    sleep(4)
    print 'function1 finished at:', ctime()

def function2():
    print 'function2 start at:', ctime()
    sleep(2)
    print 'function2 finished at:', ctime()

if __name__ == '__main__':
    print 'main thread start at:', ctime()
    start_new_thread(function1, ())
    start_new_thread(function2, ())
    sleep(6)
    print 'main thread finished at:', ctime()