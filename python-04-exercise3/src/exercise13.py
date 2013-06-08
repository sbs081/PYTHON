'''
Created on 2009-9-2

@author: selfimpr
'''

import os.path
import exercise12

ls = os.linesep

def update():
    path = raw_input("Please enter the file path:%s" % ls)
    newcontent = []
    try: 
        file = open(path, 'r+')
        for line in file.readlines():
            newcontent.append(raw_input('%s%s' % (line, ls)))
        file.writelines('%s%s' % (line, ls) for line in newcontent)
        file.close()
    except IOError, e:
        print 'file input/output error'
        path = raw_input("Please enter the file path:%s" % ls)

input = raw_input("""
  |Please input your command: |
--|---------------------------|--
  |   r   |    read           |
  |   u   |    update          |
  |   w   |    write          |
  |  :q   |    exit           |
--|---------------------------|--
  |Please input your command: |
""")
while input != ":q":
    if input == 'r':
        exercise12.read()
    elif input == 'w':
        exercise12.write()
    elif input == 'u':
        update()
    input = raw_input("""
      |Please input your command: |
    --|---------------------------|--
      |   r   |    read           |
      |   w   |    write          |
      |   u   |    update          |
      |  :q   |    exit           |
    --|---------------------------|--
      |Please input your command: |
    """)