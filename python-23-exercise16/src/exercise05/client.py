# -*- coding: UTF-8 -*-
'''
Created on 2009-10-28

@author: Administrator
'''
import socket

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = 'localhost', 88
    client.connect(address)
    flag = True
    while flag:
        command = raw_input('> ')
        client.send(command)
        msg = client.recv(128)
        if msg == 'bye':
            flag = False
        else:
            print msg
    client.close()