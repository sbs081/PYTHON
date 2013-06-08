'''
Created on 2009-9-15

@author: selfimpr
'''
def safe_input(msg):
    try:
        input = raw_input(msg)
    except EOFError, e:
        input = None
    return input
safe_input('hello')