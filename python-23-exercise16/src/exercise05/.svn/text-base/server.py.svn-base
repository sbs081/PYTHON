# -*- coding: UTF-8 -*-
'''
Created on 2009-10-28

@author: Administrator
'''
import socket
import time
import os

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = 'localhost', 88
    server.bind(address)
    server.listen(5)
    flag = True
    while flag:
        client, client_address = server.accept()
        print '%s: %d connected success' % (client_address[0], client_address[1])
        client_flag = True
        while client_flag:
            msg = client.recv(32)
            if msg == 'date':
                client.send(str(time.localtime()))
            elif msg == 'ls':
                client.send(str(os.listdir(os.getcwd())))
            elif msg == 'cd':
                os.chdir(os.pardir)
                client.send('change ok')
            else:
                client.send('bye')
                client_flag = False
                flag = False
        client.close()
    server.close()