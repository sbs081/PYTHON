'''
Created on 2009-9-14

@author: selfimpr
'''
amount = int(raw_input('Enter total number of names: '))
names = []
for i in range(amount):
    input = raw_input('Please enter name %d: ' % i)
    while ',' not in input:
        input = raw_input('Wrong format... should be Last, First. \n'\
                          'Please enter name %d: ' % i)
    name = input.split(',')
    names.append((name[0].strip(), name[1].strip()))
for firstname, lastname in names:
    print firstname, ",", lastname