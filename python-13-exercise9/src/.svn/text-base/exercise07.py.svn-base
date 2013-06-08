'''
Created on 2009-9-15

@author: selfimpr
'''
#This is commont
from os import *
from os.path import *
from sys import *
import string
file_name = 'c:\\windows\\win.ini'
f = file(file_name, 'r')
tmp = {}
try:
    line = f.next()
    while line:
        if line[0] == ';':
            line = f.next()
            continue
        elif line[0] == '[':
            name = line[1:-2]
            tmp[name] = {}
            line = f.next()
            while line and line[0] != '[':
                arr = line.strip().split('=')
                tmp[name][arr[0]] = arr[1]
                line = f.next()
            continue
except StopIteration, e:
    pass
for key in tmp:
    print key + ': '
    if tmp[key]:
        for keykey in tmp[key]:
            print '\t%s----%s' % (keykey, tmp[key][keykey])