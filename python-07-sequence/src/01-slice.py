'''
Created on 2009-9-7

@author: selfimpr
'''

s = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(s)):
    print s[0:len(s) - i]

for i in [None] + range(-1, -len(s), -1):
    print s[:i]

enum = enumerate("abcdefgh")
dic = {1: "1", 2: "2", 3: "3"}
for key, value in dict:
    print key, "---", value