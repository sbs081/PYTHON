#!/usr/bin/env python
#-*- coding:utf-8-*-

from sys import argv
from os import makedirs, unlink, sep, chdir
from os.path import dirname, exists, isdir, splitext
from string import replace, find, lower
from htmllib import HTMLParser
from urllib import urlretrieve
from urlparse import urlparse, urljoin
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO
from sgmllib import SGMLParser
from time import sleep
import JavaGroupContent
import XMLLoader
import pickle
import re

class Retriever(object): #download Web pages
    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)
        
    def filename(self, url): 
        path=url

        path = re.sub("\W","_",path)
        path+=".html"
        return path
    
    def isForbidden(self):
        return 0;
    
    def isForbidden(self):
        return 0;
    
    def download(self):
        try:
            if True:
                retval = urlretrieve(self.url, self.file)
                javaGroupContent=JavaGroupContent.JavaGroupContent() 
                javaGroupContent.meet_page(self.url, self.file)
            else:
                retval = '*** INFO: no need to download '
        except IOError:
            retval = ('*** ERROR: invalid URL "%s"' % self.url,)
        return retval
        
    def parseAndGetLinks(self):
        self.parser = HTMLParser(AbstractFormatter(DumbWriter(StringIO())))
        try:
            self.parser.feed(open(self.file).read())
            self.parser.close()
        except IOError:
            pass
        return self.parser.anchorlist

class Crawler(object):
    count =0                                  #a global count for how many pages have been down loaded
    def __init__(self,para_queue,para_seen,para_config):
        self.q = para_queue
        self.seen = para_seen
        self.config = para_config
    
    def getPage(self,url):
        r=Retriever(url)
        retval = r.download()
        if retval[0] == '*':
            return
        else:
            Crawler.count +=1
            print '\nPage: ', Crawler.count
            print 'URL:', url
            print 'FILE:', retval[0]
                
        self.seen.append(url)
        
        links=r.parseAndGetLinks()
        
        for eachLink in links:
            if eachLink[:4] != 'http' and find(eachLink, '://') == -1:
                eachLink = urljoin(url,eachLink)
            
            if find(lower(eachLink),'mailto:') != -1:
                continue
            
            eachLinks = eachLink.split("#",2)
            eachLink=eachLinks[0]

            if eachLink not in self.seen:
                if eachLink not in self.q:
                    self.q.append(eachLink)
                else:
                    pass
            else:
                pass
                           
    def go(self):
        while self.q:
            url = self.q.pop()
            print url
            downloadtag=0
            ignoretag=0;
            for dowloadpattern in self.config.downloads:
                downloadtag += url.count(dowloadpattern)
                    
            for ignorepattern in self.config.ignores:
                ignoretag += url.count(ignorepattern)
            if downloadtag==1 and ignoretag==0:
                print "Getting"+url
                self.getPage(url)
                waittime=self.config.downloadWait
                for i in range(int(waittime)):
                    print i+1, 
                    sleep(1)

def main():
    if len(argv) > 1:
        url = argv[1]
    else:
        try:
            url = raw_input('Enter a site name: ')
        except (KeyboardInterrupt, EOFError):
            url =''  
            
        try:
            chdir("../"+url)
            configFileURL=url+".xml"
            config = XMLLoader.XMLLoader(configFileURL)
            startUrl = config.startURL
            startUrl ='http://webdev.csdn.net/page/'
            queue=[]
            seen =[]
            try:
                queue = pickle.load(open("queue.txt"))
            except:
                queue.append(startUrl)
            try:
                seen = pickle.load(open("seen.txt"))
            except:
                seen=[]
                     
            robot=Crawler(queue,seen,config)              
            robot.go()
        finally:
            pickle.dump(robot.q,open("queue.txt","w"))
            pickle.dump(robot.seen,open("seen.txt","w"))
                        
if __name__=='__main__':
    main()