'''
Created on 2009-9-2

@author: selfimpr
'''

import os.path

ls = os.linesep

path = raw_input('Please input full path of file%s' % ls)
while os.path.exists(path):
    path = raw_input('Please input full path of file%s' % ls);

print 'Please enter content:%s' % ls
content = []
line = raw_input("> ")
while line != ':q':
    content.append(line)
    line = raw_input("> ")

file = open(path, 'w')
file.writelines("%s%s" % (l, ls) for l in content)
file.close()

print 'success'