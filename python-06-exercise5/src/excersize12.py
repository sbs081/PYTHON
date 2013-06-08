'''
Created on 2009-9-4

@author: selfimpr
'''

import random

def toy():
    list = []
    sublist = []
    for i in range(random.randint(2, 101)):
        list.append(random.randint(0, 231))
    for i in range(random.randint(2, list.__len__() - 1)):
        sublist.append(list[random.randint(2, list.__len__() - 1)])
    return sublist

print toy()