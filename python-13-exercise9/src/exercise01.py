'''
Created on 2009-9-15

@author: selfimpr
'''
#This is commont
from os import *
from os.path import *
from sys import *
import string
file_name = split(argv[0])[1]
f = file(file_name, 'r')
line = f.readline()
while line:
    if string.lstrip(line) and string.lstrip(line)[0] != '#':
        print line,
    line = f.readline()