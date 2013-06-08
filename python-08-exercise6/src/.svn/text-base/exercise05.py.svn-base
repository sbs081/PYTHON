'''
Created on 2009-9-9

@author: selfimpr
'''
import string

if __name__ == "__main__":
    input = raw_input("enter a string: \n")
    while input:
        for c in input:
            print '*' + c.ljust(2, '*')
        input = raw_input("enter a string: \n")

def contain(parent, child):
    if len(parent) - len(child) < 0:
        return False
    r = range(len(parent) - len(child))
    for i in r:
        r2 = range(i, len(child) + i)
        for j in r2:
            if parent[j] != child[j - i]:
                break
        else:
            return True
    return False

def isRecur(s):
    if len(s) % 2 != 0:
        return False
    t = s[:len(s)/2], s[len(s)/2:]
    return t[0] == t[1]

def isPalindrome(s):
    i = 0
    while i < len(s) / 2:
        if s[i] != s[-i-1]:
            return False
        i += 1
    return True

def toPalindrome(s):
    tmp = s
    for i in range(0, len(s)):
        tmp = tmp.__add__(s[-i-1])
    return tmp
        