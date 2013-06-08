'''
Created on 2009-9-9

@author: selfimpr
'''
import random
p_options = {"stone": 0, "fabric": 1, "shears": 2}
compares = {(0, 0): 0, (0, 1): 1, (0, 2): -1, \
            (1, 0): -1, (1, 1): 0, (1, 2): 1, \
            (2, 0): 1, (2, 1): -1, (2, 2): 0}
results = {0: "We are deuce! ", \
           1: "You are winner", -1: "You lose"}

p_option = raw_input("enter your option: \n")
while p_option and p_option != "exit":
    print results[\
              compares[\
                   (random.randint(0, 2), \
                    p_options[p_option])]]
    p_option = raw_input("enter your option: \n")
