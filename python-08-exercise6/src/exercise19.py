'''
Created on 2009-9-9

@author: selfimpr
'''
def formatPrint(*iterable, **arg):
    col = int(arg["col"]) + 1
    rows = len(iterable) / col
    for i in range(rows):
        for j in range(col):
            try:
                print iterable[j * rows + i],
            except IndexError, e:
                pass 
        print

formatPrint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, col = 6)