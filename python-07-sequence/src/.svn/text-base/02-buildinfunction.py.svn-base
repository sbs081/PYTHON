'''
Created on 2009-9-7

@author: selfimpr
'''
import operator
import random


s = "abcdefghijklmnopqrstuvwxyz"
l = [-1, 2, -3, 4, -5, 6, -7]
print sum(l, 8)
print reduce(operator.add, l, 8)

class MyObject(object):
    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return str(self.x)
    
    def __repr__(self):
        return str(self.x) + ": " + str(id(self))

def k(o):
    return o.x

def c(x, y):
    return x * x - y * y

l = []
for i in range(20):
    l.append(MyObject(random.randint(-200, 200)))

#l.sort(lambda x, y: cmp(x, y), k, reverse=False)
l.sort(c, k, reverse=False)

print l
print max(l, key = k)