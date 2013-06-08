'''
Created on 2009-10-26

@author: Administrator
'''
import socket

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = 'localhost', 88
    client.connect(address)
    flag = True
    while flag:
        input = raw_input('> ')
        client.send(input)
        print client.recv(100)
        if input == 'bye':
            flag = False
    client.close()