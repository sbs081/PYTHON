'''
Created on 2009-9-7

@author: selfimpr
'''
import codecs

CODEC = "UTF-8"
FILE = 'unicode.txt'

helloout = u"HelloWorld"
bytesout = helloout.encode(CODEC)
f = open(FILE, 'w')
f.write(bytesout)
f.close()

f = open(FILE, 'r')
bytes_in = f.read()
f.close()
print bytes_in.decode(CODEC)