# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:24:18 2016

@author: RichardG
"""
import random
nodes = []
for i in range(nodes):
    nodes.append(newNode(i)) # newNode takes one parameter, the number of the node

for i in range(len(nodes)):
	x = random.choice(nodes)
	y = random.choice(nodes)
	addEdge(x,y)
	