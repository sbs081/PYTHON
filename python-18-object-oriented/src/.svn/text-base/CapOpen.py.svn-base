'''
Created on 2009-9-29

@author: selfimpr
'''

class CapOpen(object):
    '''
    write will change lower to upper
    '''


    def __init__(self, filename, mode = 'r', buf = -1):
        '''
        Constructor
        '''
        self.file = open(filename, mode)
    def writeLine(self, line):
        self.file.write(line.upper())
    def __getattr(self, attr):
        return getattr(self, attr)
    def __del__(self):
        self.file.close()
        del self.file
if __name__ == '__main__':
    f = CapOpen('datas.data', 'w')
    f.writeLine('hello, every one')