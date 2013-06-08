'''
Created on 2009-10-23

@author: selfimpr
'''
import re

pattern = re.compile(r'www\.([a-zA-Z_]\w*)\.(com|edu|net)')

if __name__ == '__main__':
    print pattern.search('www.baidu.com').group()
    print pattern.search('www.csdn.net').group()
    print pattern.search('www.china.edu').group()