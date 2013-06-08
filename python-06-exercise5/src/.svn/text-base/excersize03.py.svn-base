'''
Created on 2009-9-4

@author: selfimpr
'''
def getScore():
    try:
        return int(raw_input("Please input a number between 0 and 100:\n"))
    except Exception, e:
        print "You must input a number:\n"
        return getInt()

def getLevel(score):
    if score < 60:
        return "F"
    elif score < 69:
        return "D"
    elif score < 79:
        return "C"
    elif score < 89:
        return "B"
    elif score <=100:
        return "A"
    else:
        return "Error"

def entry():
    score = getScore()
    while score >= 0:
        print getLevel(score)
        score = getScore()
    print "Bye!"