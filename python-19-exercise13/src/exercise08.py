'''
Created on 2009-10-5

@author: selfimpr
'''

class Stack(object):
    def __init__(self):
        self.data = []
        if 'pop' in dir(list):
            self.flag = True
        else:
            self.flag = False
    def push(self, element):
        self.data.append(element)
    def self_pop(self):
        try:
            return self.data[len(self.data) - 1]
        finally:
            del self.data[len(self.data) - 1]
    def pop(self):
        return self.data.pop() if self.flag else self.self_pop()
    def empty(self):
        return len(self.data) == 0
    def __str__(self):
        return self.data.__str__()

class Queue(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.flag = True
    def insert(self, element):
        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(element)
        while not self.stack2.empty():
            self.stack1.push(self.stack2.pop())
    def remove(self):
        return self.stack1.pop()
    def __str__(self):
        return self.stack1.__str__()

if __name__ == '__main__':
#    stack = Stack()
#    stack.push(1)
#    stack.push(2)
#    stack.push(3)
#    stack.push(4)
#    stack.push(5)
#    print stack
#    print stack.pop()
#    print stack.pop()
#    print stack
    queue = Queue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.insert(4)
    queue.insert(5)
    queue.insert(6)
    print queue
    print queue.remove()
    print queue.remove()
    print queue