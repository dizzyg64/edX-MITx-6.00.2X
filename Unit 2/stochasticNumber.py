# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:02:14 2016

@author: RichardG
"""

import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return 2 * random.randint(5,10)
    
    
"""
return random.randrange(10, 22, 2)
"""
