'''
Created on 2009-9-14

@author: selfimpr
'''
from exercise05 import *
from exercise04 import *

input = int(raw_input('enter a number: \n'))
tmp = input
result = []
factors = getfactors(input)
while tmp > 1:
    result.append(factors[1])
    tmp = tmp / factors[1]
    factors = getfactors(tmp)

print result