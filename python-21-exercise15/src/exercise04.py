'''
Created on 2009-10-23

@author: selfimpr
'''
import keyword
import re

pattern = re.compile('^\w[\w\d]*$')

def is_legality(s):
    if not isinstance(s, str):
        raise TypeError, 'except a string type, and you give a instance of %s' % type(s)
    match = pattern.match(s)
    if not match:
        return False
    else:
        return not keyword.iskeyword(s)  

if __name__ == '__main__':
    print is_legality('$hello')
    print is_legality('_hello1')
    print is_legality('hello')
    print is_legality('int')
    print is_legality('type')
    print is_legality('if')