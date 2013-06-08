'''
Created on 2009-9-5

@author: selfimpr
'''
import unittest, excersize02

class TestCase(unittest.TestCase):    
    
    def setUp(self):
        self.ex = excersize02
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testMultiply(self):
        print self.ex.multiply(18, 29.0)
    
if __name__ == '__main__':
    unittest.main()