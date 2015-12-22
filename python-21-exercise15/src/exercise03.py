'''
Created on 2009-10-23

@author: selfimpr
'''
import re

if __name__ == '__main__':
    pattern = re.compile(r'[a-zA-Z], \b[a-zA-Z0-9]+\b')
    print pattern.search('M, tom1').group()
