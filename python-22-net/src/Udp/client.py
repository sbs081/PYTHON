'''
Created on 2009-10-27

@author: Administrator
'''
import socket

if __name__ == '__main__':
    self = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = ('localhost', 82)
    self.bind(address)
    targ_address = ('localhost', 81)
    flag = True
    while flag:
        input = raw_input('> ')
        self.sendto(input, 0, targ_address)
        received = self.recvfrom(32)
        print received[1], ':', received[0]
        if received[1] == 'bye':
            flag = False
            continue