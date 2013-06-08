'''
Created on 2009-9-15

@author: selfimpr
'''
import math, cmath, sys
def safe_sqrt(number):
    try:
        sqrt = math.sqrt(number)
    except TypeError, e:
        sqrt = cmath.sqrt(number)
    return sqrt
print safe_sqrt(1+2j)