'''
Created on 2009-9-1

@author: selfimpr
'''
input = int(raw_input('enter a number between -1 and 100'))
while input > 100 or input <= -1:
    input = int(raw_input('enter a number between -1 and 100'))
print 'input successs, your number is: %d' % input
