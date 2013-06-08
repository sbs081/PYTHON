'''
Created on 2009-9-11

@author: selfimpr
'''
def endoc(s):
    for i in range(len(s)):
        n = ord(s[i])
        if n >= 65 and n <=90:
            s = s[:i] + chr(65 + n % 26) + s[i + 1: ]
        if n >= 97 and n <=122:
            s = s[:i] + chr(97 + (n - 97 + 13) % 26) + s[i + 1: ]
    return s
            
print endoc(endoc("azAZ"))
