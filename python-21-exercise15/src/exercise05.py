'''
Created on 2009-10-23

@author: selfimpr
'''
import re

pattern = re.compile('\d{4}( \w+)+')

if __name__ == '__main__':
    print pattern.search('1180 Bordeaux Drive').group()
    print pattern.search('3120 De la Cruz Boulevard').group()