'''
Created on 2009-9-9

@author: selfimpr
'''
import unittest, exercise02


class Test(unittest.TestCase):

    def testIdCheck(self):
        print '''exercise02.idcheck("-")''', exercise02.idcheck("-")
        print '''exercise02.idcheck("_")''', exercise02.idcheck("_")
        print '''exercise02.idcheck("s")''', exercise02.idcheck("s")
        print '''exercise02.idcheck("1")''', exercise02.idcheck("1")
        print '''exercise02.idcheck("-1")''', exercise02.idcheck("-1")
        print '''exercise02.idcheck("_1")''', exercise02.idcheck("_1")
        print '''exercise02.idcheck("s1")''', exercise02.idcheck("s1")
        print '''exercise02.idcheck("_2")''', exercise02.idcheck("_2")
        print '''exercise02.idcheck("se")''', exercise02.idcheck("se")
        print '''exercise02.idcheck("_`")''', exercise02.idcheck("_`")
        print '''exercise02.idcheck("s`")''', exercise02.idcheck("s`")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
