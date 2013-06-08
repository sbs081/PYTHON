'''
Created on 2009-9-9

@author: selfimpr
'''

def trim(s):
    return ltrim(rtrim(s))

def ltrim(s):
    space = "\r", "\t", "\f", "\v", "\n", " "
    i = 0
    while i < len(s):
        if s[i] not in space:
            break
        i += 1
    return s[i:]

def rtrim(s):
    space = "\r", "\t", "\f", "\v", "\n", " "
    i = -1
    while i >= -len(s):
        if s[i] not in space:
            break
        i -= 1
    return s[:i+1]

print trim('''    space ===  '' 


''')