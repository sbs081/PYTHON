'''
Created on 2009-10-27

@author: Administrator
'''
from SocketServer import *
import time


class MessageHandler(StreamRequestHandler):
    def handle(self):
        print 'connect from', self.client_address
        self.wfile.write(time.localtime() + self.rfile.readline())

if __name__ == '__main__':
    server_address = ('localhost', 88)
    tcpserver = TCPServer(server_address, MessageHandler)
    tcpserver.serve_forever()