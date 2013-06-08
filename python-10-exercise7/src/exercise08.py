'''
Created on 2009-9-11

@author: selfimpr
'''
employees = {"jack": 2009001, "tom": 2009002, "bruce": 2009003}
for name in sorted(employees):
    print name, "|", employees[name]
tmp = {}
for key, value in employees.items():
    tmp[value] = key
for number in sorted(tmp):
    print number, ":", tmp[number]