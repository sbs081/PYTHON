'''
Created on 2009-10-23

@author: selfimpr
'''
import re

pattern = re.compile('^((?P<one>1)|0)(?(one)[0-2]|[1-9])$')

if __name__ == '__main__':
    for i in range(0, 14):
        try:
            print pattern.match(str(i).rjust(2, '0')).group()
        except AttributeError, e:
            print 'The value %d can\'t match with this pattern.' % i