'''
Created on 2009-9-10

@author: selfimpr
'''
import unittest, exercise05


class Test(unittest.TestCase):


    def setUp(self):
        self.ex = exercise05


    def tearDown(self):
        pass


    def testContain(self):
        print "contain: ", self.ex.contain("hello, world", "q")
    
    def testIsRecur(self):
        print "isRecur: ", self.ex.isRecur("hellhello")
    
    def testIsPalindrome(self):
        print "isPalindrome: ", self.ex.isPalindrome("hel  \n\r\n\r\n  leh")
    
    def testToPalindrome(self):
        print "palindrome: ", self.ex.toPalindrome("hello, world")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testContain']
    unittest.main()