'''
Created on 2009-9-2

@author: selfimpr
'''

import os.path

ls = os.linesep

path = raw_input('Please input full path of file%s' % ls)
while not os.path.exists(path):
    path = raw_input('Please input full path of file%s' % ls);

file = open(path, 'r')
for line in file.readlines():
    print line.strip(ls)

print 'success'