'''
Created on 2009-9-30

@author: selfimpr
'''
class a(object):
    def __init__(self, width):
        self.__width = ~width
    def getWidth(self):
        return ~self.__width
    def setWidth(self, width):
        self.__width = ~width
        print 'now, width is: %s' % ~self.__width
    def delWidth(self):
        self.__width = ~-1
        print 'now, width is: %s' % ~self.__width
    width = property(getWidth, setWidth, delWidth)

if __name__ == '__main__':
    aa = a(1000)
    print aa.width
    aa.width = 30
    del aa.width