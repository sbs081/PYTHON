'''
Created on 2009-9-21

@author: selfimpr
'''
import time
def timeit(func):
    def wrapper(*args, **kargs):
        begin = time.clock()
        result = func(*args, **kargs)
        useTime = time.clock() - begin
        print 'result is: %s, and useTime is: %s'\
        % (result, useTime)
    return wrapper

@timeit
def f():
    for i in xrange(100000000):
        pass
    return 100

if __name__ == '__main__':
    f()