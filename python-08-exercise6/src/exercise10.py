'''
Created on 2009-9-9

@author: selfimpr
'''
import string

def f(x):
    return x*x

def swap(s):
    for i in range(len(s)):
        if s[i] in string.letters:
            s = s[:i] + string.swapcase(s[i]) + s[i+1:]
    return s

print swap("2.332klkjsadfiowesjfAFAWEFEWf")
