'''
Created on 2009-11-5

@author: Administrator
'''
from socket import *

HOST = 'localhost'
PORT = 88
ADDRESS = HOST, PORT

if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen(5)
    listen_flag = True
    try:
        while listen_flag:
            client, client_address = server.accept()
            print 'connected from %s:%d' % client_address
            receive_flag = True
            try:
                while receive_flag:
                    data = client.recv(128)
                    print '%s> %s' % (client_address, data)
                    if data == 'bye':
                        client.send('bye')
                        receive_flag = False
                        listen_flag = False
                    else:
                        input = raw_input('> ')
                        client.send(input)
            except Exception, e:
                print e
            finally:
                client.close()
    except Exception, e:
        print e
    finally:
        server.close()