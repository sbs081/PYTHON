'''
Created on 2009-9-30

@author: selfimpr
'''
class MyMetaClass(type):
    def __init__(cls, name, bases, attrd):
        print cls, name, bases, attrd
        super(MyMetaClass, cls).__init__(name, bases, attrd)
        if '__str__' not in attrd:
            raise TypeError, 'Must rewrite __str__ method'
class Class(object):
    __metaclass__ = MyMetaClass
    pass

if __name__ == '__main__':
    Class()