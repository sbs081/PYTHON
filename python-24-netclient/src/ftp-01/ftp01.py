#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import ftplib
import os
import socket
import re
import sys

class FTPClient(ftplib.FTP):
    
    COMMANDS = ['ls', 'cd', 'upload', 'download', 'open', 'bye']
    PATTERN = re.compile('^(\w+)\s*((\s+[^\s]+)*)$')
    
    def __init__(self, host = 'localhost', username = 'anonymous', password = 'anonymous@'):
        ftplib.FTP.__init__(self, host, username, password)
        self.host = host
        self.username = username
        self.password = password
    
    def getcommand(self):
        command = raw_input('ftp> ')
        match_result = FTPClient.PATTERN.match(command)
        if match_result and match_result.group(1) in FTPClient.COMMANDS:
            return command
        else:
            print 'Warning: unsupport command [%s]' % command
            return self.getcommand()
    
    def ls(self, *directory):
        directory = ' '.join(directory) if directory else '.'
        try:
            return self.dir(directory)
        except ftplib.error_perm, e:
            print 'Warning: [%s] hadn\'t exists' % directory
    
    def cd(self, directory = '.'):
        return self.cwd(directory)
    
    def open(self, host = None, username = None, password = None):
        self.host = host or self.host
        self.username = username or self.username
        self.password = password or self.password
    
    def run(self):
        flag = True
        while flag:
            command = self.getcommand()
            if command != 'bye':
                match_result = self.PATTERN.match(command)
                call_str = 'self.' + match_result.group(1) + '(' + ','.join(['\'' + arg + '\'' for arg in match_result.group(2).strip().split(' ')]) + ')'
                result = eval(call_str)
            else:
                flag = False

if __name__ == '__main__':
    client = FTPClient()
    client.run()
