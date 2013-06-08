'''
Created on 2009-10-5

'MDY' ==> MM/DD/YY
'MDYY' ==> MM/DD/YYYY
'DMY' ==> DD/MM/YY
'DMYY' ==> DD/MM/YYYY
'MODYY' ==> Mon DD, YYYY

@author: selfimpr
'''

import time

formaters = {'MDY': '%m/%d/%y', 
            'MDYY': '%m/%d/%Y', 
            'DMY': '%d/%m/%y', 
            'DMYY': '%d/%m/%Y',
            'MODYY': '%m %d, %Y'}

class TimeFormat(object):
    def __init__(self, now = time.time(), fmt = 'MDY'):
        self.now = time.localtime(now)
        self.fmt = fmt
    def register(self, key, value):
        formaters[key] = value
    def update(self, now = time.time()):
        self.now = now
    def display(self):
        print time.strftime(formaters[self.fmt], self.now)

if __name__ == '__main__':
    tf = TimeFormat(fmt = 'MODYY')
    tf.display()