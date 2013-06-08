'''
Created on 2009-9-30

@author: selfimpr
'''
class a(object):
    def __init__(self, width):
        self.__width = ~width
    @property
    def width(self):
        return ~self.__width
    @width.setter
    def width(self, width):
        self.__width = ~width
        print 'now, width is: %s' % ~self.__width
    @width.deleter
    def width(self):
        self.__width = ~-1
        print 'now, width is: %s' % ~self.__width

if __name__ == '__main__':
    aa = a(1000)
    print dir(a)
    print aa.width
    aa.width = 30
    del aa.width