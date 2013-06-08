'''
Created on 2009-9-11

@author: selfimpr
'''
d1 = {1: "one", 2: 'two', 3: 'three'}
d2 = {}
for key, value in d1.items():
    d2[value] = key
print d2