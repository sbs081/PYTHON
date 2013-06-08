'''
Created on 2009-10-23

@author: selfimpr
'''
import re

if __name__ == '__main__':
    strs = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']
    pattern = re.compile('[bh][aiu]t')
    for s in strs:
        print pattern.search(s).group()