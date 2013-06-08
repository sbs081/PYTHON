'''
Created on 2009-9-9

@author: selfimpr
'''
import re
def atoc(s):
    real_match = re.search("(-?\d+.?\d*(e[+|-]?\d+)?)", s)
    image_match = re.search("(-?\d+.?\d*(e[+|-]?\d+)?)[j|J]", s)
    real = float(real_match.group(1))
    image = float(image_match.group(1))
    return complex(real, image)

print atoc("-1.23e+4-5.67j")