'''
Created on 2009-10-23

@author: selfimpr
'''
import re

pattern = re.compile(r'(?i)^(?P<real>\d+\.\d+|(0b[01]+|0[0-7]+|0x[\da-f]+|[1-9]\d*)l?)\s*(\+\s*(?P<image>\d+\.\d+|(0b[01]+|0[0-7]+|0x[\da-f]+|[1-9]\d*)l?)j)?$')

if __name__ == '__main__':
    print pattern.search('0b101').group()
    print pattern.search('0b101L+2J').group()
    print pattern.search('07163+2J').group()
    print pattern.search('56789+2J').group()
    print pattern.search('0xff1234+2J').group()
    print pattern.search('0.123+2J').group()
    print pattern.search('1.283+2.89J').group()
    