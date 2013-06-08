'''
Created on 2009-9-14

@author: selfimpr
'''
def getfactors(number):
    tmp = 1
    result = []
    while tmp < number:
        if not number % tmp:
            result.append(tmp)
        tmp += 1
    return result
def isperfect(number):
    return sum(getfactors(number)) == number and 1 or 0
print isperfect(int(raw_input('enter a number: \n')))

for i in range(100000):
    if isperfect(i):
        print i, 