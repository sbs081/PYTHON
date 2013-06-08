#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import ftplib
import os
import socket
import re
import sys

def upload_callback(line):
    print '1024 uploaded'

def upload():
    f = ftplib.FTP('localhost')
    f.login('anonymous', 'anonymous@')
    f.dir()
    local_file = open('c:\seasy.sql', 'rb')
    f.storlines('STOR seasy.sql', local_file)

if __name__ == '__main__':
    upload()