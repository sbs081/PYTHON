'''
Created on 2009-9-7

@author: selfimpr
'''
import urllib

f = urllib.urlopen("http://localhost/eweb/bbs/space.php", {"uid": 1})
print f.geturl()
print f.getcode()
print f.info()
line = f.readline()
while line:
    print line
    line = f.readline()