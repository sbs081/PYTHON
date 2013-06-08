'''
Created on 2009-9-16

@author: selfimpr
'''
import time
def mydecorator(func):
    def wrappedFunc(*args):
        print '[%s] %s() called' % (time.ctime(), func.__name__)
        print arg
        print args
        return func(*args)
    return wrappedFunc

def call():
    print 'I am called'

@mydecorator
def f(s, y):
    return 'Hello decorator! %s, %s' % (s, y)

print f('Jack', 'Tom')