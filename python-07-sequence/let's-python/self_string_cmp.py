#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: selfimpr
@blog: http://blog.csdn.net/lgg201
@mail: lgg860911@yahoo.com.cn
@date: 2009-11-20
'''

def self_cmp(a, b):
    for index, char in enumerate(a):
        try:
            if ord(char) > ord(b[index]):
                return 1
            elif ord(char) < ord(b[index]):
                return -1
        except IndexError, e:
            return 1
    else:
        return 0

if __name__ == '__main__':
    print self_cmp('abcdeff', 'bbcdef')
    print self_cmp('bbcdef', 'abcdef')
    print self_cmp('abcdef', 'abcdef')
    print self_cmp('abcdefghk', 'abcdef')