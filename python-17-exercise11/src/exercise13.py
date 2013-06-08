'''
Created on 2009-9-21

@author: selfimpr
'''
import time
print globals()
print locals()
def timeit(func, *args, **kargs):
    begin = time.clock()
    result = func(*args, **kargs)
    useTime = time.clock() - begin
    return result, useTime
mult = lambda x, y: x * y
factorial1 = lambda n: reduce(mult, range(1, n + 1))
factorial2 = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
factorial4Recursion = lambda n: n == 1 and 1 \
    or n * factorial4Recursion(n - 1)

if __name__ == '__main__':
    print mult(2, 3)
    print factorial1(6)
    print factorial2(6)
    print factorial4Recursion(6)
    print timeit(mult, 2, 3)
    print timeit(factorial1, 6)
    print timeit(factorial2, 6)
    print timeit(factorial4Recursion, 6)