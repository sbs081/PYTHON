'''
Created on 2009-9-28

@author: selfimpr
'''
class P1(object):
    def foo(self):
        print 'called class p1-foo()'
class P2(object):
    def foo(self):
        print 'called class p2-foo()'
    def bar(self):
        print 'called class p2-bar()'
class C1(P1, P2):
    pass
class C2(P1, P2):
    def bar(self):
        print 'called class c2-bar()'
class GC(C1, C2):
    pass

if __name__ == '__main__':
    GC().foo()
    GC().bar()
    print GC.__mro__