'''
Created on 2009-9-17

@author: selfimpr
'''
import time

def func1():
    return 1
func2 = lambda : 1 

times = 99999999
start = time.time()
for i in xrange(times):
    func1()
print time.time() - start

start = time.time()
for i in xrange(times):
    func2()
print time.time() - start