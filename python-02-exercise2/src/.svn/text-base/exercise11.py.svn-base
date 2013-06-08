'''
Created on 2009-9-1

@author: selfimpr
'''

support_command = ('1', '2', 'x')
def getCommand():
    'This is my document'
    input = raw_input('''
      |Please input your command: |
    --|---------------------------|--
      |   1   |    sum            |
      |   2   |    avg            |
      |   x   |    exit           |
    --|---------------------------|--
      |Please input your command: |
    ''')
    if input in support_command:
        return input
    else:
        return getCommand()

def getValue():
    input = raw_input('''
      |Please input a number or q(exit): |
    --|----------------------------------|--
      | number |    sum                  |
      |    q   |    exit                 |
      |  exit  |    exit                 |
    --|----------------------------------|--
      |Please input a number or q(exit): |
    ''')
    if input == 'exit' or input == 'q':
        return input
    try:
        ivalue = int(input)
        return ivalue
    except ValueError, e:
        print 'please ensure input legal'
        return getValue()

command = getCommand()
while command != 'x':
    sum = 0
    index = 0
    if command == '1':
        value = getValue()
        while isinstance(value, int) and value != 'exit' and value != 'q':
            sum += value
            value = getValue()
        print 'sum:', sum
    elif command == '2':
        value = getValue()
        while isinstance(value, int) and value != 'exit' and value != 'q':
            sum += value
            index += 1
            value = getValue()
        print 'avg:', float(sum) / index
    else:
        print 'legal input'
    command = getCommand()
