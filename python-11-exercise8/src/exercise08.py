'''
Created on 2009-9-14

@author: selfimpr
'''
def factorial(number):
    result = 1
    tmp = 1
    while tmp <= number:
        result *= tmp
        tmp += 1
    return result
print factorial(10)