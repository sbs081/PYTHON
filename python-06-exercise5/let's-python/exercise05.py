#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: selfimpr
@blog: http://blog.csdn.net/lgg201
@mail: lgg860911@yahoo.com.cn
@date: 2009-11-19
'''

total = 89

use_able = {5: 0, 1: 0, 25: 0, 10: 0}
keys = use_able.keys()
keys.sort(reverse = True)

tmp = total
for key in keys:
    while tmp >= key:
        tmp -= key
        use_able[key] += 1
    if tmp < 1:
        break

if __name__ == '__main__':
    print use_able