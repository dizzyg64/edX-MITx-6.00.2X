# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:00:12 2016

@author: RichardG
"""

import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed(0)
    return 2 * random.randint(5,10)
    
    
    
"""
def deterministicNumber():
    return 10 # or 12 or 14 or 16 or 18 or 20
    
"""
