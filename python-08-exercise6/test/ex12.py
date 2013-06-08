'''
Created on 2009-9-10

@author: selfimpr
'''
import unittest, exercise12


class Test(unittest.TestCase):


    def setUp(self):
        self.ex = exercise12


    def tearDown(self):
        pass


    def testFindchr(self):
        print self.ex.findchr("helloworld", "w")
   
    def testRfindchr(self):
        print self.ex.rfindchr("helloworld", "w")
    
    def testSubchr(self):
        print self.ex.subchr("helloworld", "w", "****")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testContain']
    unittest.main()