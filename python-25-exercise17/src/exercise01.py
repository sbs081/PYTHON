'''
Created on 2009-11-13

@author: Administrator
'''
import ftplib
if __name__ == '__main__':
    heyjava = ftplib.FTP('ftp.heyjava.com')
    heyjava.login('selfimpr', '201229')
    heyjava.dir()