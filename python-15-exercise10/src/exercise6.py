'''
Created on 2009-9-15

@author: selfimpr
'''
def o(file_name, mode):
    try:
        f = open(file_name, mode)
    except IOError, e:
        f = None
    return f
print o('c:\\1.txt', 'r')