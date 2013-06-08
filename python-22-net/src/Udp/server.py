'''
Created on 2009-10-27

@author: Administrator
'''
import socket

if __name__ == '__main__':
    self = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = ('localhost', 81)
    self.bind(address)
    flag = True
    while flag:
        received = self.recvfrom_into(32)
        print received[1], ':', received[0]
        if received[1] == 'bye':
            flag = False
            continue
        input = raw_input('> ')
        self.sendto(input, 0, received[1])