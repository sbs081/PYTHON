'''
Created on 2009-10-7

@author: selfimpr
'''

class Queue(object):
    def __init__(self):
        self.data = []
    def enqueue(self, element):
        self.data.append(element)
    
    def dequeue(self):
        if self.empty():
            return None
        try:
            return self.data[0]
        finally:
            del self.data[0]
    
    def empty(self):
        return len(self.data) < 1
    
    def __str__(self):
        return self.data.__str__()

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print queue
    print queue.dequeue()
    print queue.dequeue()
    print queue