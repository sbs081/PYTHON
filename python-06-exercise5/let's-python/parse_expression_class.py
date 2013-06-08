# -*- coding: UTF-8 -*-
'''
Created on 2009-11-9

@author: Administrator
'''
import re, stack

class Calc(object):
    SUPPORT_SIGN = {'(': 99, '*': 3, '/': 3, '-': 1, '+': 1}
    NUMBER_PATTERN = re.compile('\d')
    
    def __init__(self):    
        self.sign_stack = None
        self.number_stack = None

    #===============================================================================
    # init 初始化符号栈和数字站 在局部名称空间中, 要使用全局名称空间中定义的变量, 首先要使用关键字global声明一下.
    #===============================================================================
    def _init(self):
        self.sign_stack = stack.Stack()
        self.number_stack = stack.Stack()
    
    #===============================================================================
    # to_suffix 将中坠表达式转换成后缀表达式的形式
    # @return: 方便操作, 返回列表.
    #===============================================================================
    def _to_suffix(self, expression):
        #check type
        result = []
        pre_char = None
        if not isinstance(expression, str):
            raise TypeError, '表达式类型错误'
        for char in expression:
            if char in Calc.SUPPORT_SIGN:
                pre_sign = self.sign_stack.peek()
                while pre_sign and Calc.SUPPORT_SIGN[char] <= Calc.SUPPORT_SIGN[pre_sign]:
                    if pre_sign == '(':
                        break
                    result.append(self.sign_stack.pop())
                    pre_sign = self.sign_stack.peek()
                self.sign_stack.push(char)
            elif char == ')':
                pre_sign = self.sign_stack.peek()
                while pre_sign != '(':
                    pre_sign = self.sign_stack.pop()
                    result.append(pre_sign)
                    pre_sign = self.sign_stack.peek()
                self.sign_stack.pop()
            elif Calc.NUMBER_PATTERN.match(char):
                if pre_char and Calc.NUMBER_PATTERN.match(pre_char):
                    result[len(result) - 1] += char
                else:
                    result.append(char)
            else:
                raise TypeError, '不支持的符号'
            pre_char = char
        while not self.sign_stack.empty():
            result.append(self.sign_stack.pop())
        return result
    
    #===============================================================================
    # count 接口独立
    #===============================================================================
    def _count(self, suffix):
        #check type
        if not isinstance(suffix, list):
            raise TypeError, '后缀表达式类型错误'
        for element in suffix:
            if element in Calc.SUPPORT_SIGN:
                number2 = self.number_stack.pop()
                number1 = self.number_stack.pop()
                eval_str = number1 + element + number2
                self.number_stack.push(str(eval(eval_str)))
            else:
                try:
                    self.number_stack.push(element)
                except TypeError, e:
                    print '后缀表达式中有不支持的字符'
                    exit()
        return self.number_stack.pop()
    
    def calc(self, expression):
        self._init()
        return Calc._count(self, self._to_suffix(expression))

if __name__ == '__main__':
    calc = Calc()
    print calc.calc('31+22*55*(1+22*3-4/(5-6))')
