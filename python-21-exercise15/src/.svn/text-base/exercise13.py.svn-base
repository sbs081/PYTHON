'''
Created on 2009-10-23

@author: selfimpr
'''
import re

pattern = re.compile(r'^<type \'(?P<name>\w+)\'>$')

def gettype(obj):
    match = pattern.match(str(type(obj)))
    if not match:
        raise TypeError, 'it is unsupport type'
    return eval(match.group('name'))

if __name__ == '__main__':
    print gettype(1)