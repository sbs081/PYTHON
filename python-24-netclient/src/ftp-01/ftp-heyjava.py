'''
Created on 2009-11-13

@author: Administrator
'''
import ftplib

if __name__ == '__main__':
    address = 'ftp.heyjava.com'
    username = 'selfimpr'
    password = '201229'
    heyjava = ftplib.FTP(address)
    heyjava.login(username, password)
    heyjava.sendcmd('list')
    print heyjava.getwelcome()
    print heyjava.getmultiline()