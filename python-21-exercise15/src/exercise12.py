'''
Created on 2009-10-23

@author: selfimpr
'''
import re

pattern = re.compile(r'^https?://(\w+\.)*(\w+)(:\d{0,5})?(/.+)*$')

if __name__ == '__main__':
    print pattern.search('http://localhost:8080/manage/department/get_users/depid35').groups()
    print pattern.search('http://hi.csdn.net/attachment/200910/22/8670_1256173858K9Z1.jpg').groups()
    print pattern.search('http://qxsvr22.webgame.xunlei.com/sword/enterGameAction.action?userinfo=AAAAcFkNuBiVrIzP28JaJUyU59SXENrXuhpafaf%2FuvhHqihXcvRDqXgHT%2BrrvWEgfDI0BG3AY6kz4IDk%2BIscW%2FTbi7tLMHh0iekQaBvQZ4H6BNMgZHWkcpIXLXYmV0V4YV0B9NzlFt6yJQuokXjpN3ndn6o%3D').groups()
    print pattern.search('http://tieba.baidu.com/tousu/new/show/kz/2234402').groups()
    