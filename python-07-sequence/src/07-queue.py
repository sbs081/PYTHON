'''
Created on 2009-9-9

@author: selfimpr
'''
import random

class Queue(object):
    def __init__(self):
        self.datas = list()
    def insert(self, data):
        i = len(self.datas) - 1
        while i >= 0 and data > self.datas[i]:
            i -= 1
        data, self.datas.insert(i + 1, data)
    def remove(self):
        if self.empty():
            raise Exception("I'm empty")
        else:
            tmp = self.datas.__getitem__(0)
            self.datas.__delitem__(0)
            return tmp
    def empty(self):
        return not len(self.datas)

q = Queue()
for i in range(100):
    q.insert(random.randint(0, 20))

for i in range(50):
    print q.remove()

print 


def f(x, y, *z):
    print x, y, z

t = (1, 2, 3, 4)
f(1, 2, t)