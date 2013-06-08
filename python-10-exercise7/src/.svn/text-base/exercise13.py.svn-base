'''
Created on 2009-9-11

@author: selfimpr
'''
import random
s1 = set()
s2 = set()
def generate_set():
    for i in range(random.randint(0, 9)):
        s1.add(random.randint(1, 10))
        s2.add(random.randint(1, 10))
generate_set()
count = 0
while input and count <=2:
    input = raw_input("enter a set")
    l = [int(n.strip()) for n in input.split(",")]
    s = set(l)
    if s == s1 | s2:
        print "congratulations"
        break
    else:
        count += 1
print s1 | s2
print s2 & s1