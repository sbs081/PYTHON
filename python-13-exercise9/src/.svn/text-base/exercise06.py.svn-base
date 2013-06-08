'''
Created on 2009-9-15

@author: selfimpr
'''
#This is commont
from os import *
from os.path import *
from sys import *
import string
file_name1 = raw_input('please enter filename1: \n')
file_name2 = raw_input('please enter filename2: \n')
f1 = file(file_name1, 'r')
f2 = file(file_name2, 'r')
line1 = f1.next()
line2 = f2.next()
i = 1
while line1 and line2:
    l1 = len(line1)
    l2 = len(line2)
    if l1 != l2:
        print i
    else:
        for j in range(l1):
            if line1[j] != line2[j]:
                print i
    try:
        line1 = f1.next()
        line2 = f2.next()
    except StopIteration, e:
        print 'same file'
        break
    i += 1