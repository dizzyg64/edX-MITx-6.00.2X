# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 23:48:23 2016

@author: RichardG
"""

g.addEdge(Edge(nodes[0], nodes[1]))
g.addEdge(Edge(nodes[0], nodes[2]))
g.addEdge(Edge(nodes[1], nodes[4]))
g.addEdge(Edge(nodes[2], nodes[3]))
g.addEdge(Edge(nodes[3], nodes[5]))
g.addEdge(Edge(nodes[4], nodes[5]))

#or some variation of this. Obviously, in a graph
# g.addEdge(Edge(nodes[0], nodes[1])) functions just as well as
# g.addEdge(Edge(nodes[1], nodes[0])).