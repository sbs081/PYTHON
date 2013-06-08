'''
Created on 2009-9-7

@author: selfimpr
'''
import time
import string
s = "abcdefg"
s[:2]
print id(s[:3])
print id("abc")
print id("ab") == id(s[:2])

def idcheck(marker):
    if not (string.ascii_letters + "_")\
    .__contains__(marker[0]):
        return False
    for ch in marker[1:]:
        if not (string.ascii_letters + string.digits + "_") \
        .__contains__(ch):
            return False
    return True

idcheck("7assd")

def t():
    print "I am called"
    return 20

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
        print "My size method is called"
        return len(self.datas)
    
    def empty(self):
        return len(self.datas) < 1

def testLoop():
    stack = Stack()
    for i in range(t()):
        stack.push(id(i))
    j = 0
    while j < stack.size():
        id(j)
        print j
        j += 1
testLoop()

def compareLoop():
    count = 50000000
    l = []
    for i in xrange(count):
        l.append(i)
    fi = 0
    first = time.time()
    while fi < count:
        fi += 1
    ft = time.time() - first
    print ft
    si = 0
    second = time.time()
    while si < len(l):
        si += 1
    st = time.time() - second
    print st
    print (st - ft) / count
#compareLoop()

for i in range(20):
    print i, 
else:
    print "This is for-else case"
