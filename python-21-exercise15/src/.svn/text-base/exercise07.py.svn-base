'''
Created on 2009-10-23

@author: selfimpr
'''
import re

pattern = re.compile(r'(?i)^0b[01]+$|^0[0-7]+$|^0x[\da-f]+$|^\d+$')

if __name__ == '__main__':
    print pattern.search('0b101010').group()
    print pattern.search('0x123479FF').group()