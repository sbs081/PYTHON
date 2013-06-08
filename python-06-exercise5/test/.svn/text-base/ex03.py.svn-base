'''
Created on 2009-9-5

@author: selfimpr
'''
import unittest, excersize03

class TestCase(unittest.TestCase):    
    
    def setUp(self):
        self.ex = excersize03
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testGetInt(self):
        print self.ex.getScore()
    
    def testGetLevel(self):
        print self.ex.getLevel(100)
    
    def testEntry(self):
        print self.ex.entry()
    
if __name__ == '__main__':
    unittest.main()