#!/usr/bin/env python
""" Edge Class
Represent a edge of the graph with properties.

Author: 	Patryk Zabkiewicz
Date:		2015.08.03

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

class Edge:
    def __init__(self,edge={}):
        if edge:
            self.A = edge.A
            self.B = edge.B
            self.capacity = edge.capacity
            self.flow = edge.flow
            self.lenght = edge.lenght
            self.speed = edge.speed
            self.cost = edge.cost
        else:
            self.A = []
            self.B = []
            self.capacity = 0
            self.flow = 0
            self.lenght = 0
            self.speed = 0
            self.cost = 0
