'''
Created on 2009-9-5

@author: selfimpr
'''
import unittest, excersize05

class TestCase(unittest.TestCase):    
    
    def setUp(self):
        self.ex = excersize05
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testGetMinCentes(self):
        print self.ex.getMinCentes(0.94)
    
if __name__ == '__main__':
    unittest.main()