'''
Created on 2009-9-14

@author: selfimpr
'''
vowels = 'aeiou'
def count(s):
    result = 0
    for word in s.split():
        if word[0] in vowels:
            result += 1
    return result
print count('hello, every are you fine these days')