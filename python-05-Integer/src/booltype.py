'''
Created on 2009-9-4

@author: selfimpr
'''
class C:
    def __nonzero__(self):
        return 0
    
    def __repr__(self):
        return "__repr__"
    
    def __str__(self):
        return "__str__"

c = C()
print bool(c)