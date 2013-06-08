'''
Created on 2009-11-5

@author: Administrator
'''
from socket import *

HOST = 'localhost'
PORT = 88
ADDRESS = HOST,  PORT

if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDRESS)
    receive_flag = True
    try:
        while receive_flag:
            input = raw_input('> ')
            client.send(input)
            data = client.recv(128)
            print 'server> %s' % data
            if data == 'bye':
                receive_flag = False
    except Exception, e:
        print e
    finally:
        client.close()
        