#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: selfimpr
@blog: http://blog.csdn.net/lgg201
@mail: lgg860911@yahoo.com.cn
@date: 2009-11-19
'''

#===============================================================================
# switch 模拟switch语法
# @param value: 选择分支的值
# @param cases: 可变关键字参数, key: 分支的取向导向, value: 分支的操作, 使用字符串表达式传递
#===============================================================================
def switch(value, value_name, **cases):
    return eval(cases[value] % {value_name: value})

if __name__ == '__main__':
    cases = {'A': '"%(value)s: 90-100"', \
           'B': '"%(value)s: 60-90"', \
           'C': '"%(value)s: 0-60"'}
    print switch('B', 'value', **cases)