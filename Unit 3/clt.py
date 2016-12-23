# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:15:18 2016

@author: RichardG
"""

def clt():
    for sampleSize in sampleSizes:
        sampleMeans = []
        for t in range(20):
            sample = flipCoin(sampleSize)
            sampleMeans.append(getMeanAndStd(sample)[0])
        meanOfMeans.append(getMeanAndStd(sampleMeans)[0])
        stdOfMeans.append(getMeanAndStd(sampleMeans)[1])