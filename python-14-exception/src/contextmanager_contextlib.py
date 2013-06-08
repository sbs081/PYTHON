#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: selfimpr
@blog: http://blog.csdn.net/lgg201
@mail: lgg860911@yahoo.com.cn
@date: 2010-3-7
'''

from contextlib import contextmanager

@contextmanager
def fun():
    print 'enter'
    try:
        yield
    except Exception as a:
        print type(a)
    finally:
        print 'finally'

with fun():
    print t
    print 'content'