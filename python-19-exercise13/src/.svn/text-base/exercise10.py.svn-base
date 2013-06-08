'''
Created on 2009-10-7

@author: selfimpr
'''

class StackQueue(object):
    def __init__(self):
        self.data = []
    
    def unshift(self, element):
        self.data.insert(0, element)
    
    def shift(self):
        if self.empty():
            return None
        try:
            return self.data[0]
        finally:
            del self.data[0]
    
    def push(self, element):
        self.data.append(element)
    
    def pop(self):
        return self.data.pop()
    
    def empty(self):
        return len(self.data) < 1
    
    def __str__(self):
        return self.data.__str__()

if __name__ == '__main__':
    stackQueue = StackQueue()
    stackQueue.unshift(1)
    stackQueue.unshift(2)
    stackQueue.unshift(3)
    stackQueue.unshift(4)
    stackQueue.unshift(5)
    stackQueue.push(6)
    stackQueue.push(7)
    stackQueue.push(8)
    stackQueue.push(9)
    stackQueue.push(10)
    stackQueue.push(11)
    print stackQueue
    print stackQueue.shift()
    print stackQueue.pop()
    print stackQueue.shift()
    print stackQueue.shift()
    print stackQueue.pop()
    print stackQueue