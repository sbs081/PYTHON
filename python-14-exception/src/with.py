'''
Created on 2009-9-15

@author: selfimpr
'''
class mycontext(object):
    def __enter__(self):
        print 'context initial'
        return 9
    def __exit__(self, err_type, err_ins, err_trace):
        print err_ins
class mycontextmanager(object):
    def __context__(self):
        return mycontext()
with mycontextmanager() as a:
    print 'mycontext block %d' % a