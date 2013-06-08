'''
Created on 2009-10-4

@author: selfimpr
'''
import time
def dollarize(f, sign = '$', negative = True):
    strF = str(abs(f))
    fList = strF.split('.')
    intF = fList[0]
    floatF = ('.' + fList[1][:2]) if '.' in strF else ''
    maxIndex = len(intF) + 1
    l = [(intF[-i-2] if i+2 < maxIndex else '') \
         + (intF[-i-1] if i+1 < maxIndex else '') \
         + intF[-i] for i in range(1, maxIndex, 3)]
    l.reverse()
    s = sign + ','.join(l)
    s += floatF
    if f < 0:
        if negative:
            s = '-' + s
        else :
            s = s.join('<>')
    return s

class MoneyFormat(object):
    def __init__(self, value):
        self.value = value
    def update(self, value):
        self.value = value
    def __nonzero__(self):
        return self.value and self.value != 0
    def __str__(self, negative = True):
        return dollarize(self.value, sign = '$', negative = negative)
    def __repr__(self):
        return str(self.value)

if __name__ == '__main__':
    print dollarize(12345678)
    m = MoneyFormat(-1234567898.45678)
    m.update(-98765432.5678)
    print bool(m)
    print m.__str__(False)
    print '%r' % m