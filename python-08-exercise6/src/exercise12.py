'''
Created on 2009-9-9

@author: selfimpr
'''
def findchr(s, c):
    if len(c) != 1:
        raise Exception("You must give me a char length one")
    i = 0
    for i in range(len(s)):
        if s[i] == c:
            return i
    else:
        return -1

def rfindchr(s, c):
    if len(c) != 1:
        raise Exception("You must give me a char length one")
    i = -1
    for i in range(-len(s) + 1, i):
        if s[i] == c:
            return i
    else:
        return 1

def subchr(s, o, n):
    i = findchr(s, o)
    if i > -1:
        return s[:i] + n + s[i+1:]