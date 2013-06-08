'''
Created on 2009-9-5

@author: selfimpr
'''
import unittest, excersize06

class TestCase(unittest.TestCase):    
    
    def setUp(self):
        self.ex = excersize06
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testPush(self):
        stack = self.ex.Stack()
        for i in range(20):
            stack.push(i)
#        print stack.datas
    
    def testPop(self):
        stack = self.ex.Stack()
        for i in range(20):
            stack.push(i)
#        for i in range(len(stack.datas)):
#            print "Element [", stack.pop(), "] was removed"
#        print stack.datas
    
    def testSize(self):
        stack = self.ex.Stack()
        for i in range(20):
            stack.push(i)
#        print stack.size()
    
    def testParseElement(self):
        print
        print self.ex.parseElement("((-2+3))*-4+(+5)+-6**8+(8-2*7)")

    def testChangeToSuffix(self):
        print
#        print self.ex.changeToSuffix(self.ex.parseElement("((-2+3))*-4+(+5)+-6**8"))

    def testAccount(self):
        print self.ex.account(self.ex.changeToSuffix(self.ex.parseElement("((-2+3))*-4+(+5)+-6**8")))
    
if __name__ == '__main__':
    unittest.main()