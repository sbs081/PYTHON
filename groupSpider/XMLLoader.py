from os import makedirs, unlink, sep, chdir
from xml.dom import minidom,Node
import re,textwrap

class XMLLoader:
    def __init__(self,docURL):
        self.doc = minidom.parse(docURL)
        self.startURL =""
        self.forbidens =[]
        self.downloads =[]
        self.ignores =[]
        self.forbidenWait =0 
        self.downloadWait =0
        for child in self.doc.childNodes:
            if child.nodeType == Node.ELEMENT_NODE and child.tagName == 'site':
                self.handleSite(child);

    def gettext(self,nodelist):
        retlist=[]
        for node in nodelist:
            if node.nodeType == Node.TEXT_NODE:
                retlist.append(node.wholeText)
        return re.sub('\s+', ' ', ''.join(retlist))

    def handleSite(self,node):
        for child in node.childNodes:
            if child.nodeType != Node.ELEMENT_NODE:
                continue
            if child.tagName == 'starturl':
                self.startURL = self.gettext(child.childNodes)
                print self.startURL 
            if child.tagName == 'forbidens':
                self.handleForbidens(child)
                print self.forbidens
            if child.tagName == 'downloads':
                self.handleDownloads(child)
                print self.downloads
            if child.tagName == 'ignores':
                self.handleIgnores(child)
                print self.ignores
            if child.tagName == 'forbidenwait':
                self.forbidenWait = self.gettext(child.childNodes)
                print self.forbidenWait
            if child.tagName == 'downloadwait':
                self.downloadWait = self.gettext(child.childNodes)
                print self.downloadWait
    
    def handleForbidens(self,node):
        for child in node.childNodes:
            if child.nodeType != Node.ELEMENT_NODE:
                continue
            if child.tagName == 'forbiden':
                self.forbidens.append(self.gettext(child.childNodes))
    def handleDownloads(self,node):
        for child in node.childNodes:
            if child.nodeType != Node.ELEMENT_NODE:
                continue
            if child.tagName == 'download':
                self.downloads.append(self.gettext(child.childNodes))
    def handleIgnores(self,node):
        for child in node.childNodes:
            if child.nodeType != Node.ELEMENT_NODE:
                continue
            if child.tagName == 'ignore':
                self.ignores.append(self.gettext(child.childNodes))
    
def main():
    temp = XMLLoader("java_group.xml")
    pass

if __name__=='__main__':
    main()


