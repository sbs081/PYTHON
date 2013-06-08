# -*- coding: UTF-8 -*-
'''
Created on 2009-11-9

@author: Administrator
'''
import re, stack

SUPPORT_SIGN = {'(': 99, '*': 3, '/': 3, '-': 1, '+': 1}
NUMBER_PATTERN = re.compile('\d')

sign_stack = None
number_stack = None

#===============================================================================
# init 初始化符号栈和数字站 在局部名称空间中, 要使用全局名称空间中定义的变量, 首先要使用关键字global声明一下.
#===============================================================================
def init():
    global sign_stack
    global number_stack
    sign_stack = stack.Stack()
    number_stack = stack.Stack()

#===============================================================================
# to_suffix 将中坠表达式转换成后缀表达式的形式
# @return: 方便操作, 返回列表.
#===============================================================================
def to_suffix(expression):
    global sign_stack
    #check type
    result = []
    pre_char = None
    if not isinstance(expression, str):
        raise TypeError, '表达式类型错误'
    for char in expression:
        if char in SUPPORT_SIGN:
            pre_sign = sign_stack.peek()
            while pre_sign and SUPPORT_SIGN[char] <= SUPPORT_SIGN[pre_sign]:
                if pre_sign == '(':
                    break
                result.append(sign_stack.pop())
                pre_sign = sign_stack.peek()
            sign_stack.push(char)
        elif char == ')':
            pre_sign = sign_stack.peek()
            while pre_sign != '(':
                pre_sign = sign_stack.pop()
                result.append(pre_sign)
                pre_sign = sign_stack.peek()
            sign_stack.pop()
        elif NUMBER_PATTERN.match(char):
            if pre_char and NUMBER_PATTERN.match(pre_char):
                result[len(result) - 1] += char
            else:
        	result.append(char)
        else:
            raise TypeError, '不支持的符号'
        pre_char = char
    while not sign_stack.empty():
        result.append(sign_stack.pop())
    return result

#===============================================================================
# count 接口独立
#===============================================================================
def count(suffix):
    global number_stack
    #check type
    if not isinstance(suffix, list):
        raise TypeError, '后缀表达式类型错误'
    for element in suffix:
        if element in SUPPORT_SIGN:
            number2 = number_stack.pop()
            number1 = number_stack.pop()
            eval_str = number1 + element + number2
            number_stack.push(str(eval(eval_str)))
        else:
            try:
                number_stack.push(element)
            except TypeError, e:
                print '后缀表达式中有不支持的字符'
                exit()
    return number_stack

def parse(expression):
    return count(to_suffix(expression))

if __name__ == '__main__':
    init()
    print to_suffix('31+22*55*(1+22*3-4/(5-6))')
    print count(to_suffix('31+22*55*(1+22*3-4/(5-6))'))
