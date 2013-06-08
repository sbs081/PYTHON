#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: selfimpr
@blog: http://blog.csdn.net/lgg201
@mail: lgg860911@yahoo.com.cn
@date: 2009-12-7
'''
from time import *
from thread import *

loops = [4, 2]

def loop(nloop, nsec, lock):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()

def main():
    print 'starting at:', ctime()
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked(): pass
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()