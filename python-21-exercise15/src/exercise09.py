'''
Created on 2009-10-23

@author: selfimpr
'''
import re

pattern = re.compile(r'^\d+\.\d+$')

if __name__ == '__main__':
    print pattern.search('1.2').group()
    print pattern.search('1.00091').group()