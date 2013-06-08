'''
Created on 2009-10-23

@author: selfimpr
'''
import re

pattern = re.compile(r'^[a-z_]\w*@(\w+\.)+(com|edu|cn)$')

if __name__ == '__main__':
    print pattern.search('lgg860911@yahoo.com.cn').group()
    print pattern.search('lgg201@tom.com').group()
    print pattern.search('selfimpr@vip.qq.com').group()
    print pattern.search('lgg860911@gmail.com').group()
    