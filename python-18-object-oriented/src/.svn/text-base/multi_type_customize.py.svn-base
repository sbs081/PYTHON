'''
Created on 2009-9-29

@author: selfimpr
'''
class NumStr(object):
    def __init__(self, self_number = 0, \
                 self_string = ''):
        self.self_number = self_number
        self.self_string = self_string
    def __add__(self, target):
        return self.__class__( \
               self.self_number + target.self_number, \
               self.self_string + target.self_string)
    def __mul__(self, n):
        return self.__class__( \
               self.self_number * n, \
               self.self_string * n)
    def __nonzero__(self):
        return self.self_number != 0 \
                and self.self_string != ''
    def __cmp__(self, target):
        if self.self_number > target.self_number \
            and self.self_string > target.self_string:
            return 1
        elif self.self_number < target.self_number \
            and self.self_string < target.self_string:
            return -1
        else: return 0
    def __str__(self):
        return '[number: %s, string: %s]' % \
                (self.self_number, self.self_string)

if __name__ == '__main__':
    n1 = NumStr(100, 'Hello')
    n2 = NumStr(200, 'World')
    n3 = NumStr(50, 'Jack')
    n4 = NumStr()
    print  n1 + n2
    print n3 * 5
    print bool(n4)
    print n1 < n2
    print n2 > n1
    print n3 == n1