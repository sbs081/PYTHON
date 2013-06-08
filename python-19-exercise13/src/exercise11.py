'''
Created on 2009-10-7

@author: selfimpr
'''

class User(object):
    def __init__(self):
        self.carts = []
    
    def addCart(self, cart):
        if not isinstance(cart, Cart):
            raise TypeError, 'required an instance of Cart'
        self.carts.append(cart)

class Item(object):
    def __init__(self):
        pass

class Cart(object):
    def __init__(self):
        self.items = []
    
    def add(self, item):
        if not isinstance(item, Item):
            raise TypeError, 'required an instance of Item'
        self.items.append(item)
    
    

if __name__ == '__main__':
    pass