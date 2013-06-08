'''
Created on 2009-8-31

@author: selfimpr
'''

array = [0, 1, 2, 3, 4, 5]
list = ["hello", "world", 1, "2"]
tuple = ("hello", "world", 1, "2")
map = {1: "one", 2: "two", 3: "three"}
for data in array:
    print data,
print

for data in list:
    print data,
print 

for data in tuple:
    print data,
print

for data in map:
    print data,
print 

who = "knights"
what = "Ni!"
print "We are the", who, "who say", what, what, what, what
print "We are the %s who say %s" % (who, ((what + " ") * 4))
arr1 = array * 4
for data in arr1:
    print data, 
print

print range(len(array))

for index, data in enumerate(list):
    print "[", index, "]", data, 
print

print '''---------------------'''

a={"0":"0","1":"1"}
print a
print type(a)
print dir(a)
print a.pop("1")
print a













