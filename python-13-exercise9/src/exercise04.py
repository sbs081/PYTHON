'''
Created on 2009-9-15

@author: selfimpr
'''
#This is commont
from os import *
from os.path import *
from sys import *
import string
file_name = raw_input('please enter filename: \n')
command = 'pause'
f = file(file_name, 'r')
line = f.next()
i = 1
while line and i :
    print line, 
    try:
        line = f.next()
    except StopIteration, e:
        break
    i += 1
    if i % 25 == 0:
        system(command)