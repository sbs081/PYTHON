'''
Created on 2009-9-5

@author: selfimpr
'''
import unittest, excersize04

class TestCase(unittest.TestCase):    
    
    def setUp(self):
        self.ex = excersize04
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testIsLeapYear(self):
        print self.ex.isLeapYear(1996)
    
if __name__ == '__main__':
    unittest.main()