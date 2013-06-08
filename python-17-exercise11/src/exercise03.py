'''
Created on 2009-9-20

@author: selfimpr
'''
def max2(*arg):
    if not len(arg):
        raise ValueError, "except at least one argument"
    elif len(arg) == 1:
        return arg[0]
    else:
        def max_in(a, b):
            return cmp(a, b) >= 0 and a or b
        tmp = arg[0]
        for x in arg:
            tmp = max_in(tmp, x)
        return tmp

def min2(*arg):
    if not len(arg):
        raise ValueError, "except at least one argument"
    elif len(arg) == 1:
        return arg[0]
    else:
        def max_in(a, b):
            return cmp(a, b) <= 0 and a or b
        tmp = arg[0]
        for x in arg:
            tmp = max_in(tmp, x)
        return tmp
