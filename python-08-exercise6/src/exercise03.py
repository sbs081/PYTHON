'''
Created on 2009-9-9

@author: selfimpr
'''

input = raw_input("enter a number list:\n")

a = eval(input)
print(sorted(a))

b = [str(e) for e in a]

print(sorted(b))