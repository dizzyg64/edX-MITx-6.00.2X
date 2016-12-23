# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 23:58:29 2016

@author: RichardG
"""

import random
def genEven():
    return random.randrange(0, 100, 2)


"""
Other Possibilities
def genEven():
    return random.choice(range(0, 100, 2))

def genEven():
    return int(random.random() * 50)*2

def genEven():
    return random.choice(range(0, 50))*2

def genEven():
    x = random.randint(0, 98)
    while x % 2 != 0:
        x = random.randint(0, 98)
    return x
"""

