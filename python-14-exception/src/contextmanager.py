#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: selfimpr
@blog: http://blog.csdn.net/lgg201
@mail: lgg860911@yahoo.com.cn
@date: 2010-3-7
'''
class my_obj(object):
    def __init__(self, x):
        self.x = x
    def __enter__(self):
        print 'enter'
        a = "helo"
        return a
    def __exit__(self, e_type, e_value, e_traceback):
        print 'exit'
        print e_type, e_value, e_traceback
        return False

with my_obj(5) as a:
    print 'content'
    print 'a.x: ', a