'''
Created on 2009-9-20

@author: selfimpr
'''
import os, os.path
import re

path = raw_input("please input a path:")
if not os.path.isfile(path):
    print "the path you input is not a file"
    exit()
f = open(path, 'r')
content = [line for line in f]
flag = True
while flag:
    for i in range(len(content)):
        line = content[i]
        for j in range(len(line)):
            if not re.search('\s', line[j]):
                line = line[j:]
                flag = False
                break
        if not flag:
            content[i] = line
            break
        del content[i]
content.reverse()
flag = True
while flag:
    for i in range(len(content)):
        line = content[i]
        for j in range(-len(line), 0):
            print j
            if not re.search('\s', line[j]):
                line = line[:j]
                flag = False
                break
        if not flag:
            content[i] = line
            break
        del content[i]
content.reverse()
print content