'''
Created on 2009-10-23

@author: selfimpr
'''
import re

pattern = re.compile('^\d{4}(?=-)(?:-)(\d{6}(?=-)(?:-)\d{5}|(\d{4}(?=-)(?:-)){2}\d{4})$')

if __name__ == '__main__':
    print pattern.search('1234-567890-12345').group()
    print pattern.search('1234-5678-9012-3456').group()