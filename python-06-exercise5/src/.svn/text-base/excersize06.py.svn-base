'''
Created on 2009-9-4

@author: selfimpr
'''
signable = ["+", "-", "*", "/", "%", "(", ")"]
numberable = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
signs = ["+", "-", "*", "/", "%", "**", "//"]
priorities = {"(": 9, ")": 9, "**": 7, "*": 5, "/": 5, "%": 5, "//": 5, "+": 3, "-": 3}

class Stack(object):
    '''
    author: selfimpr
    blog: http://blog.csdn.net/lgg201
    mail: lgg860911@yahoo.com.cn
    company: http://www.dartfar.com
    function: This is a general stack, use to do the sign and number's temp store
    '''
    def __init__(self):
        self.datas = []
    
    def push(self, data):
        self.datas.append(data)
    
    def pop(self):
        return self.datas.pop()
    
    def peek(self):
        if self.datas:
            return self.datas[len(self.datas) - 1]
    
    def size(self):
        return len(self.datas)
    
    def empty(self):
        return len(self.datas) < 1

#a bit function, return last element of list
def getLast(l):
    if l:
        return l[len(l) - 1]

def parseElement(expression):
    '''
    author: selfimpr
    blog: http://blog.csdn.net/lgg201
    mail: lgg860911@yahoo.com.cn
    company: http://www.dartfar.com
    function: parse a string expression to list
    '''
    result = []
    cur = ""
    for index in range(len(expression)):
        ch = expression[index]
        if numberable.__contains__(ch):
            cur += ch
        elif signable.__contains__(ch):
            if cur:
                result.append(float(cur))
                cur = ""
            if ["*", "/"].__contains__(ch) and getLast(result) == ch:
                result[len(result) - 1] *= 2
            elif ["+", "-"].__contains__(ch) \
            and ["+", "-", "*", "/", "%", "**", "//", "(", ")"].__contains__(getLast(result)) \
            and not ["+", "-", "*", "/", "%", "**", "//", "(", ")"].__contains__(expression[index + 1]):
                cur += ch
            else:
                result.append(ch)
        else:
            raise Exception, "Error"
    if cur:
        result.append(float(cur))
    return result

def priority(sign1, sign2):
    '''
    author: selfimpr
    blog: http://blog.csdn.net/lgg201
    mail: lgg860911@yahoo.com.cn
    company: http://www.dartfar.com
    function: check priority between two arguments
    '''
    return priorities[sign1] > priorities[sign2]
    

def changeToSuffix(expression):
    '''
    author: selfimpr
    blog: http://blog.csdn.net/lgg201
    mail: lgg860911@yahoo.com.cn
    company: http://www.dartfar.com
    function: change a infix expression to suffix
    (Notice: the infix is a list, you can parse a 
    infix expression to list by previous function 
    names parseElement)
    '''
    if not isinstance(expression, list) or not list or isinstance(expression[0], list):
        raise Exception("expression must be a not-null list and first element must be a number")
    suffix = []
    signStack = Stack()
    for element in expression:
        if isinstance(element, float):
            suffix.append(element)
        elif ["+", "-", "*", "/", "%", "**", "//", "(", ")"].__contains__(element):
            if element == "(":
                signStack.push(element)
            elif element == ")":
                while not signStack.empty()\
                and signStack.peek() != "(":
                    suffix.append(signStack.pop())
                signStack.pop()
            else:
                while not signStack.empty()\
                and not priority(element, signStack.peek()):
                    if signStack.peek() == "(":
                        break
                    suffix.append(signStack.pop())
                signStack.push(element)
        else:
            raise Exception("Unsupport sign or number")
    while not signStack.empty():
        suffix.append(signStack.pop())
    return suffix

def calc(a, b, sign):
    '''
    author: selfimpr
    blog: http://blog.csdn.net/lgg201
    mail: lgg860911@yahoo.com.cn
    company: http://www.dartfar.com
    function: calculate result a sign b
    '''
    if sign == "+":
        return b + a
    elif sign == "-":
        return b - a
    elif sign == "*":
        return b * a
    elif sign == "/":
        return b / a
    elif sign == "**":
        return b ** a
    elif sign == "//":
        return b // a
    else:
        raise Exception("Unsupport sign: %s" % sign)

def account(expression):
    '''
    author: selfimpr
    blog: http://blog.csdn.net/lgg201
    mail: lgg860911@yahoo.com.cn
    company: http://www.dartfar.com
    function: calculate a suffix expression (Notice: it must a list)
    '''
    if not isinstance(expression, list) or not list or isinstance(expression[0], list):
        raise Exception("expression must be a not-null list and first element must be a number")
    numberStack = Stack()
    for element in expression:
        if isinstance(element, float):
            numberStack.push(element)
        else:
            numberStack.push(calc(numberStack.pop(), numberStack.pop(), element))
    return numberStack.pop()