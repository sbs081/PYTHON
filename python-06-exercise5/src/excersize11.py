'''
Created on 2009-9-4

@author: selfimpr
'''

def getEven(area):
    result = []
    for i in range(area):
        if not i % 2:
            result.append(i)
    return result

def getOdd(area):
    result = []
    for i in range(area):
        if i % 2:
            result.append(i)
    return result

def checkDivision(a, b):
    return not bool(a % b)