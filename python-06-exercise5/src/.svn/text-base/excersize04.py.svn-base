'''
Created on 2009-9-4

@author: selfimpr
'''
def isLeapYear(year):
    if isinstance(year, str):
        try:
            year = int(year)
        except Exception, e:
            print "Argument must to be a integer"
    if year > 9999 or year < -9999:
        raise Exception("Year must between -9999 and 9999")
    return year % 4 == 0