'''
Created on 2009-10-11

@author: selfimpr
'''

if __name__ == '__main__':
    input = raw_input('Please input a number')
    while input != 'q':
        result = int(input)
        print result, type(result)
        input = raw_input('Please input a number')