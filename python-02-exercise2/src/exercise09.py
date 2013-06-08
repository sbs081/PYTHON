'''
Created on 2009-9-1

@author: selfimpr
'''
import decimal

list = [1, 2, 9, 4, 5, 7]

length = len(list)
result = 0
for i in list:
    result += float(i) / length
print result
