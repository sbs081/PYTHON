'''
Created on 2009-9-9

@author: selfimpr
'''
import string, keyword

def idcheck(flag):
    return (flag[0] in string.letters \
    or flag[0] == '_') \
    and not keyword.iskeyword(flag) \
    and not [s for s in flag[1:] \
    if s not in string.letters + string.digits + "_"]
