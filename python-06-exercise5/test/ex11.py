'''
Created on 2009-9-5

@author: selfimpr
'''
import unittest, excersize11

class TestCase(unittest.TestCase):    
    
    def setUp(self):
        self.ex = excersize11
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testGetEven(self):
        print self.ex.getEven(100) 
    
    def testGetOdd(self):
        print self.ex.getOdd(100)
    
    def testCheckDivision(self):
        print self.ex.checkDivision(100, 11)

if __name__ == '__main__':
    unittest.main()