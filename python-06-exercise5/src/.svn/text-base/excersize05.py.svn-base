'''
Created on 2009-9-4

@author: selfimpr
'''

def getMinCentes(dollar):
    if dollar <=0 or dollar >=1:
        raise Exception, "You must provide a number between 0 and 1"
    centes = int(dollar * 100)
    useAble = {5: 0, 25: 0, 10: 0, 1: 0}
    keys = useAble.keys()
    keys.sort(cmp=None, key=None, reverse=True)
    for key in keys:
        while centes >= key:
            useAble[key] += 1
            centes = centes - key
        if centes <= 0:
            break
    return useAble