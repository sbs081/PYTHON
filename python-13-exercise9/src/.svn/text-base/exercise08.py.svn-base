'''
Created on 2009-9-15

@author: selfimpr
'''
#This is commont
from os import *
from os.path import *
from sys import *
import string
model_name = raw_input('please enter a model name; \n')
exec('import ' + model_name)
print 'name'.ljust(19), 'type'.ljust(19), 'value'.ljust(19)
for attr in dir(model_name):
    result = ''
    try:
        result = str(eval(model_name + '.' + attr))
    except AttributeError, e:
        pass
    print attr.ljust(19), str(type(attr)).ljust(19), result.ljust(19)
