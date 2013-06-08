'''
Created on 2009-10-4

@author: selfimpr
'''
import math

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return 'x: %s, y: %s.' % (self.x, self.y)
    def __repr__(self):
        return '(%s, %s)' % (self.x, self.y)

class Line(object):
    def __init__(self, begin = Point(), end = Point()):
        self.begin = begin
        self.end = end
    def length(self):
        return math.sqrt(\
                  math.pow(self.begin.x - self.end.x, 2)
                  + math.pow(self.begin.y - self.end.y, 2))
    def slope(self):
        if self.begin.x == self.end.x:
            return str(90) + ' angle'
        if self.begin.y == self.end.y:
            return str(0) + ' angle'
        realSlope = math.asin(abs(self.begin.y - self.end.y) / self.length())
        if (self.begin.x > self.end.x and self.begin.y > self.end.y)\
            or (self.begin.x < self.end.x and self.begin.y < self.end.y):
            return str(realSlope / math.pi * 180) + ' angle'
        return str((realSlope + math.pi / 2) / math.pi * 180) + ' angle'
    def __repr__(self):
        return '(%r, %r)' % (self.begin, self.end)
        

if __name__ == '__main__':
    l = Line(Point(0, 0), Point(1, 1))
    print l
    print l.length()
    print l.slope()