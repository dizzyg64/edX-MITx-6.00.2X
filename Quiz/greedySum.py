# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:49:21 2016

@author: RichardG
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    result = []
    while (s >= L[0]):
        if (s >= L[0]):
            num = s // L[0]
            s -= (num * L[0])
            result.append(num)
            L = L[1:]
        else:
            result = 'no solution'
    return str(result)[1:-1]
#    return result

#    print (str(L, s, result)[1:-1])
#print(greedySum([2], 5))
print(greedySum([], 10))
print(greedySum([30, 20, 10], 60))
#print(greedySum([101, 51, 11, 2, 1], 3000))
#print(greedySum([21, 10, 8, 3, 1], 11))
#print(greedySum([20, 10, 4, 3, 1], 21))
#print(greedySum([1], 20))
#print(greedySum([10, 5, 1], 14))
