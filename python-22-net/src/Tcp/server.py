'''
Created on 2009-10-26

@author: Administrator
'''
import socket
import time

clients = {}

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = 'localhost', 88
    server.bind(address)
    server.listen(5)
    flag = True
    while flag:
        client = server.accept()
        clients[client[1]] = client[0]
        address = client[1]
        client = client[0]
        client_flag = True
        client.send('connect_success')
        while client_flag:
            msg = client.recv(64)
            client.send(str(time.localtime()) + msg)
            print str(address), msg
            if msg == 'bye':
                client_flag = False
        client.close()
        flag = False
    server.close()