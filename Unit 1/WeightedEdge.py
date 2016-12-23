# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 23:54:34 2016

@author: RichardG
"""

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return Edge.__str__(self) + " (" + str(self.weight) + ")"