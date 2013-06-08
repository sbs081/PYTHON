'''
Created on 2009-10-29

@author: Administrator
'''
import socket, os

if __name__ == '__main__':
    local_address = 'localhost', 81
    remote_address = 'localhost', socket.getservbyname('daytime', 'udp')
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind(local_address)
    while True:
        client.sendto('Hello, daytime service!', 0, remote_address)
        print client.recvfrom(1024 * 1024)