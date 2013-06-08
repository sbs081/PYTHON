'''
Created on 2009-9-11

@author: selfimpr
'''
a = {}
for i in xrange(1000000):
    a[i] = -i
keys = a.iterkeys()
for i in keys:
    print i