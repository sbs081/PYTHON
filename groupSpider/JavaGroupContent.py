#!/usr/bin/env python
#-*- coding:utf-8-*-

import MySQLdb
import sys
import re


class JavaGroupContent:
    def __init__(self):
        self.title = ''
        self.user =''
        self.group =''
        
    def select_page(self):
        conn=MySQLdb.connect(host="localhost",
                   user="root",passwd="csdtcsdt",db="csdn",
                   connect_timeout=3600,charset="utf8",use_unicode=True)
        cur=conn.cursor()
        cur.execute('select * from csdn_java_content')
        cur.scroll(0)
        row1=cur.fetchone()
        print row1[0]
        print row1[1]
        print row1[2]
                
    def insert_page(self,url,filename,title,author,group):
        conn=MySQLdb.connect(host="localhost",
                   user="root",passwd="csdtcsdt",db="csdn",
                   connect_timeout=3600,charset="utf8",use_unicode=True)
        cur=conn.cursor()
        sqlStr='insert into csdn_java_content (content_url,content_fn,title,author,group_name) values \
        (\''+str(url)+'\',\''+str(filename)+'\',\''+title+'\',\''+author+'\',\''+group+'\')'
        sqlStr=sqlStr.decode("utf-8")
        print sqlStr
        try:
            cur.execute(sqlStr)
            conn.commit()
        except:
            pass
        conn.close()
        
    def meet_page(self,url,file):
        fd =open(file)
        htmlContent = fd.read()
        titlePattern=re.compile("<title>\n(.+?) - ([^-]+) - ([^-]+)</title>")
        match=titlePattern.search(htmlContent)
        if match:
            title =match.group(1)
            author =match.group(2)
            group=match.group(3) 
            self.insert_page(url, file, title, author, group)