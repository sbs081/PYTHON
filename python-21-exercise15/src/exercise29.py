#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2009-10-23

@author: selfimpr
@blog: http://blog.csdn.net/lgg201
@mail: lgg860911@yahoo.com.cn
@copyright: keep all copyright
'''

##########################
# 转载请声明出处.
# http://blog.csdn.net/lgg201
##########################

import re, time

datas = ['800-555-1212', 
         '555-1212', 
         '(800)555-1212']

pattern = re.compile(r'^((?P<bracket>\()?(?P<area_no>\d{3})(?(bracket)\)|-))?(?P<no>\d{3}-\d{4})$')

if __name__ == '__main__':
    for data in datas:
        print pattern.search(data).group()