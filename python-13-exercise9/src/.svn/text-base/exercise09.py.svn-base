'''
Created on 2009-9-15

@author: selfimpr
'''
#This is commont
#C:\Python26\Lib
import os
import os.path
dirs = os.walk('C:\\Python26\\Lib\\')
f = open('c:\\documents.txt', 'w')
never_docs = []
for dir, subdirnames, subfilenames in dirs:
    parents = dir.split('C:\\Python26\\Lib\\')[1].split('\\')
    for module_name in subfilenames:
        module_name = os.path.splitext(module_name)
        if module_name[1] in ['.py', '.pyc'] and module_name[0] != '__init__':
            exec('import ' + module_name[0])
            try:
                docum = eval(module_name[0] + '.__doc__')
                if docum:
                    print >> f, docum
                    f.flush()
                else:
                    never_docs.append(module_name[0])
            except ImportError, e:
                pass
