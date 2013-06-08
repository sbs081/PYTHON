'''
Created on 2009-8-31

@author: selfimpr
'''
#file name is F:\python_workspace\python-01-basesyntax\src\file.file
try:
    filename = raw_input("Please enter file name: \n")
    file = open(filename)
    for line in file:
        print line, file.close()
except IOError, e:
    print "file open error: ", e
