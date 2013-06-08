'''
Created on 2009-9-14

@author: selfimpr
'''
import sys

print dir(sys)
print
print sys.exc_info()
i = sys.stdin
o = sys.stdout
e = sys.stderr
o.write(i.readline())
e.write(i.readline())

